import os

new_content = """# Topic 13 — CameraX, Images, and Compose Animations

**Estimated effort:** 7–9 hours this topic
**Format:** Asynchronous online — work at your own pace
**Prerequisites:** Topics 1–12

---

## Learning Objectives

By the end of this session, students will be able to:

1. Pick images and videos using the Android Photo Picker (no permission needed).
2. Capture photos using CameraX with a Compose preview.
3. Load remote images efficiently with Coil, including placeholders and error states.
4. Apply Material 3 dynamic color and theming.
5. Animate visibility, size, and position with `AnimatedVisibility`, `animateContentSize`, and `animate*AsState`.
6. Use `AnimatedContent` for smooth transitions between states.

---

## Before You Start

Spread the work across the assigned time — don't leave it all for the day before the lab is due. A rough breakdown:

- **Walkthrough: Building SkyCast** — step-by-step lab building the real app while learning concepts. Budget about 90 minutes.

**Before you begin the lab, you should have:**

- Run every code example in Android Studio as you go.
- Completed the pre-topic quiz on Canvas (ungraded, just a self-check).

---

## The Story So Far...

In the previous topic, we added location permissions and integrated Google Maps to show the user's current weather context.

To continue the story, **open your existing Android Studio project from the previous topic**. We will be directly building upon the code you wrote previously. 

> 🆘 **Lost your code?** If your previous project is broken or missing, don't worry! You can download a clean starting point here: [Starter Project: topic_12_location_maps.zip](/downloads/topic_12_location_maps.zip). 

---

## Walkthrough: Building SkyCast

> 📁 **Target Project Reference (Completed Code)** — [topic_13_camerax_animations.zip](/downloads/topic_13_camerax_animations.zip)
>
> This project contains the complete, runnable SkyCast snapshot at Topic 13. Import into Android Studio and click Run.
>
> **Heads up:** The source files show the finished version of each step. Working through the walkthrough yourself first — then comparing to the download — is far more effective than reading the code directly.

SkyCast gets visual polish: animated weather icons, smooth state transitions, a camera weather-log feature, and Material You dynamic color.

### Step 1: The Modern Photo Picker

> **SkyCast Briefing:** The Android Photo Picker (API 19+) lets users select images or videos without requiring `READ_MEDIA_IMAGES` permission. The system scopes access to only the selected item.

Create `WeatherPhotoLogButton.kt` in your `ui/home/` package:

```kotlin
package com.example.skycast.ui.home

import android.net.Uri
import androidx.activity.compose.rememberLauncherForActivityResult
import androidx.activity.result.PickVisualMediaRequest
import androidx.activity.result.contract.ActivityResultContracts
import androidx.compose.foundation.layout.Spacer
import androidx.compose.foundation.layout.width
import androidx.compose.material.icons.Icons
import androidx.compose.material.icons.filled.AddAPhoto
import androidx.compose.material3.FilledTonalButton
import androidx.compose.material3.Icon
import androidx.compose.material3.Text
import androidx.compose.runtime.Composable
import androidx.compose.ui.Modifier
import androidx.compose.ui.unit.dp

@Composable
fun WeatherPhotoLogButton(onPhotoSelected: (Uri) -> Unit) {
    val launcher = rememberLauncherForActivityResult(
        ActivityResultContracts.PickVisualMedia()
    ) { uri -> uri?.let(onPhotoSelected) }

    FilledTonalButton(onClick = {
        launcher.launch(
            PickVisualMediaRequest(ActivityResultContracts.PickVisualMedia.ImageOnly)
        )
    }) {
        Icon(Icons.Default.AddAPhoto, contentDescription = null)
        Spacer(Modifier.width(8.dp))
        Text("Log weather photo")
    }
}
```

---

### Step 2: Displaying Remote Images with Coil

> **SkyCast Briefing:** Coil is a Kotlin-first image loading library for Android. It handles caching, placeholders, and error states automatically.

Add the Gradle dependency to `app/build.gradle.kts`:
```kotlin
implementation("io.coil-kt:coil-compose:2.7.0")
```

Create `WeatherIcon.kt` in your `ui/common/` package to load free weather icons from OpenWeatherMap:

```kotlin
package com.example.skycast.ui.common

import androidx.compose.foundation.layout.size
import androidx.compose.runtime.Composable
import androidx.compose.ui.Modifier
import androidx.compose.ui.layout.ContentScale
import androidx.compose.ui.platform.LocalContext
import androidx.compose.ui.unit.dp
import coil.compose.AsyncImage
import coil.request.ImageRequest

// OpenWeatherMap hosts a free icon set — no API key needed for the images alone.
// Icon URL: https://openweathermap.org/img/wn/{code}@2x.png

@Composable
fun WeatherIcon(iconCode: String, description: String, modifier: Modifier = Modifier) {
    AsyncImage(
        model = ImageRequest.Builder(LocalContext.current)
            .data("https://openweathermap.org/img/wn/$iconCode@2x.png")
            .crossfade(true)
            .build(),
        contentDescription = description,
        modifier           = modifier.size(64.dp),
        contentScale       = ContentScale.Fit
    )
}
```

---

### Step 3: Taking Photos with CameraX

> **SkyCast Briefing:** CameraX is Jetpack's camera library. It abstracts away the complexity of the old Camera2 API and works consistently across Android devices.

**Gradle:**
```kotlin
implementation("androidx.camera:camera-camera2:1.3.4")
implementation("androidx.camera:camera-lifecycle:1.3.4")
implementation("androidx.camera:camera-view:1.3.4")
```

**Camera permission in AndroidManifest.xml:**
```xml
<uses-permission android:name="android.permission.CAMERA" />
```

Create `WeatherCameraCapture.kt` in your `ui/camera/` package:

```kotlin
package com.example.skycast.ui.camera

import android.net.Uri
import androidx.camera.core.CameraSelector
import androidx.camera.core.ImageCapture
import androidx.camera.core.ImageCaptureException
import androidx.camera.core.Preview
import androidx.camera.lifecycle.ProcessCameraProvider
import androidx.camera.view.PreviewView
import androidx.compose.foundation.layout.*
import androidx.compose.material3.Button
import androidx.compose.material3.OutlinedButton
import androidx.compose.material3.Text
import androidx.compose.runtime.*
import androidx.compose.ui.Alignment
import androidx.compose.ui.Modifier
import androidx.compose.ui.platform.LocalContext
import androidx.compose.ui.platform.LocalLifecycleOwner
import androidx.compose.ui.unit.dp
import androidx.compose.ui.viewinterop.AndroidView
import androidx.core.content.ContextCompat
import kotlinx.coroutines.guava.await
import java.io.File

@Composable
fun WeatherCameraCapture(onPhotoCaptured: (Uri) -> Unit, onDismiss: () -> Unit) {
    val context        = LocalContext.current
    val lifecycleOwner = LocalLifecycleOwner.current
    val previewView    = remember { PreviewView(context) }
    val imageCapture   = remember { ImageCapture.Builder().build() }

    LaunchedEffect(Unit) {
        val provider = ProcessCameraProvider.getInstance(context).await()
        val preview  = Preview.Builder().build()
            .also { it.setSurfaceProvider(previewView.surfaceProvider) }
        
        provider.unbindAll()
        provider.bindToLifecycle(
            lifecycleOwner, 
            CameraSelector.DEFAULT_BACK_CAMERA, 
            preview, 
            imageCapture
        )
    }

    Box(Modifier.fillMaxSize()) {
        AndroidView({ previewView }, Modifier.fillMaxSize())
        
        Row(
            Modifier.align(Alignment.BottomCenter).padding(24.dp),
            horizontalArrangement = Arrangement.spacedBy(16.dp)
        ) {
            OutlinedButton(onClick = onDismiss) { Text("Cancel") }
            Button(onClick = {
                val file = File(context.cacheDir, "obs_${System.currentTimeMillis()}.jpg")
                imageCapture.takePicture(
                    ImageCapture.OutputFileOptions.Builder(file).build(),
                    ContextCompat.getMainExecutor(context),
                    object : ImageCapture.OnImageSavedCallback {
                        override fun onImageSaved(r: ImageCapture.OutputFileResults) {
                            onPhotoCaptured(Uri.fromFile(file))
                        }
                        override fun onError(e: ImageCaptureException) {}
                    }
                )
            }) { Text("Capture") }
        }
    }
}
```

---

### Step 4: Compose Animations

> **SkyCast Briefing:** Compose has a rich animation API. We will use `AnimatedContent` to crossfade between weather conditions, and `animateContentSize()` to smoothly expand a card.

Update your `WeatherCard.kt`:

```kotlin
package com.example.skycast.ui.home

import androidx.compose.animation.*
import androidx.compose.animation.core.tween
import androidx.compose.foundation.clickable
import androidx.compose.foundation.layout.*
import androidx.compose.material.icons.Icons
import androidx.compose.material.icons.filled.ExpandLess
import androidx.compose.material.icons.filled.ExpandMore
import androidx.compose.material3.*
import androidx.compose.runtime.*
import androidx.compose.ui.Alignment
import androidx.compose.ui.Modifier
import androidx.compose.ui.unit.dp
import com.example.skycast.model.WeatherCondition

@Composable
fun AnimatedWeatherDisplay(
    condition: WeatherCondition,
    tempC: Double,
    isCelsius: Boolean
) {
    AnimatedContent(
        targetState = condition,
        transitionSpec = {
            (fadeIn(tween(600)) + scaleIn(tween(600), initialScale = 0.9f)) togetherWith
            (fadeOut(tween(300)) + scaleOut(tween(300), targetScale = 0.9f))
        },
        label = "weather_transition"
    ) { cond ->
        Column(
            horizontalAlignment = Alignment.CenterHorizontally,
            modifier = Modifier.padding(24.dp)
        ) {
            Text(cond.emoji(), style = MaterialTheme.typography.displayLarge)
            Text(
                if (isCelsius) "${"%.1f".format(tempC)}°C"
                else           "${"%.1f".format(tempC * 9/5 + 32)}°F",
                style = MaterialTheme.typography.displayMedium
            )
            Text(cond.description(), style = MaterialTheme.typography.bodyLarge)
        }
    }
}

@Composable
fun ExpandableRainDetails(rain: WeatherCondition.Rain) {
    var expanded by remember { mutableStateOf(false) }
    
    Card(
        Modifier
            .fillMaxWidth()
            .animateContentSize()
            .clickable { expanded = !expanded }
    ) {
        Column(Modifier.padding(16.dp)) {
            Row(verticalAlignment = Alignment.CenterVertically) {
                Text("Rain details", Modifier.weight(1f))
                Icon(
                    if (expanded) Icons.Default.ExpandLess else Icons.Default.ExpandMore,
                    if (expanded) "Collapse" else "Expand"
                )
            }
            
            if (expanded) {
                Spacer(Modifier.height(8.dp))
                Text("Intensity: ${rain.mmPerHour} mm/h")
                LinearProgressIndicator(
                    progress = { (rain.mmPerHour / 10f).coerceIn(0f, 1f) },
                    modifier = Modifier.fillMaxWidth().padding(top = 8.dp)
                )
            }
        }
    }
}
```

---

### Step 5: Material 3 Dynamic Color

> **SkyCast Briefing:** Material 3 introduces *dynamic color* — on Android 12+ the system extracts a color scheme from the user's wallpaper and your app adopts it automatically.

Update `Theme.kt` in your `ui/theme/` package:

```kotlin
package com.example.skycast.ui.theme

import android.os.Build
import androidx.compose.foundation.isSystemInDarkTheme
import androidx.compose.material3.*
import androidx.compose.runtime.Composable
import androidx.compose.ui.graphics.Color
import androidx.compose.ui.platform.LocalContext

@Composable
fun SkyCastTheme(
    darkTheme: Boolean = isSystemInDarkTheme(),
    dynamicColor: Boolean = true,
    content: @Composable () -> Unit
) {
    val colorScheme = when {
        // Dynamic color is available on Android 12+
        dynamicColor && Build.VERSION.SDK_INT >= Build.VERSION_CODES.S -> {
            val ctx = LocalContext.current
            if (darkTheme) dynamicDarkColorScheme(ctx) else dynamicLightColorScheme(ctx)
        }
        darkTheme -> darkColorScheme(
            primary = Color(0xFF90CAF9), 
            secondary = Color(0xFF80DEEA),
            background = Color(0xFF1A237E)
        )
        else -> lightColorScheme(
            primary = Color(0xFF1565C0), 
            secondary = Color(0xFF0288D1),
            background = Color(0xFFF0F4FF)
        )
    }
    
    MaterialTheme(colorScheme = colorScheme, content = content)
}
```


## Guided Practice Challenges

Before diving into the full assignment, try these low-stakes practice challenges in Android Studio. They will build the exact muscle memory you need for rich media and animations.

### Challenge 1: The Modern Gallery (`PickVisualMedia`)
**The Scenario:** SkyCast needs a way for users to upload screenshots of extreme weather, but we don't want to ask for invasive file permissions.
**The Task:** 
1. Create a `rememberLauncherForActivityResult(ActivityResultContracts.PickVisualMedia())`.
2. Add a `Button` that calls `launcher.launch(PickVisualMediaRequest(ActivityResultContracts.PickVisualMedia.ImageOnly))`.
3. When the user picks an image, load the `Uri` into an `AsyncImage` (using Coil).

### Challenge 2: The Viewfinder (`CameraX`)
**The Scenario:** Users want to take photos of storms in real time directly from the app.
**The Task:**
1. Look at Snippet 3.
2. Build the `WeatherCameraCapture` composable.
3. Test it on a physical device. Make sure the preview rotates correctly when you turn the phone.

### Challenge 3: Making It Pop (`AnimatedVisibility` & `animateContentSize`)
**The Scenario:** The weather cards snap open abruptly when tapped, making the app feel cheap. We need it to feel premium.
**The Task:**
1. Create a `Card` containing a title and some "extra details" text.
2. Add a `var expanded by remember { mutableStateOf(false) }` and toggle it when the Card is clicked.
3. Wrap the "extra details" text in `AnimatedVisibility(visible = expanded)`.
4. Add `Modifier.animateContentSize()` to the `Card` itself so the card smoothly grows to accommodate the appearing text.

## References

1. [Photo picker](https://developer.android.com/training/data-storage/shared/photopicker)
2. [CameraX overview](https://developer.android.com/training/camerax)
3. [Coil](https://coil-kt.github.io/coil/)
4. [Animations in Compose](https://developer.android.com/jetpack/compose/animation)
5. [Material Design 3 dynamic color](https://m3.material.io/styles/color/dynamic-color/overview)

---

## Getting Help

Because this course is fully asynchronous, here's how to get unstuck:

- **Piazza** is the primary help channel. Every topic has a dedicated thread. When asking a question, include: (1) what you're trying to do, (2) what you've tried, (3) the exact error message or Logcat output. Most questions get answered within a few hours.
- **TA office hours** — each TA hosts 1–2 hours per timeline on Zoom. Schedule is posted on Canvas. These are open-form drop-in sessions: show up, share your screen, get help.
- **Instructor office hours** — by appointment for deeper issues (design questions, project direction, grading questions).
- **On using AI tools:** The use of AI is not recommended at least for the first 6 modules, until you understand the basics of the development cycle. I do not ban using AI, but when you use AI, you should be able to answer any conceptual questions asked by the TAs or the professor. See the Academic Integrity policy on Canvas for specifics.
"""

with open("/Users/nsm/cs4520/lessons/Topic_13_CameraX_Animations.md", "w") as f:
    f.write(new_content)

print("Rewrote Topic 13 successfully!")
