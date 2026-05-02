import os

new_content = """# Topic 08 — Gradle, Dependencies, and Networking with Retrofit + Coroutines

**Estimated effort:** 7–9 hours this topic
**Format:** Asynchronous online — work at your own pace
**Prerequisites:** Topics 1–6

---

## Learning Objectives

By the end of this session, students will be able to:

1. Read and modify `build.gradle.kts` to add dependencies and configure build types.
2. Understand the module structure of a Gradle project (settings, project, app).
3. Use the Kotlin version catalog (`libs.versions.toml`).
4. Configure Retrofit with OkHttp and a JSON converter.
5. Define a Retrofit API interface with `suspend` functions.
6. Use `Dispatchers.IO` appropriately for network work (and understand that Retrofit already switches for you).
7. Display a loading state, success state, and error state driven by a coroutine-based repository.

---

## Before You Start

Spread the work across the assigned time — don't leave it all for the day before the lab is due. A rough breakdown:

- **Walkthrough: Building SkyCast** — step-by-step lab building the real app while learning concepts. Budget about 90 minutes.

**Before you begin the lab, you should have:**

- Run every code example in Android Studio as you go.
- Completed the pre-topic quiz on Canvas (ungraded, just a self-check).

---

## The Story So Far...

In the previous topic, we implemented a LazyColumn to display a scrollable list of saved cities and forecast days.

To continue the story, **open your existing Android Studio project from the previous topic**. We will be directly building upon the code you wrote previously. 

> 🆘 **Lost your code?** If your previous project is broken or missing, don't worry! You can download a clean starting point here: [Starter Project: topic_07_lists_lazycolumn.zip](/downloads/topic_07_lists_lazycolumn.zip). 

---

## Walkthrough: Building SkyCast

> 📁 **Target Project Reference (Completed Code)** — [topic_08_networking_retrofit.zip](/downloads/topic_08_networking_retrofit.zip)
>
> This project contains the complete, runnable SkyCast snapshot at Topic 8. Import into Android Studio and click Run.
>
> **Heads up:** The source files show the finished version of each step. Working through the walkthrough yourself first — then comparing to the download — is far more effective than reading the code directly.

SkyCast gets real data this topic. We connect to **Open-Meteo** — completely free, no API key, no sign-up.

### Step 1: Gradle and the Version Catalog

> **SkyCast Briefing:** Every Android project uses Gradle as its build system. To talk to the internet, we need to add a library called **Retrofit**. Instead of hardcoding version numbers everywhere, modern Android uses a Version Catalog (`libs.versions.toml`) to centralize all dependencies.

First, add the Internet permission to your `AndroidManifest.xml` (right before the `<application>` tag):
```xml
<uses-permission android:name="android.permission.INTERNET"/>
```

Next, open `gradle/libs.versions.toml` and add the Retrofit and Moshi libraries:

```toml
[versions]
retrofit  = "2.11.0"
okhttp    = "4.12.0"
moshi     = "1.15.1"

[libraries]
retrofit           = { group = "com.squareup.retrofit2", name = "retrofit",            version.ref = "retrofit" }
retrofit-moshi     = { group = "com.squareup.retrofit2", name = "converter-moshi",     version.ref = "retrofit" }
okhttp-logging     = { group = "com.squareup.okhttp3",   name = "logging-interceptor", version.ref = "okhttp" }
moshi-kotlin       = { group = "com.squareup.moshi",     name = "moshi-kotlin",        version.ref = "moshi" }
```

Finally, open your `app/build.gradle.kts` and add them to the dependencies block. (Notice how dots replace dashes from the TOML file). Click **Sync Now** when Android Studio prompts you.

```kotlin
dependencies {
    implementation(libs.retrofit)
    implementation(libs.retrofit.moshi)
    implementation(libs.okhttp.logging)
    implementation(libs.moshi.kotlin)
    // ... existing dependencies
}
```

---

### Step 2: Defining the API Interface

> **SkyCast Briefing:** Retrofit turns a simple Kotlin `interface` into a working network client. You just annotate the functions with HTTP verbs (`@GET`, `@POST`) and define the expected JSON response type.

Create a new package `network/` and add `SkyCastApi.kt`:

```kotlin
package com.example.skycast.network

import retrofit2.http.GET
import retrofit2.http.Query

interface OpenMeteoApi {
    @GET("forecast")
    suspend fun getForecast(
        @Query("latitude")      lat: Double,
        @Query("longitude")     lon: Double,
        @Query("current")       current: String = "temperature_2m,weather_code,wind_speed_10m,relative_humidity_2m",
        @Query("daily")         daily: String = "temperature_2m_max,temperature_2m_min,weather_code",
        @Query("timezone")      timezone: String = "auto",
        @Query("forecast_days") days: Int = 7
    ): OpenMeteoForecastDto

    companion object { const val BASE_URL = "https://api.open-meteo.com/v1/" }
}

interface GeocodingApi {
    @GET("search")
    suspend fun searchCity(
        @Query("name")     name: String,
        @Query("count")    count: Int = 5,
        @Query("language") language: String = "en",
        @Query("format")   format: String = "json"
    ): GeocodingResponseDto

    companion object { const val BASE_URL = "https://geocoding-api.open-meteo.com/v1/" }
}
```

*(Note: `OpenMeteoForecastDto` and `GeocodingResponseDto` will show errors right now. We will build these Data Transfer Objects in Topic 09).*

##### Code Breakdown: SkyCastApi
- The `suspend` modifier means Retrofit will handle background threading automatically — you don't need to manually switch to `Dispatchers.IO`. It suspends the coroutine while waiting for the network, without blocking the main UI thread.

---

### Step 3: Building the Retrofit Client

> **SkyCast Briefing:** We have the interface, but we need an actual instance of the client to execute the requests. We'll set up OkHttp with a logging interceptor so we can see the raw network traffic in Logcat.

Create `SkyCastNetwork.kt` in your `network/` package:

```kotlin
package com.example.skycast.network

import com.example.skycast.BuildConfig
import com.squareup.moshi.Moshi
import com.squareup.moshi.kotlin.reflect.KotlinJsonAdapterFactory
import okhttp3.OkHttpClient
import okhttp3.logging.HttpLoggingInterceptor
import retrofit2.Retrofit
import retrofit2.converter.moshi.MoshiConverterFactory
import java.util.concurrent.TimeUnit

object SkyCastNetwork {
    private val logging = HttpLoggingInterceptor().apply {
        // Print the full JSON body in debug builds, but turn it off for release builds
        level = if (BuildConfig.DEBUG) HttpLoggingInterceptor.Level.BODY
                else HttpLoggingInterceptor.Level.NONE
    }
    
    private val client = OkHttpClient.Builder()
        .addInterceptor(logging)
        .connectTimeout(10, TimeUnit.SECONDS)
        .readTimeout(15, TimeUnit.SECONDS)
        .build()

    private fun <T> build(baseUrl: String, service: Class<T>): T =
        Retrofit.Builder()
            .baseUrl(baseUrl)
            .client(client)
            .addConverterFactory(
                MoshiConverterFactory.create(
                    Moshi.Builder().add(KotlinJsonAdapterFactory()).build()
                )
            )
            .build()
            .create(service)

    val weather: OpenMeteoApi   = build(OpenMeteoApi.BASE_URL, OpenMeteoApi::class.java)
    val geocoding: GeocodingApi = build(GeocodingApi.BASE_URL, GeocodingApi::class.java)
}
```

##### Code Breakdown: SkyCastNetwork
- `SkyCastNetwork` is a singleton `object`. We only ever want one Retrofit instance in the entire app.
- The `HttpLoggingInterceptor` prints every request and response in Logcat. This is invaluable for debugging why a network call failed.

---

### Step 4: The Repository Pattern

> **SkyCast Briefing:** Never call Retrofit directly from a ViewModel. Use a **Repository** to isolate network code. If we ever switch from Open-Meteo to OpenWeatherMap, the ViewModel won't have to change at all.

Create a `data/` package and add `WeatherRepository.kt`:

```kotlin
package com.example.skycast.data

import com.example.skycast.model.CityResult
import com.example.skycast.model.WeatherReport
import com.example.skycast.network.GeocodingApi
import com.example.skycast.network.OpenMeteoApi
import com.example.skycast.network.SkyCastNetwork

class WeatherRepository(
    private val api: OpenMeteoApi  = SkyCastNetwork.weather,
    private val geo: GeocodingApi  = SkyCastNetwork.geocoding
) {
    suspend fun fetchWeather(lat: Double, lon: Double, city: String): WeatherReport {
        val dto = api.getForecast(lat, lon)
        // We will build the .toDomain() mapping in Topic 09
        return dto.toDomain(city)    
    }

    suspend fun searchCities(query: String): List<CityResult> {
        if (query.length < 2) return emptyList()
        return geo.searchCity(query).results?.map { it.toDomain() } ?: emptyList()
    }
}
```

---

### Step 5: Connecting Real Data to the ViewModel

> **SkyCast Briefing:** Now we just swap out our hardcoded mock data for the real repository! We'll catch network errors so the app doesn't crash.

Update your `WeatherViewModel.kt`:

```kotlin
package com.example.skycast.ui.home

import androidx.lifecycle.ViewModel
import androidx.lifecycle.viewModelScope
import com.example.skycast.data.WeatherRepository
import kotlinx.coroutines.flow.MutableStateFlow
import kotlinx.coroutines.flow.StateFlow
import kotlinx.coroutines.flow.asStateFlow
import kotlinx.coroutines.launch
import retrofit2.HttpException
import java.io.IOException

class WeatherViewModel(
    private val repo: WeatherRepository = WeatherRepository()
) : ViewModel() {
    private val _uiState = MutableStateFlow<WeatherUiState>(WeatherUiState.Loading)
    val uiState: StateFlow<WeatherUiState> = _uiState.asStateFlow()

    init {
        loadWeather() // Load Boston by default
    }

    fun loadWeather(lat: Double = 42.35, lon: Double = -71.06, city: String = "Boston") {
        viewModelScope.launch {
            _uiState.value = WeatherUiState.Loading
            
            _uiState.value = try {
                val report = repo.fetchWeather(lat, lon, city)
                WeatherUiState.Success(
                    snapshot = report.current, 
                    forecast = report.forecast
                )
            } catch (e: IOException) { 
                WeatherUiState.Error("No internet connection.") 
            } catch (e: HttpException) { 
                WeatherUiState.Error("Server error: ${e.code()}") 
            }
        }
    }
}
```

At this point in the semester, running SkyCast will show **real weather data** from Open-Meteo!

---

## Guided Practice Challenges

Before diving into the full assignment, try these low-stakes practice challenges in Android Studio. They will build the exact muscle memory you need for wiring up SkyCast to the internet.

### Challenge 1: The Gateway (`Retrofit` and `suspend`)
**The Scenario:** We need to define exactly *how* our app talks to the Open-Meteo API before we can actually do it.
**The Task:** 
1. Open your `AndroidManifest.xml` and add the `INTERNET` permission.
2. Create an `interface SkyCastApi`.
3. Add a function inside it: `@GET("forecast") suspend fun fetchCurrentWeather(): ResponseDto`.
4. Create a singleton `object Network` that builds the `Retrofit` instance pointing to `"https://api.open-meteo.com/v1/"`.

### Challenge 2: The Middleman (`Repository`)
**The Scenario:** The ViewModel shouldn't know what Retrofit is. We need a Repository to act as the middleman between the network and the UI state.
**The Task:**
1. Create a `class WeatherRepository(private val api: SkyCastApi)`.
2. Write a `suspend fun getWeather()` inside the Repository that calls your API.
3. In your `ViewModel`, initialize the `WeatherRepository` and launch a coroutine (`viewModelScope.launch`) to call `getWeather()`.

### Challenge 3: The Loading Spinner (Three-State UI)
**The Scenario:** Network requests take time. If the screen is blank while loading, users will think the app crashed.
**The Task:**
1. Create a `sealed class UiState`. Give it `Loading`, `Success(val data: String)`, and `Error(val msg: String)` subclasses.
2. In your Composable, use a `when` block on your state.
3. When it is `Loading`, render a `CircularProgressIndicator()`.
4. When it is `Error`, render the error text and a "Retry" button.

## References

1. [Migrate to Version Catalogs](https://developer.android.com/build/migrate-to-catalogs)
2. [Retrofit](https://square.github.io/retrofit/)
3. [Connect to the network](https://developer.android.com/training/basics/network-ops/connecting)
4. [Data layer architecture](https://developer.android.com/topic/architecture/data-layer)

---

## Getting Help

Because this course is fully asynchronous, here's how to get unstuck:

- **Piazza** is the primary help channel. Every topic has a dedicated thread. When asking a question, include: (1) what you're trying to do, (2) what you've tried, (3) the exact error message or Logcat output. Most questions get answered within a few hours.
- **TA office hours** — each TA hosts 1–2 hours per timeline on Zoom. Schedule is posted on Canvas. These are open-form drop-in sessions: show up, share your screen, get help.
- **Instructor office hours** — by appointment for deeper issues (design questions, project direction, grading questions).
- **On using AI tools:** The use of AI is not recommended at least for the first 6 modules, until you understand the basics of the development cycle. I do not ban using AI, but when you use AI, you should be able to answer any conceptual questions asked by the TAs or the professor. See the Academic Integrity policy on Canvas for specifics.
"""

with open("/Users/nsm/cs4520/lessons/Topic_08_Gradle_Retrofit_Networking.md", "w") as f:
    f.write(new_content)

print("Rewrote Topic 08 successfully!")
