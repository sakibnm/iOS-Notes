import os

new_content = """# Topic 06 — ViewModel, StateFlow, Notifications, and Broadcast Receivers

**Estimated effort:** 7–9 hours this topic
**Format:** Asynchronous online — work at your own pace
**Prerequisites:** Topics 1–4

---

## Learning Objectives

By the end of this session, students will be able to:

1. Create a `ViewModel` and understand its lifecycle relative to an Activity.
2. Expose UI state using `StateFlow` and collect it with `collectAsStateWithLifecycle`.
3. Handle one-shot events (snackbars, navigation triggers) with `SharedFlow`/`Channel`.
4. Post a local notification, creating a notification channel first.
5. Register and unregister a `BroadcastReceiver`, and understand the difference between explicit and implicit broadcasts.
6. Request the `POST_NOTIFICATIONS` runtime permission on Android 13+.

---

## Before You Start

Spread the work across the assigned time — don't leave it all for the day before the lab is due. A rough breakdown:

- **Walkthrough: Building SkyCast** — step-by-step lab building the real app while learning concepts. Budget about 90 minutes.

**Before you begin the lab, you should have:**

- Run every code example in Android Studio as you go.
- Completed the pre-topic quiz on Canvas (ungraded, just a self-check).

---

## The Story So Far...

In the previous topic, we wrapped the SkyCast prototype in a Material Scaffold and set up navigation routes to move between screens.

To continue the story, **open your existing Android Studio project from the previous topic**. We will be directly building upon the code you wrote previously. 

> 🆘 **Lost your code?** If your previous project is broken or missing, don't worry! You can download a clean starting point here: [Starter Project: topic_05_layouts_dialogs_navigation.zip](/downloads/topic_05_layouts_dialogs_navigation.zip). 

---

## Walkthrough: Building SkyCast

> 📁 **Target Project Reference (Completed Code)** — [topic_06_viewmodel_stateflow.zip](/downloads/topic_06_viewmodel_stateflow.zip)
>
> This project contains the complete, runnable SkyCast snapshot at Topic 6. Import into Android Studio and click Run.
>
> **Heads up:** The source files show the finished version of each step. Working through the walkthrough yourself first — then comparing to the download — is far more effective than reading the code directly.

SkyCast gets a brain this topic. `WeatherViewModel` becomes the single source of truth for weather state — current conditions, forecast, and errors.

### Step 1: The Brain of the App (ViewModel)

> **SkyCast Briefing:** In Topic 4 you stored state with `remember`. That works for simple, local state, but it has two problems: It doesn't survive configuration changes (like rotating the phone), and it mixes UI with business logic. We need a `ViewModel` to solve both.

A `ViewModel` is a class that holds state and business logic for a screen. It survives configuration changes because Android creates it before creating the Activity and keeps it alive until the Activity is *finished*.

ViewModel enforces a clean architecture called *Unidirectional Data Flow* (UDF):

```mermaid
flowchart LR
    subgraph UILayer ["UI Layer"]
        A["User Action"]
        D["UI Recompose"]
    end
    subgraph VM ["ViewModel"]
        B["ViewModel Function"]
        C["State Update"]
    end
    A -->|"Trigger"| B
    B -->|"Mutate"| C
    C -->|"Observe"| D
    D -.->|"Wait for"| A
```

We will use **StateFlow** for persistent state, and **Channels** for one-shot events (like navigating or showing a snackbar). Create `WeatherViewModel.kt` in your `ui/home/` package:

```kotlin
package com.example.skycast.ui.home

import androidx.lifecycle.ViewModel
import androidx.lifecycle.viewModelScope
import com.example.skycast.model.DailyForecast
import com.example.skycast.model.WeatherCondition
import com.example.skycast.model.WeatherSnapshot
import kotlinx.coroutines.channels.Channel
import kotlinx.coroutines.delay
import kotlinx.coroutines.flow.MutableStateFlow
import kotlinx.coroutines.flow.StateFlow
import kotlinx.coroutines.flow.asStateFlow
import kotlinx.coroutines.flow.receiveAsFlow
import kotlinx.coroutines.flow.update
import kotlinx.coroutines.launch

sealed class WeatherUiState {
    data object Loading : WeatherUiState()
    data class Success(
        val snapshot : WeatherSnapshot,
        val forecast : List<DailyForecast>
    ) : WeatherUiState()
    data class Error(val message: String) : WeatherUiState()
}

sealed class SkyCastEvent {
    data class ShowSnackbar(val message: String) : SkyCastEvent()
    data class NavigateToCity(val city: String)  : SkyCastEvent()
}

class WeatherViewModel : ViewModel() {
    // Persistent State (StateFlow)
    private val _uiState = MutableStateFlow<WeatherUiState>(WeatherUiState.Loading)
    val uiState: StateFlow<WeatherUiState> = _uiState.asStateFlow()

    private val _isCelsius = MutableStateFlow(true)
    val isCelsius: StateFlow<Boolean> = _isCelsius.asStateFlow()

    // One-shot Events (Channel)
    private val _events = Channel<SkyCastEvent>(Channel.BUFFERED)
    val events = _events.receiveAsFlow()

    init { loadWeather("Boston") }

    fun loadWeather(city: String) = viewModelScope.launch {
        _uiState.value = WeatherUiState.Loading
        delay(1000)   // simulated network — replaced with Retrofit in Topic 8
        _uiState.value = WeatherUiState.Success(
            snapshot = WeatherSnapshot(city, 18.5, 65, 22.0, "Partly cloudy"),
            forecast = listOf(
                DailyForecast("Mon", 21.0, 12.0, WeatherCondition.Clear),
                DailyForecast("Tue", 18.5, 11.0, WeatherCondition.Cloudy),
                DailyForecast("Wed", 14.0,  9.5, WeatherCondition.Rain(3.0))
            )
        )
    }

    fun toggleUnit() = _isCelsius.update { !it }
    
    fun triggerNetworkError() = viewModelScope.launch {
        _events.send(SkyCastEvent.ShowSnackbar("No internet connection."))
    }
}
```

##### Code Breakdown: WeatherViewModel
- `WeatherUiState` is a sealed class — the screen is always in exactly one state (Loading, Success, or Error), preventing contradictory states.
- Always use the **Private mutable, public read-only** pattern: `_uiState` is a `MutableStateFlow` that only the ViewModel can change, while `uiState` is exposed as an immutable `StateFlow` for the UI to read.

---

### Step 2: Connecting the Brain to the UI

> **SkyCast Briefing:** Now that our brain is built, we need our UI to listen to it safely. We will use `collectAsStateWithLifecycle` to subscribe to the ViewModel's state.

`collectAsStateWithLifecycle` is the right collector to use in Compose. It automatically pauses collection when the app is in the background (saving battery and avoiding wasted work) and resumes when the app is foregrounded.

First, add the required dependency to your `app/build.gradle.kts`:
```kotlin
implementation("androidx.lifecycle:lifecycle-runtime-compose:2.8.4")
```

Update your `HomeScreen.kt`:

```kotlin
package com.example.skycast.ui.home

import androidx.compose.foundation.layout.*
import androidx.compose.material.icons.Icons
import androidx.compose.material.icons.filled.Search
import androidx.compose.material3.*
import androidx.compose.runtime.*
import androidx.compose.ui.Alignment
import androidx.compose.ui.Modifier
import androidx.compose.ui.platform.testTag
import androidx.lifecycle.compose.collectAsStateWithLifecycle
import androidx.lifecycle.viewmodel.compose.viewModel
import com.example.skycast.ui.common.SkyCastTopBar
import com.example.skycast.ui.common.WeatherContent

@Composable
fun HomeScreen(
    vm: WeatherViewModel = viewModel(),
    onSearchClick: () -> Unit,
    onSettingsClick: () -> Unit
) {
    // 1. Collect persistent state
    val state     by vm.uiState.collectAsStateWithLifecycle()
    val isCelsius by vm.isCelsius.collectAsStateWithLifecycle()

    val snackbarHostState = remember { SnackbarHostState() }

    // 2. Collect one-shot events
    LaunchedEffect(Unit) {
        vm.events.collect { event ->
            when (event) {
                is SkyCastEvent.ShowSnackbar -> snackbarHostState.showSnackbar(event.message)
                is SkyCastEvent.NavigateToCity -> { /* handled by navigation */ }
            }
        }
    }

    Scaffold(
        topBar = { SkyCastTopBar("SkyCast", onSettingsClick = onSettingsClick) },
        floatingActionButton = {
            FloatingActionButton(onClick = onSearchClick) {
                Icon(Icons.Default.Search, contentDescription = "Search")
            }
        },
        snackbarHost = { SnackbarHost(snackbarHostState) }
    ) { padding ->
        Box(Modifier.padding(padding).fillMaxSize()) {
            when (val s = state) {
                WeatherUiState.Loading ->
                    CircularProgressIndicator(
                        Modifier.align(Alignment.Center).testTag("loading_indicator"))

                is WeatherUiState.Error ->
                    Column(Modifier.align(Alignment.Center),
                           horizontalAlignment = Alignment.CenterHorizontally) {
                        Text(s.message)
                        Button(onClick = { vm.loadWeather("Boston") }) { Text("Retry") }
                    }

                is WeatherUiState.Success ->
                    WeatherContent(s.snapshot, s.forecast, isCelsius) { vm.toggleUnit() }
            }
        }
    }
}
```

##### Code Breakdown: HomeScreen
- `LaunchedEffect(Unit)` collects events (like snackbars) for the lifetime of the composable, then cancels automatically.
- `when (val s = state)` smart-casts `s` — inside `is Success` you get `s.snapshot` and `s.forecast` without explicit casting.

---

### Step 3: Alerts and Notifications

> **SkyCast Briefing:** Notifications let your app communicate with the user even when the app isn't open. We need to alert users about severe weather.

Notifications require a specific flow:

```mermaid
flowchart TD
    A["Start"] --> B{"Android 13+?"}
    B -- "Yes" --> C["Request POST_NOTIFICATIONS Permission"]
    C --> D{"Granted?"}
    D -- "No" --> E["Do not post"]
    D -- "Yes" --> F["Create Notification Channel"]
    B -- "No" --> F
    F --> G["Build Notification"]
    G --> H["Notify Manager"]
```

Declare the permission in your `AndroidManifest.xml`:
```xml
<uses-permission android:name="android.permission.POST_NOTIFICATIONS" />
```

Create a new file `WeatherAlerts.kt` in your `ui/common/` package:

```kotlin
package com.example.skycast.ui.common

import android.app.NotificationChannel
import android.app.NotificationManager
import android.content.Context
import androidx.core.app.NotificationCompat
import androidx.core.app.NotificationManagerCompat

fun postWeatherAlert(context: Context, city: String, message: String) {
    // 1. Create a notification channel (required on API 26+)
    val channel = NotificationChannel(
        "weather_alerts", "Weather Alerts", NotificationManager.IMPORTANCE_HIGH
    ).apply { description = "Severe weather alerts for your saved cities" }
    
    context.getSystemService(NotificationManager::class.java)
           .createNotificationChannel(channel)

    // 2. Build and post the notification
    val notification = NotificationCompat.Builder(context, "weather_alerts")
        .setSmallIcon(android.R.drawable.ic_dialog_info)
        .setContentTitle("⛈️ Weather alert — $city")
        .setContentText(message)
        .setPriority(NotificationCompat.PRIORITY_HIGH)
        .setAutoCancel(true)
        .build()

    // Suppressing permission check because we assume the Compose UI requested it
    try {
        NotificationManagerCompat.from(context).notify(1001, notification)
    } catch (e: SecurityException) {
        // Handle missing permission
    }
}
```

The notification ID (`1001`) identifies this notification. Using the same ID for a later `notify()` call *updates* the existing notification rather than creating a new one.

---

### Step 4: System Events with BroadcastReceiver

> **SkyCast Briefing:** A `BroadcastReceiver` listens for system-wide events, like the network connectivity changing. We want to auto-refresh the weather when the internet connects.

Create `NetworkChangeReceiver.kt` and register it inside your `MainActivity.kt`.

```kotlin
package com.example.skycast

import android.content.BroadcastReceiver
import android.content.Context
import android.content.Intent
import android.content.IntentFilter
import android.net.ConnectivityManager
import android.os.Bundle
import androidx.activity.ComponentActivity
import androidx.activity.compose.setContent
import androidx.activity.viewModels
import com.example.skycast.ui.home.WeatherViewModel
import com.example.skycast.ui.navigation.SkyCastNavigation

class NetworkChangeReceiver(private val onAvailable: () -> Unit) : BroadcastReceiver() {
    override fun onReceive(context: Context, intent: Intent) {
        val cm = context.getSystemService(ConnectivityManager::class.java)
        if (cm?.activeNetworkInfo?.isConnected == true) onAvailable()
    }
}

class MainActivity : ComponentActivity() {
    private val weatherViewModel: WeatherViewModel by viewModels()
    private lateinit var networkReceiver: NetworkChangeReceiver

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContent {
            // Your Compose Navigation goes here, passing the ViewModel down if needed
            SkyCastNavigation(weatherViewModel)
        }
    }

    override fun onStart() {
        super.onStart()
        networkReceiver = NetworkChangeReceiver {
            // When internet reconnects, reload the weather
            weatherViewModel.loadWeather("Boston")
        }
        registerReceiver(networkReceiver, IntentFilter(ConnectivityManager.CONNECTIVITY_ACTION))
    }
    
    override fun onStop() {
        super.onStop()
        unregisterReceiver(networkReceiver)   // always unregister to prevent leaks
    }
}
```

**Always pair register with unregister.** Forgetting to unregister causes a memory leak when Android destroys the Activity and the receiver is still registered.

---

## Guided Practice Challenges

Before diving into the full assignment, try these low-stakes practice challenges in Android Studio. They will build the exact muscle memory you need for managing SkyCast's architecture.

### Challenge 1: The Brain of the App (`ViewModel` & `StateFlow`)
**The Scenario:** Our weather UI loses all its data when the user rotates their phone because the state is trapped in the `Activity`. We need to move it to a `ViewModel`.
**The Task:** 
1. Create a `class WeatherViewModel : ViewModel()`.
2. Add a private `_temperature = MutableStateFlow(20)`.
3. Add a public, read-only `val temperature: StateFlow<Int> = _temperature.asStateFlow()`.
4. Add a function `fun refresh() { _temperature.value = (10..30).random() }`.

### Challenge 2: Connecting the Brain to the UI (`collectAsStateWithLifecycle`)
**The Scenario:** The UI needs to safely listen to the ViewModel without draining the battery when the app is in the background.
**The Task:**
1. In your Composable, add a parameter `vm: WeatherViewModel = viewModel()`.
2. Collect the temperature using `val temp by vm.temperature.collectAsStateWithLifecycle()`.
3. Add a `Text` displaying `temp`, and a `Button` that calls `vm.refresh()`.
4. Run the app, click the button a few times, and then **rotate the emulator**. Verify the temperature does NOT reset!

### Challenge 3: The Danger Alert (`NotificationChannel`)
**The Scenario:** SkyCast needs to warn users about severe weather even when they are looking at another app.
**The Task:**
1. Write a function `createAlertChannel(context: Context)`.
2. Inside it, create a `NotificationChannel` named "Severe Weather" with `IMPORTANCE_HIGH`.
3. Register the channel with the `NotificationManager`.
4. Call this function exactly once inside your `MainActivity`'s `onCreate`.

## References

1. [ViewModel Overview](https://developer.android.com/topic/libraries/architecture/viewmodel)
2. [StateFlow and SharedFlow](https://developer.android.com/kotlin/flow/stateflow-and-sharedflow)
3. [Consuming flows safely in Compose](https://developer.android.com/jetpack/compose/state#use-other-types-of-state-in-compose)
4. [Channels (Kotlin)](https://kotlinlang.org/docs/channels.html)
5. [Create a Notification](https://developer.android.com/training/notify-user/build-notification)
6. [Broadcasts Overview](https://developer.android.com/guide/components/broadcasts)

---

## Getting Help

Because this course is fully asynchronous, here's how to get unstuck:

- **Piazza** is the primary help channel. Every topic has a dedicated thread. When asking a question, include: (1) what you're trying to do, (2) what you've tried, (3) the exact error message or Logcat output. Most questions get answered within a few hours.
- **TA office hours** — each TA hosts 1–2 hours per timeline on Zoom. Schedule is posted on Canvas. These are open-form drop-in sessions: show up, share your screen, get help.
- **Instructor office hours** — by appointment for deeper issues (design questions, project direction, grading questions).
- **On using AI tools:** The use of AI is not recommended at least for the first 6 modules, until you understand the basics of the development cycle. I do not ban using AI, but when you use AI, you should be able to answer any conceptual questions asked by the TAs or the professor. See the Academic Integrity policy on Canvas for specifics.
"""

with open("/Users/nsm/cs4520/lessons/Topic_06_ViewModel_StateFlow_Notifications.md", "w") as f:
    f.write(new_content)

print("Rewrote Topic 06 successfully!")
