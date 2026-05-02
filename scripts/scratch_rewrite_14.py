import os

new_content = """# Topic 14 — Debugging, Accessibility, and App Polish

**Estimated effort:** 6–8 hours this topic
**Format:** Asynchronous online — work at your own pace
**Prerequisites:** Topics 1–13

---

## Learning Objectives

By the end of this topic, students will be able to:

1. Use Logcat filters, Layout Inspector, and the Android Profiler to diagnose crashes and performance issues.
2. Identify and fix common accessibility problems using `contentDescription`, semantic modifiers, and TalkBack.
3. Write meaningful log statements with structured tags and use breakpoints inside coroutines.
4. Explain what Kotlin Multiplatform is and identify which parts of an app are good candidates for sharing.
5. Apply at least one concrete optimisation or polish improvement to a running Android app.

---

## Before You Start

Spread the work across the assigned time — don't leave it all for the day before the lab is due. A rough breakdown:

- **Walkthrough: Building SkyCast** — step-by-step lab building the real app while learning concepts. Budget about 90 minutes.

**Before you begin the lab, you should have:**

- Run every code example in Android Studio as you go.
- Completed the pre-topic quiz on Canvas (ungraded, just a self-check).

---

## The Story So Far...

In the previous topic, we used CameraX to let users snap a photo of the sky and added smooth Compose animations to our UI.

To continue the story, **open your existing Android Studio project from the previous topic**. We will be directly building upon the code you wrote previously. 

> 🆘 **Lost your code?** If your previous project is broken or missing, don't worry! You can download a clean starting point here: [Starter Project: topic_13_camerax_animations.zip](/downloads/topic_13_camerax_animations.zip). 

---

## Walkthrough: Building SkyCast

> 📁 **Target Project Reference (Completed Code)** — [topic_14_debugging_accessibility.zip](/downloads/topic_14_debugging_accessibility.zip)
>
> This project contains the complete, runnable SkyCast snapshot at Topic 14. Import into Android Studio and click Run.
>
> **Heads up:** The source files show the finished version of each step. Working through the walkthrough yourself first — then comparing to the download — is far more effective than reading the code directly.

We audit SkyCast this topic: structured logging, TalkBack accessibility, and semantic roles.

### Step 1: The Debugging Toolkit

> **SkyCast Briefing:** Android Studio ships with several tools to diagnose problems. 
> 1. **Logcat** is the live log stream from your device. 
> 2. **Layout Inspector** gives a live 3D view of your composables and recomposition counts. 
> 3. **App Inspection** lets you browse your Room database and Network requests in real time.

Update your `WeatherRepository.kt` to include structured logging:

```kotlin
package com.example.skycast.data

import android.util.Log
import com.example.skycast.model.WeatherReport
import retrofit2.HttpException
import java.io.IOException

private const val TAG = "WeatherRepository"

class WeatherRepository(/* ... */) {
    suspend fun fetchWeather(lat: Double, lon: Double, city: String): WeatherReport {
        Log.d(TAG, "fetchWeather city=$city lat=$lat lon=$lon")
        
        return try {
            val dto = api.getForecast(lat, lon)
            Log.d(TAG, "fetchWeather success tempC=${dto.current.tempC}")
            dto.toDomain(city)
        } catch (e: IOException) {
            Log.e(TAG, "fetchWeather network error", e)
            throw e
        } catch (e: HttpException) {
            Log.e(TAG, "fetchWeather HTTP ${e.code()}", e)
            throw e
        }
    }
}
```

In Android Studio Logcat, type `tag:WeatherRepository` to see only these logs. Use `Log.d` for normal flow and `Log.e` for errors (always pass the `Exception` so you get a stack trace!).

---

### Step 2: Accessibility in Android

> **SkyCast Briefing:** Accessibility means making your app usable by people who use assistive technologies like TalkBack (a screen reader). Every `Icon` and `Image` that conveys meaning needs a `contentDescription`.

Update your `WeatherCard.kt`:

```kotlin
package com.example.skycast.ui.home

import androidx.compose.foundation.layout.fillMaxWidth
import androidx.compose.foundation.layout.padding
import androidx.compose.material.icons.Icons
import androidx.compose.material.icons.filled.Thermostat
import androidx.compose.material3.Card
import androidx.compose.material3.Icon
import androidx.compose.material3.IconButton
import androidx.compose.runtime.Composable
import androidx.compose.ui.Modifier
import androidx.compose.ui.semantics.contentDescription
import androidx.compose.ui.semantics.semantics
import androidx.compose.ui.unit.dp

@Composable
fun WeatherCard(
    city: String, tempC: Double, condition: String, humidity: Int,
    isCelsius: Boolean, modifier: Modifier = Modifier
) {
    val tempLabel = if (isCelsius) "${"%.1f".format(tempC)} degrees Celsius"
                   else           "${"%.1f".format(tempC * 9/5 + 32)} degrees Fahrenheit"

    Card(
        modifier = modifier
            .fillMaxWidth()
            .padding(horizontal = 16.dp)
            .semantics {
                // This makes TalkBack read a natural sentence instead of raw UI elements
                contentDescription = "$city: $tempLabel, $condition, humidity $humidity percent"
            }
    ) {
        // ... card content unchanged ...
    }
}

// Buttons always need a meaningful label for TalkBack
@Composable
fun UnitToggleButton(isCelsius: Boolean, onToggle: () -> Unit) {
    IconButton(
        onClick  = onToggle,
        modifier = Modifier.semantics {
            contentDescription = if (isCelsius) "Switch to Fahrenheit" else "Switch to Celsius"
        }
    ) {
        // The label is on the button itself, so the icon description is null
        Icon(Icons.Default.Thermostat, contentDescription = null)  
    }
}
```

---

### Step 3: Semantic Merging for Complex Layouts

> **SkyCast Briefing:** For complex rows (like our 7-day forecast), we don't want TalkBack to pause awkwardly between the date, the emoji, and the temperature. We use `mergeDescendants` to collapse them into a single phrase.

Update your `ForecastDayCard` in `ui/home/`:

```kotlin
package com.example.skycast.ui.home

import androidx.compose.foundation.layout.*
import androidx.compose.material3.Card
import androidx.compose.material3.Text
import androidx.compose.runtime.Composable
import androidx.compose.ui.Alignment
import androidx.compose.ui.Modifier
import androidx.compose.ui.semantics.clearAndSetSemantics
import androidx.compose.ui.semantics.contentDescription
import androidx.compose.ui.semantics.invisibleToUser
import androidx.compose.ui.semantics.semantics
import androidx.compose.ui.unit.dp
import com.example.skycast.model.DailyForecast

@Composable
fun ForecastDayCard(day: DailyForecast, isCelsius: Boolean, modifier: Modifier = Modifier) {
    val hi   = if (isCelsius) day.maxC else day.maxC * 9/5 + 32
    val lo   = if (isCelsius) day.minC else day.minC * 9/5 + 32
    val unit = if (isCelsius) "C" else "F"

    Card(
        modifier = modifier
            .fillMaxWidth()
            .semantics(mergeDescendants = true) {
                // Collapses all child Text nodes into one TalkBack announcement
                contentDescription =
                    "${day.date}: ${day.condition.description()}, " +
                    "high ${"%.0f".format(hi)} degrees, low ${"%.0f".format(lo)} degrees $unit"
            }
    ) {
        Row(Modifier.padding(16.dp), verticalAlignment = Alignment.CenterVertically) {
            Text(day.date, Modifier.width(48.dp))
            Text(
                day.condition.emoji(),
                modifier = Modifier.semantics { invisibleToUser() }   // decorative — skip in TalkBack
            )
            Spacer(Modifier.weight(1f))
            Text("${"%.0f".format(lo)}° / ${"%.0f".format(hi)}°$unit")
        }
    }
}
```

---

### Step 4: Looking Ahead to Kotlin Multiplatform (Optional)

> **SkyCast Briefing:** Kotlin Multiplatform (KMP) lets you share Kotlin code between Android, iOS, desktop, and the web. You can share your data models, repositories, and ViewModels (`commonMain`), while keeping the UI platform-specific (`androidMain` for Compose, `iosMain` for SwiftUI).

We won't convert SkyCast to KMP in the core curriculum, but **there is a full, optional KMP module at the end of this course** if you want to see how to run SkyCast on an iPhone!


## Guided Practice Challenges

Before diving into the full assignment, try these low-stakes practice challenges in Android Studio. They will build the exact muscle memory you need for professional-grade debugging and polish.

### Challenge 1: The Detective (Logcat & Profiler)
**The Scenario:** Users report that the app sometimes crashes silently when saving a city. We need to catch the error.
**The Task:** 
1. Add `Log.d("SkyCast", "Attempting to save city...")` before a database insert.
2. Intentionally throw an exception right after it: `throw IllegalStateException("Simulated crash")`.
3. Run the app, cause the crash, and find the exact line number in Logcat by filtering for `tag:SkyCast` or `FATAL EXCEPTION`.
4. (Remove the intentional crash before moving on!)

### Challenge 2: The Invisible UI (Accessibility)
**The Scenario:** A visually impaired user is trying to use the app, but TalkBack just says "Unlabelled button" over and over.
**The Task:**
1. Turn on TalkBack on your emulator or physical device.
2. Navigate to your app and close your eyes. Try to delete a saved city.
3. If you can't tell what the button does, open the code and add `contentDescription = "Delete city"` to the `Icon`.
4. Test it again with TalkBack.

### Challenge 3: Merging the Noise (`semantics(mergeDescendants = true)`)
**The Scenario:** When TalkBack reads a weather forecast row, it pauses awkwardly between the date, the emoji, and the temperature.
**The Task:**
1. Look at Snippet 3.
2. Wrap your `Row` composable in a `Card` or `Box` that uses `Modifier.semantics(mergeDescendants = true)`.
3. Provide a single, cohesive `contentDescription` that reads like a natural sentence (e.g., "Monday: Cloudy, high 20, low 10").
4. Add `Modifier.semantics { invisibleToUser() }` to the individual text nodes inside the row.

---

## Advanced Accessibility & Usability Testing

While TalkBack is essential, true accessibility (and usability) extends to all users. 

**Visual Accessibility:**
Ensure your text colors contrast sharply with their backgrounds. Avoid light gray text on a white background.

**Dynamic Type Scaling:**
Android users can increase their system font size by up to 200%. If you hardcode your layout heights (e.g., `Modifier.height(50.dp)`), the enlarged text will clip and become unreadable. Always use `Modifier.wrapContentHeight()` or padding to let your containers grow dynamically.

**Hallway Usability Testing:**
You are not your user. The interface that makes perfect sense to the person who coded it will often baffle a new user. Hand your phone to a friend who has never seen it before. Give them a goal: "Try to add a city and then delete it." Watch them silently. When they tap the wrong thing, write it down. That is a UX failure, not user error.

## References

1. [Debug your app](https://developer.android.com/studio/debug)
2. [Layout Inspector](https://developer.android.com/studio/debug/layout-inspector)
3. [Accessibility in Compose](https://developer.android.com/jetpack/compose/accessibility)
4. [Kotlin Multiplatform](https://kotlinlang.org/docs/multiplatform.html)

---

## Getting Help

Because this course is fully asynchronous, here's how to get unstuck:

- **Piazza** is the primary help channel. Every topic has a dedicated thread. When asking a question, include: (1) what you're trying to do, (2) what you've tried, (3) the exact error message or Logcat output. Most questions get answered within a few hours.
- **TA office hours** — each TA hosts 1–2 hours per timeline on Zoom. Schedule is posted on Canvas. These are open-form drop-in sessions: show up, share your screen, get help.
- **Instructor office hours** — by appointment for deeper issues (design questions, project direction, grading questions).
- **On using AI tools:** The use of AI is not recommended at least for the first 6 modules, until you understand the basics of the development cycle. I do not ban using AI, but when you use AI, you should be able to answer any conceptual questions asked by the TAs or the professor. See the Academic Integrity policy on Canvas for specifics.
"""

with open("/Users/nsm/cs4520/lessons/Topic_14_Project_Work_KMP_Kickoff.md", "w") as f:
    f.write(new_content)

print("Rewrote Topic 14 successfully!")
