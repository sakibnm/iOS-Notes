import os

new_content = """# Topic 15 — State Restoration, Testing, and Release Builds

**Estimated effort:** 6–8 hours this topic
**Format:** Asynchronous online — work at your own pace
**Prerequisites:** Topics 1–14

---

## Learning Objectives

By the end of this topic, students will be able to:

1. Use `rememberSaveable` and `SavedStateHandle` to preserve UI state across process death.
2. Identify and fix unnecessary recompositions using the Layout Inspector's recomposition counter.
3. Write Compose UI tests using `createComposeRule`, test tags, and common assertions.
4. Generate a signed release APK/AAB and understand the difference between debug and release builds.
5. Explain why process death differs from a configuration change and handle both correctly.
6. [Optional] Understand the role of the Play Integrity API in protecting app integrity.

---

## Before You Start

Spread the work across the assigned time — don't leave it all for the day before the lab is due. A rough breakdown:

- **Walkthrough: Building SkyCast** — step-by-step lab building the real app while learning concepts. Budget about 90 minutes.

**Before you begin the lab, you should have:**

- Run every code example in Android Studio as you go.
- Completed the pre-topic quiz on Canvas (ungraded, just a self-check).

---

## The Story So Far...

In the previous topic, we audited SkyCast for accessibility (adding TalkBack support) and added structured logging.

To continue the story, **open your existing Android Studio project from the previous topic**. We will be directly building upon the code you wrote previously. 

> 🆘 **Lost your code?** If your previous project is broken or missing, don't worry! You can download a clean starting point here: [Starter Project: topic_14_debugging_accessibility.zip](/downloads/topic_14_debugging_accessibility.zip). 

---

## Walkthrough: Building SkyCast

> 📁 **Target Project Reference (Completed Code)** — [topic_15_testing_state_restoration.zip](/downloads/topic_15_testing_state_restoration.zip)
>
> This project contains the complete, runnable SkyCast snapshot at Topic 15. Import into Android Studio and click Run.
>
> **Heads up:** The source files show the finished version of each step. Working through the walkthrough yourself first — then comparing to the download — is far more effective than reading the code directly.

SkyCast is complete. Now we harden it for release: fix state loss on process death, write UI tests, and produce a signed APK.

### Step 1: Surviving Process Death with rememberSaveable

> **SkyCast Briefing:** `remember` survives recomposition. `ViewModel` survives rotation. But when the app is backgrounded, Android might kill its process to free memory. Neither survives that! Only `rememberSaveable` and `SavedStateHandle` survive process death because they save to an OS bundle.

Update your `SearchScreen.kt`:

```kotlin
package com.example.skycast.ui.search

import androidx.compose.runtime.Composable
import androidx.compose.runtime.getValue
import androidx.compose.runtime.mutableStateOf
import androidx.compose.runtime.saveable.rememberSaveable
import androidx.compose.runtime.setValue
// ...

@Composable
fun SearchScreen(onCitySelected: (CityResult) -> Unit, onBack: () -> Unit) {
    // remember: survives recomposition, NOT rotation
    // rememberSaveable: survives rotation AND process death
    var query by rememberSaveable { mutableStateOf("") }
    
    // ... rest of the search screen using `query`
}
```

**Test:** Enable "Don't keep activities" in Developer Options → open Search → type a query → press Home → reopen. The query should still be there.

---

### Step 2: SavedStateHandle in the ViewModel

> **SkyCast Briefing:** For state stored in the ViewModel, we use `SavedStateHandle`. It gives the ViewModel access to the same saved state bundle.

Update `WeatherViewModel.kt`:

```kotlin
package com.example.skycast.ui.home

import androidx.lifecycle.SavedStateHandle
import androidx.lifecycle.ViewModel
import androidx.lifecycle.viewModelScope
import com.example.skycast.data.WeatherRepository
import kotlinx.coroutines.flow.StateFlow
import kotlinx.coroutines.launch

class WeatherViewModel(
    private val savedState: SavedStateHandle, // Injected automatically!
    private val repo: WeatherRepository = WeatherRepository()
) : ViewModel() {

    // This StateFlow is backed by the Bundle — survives process death
    val lastCity: StateFlow<String> =
        savedState.getStateFlow("last_city", "Boston")

    fun loadWeather(city: String) = viewModelScope.launch {
        savedState["last_city"] = city   // persisted across process death
        _uiState.value = WeatherUiState.Loading
        // ... fetch
    }

    init { 
        // The initial load restores exactly the city the user was viewing
        loadWeather(savedState.get<String>("last_city") ?: "Boston") 
    }
}
```

---

### Step 3: Compose UI Testing

> **SkyCast Briefing:** UI tests let you verify that screens behave correctly without running the app manually. They run on a device or emulator and exercise your composables directly.

Add dependencies to `app/build.gradle.kts`:
```kotlin
androidTestImplementation("androidx.compose.ui:ui-test-junit4")
debugImplementation("androidx.compose.ui:ui-test-manifest")
```

Create `WeatherScreenTest.kt` in the `androidTest` folder (not `test`):

```kotlin
package com.example.skycast

import androidx.compose.ui.test.assertIsDisplayed
import androidx.compose.ui.test.junit4.createComposeRule
import androidx.compose.ui.test.onNodeWithTag
import androidx.compose.ui.test.onNodeWithText
import androidx.compose.ui.test.performClick
import com.example.skycast.model.WeatherSnapshot
import com.example.skycast.ui.home.HomeScreen
import com.example.skycast.ui.home.WeatherUiState
import com.example.skycast.ui.theme.SkyCastTheme
import org.junit.Rule
import org.junit.Test

class WeatherScreenTest {
    @get:Rule val rule = createComposeRule()

    @Test
    fun loadingState_showsSpinner() {
        rule.setContent {
            SkyCastTheme {
                HomeScreen(
                    state = WeatherUiState.Loading, isCelsius = true,
                    onToggleUnit = {}, onSearchClick = {}
                )
            }
        }
        rule.onNodeWithTag("loading_indicator").assertIsDisplayed()
    }

    @Test
    fun successState_showsCityAndTemperature() {
        val snapshot = WeatherSnapshot("Boston", 18.5, 65, 22.0, "Partly cloudy")
        rule.setContent {
            SkyCastTheme {
                HomeScreen(
                    state = WeatherUiState.Success(snapshot, emptyList()), isCelsius = true,
                    onToggleUnit = {}, onSearchClick = {}
                )
            }
        }
        rule.onNodeWithText("Boston").assertIsDisplayed()
        rule.onNodeWithText("18.5°C").assertIsDisplayed()
    }
}
```

Make sure your UI actually has `Modifier.testTag("loading_indicator")` on the `CircularProgressIndicator`!

---

### Step 4: Release Builds and Signing

> **SkyCast Briefing:** Debug and release builds are different. Release builds require a cryptographic signature (keystore), strip out logs, and run an obfuscator (ProGuard) to shrink the code.

**Create a Keystore:**
Go to **Build → Generate Signed Bundle / APK** → APK. Create a keystore, give it a password and alias. **Never commit the keystore file to Git.**

Automate signing in `app/build.gradle.kts` (useful for CI/CD):
```kotlin
android {
    signingConfigs {
        create("release") {
            storeFile = file(System.getenv("KEYSTORE_PATH") ?: "release.keystore")
            storePassword = System.getenv("KEYSTORE_PASSWORD") ?: ""
            keyAlias = System.getenv("KEY_ALIAS") ?: ""
            keyPassword = System.getenv("KEY_PASSWORD") ?: ""
        }
    }
    buildTypes {
        release {
            signingConfig = signingConfigs.getByName("release")
            isMinifyEnabled = true
            proguardFiles(
                getDefaultProguardFile("proguard-android-optimize.txt"),
                "proguard-rules.pro"
            )
        }
    }
}
```

Add rules to `proguard-rules.pro` so ProGuard doesn't break Retrofit/Moshi:
```pro
-keep class com.squareup.moshi.** { *; }
-keepclassmembers class * { @com.squareup.moshi.Json <fields>; }
-keep,allowobfuscation interface * { @retrofit2.http.* <methods>; }
-keep class com.example.skycast.data.** { *; }
```

**(Optional) Play Integrity API Check**
If you want to ensure the app hasn't been pirated or rooted, you can request an Integrity Token:
```kotlin
// Gradle: implementation("com.google.android.play:integrity:1.3.0")
val integrityManager = IntegrityManagerFactory.create(context)
val request = IntegrityTokenRequest.builder()
    .setCloudProjectNumber(123456789) // From GCP
    .setNonce("a_random_nonce_from_your_server") // Prevent replay
    .build()

integrityManager.requestIntegrityToken(request)
    .addOnSuccessListener { response -> val token = response.token() /* send to backend */ }
```

### Final Release Checklist

Build a signed APK:
```bash
./gradlew assembleRelease
adb install -r app/build/outputs/apk/release/app-release.apk
```

- [ ] All API calls target the real Open-Meteo base URL (no localhost)
- [ ] `google-services.json` points to the production Firebase project
- [ ] No `Log.d` output in Logcat when running the release build
- [ ] TalkBack announces every weather card meaningfully
- [ ] The last-viewed city is restored after process death (`SavedStateHandle`)
- [ ] APK installs on a fresh emulator without developer mode


## Guided Practice Challenges

Before diving into the full assignment, try these low-stakes practice challenges in Android Studio. They will build the exact muscle memory you need for polishing and releasing an app.

### Challenge 1: The Doomsday Test (Process Death)
**The Scenario:** A user types half a search query, switches to a messaging app, and when they return, their typing is gone.
**The Task:** 
1. Enable "Don't keep activities" in your device's Developer Options.
2. Run the app, type in a text field (using a plain `remember { mutableStateOf("") }`), press Home, then open the app again. See it vanish.
3. Change the `remember` to `rememberSaveable`.
4. Repeat step 2. Marvel at your indestructible state. (Disable "Don't keep activities" when you're done!)

### Challenge 2: The Robot User (Compose UI Tests)
**The Scenario:** Manual testing is tedious. We need a robot to verify the UI.
**The Task:**
1. Create a file in `androidTest`.
2. Write a test function annotated with `@Test`.
3. Add `@get:Rule val rule = createComposeRule()`.
4. Inside the test, call `rule.setContent { Text("Hello World") }`, then write `rule.onNodeWithText("Hello World").assertIsDisplayed()`.
5. Run the test by clicking the green arrow next to the function.

### Challenge 3: The Golden Ticket (Release Keystore)
**The Scenario:** We need a cryptographically signed version of SkyCast to distribute.
**The Task:**
1. In Android Studio, go to Build -> Generate Signed Bundle / APK. Select APK.
2. Click "Create new..." and make a keystore. Use a simple password and alias for this class.
3. Finish the wizard to build the `app-release.apk`.
4. Open the `app/build/outputs/apk/release` folder in your file explorer to verify the file was created.

## References

1. [Save UI state (rememberSaveable)](https://developer.android.com/jetpack/compose/state#restore-ui-state)
2. [SavedStateHandle](https://developer.android.com/topic/libraries/architecture/viewmodel/viewmodel-savedstate)
3. [Testing your Compose layout](https://developer.android.com/jetpack/compose/testing)
4. [Sign your app](https://developer.android.com/studio/publish/app-signing)

---

## Getting Help

Because this course is fully asynchronous, here's how to get unstuck:

- **Piazza** is the primary help channel. Every topic has a dedicated thread. When asking a question, include: (1) what you're trying to do, (2) what you've tried, (3) the exact error message or Logcat output. Most questions get answered within a few hours.
- **TA office hours** — each TA hosts 1–2 hours per timeline on Zoom. Schedule is posted on Canvas. These are open-form drop-in sessions: show up, share your screen, get help.
- **Instructor office hours** — by appointment for deeper issues (design questions, project direction, grading questions).
- **On using AI tools:** The use of AI is not recommended at least for the first 6 modules, until you understand the basics of the development cycle. I do not ban using AI, but when you use AI, you should be able to answer any conceptual questions asked by the TAs or the professor. See the Academic Integrity policy on Canvas for specifics.
"""

with open("/Users/nsm/cs4520/lessons/Topic_15_Project_Work_Polish_Testing.md", "w") as f:
    f.write(new_content)

print("Rewrote Topic 15 successfully!")
