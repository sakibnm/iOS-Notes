import os

new_content = """# Topic 09 — JSON Parsing and Robust API Consumption

**Estimated effort:** 6–8 hours this topic
**Format:** Asynchronous online — work at your own pace
**Prerequisites:** Topics 1–7

---

## Learning Objectives

By the end of this session, students will be able to:

1. Compare Moshi and `kotlinx.serialization`; pick one and configure it.
2. Model nested and optional JSON fields using `data class`, nullable types, and defaults.
3. Map network DTOs to domain models, keeping UI code independent of wire format.
4. Design a typed `ApiResult` / `Result`-style wrapper and use it consistently.
5. Handle rate limiting, timeouts, and transient errors with exponential backoff.
6. Write a simple unit test for the DTO → domain mapper.

---

## Before You Start

Spread the work across the assigned time — don't leave it all for the day before the lab is due. A rough breakdown:

- **Walkthrough: Building SkyCast** — step-by-step lab building the real app while learning concepts. Budget about 90 minutes.

**Before you begin the lab, you should have:**

- Run every code example in Android Studio as you go.
- Completed the pre-topic quiz on Canvas (ungraded, just a self-check).

---

## The Story So Far...

In the previous topic, we set up Gradle dependencies and configured Retrofit to fetch real weather data from the internet.

To continue the story, **open your existing Android Studio project from the previous topic**. We will be directly building upon the code you wrote previously. 

> 🆘 **Lost your code?** If your previous project is broken or missing, don't worry! You can download a clean starting point here: [Starter Project: topic_08_networking_retrofit.zip](/downloads/topic_08_networking_retrofit.zip). 

---

## Walkthrough: Building SkyCast

> 📁 **Target Project Reference (Completed Code)** — [topic_09_json_robust_apis.zip](/downloads/topic_09_json_robust_apis.zip)
>
> This project contains the complete, runnable SkyCast snapshot at Topic 9. Import into Android Studio and click Run.
>
> **Heads up:** The source files show the finished version of each step. Working through the walkthrough yourself first — then comparing to the download — is far more effective than reading the code directly.

We map the raw Open-Meteo response to clean domain models this topic, making our network layer robust against errors.

### Step 1: JSON Parsing (DTOs)

> **SkyCast Briefing:** You need a JSON library to convert the raw text your server sends into Kotlin data classes. The two main options are Moshi and `kotlinx.serialization`. We are using Moshi.

A *DTO* (Data Transfer Object) is a class that mirrors the JSON exactly. It is a dumb container. No logic, no UI awareness.

Create a new package `model/dto/` and add `OpenMeteoDto.kt`:

```kotlin
package com.example.skycast.model.dto

import com.squareup.moshi.Json
import com.squareup.moshi.JsonClass

@JsonClass(generateAdapter = true)
data class OpenMeteoForecastDto(
    val latitude:  Double,
    val longitude: Double,
    val timezone:  String,
    val current:   CurrentWeatherDto,
    val daily:     DailyForecastDto
)

@JsonClass(generateAdapter = true)
data class CurrentWeatherDto(
    @Json(name = "temperature_2m")       val tempC:    Double,
    @Json(name = "weather_code")         val code:     Int,
    @Json(name = "wind_speed_10m")       val windKph:  Double,
    @Json(name = "relative_humidity_2m") val humidity: Int
)

@JsonClass(generateAdapter = true)
data class DailyForecastDto(
    val time:                     List<String>,
    @Json(name = "temperature_2m_max") val maxC:  List<Double>,
    @Json(name = "temperature_2m_min") val minC:  List<Double>,
    @Json(name = "weather_code")       val codes: List<Int>
)

@JsonClass(generateAdapter = true)
data class GeocodingResponseDto(val results: List<CityResultDto>?)

@JsonClass(generateAdapter = true)
data class CityResultDto(
    val name:     String,
    val latitude: Double,
    val longitude:Double,
    val country:  String?,
    @Json(name = "admin1") val region: String?
)
```

##### Code Breakdown: OpenMeteoDto
- `@JsonClass(generateAdapter = true)` triggers KSP (Kotlin Symbol Processing) to generate a fast, reflection-free adapter at compile time. 
- `@Json(name = "...")` maps snake_case JSON fields from the server to camelCase Kotlin properties.

---

### Step 2: Decoding Weather Codes

> **SkyCast Briefing:** The Open-Meteo API doesn't send us the word "Cloudy" or "Rain". It sends an integer (a WMO weather interpretation code). We need to decode this.

Create `WmoCode.kt` in your `model/` package:

```kotlin
package com.example.skycast.model

// Open-Meteo uses WMO weather interpretation codes (0-99)
// https://open-meteo.com/en/docs#weathervariables
object WmoCode {
    fun toCondition(code: Int): WeatherCondition = when (code) {
        0           -> WeatherCondition.Clear
        in 1..3     -> WeatherCondition.Cloudy
        in 45..48   -> WeatherCondition.Fog
        in 51..67   -> WeatherCondition.Rain(mmPerHour = rainRate(code))
        in 71..77   -> WeatherCondition.Snow(cmPerHour = 0.5)
        in 80..82   -> WeatherCondition.Rain(mmPerHour = rainRate(code))
        in 85..86   -> WeatherCondition.Snow(cmPerHour = 1.0)
        in 95..99   -> WeatherCondition.Thunderstorm
        else        -> WeatherCondition.Cloudy
    }
    
    private fun rainRate(code: Int) = when (code) {
        in 51..53, 61, 80 -> 1.0
        in 55..57, 63, 81 -> 3.5
        65, 67, 82        -> 8.0
        else              -> 2.0
    }
}
```

---

### Step 3: Domain Models

> **SkyCast Briefing:** A domain model is what your app actually uses — cleaned up, with sensible types and no server-side quirks. Why separate DTOs from Domain models? Because if we switch from Open-Meteo to a different weather API, our UI doesn't have to change at all! We just write a new DTO mapping.

Create `WeatherDomain.kt` in your `model/` package:

```kotlin
package com.example.skycast.model

// These are API-agnostic. 
// Switching from Open-Meteo to OpenWeatherMap only changes the DTOs and mappers.
data class WeatherReport(
    val city:     String,
    val lat:      Double,
    val lon:      Double,
    val current:  WeatherSnapshot,
    val forecast: List<DailyForecast>
)

data class CityResult(
    val name:    String,
    val display: String,   // E.g., "Boston, Massachusetts, United States"
    val lat:     Double,
    val lon:     Double
)
```

---

### Step 4: The Mappers

> **SkyCast Briefing:** We need a way to convert the ugly `OpenMeteoForecastDto` into our beautiful `WeatherReport` domain model. We do this using Extension Functions in the data layer.

Create `Mappers.kt` in your `data/` package:

```kotlin
package com.example.skycast.data

import com.example.skycast.model.CityResult
import com.example.skycast.model.DailyForecast
import com.example.skycast.model.WmoCode
import com.example.skycast.model.WeatherReport
import com.example.skycast.model.WeatherSnapshot
import com.example.skycast.model.dto.CityResultDto
import com.example.skycast.model.dto.OpenMeteoForecastDto

fun OpenMeteoForecastDto.toDomain(cityName: String = "My Location"): WeatherReport {
    val currentSnapshot = WeatherSnapshot(
        city      = cityName,
        tempC     = current.tempC,
        humidity  = current.humidity,
        windKph   = current.windKph,
        condition = WmoCode.toCondition(current.code).description()
    )
    
    // Open-Meteo gives us 4 separate arrays of data.
    // mapIndexed lets us zip them together into DailyForecast objects.
    val forecastList = daily.time.mapIndexed { i, date ->
        DailyForecast(
            date      = date,
            maxC      = daily.maxC[i],
            minC      = daily.minC[i],
            condition = WmoCode.toCondition(daily.codes[i])
        )
    }
    
    return WeatherReport(
        city = cityName, 
        lat = latitude, 
        lon = longitude, 
        current = currentSnapshot, 
        forecast = forecastList
    )
}

fun CityResultDto.toDomain() = CityResult(
    name    = name,
    display = listOfNotNull(name, region, country).joinToString(", "),
    lat     = latitude,
    lon     = longitude
)
```

---

### Step 5: Typed Error Handling (ApiResult)

> **SkyCast Briefing:** Network calls fail in two distinct ways. Handle them differently.
> - **`HttpException`**: the server responded, but with an error status (4xx or 5xx). The client got a response; the server just said "no". Don't retry 4xx errors — they won't get better.
> - **`IOException`**: no response arrived. The network is down, the DNS failed, or the connection timed out. These are transient and worth retrying.

Let's update our `WeatherRepository.kt` to safely wrap these errors and apply **exponential backoff** for transient network drops:

```kotlin
package com.example.skycast.data

import com.example.skycast.model.WeatherReport
import com.example.skycast.network.OpenMeteoApi
import com.example.skycast.network.SkyCastNetwork
import retrofit2.HttpException
import java.io.IOException

// 1. Define the Result Wrapper
sealed class WeatherResult<out T> {
    data class Ok<T>(val data: T)                : WeatherResult<T>()
    data class NetworkError(val msg: String)      : WeatherResult<Nothing>()
    data class ServerError(val code: Int)         : WeatherResult<Nothing>()
}

// 2. Exponential Backoff helper
suspend fun <T> retryWithBackoff(attempts: Int = 3, block: suspend () -> T): T {
    var delay = 500L
    repeat(attempts - 1) {
        try   { return block() }
        catch (e: IOException) { /* transient — try again */ }
        
        kotlinx.coroutines.delay(delay)
        delay = (delay * 2).coerceAtMost(8_000L)
    }
    return block()   // final attempt — let exceptions propagate
}

// 3. The updated Repository
class WeatherRepository(
    private val api: OpenMeteoApi = SkyCastNetwork.weather
) {
    suspend fun fetchWeather(lat: Double, lon: Double, city: String): WeatherResult<WeatherReport> =
        try {
            // Using the backoff and mapping DTO -> Domain!
            val report = retryWithBackoff { api.getForecast(lat, lon).toDomain(city) }
            WeatherResult.Ok(report)
        } catch (e: IOException)   { 
            WeatherResult.NetworkError(e.message ?: "Network error") 
        } catch (e: HttpException) { 
            WeatherResult.ServerError(e.code()) 
        }
}
```

Now, your UI is completely shielded from HTTP codes, IOExceptions, and weird JSON structures!

---

## Guided Practice Challenges

Before diving into the full assignment, try these low-stakes practice challenges in Android Studio. They will build the exact muscle memory you need for parsing API data robustly.

### Challenge 1: The Translator (DTO vs Domain)
**The Scenario:** The server returns temperatures in Kelvin and timestamps in Unix epoch, but the UI team wants Celsius and formatted dates.
**The Task:** 
1. Create a `WeatherDto` with `val tempKelvin: Double` and `val timestamp: Long`.
2. Create a `Weather` domain class with `val tempCelsius: Double` and `val timeString: String`.
3. Write an extension function `fun WeatherDto.toDomain(): Weather`.
4. In the function, convert Kelvin to Celsius (`tempKelvin - 273.15`) and format the Unix timestamp.

### Challenge 2: Graceful Failure (`ApiResult` Wrapper)
**The Scenario:** When the network goes down, the app currently crashes with an unhandled exception.
**The Task:**
1. Create a `sealed class ApiResult<out T>`.
2. Add subclasses: `Success(val data: T)`, `HttpError(val code: Int)`, and `NetworkError`.
3. Write a helper function `suspend fun <T> safeApiCall(block: suspend () -> T): ApiResult<T>`.
4. Inside `safeApiCall`, use a `try/catch` block. Catch `HttpException` and return `HttpError`. Catch `IOException` and return `NetworkError`.

### Challenge 3: Try, Try Again (Exponential Backoff)
**The Scenario:** Sometimes the user's connection drops for just a second. We shouldn't instantly show an error if a quick retry would work.
**The Task:**
1. Look at Snippet 6 in Chapter 3.
2. Implement the `retryWithBackoff` function.
3. Call it around a mocked network request that throws an `IOException` the first two times, but succeeds on the third try.

## References

1. [kotlinx.serialization](https://kotlinlang.org/docs/serialization.html)
2. [Moshi](https://github.com/square/moshi)
3. [Domain layer architecture](https://developer.android.com/topic/architecture/domain-layer)
4. [Coroutines exceptions handling](https://kotlinlang.org/docs/exception-handling.html)

---

## Getting Help

Because this course is fully asynchronous, here's how to get unstuck:

- **Piazza** is the primary help channel. Every topic has a dedicated thread. When asking a question, include: (1) what you're trying to do, (2) what you've tried, (3) the exact error message or Logcat output. Most questions get answered within a few hours.
- **TA office hours** — each TA hosts 1–2 hours per timeline on Zoom. Schedule is posted on Canvas. These are open-form drop-in sessions: show up, share your screen, get help.
- **Instructor office hours** — by appointment for deeper issues (design questions, project direction, grading questions).
- **On using AI tools:** The use of AI is not recommended at least for the first 6 modules, until you understand the basics of the development cycle. I do not ban using AI, but when you use AI, you should be able to answer any conceptual questions asked by the TAs or the professor. See the Academic Integrity policy on Canvas for specifics.
"""

with open("/Users/nsm/cs4520/lessons/Topic_09_JSON_Robust_APIs.md", "w") as f:
    f.write(new_content)

print("Rewrote Topic 09 successfully!")
