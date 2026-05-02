import os

new_content = """# Topic 12 — Firebase Storage II, Location, and Google Maps

**Estimated effort:** 8–10 hours this topic (Maps API setup takes time)
**Format:** Asynchronous online — work at your own pace
**Prerequisites:** Topics 1–10

---

## Learning Objectives

By the end of this session, students will be able to:

1. Handle multi-file uploads and progress reporting with Firebase Storage.
2. Request fine and coarse location permissions at runtime.
3. Read the device's current location using the Fused Location Provider.
4. Embed an interactive Google Map in a Compose UI.
5. Add, update, and remove markers on the map.
6. Persist geolocated data to Firestore with `GeoPoint`.

---

## Before You Start

Spread the work across the assigned time — don't leave it all for the day before the lab is due. A rough breakdown:

- **Walkthrough: Building SkyCast** — step-by-step lab building the real app while learning concepts. Budget about 90 minutes.

**Before you begin the lab, you should have:**

- Run every code example in Android Studio as you go.
- Completed the pre-topic quiz on Canvas (ungraded, just a self-check).

---

## The Story So Far...

In the previous topic, we implemented Room Database and DataStore for local offline caching of weather data and user preferences.

To continue the story, **open your existing Android Studio project from the previous topic**. We will be directly building upon the code you wrote previously. 

> 🆘 **Lost your code?** If your previous project is broken or missing, don't worry! You can download a clean starting point here: [Starter Project: topic_11_storage_room_datastore.zip](/downloads/topic_11_storage_room_datastore.zip). 

---

## Walkthrough: Building SkyCast

> 📁 **Target Project Reference (Completed Code)** — [topic_12_location_maps.zip](/downloads/topic_12_location_maps.zip)
>
> This project contains the complete, runnable SkyCast snapshot at Topic 12. Import into Android Studio and click Run.
>
> **Heads up:** The source files show the finished version of each step. Working through the walkthrough yourself first — then comparing to the download — is far more effective than reading the code directly.

SkyCast learns where the user is! We will ask for permission, read the GPS coordinates, and display saved cities on a Google Map.

### Step 1: Requesting Location Permissions

> **SkyCast Briefing:** Location access requires explicit user permission at runtime. Android's permission model has three outcomes: 1. Granted, 2. Denied, 3. Permanently Denied. We must handle all three.

First, add the permission to your `AndroidManifest.xml`:
```xml
<uses-permission android:name="android.permission.ACCESS_COARSE_LOCATION" />
```

Create `LocationWeatherButton.kt` in your `ui/home/` package:

```kotlin
package com.example.skycast.ui.home

import android.Manifest
import android.content.Intent
import android.content.pm.PackageManager
import android.net.Uri
import android.provider.Settings
import androidx.activity.compose.rememberLauncherForActivityResult
import androidx.activity.result.contract.ActivityResultContracts
import androidx.compose.foundation.layout.Column
import androidx.compose.material3.Button
import androidx.compose.material3.Text
import androidx.compose.runtime.*
import androidx.compose.ui.platform.LocalContext
import androidx.core.content.ContextCompat

@Composable
fun LocationWeatherButton(onGranted: (Double, Double) -> Unit) {
    val context = LocalContext.current
    var hasPermission by remember {
        mutableStateOf(
            ContextCompat.checkSelfPermission(
                context, 
                Manifest.permission.ACCESS_COARSE_LOCATION
            ) == PackageManager.PERMISSION_GRANTED
        )
    }
    
    val permissionLauncher = rememberLauncherForActivityResult(
        ActivityResultContracts.RequestPermission()
    ) { isGranted -> hasPermission = isGranted }

    if (hasPermission) {
        LocationFetcher(onLocation = onGranted)
    } else {
        Column {
            Text("SkyCast needs your location to show local weather.")
            Button(onClick = { 
                permissionLauncher.launch(Manifest.permission.ACCESS_COARSE_LOCATION) 
            }) {
                Text("Allow location")
            }
            Button(onClick = {
                // If permanently denied, direct them to Settings
                context.startActivity(
                    Intent(
                        Settings.ACTION_APPLICATION_DETAILS_SETTINGS,
                        Uri.fromParts("package", context.packageName, null)
                    )
                )
            }) { Text("Open Settings") }
        }
    }
}
```

---

### Step 2: The Fused Location Provider

> **SkyCast Briefing:** The Fused Location Provider combines GPS, Wi-Fi, and cell towers into a single, power-efficient location API. We will use `PRIORITY_BALANCED_POWER_ACCURACY` to save battery.

Add the Gradle dependency to `app/build.gradle.kts`:
```kotlin
implementation("com.google.android.gms:play-services-location:21.3.0")
```

Create `LocationFetcher.kt` in your `util/` package:

```kotlin
package com.example.skycast.util

import android.annotation.SuppressLint
import android.content.Context
import androidx.compose.runtime.Composable
import androidx.compose.runtime.LaunchedEffect
import androidx.compose.ui.platform.LocalContext
import com.google.android.gms.location.LocationServices
import com.google.android.gms.location.Priority
import com.google.android.gms.tasks.CancellationTokenSource
import kotlinx.coroutines.suspendCancellableCoroutine
import kotlin.coroutines.resume

@SuppressLint("MissingPermission") // Caller has already checked permission in Step 1
suspend fun getCurrentLocation(context: Context): Pair<Double, Double>? =
    suspendCancellableCoroutine { cont ->
        val cts = CancellationTokenSource()
        LocationServices.getFusedLocationProviderClient(context)
            .getCurrentLocation(Priority.PRIORITY_BALANCED_POWER_ACCURACY, cts.token)
            .addOnSuccessListener { loc ->
                cont.resume(loc?.let { it.latitude to it.longitude })
            }
            .addOnFailureListener { cont.resume(null) }
            
        cont.invokeOnCancellation { cts.cancel() }
    }

@Composable
fun LocationFetcher(onLocation: (Double, Double) -> Unit) {
    val context = LocalContext.current
    LaunchedEffect(Unit) {
        getCurrentLocation(context)?.let { (lat, lon) -> onLocation(lat, lon) }
    }
}
```

---

### Step 3: Integrating Location into the ViewModel

> **SkyCast Briefing:** We need to update our ViewModel to fetch the weather for the device's actual location!

Update `WeatherViewModel.kt`:

```kotlin
package com.example.skycast.ui.home

import android.content.Context
import androidx.lifecycle.ViewModel
import androidx.lifecycle.viewModelScope
import com.example.skycast.data.WeatherRepository
import com.example.skycast.util.getCurrentLocation
import kotlinx.coroutines.launch
import java.io.IOException

// ... existing code ...

    fun loadCurrentLocation(context: Context) = viewModelScope.launch {
        _uiState.value = WeatherUiState.Loading
        
        val coords = getCurrentLocation(context)
        if (coords == null) {
            _uiState.value = WeatherUiState.Error("Could not get location")
            return@launch
        }
        
        val (lat, lon) = coords
        _uiState.value = try {
            val report = repo.fetchWeather(lat, lon, "My Location")
            WeatherUiState.Success(report.current, report.forecast)
        } catch (e: IOException) { 
            WeatherUiState.Error("No connection") 
        }
    }
```

---

### Step 4: Google Maps Compose

> **SkyCast Briefing:** Google Maps Compose wraps the Maps SDK in a composable. We will plot all of the user's saved cities on an interactive map.

**Setup:**
1. Enable the Maps SDK for Android in Google Cloud Console.
2. Create an API key.
3. Put `MAPS_API_KEY=your_key_here` in your `local.properties` file.

**Gradle dependencies:**
```kotlin
implementation("com.google.maps.android:maps-compose:4.4.1")
implementation("com.google.android.gms:play-services-maps:19.0.0")
```

Create `SavedCitiesMap.kt` and `MapScreen.kt` in your `ui/map/` package:

```kotlin
package com.example.skycast.ui.map

import androidx.compose.foundation.layout.fillMaxSize
import androidx.compose.runtime.Composable
import androidx.compose.ui.Modifier
import com.example.skycast.data.SavedCity
import com.google.android.gms.maps.model.CameraPosition
import com.google.android.gms.maps.model.LatLng
import com.google.maps.android.compose.CameraPositionState
import com.google.maps.android.compose.GoogleMap
import com.google.maps.android.compose.MapProperties
import com.google.maps.android.compose.MapUiSettings
import com.google.maps.android.compose.Marker
import com.google.maps.android.compose.MarkerState
import com.google.maps.android.compose.rememberCameraPositionState

@Composable
fun SavedCitiesMap(cities: List<SavedCity>, onCityClick: (SavedCity) -> Unit) {
    val cameraState = rememberCameraPositionState {
        position = CameraPosition.fromLatLngZoom(LatLng(42.35, -71.06), 5f)
    }
    
    GoogleMap(
        modifier            = Modifier.fillMaxSize(),
        cameraPositionState = cameraState,
        properties          = MapProperties(isMyLocationEnabled = true),
        uiSettings          = MapUiSettings(myLocationButtonEnabled = true)
    ) {
        cities.forEach { city ->
            Marker(
                state   = MarkerState(LatLng(city.lat, city.lon)),
                title   = city.name,
                snippet = "Tap to view weather",
                onClick = { onCityClick(city); false }
            )
        }
    }
}
```

```kotlin
package com.example.skycast.ui.map

import androidx.compose.foundation.layout.Box
import androidx.compose.foundation.layout.padding
import androidx.compose.material3.Scaffold
import androidx.compose.material3.Text
import androidx.compose.runtime.Composable
import androidx.compose.runtime.getValue
import androidx.compose.ui.Alignment
import androidx.compose.ui.Modifier
import androidx.lifecycle.compose.collectAsStateWithLifecycle
import androidx.lifecycle.viewmodel.compose.viewModel
import com.example.skycast.ui.common.SkyCastTopBar

@Composable
fun MapScreen(
    vm: SavedCitiesViewModel = viewModel(),
    onCitySelected: (SavedCity) -> Unit,
    onBack: () -> Unit
) {
    val cities by vm.cities.collectAsStateWithLifecycle()
    
    Scaffold(topBar = {
        SkyCastTopBar("City Map", showBack = true, onBack = onBack)
    }) { padding ->
        Box(Modifier.padding(padding)) {
            if (cities.isEmpty()) {
                Text("Add cities to see them on the map", Modifier.align(Alignment.Center))
            } else {
                SavedCitiesMap(cities = cities, onCityClick = onCitySelected)
            }
        }
    }
}
```

---

### Step 5: Logging Weather Pins to Firestore

> **SkyCast Briefing:** To make this social, let's let users drop "Pins" on the map to log their current weather observations for others to see. We will save these geolocated pins to Firestore.

Create `WeatherPinsRepository.kt` in your `data/` package:

```kotlin
package com.example.skycast.data

import com.example.skycast.model.WeatherSnapshot
import com.google.firebase.firestore.Query
import com.google.firebase.firestore.ktx.firestore
import com.google.firebase.ktx.Firebase
import kotlinx.coroutines.channels.awaitClose
import kotlinx.coroutines.flow.Flow
import kotlinx.coroutines.flow.callbackFlow
import kotlinx.coroutines.tasks.await

data class WeatherPin(
    val id: String = "", 
    val lat: Double = 0.0, 
    val lon: Double = 0.0,
    val note: String = "", 
    val tempC: Double = 0.0, 
    val condition: String = "",
    val uid: String = "", 
    val createdAt: Long = System.currentTimeMillis()
)

class WeatherPinsRepository(private val uid: String) {
    private val pins = Firebase.firestore
        .collection("users").document(uid).collection("weatherPins")

    suspend fun addPin(lat: Double, lon: Double, snapshot: WeatherSnapshot, note: String) =
        pins.add(
            WeatherPin(
                lat = lat, lon = lon, note = note,
                tempC = snapshot.tempC, condition = snapshot.condition, uid = uid
            )
        ).await()

    fun observePins(): Flow<List<WeatherPin>> = callbackFlow {
        val reg = pins.orderBy("createdAt", Query.Direction.DESCENDING)
            .addSnapshotListener { snap, _ ->
                trySend(snap?.documents?.mapNotNull { doc ->
                    doc.toObject(WeatherPin::class.java)?.copy(id = doc.id)
                }.orEmpty())
            }
        awaitClose { reg.remove() }
    }
}
```

You can now plot `WeatherPin` objects on your `GoogleMap` using the exact same `Marker` approach!


## Guided Practice Challenges

Before diving into the full assignment, try these low-stakes practice challenges in Android Studio. They will build the exact muscle memory you need for maps and location.

### Challenge 1: The Polite Request (Runtime Permissions)
**The Scenario:** SkyCast crashes if it tries to read the location without asking first. We need to ask politely.
**The Task:** 
1. Add `<uses-permission android:name="android.permission.ACCESS_COARSE_LOCATION" />` to your manifest.
2. Create a `@Composable` that uses `rememberLauncherForActivityResult`.
3. Pass in `ActivityResultContracts.RequestPermission()`.
4. Add a button that calls `launcher.launch(Manifest.permission.ACCESS_COARSE_LOCATION)`. Test what happens when you click "Deny".

### Challenge 2: "Where Am I?" (Fused Location Provider)
**The Scenario:** Now that we have permission, we actually need to read the GPS chip.
**The Task:**
1. Write a `suspend fun getCurrentLocation(context: Context): Location?`.
2. Inside, use `LocationServices.getFusedLocationProviderClient(context)`.
3. Call `.getCurrentLocation(Priority.PRIORITY_BALANCED_POWER_ACCURACY, null)`.
4. Launch a coroutine to call your function, and print the resulting latitude and longitude to Logcat.

### Challenge 3: Dropping Pins (Google Maps Compose)
**The Scenario:** The UX team wants users to be able to drop pins on a map to report local rain.
**The Task:**
1. Enable the Maps SDK in Google Cloud Console and add your API key to `local.properties`.
2. Add a `GoogleMap` composable to your screen.
3. Pass an `onMapClick` lambda to `GoogleMap`. When clicked, add the resulting `LatLng` to a `remember { mutableStateListOf<LatLng>() }`.
4. Inside the `GoogleMap` content lambda, iterate over your list and draw a `Marker` for each one.

## References

1. [Request app permissions](https://developer.android.com/training/permissions/requesting)
2. [Get the last known location](https://developer.android.com/training/location/retrieve-current)
3. [Maps Compose](https://developers.google.com/maps/documentation/android-sdk/maps-compose)
4. [osmdroid](https://github.com/osmdroid/osmdroid)

---

## Getting Help

Because this course is fully asynchronous, here's how to get unstuck:

- **Piazza** is the primary help channel. Every topic has a dedicated thread. When asking a question, include: (1) what you're trying to do, (2) what you've tried, (3) the exact error message or Logcat output. Most questions get answered within a few hours.
- **TA office hours** — each TA hosts 1–2 hours per timeline on Zoom. Schedule is posted on Canvas. These are open-form drop-in sessions: show up, share your screen, get help.
- **Instructor office hours** — by appointment for deeper issues (design questions, project direction, grading questions).
- **On using AI tools:** The use of AI is not recommended at least for the first 6 modules, until you understand the basics of the development cycle. I do not ban using AI, but when you use AI, you should be able to answer any conceptual questions asked by the TAs or the professor. See the Academic Integrity policy on Canvas for specifics.
"""

with open("/Users/nsm/cs4520/lessons/Topic_12_Location_Maps.md", "w") as f:
    f.write(new_content)

print("Rewrote Topic 12 successfully!")
