import os

new_content = """# Topic 10 — Firebase Authentication and Cloud Firestore

**Estimated effort:** 7–9 hours this topic
**Format:** Asynchronous online — work at your own pace
**Prerequisites:** Topics 1–8

---

## Learning Objectives

By the end of this session, students will be able to:

1. Create a Firebase project, register an Android app, and add `google-services.json`.
2. Implement email/password sign-up, sign-in, and sign-out using FirebaseAuth.
3. Observe authentication state and gate content on whether a user is signed in.
4. Read and write documents in Cloud Firestore.
5. Query Firestore with `where`, `orderBy`, and `limit`.
6. Subscribe to real-time updates with a `SnapshotListener` exposed as a `Flow`.
7. Write basic Firestore security rules to restrict access to the signed-in user's data.

---

## Before You Start

Spread the work across the assigned time — don't leave it all for the day before the lab is due. A rough breakdown:

- **Walkthrough: Building SkyCast** — step-by-step lab building the real app while learning concepts. Budget about 90 minutes.

**Before you begin the lab, you should have:**

- Run every code example in Android Studio as you go.
- Completed the pre-topic quiz on Canvas (ungraded, just a self-check).

---

## The Story So Far...

In the previous topic, we parsed real JSON responses using Kotlinx Serialization and handled robust API errors.

To continue the story, **open your existing Android Studio project from the previous topic**. We will be directly building upon the code you wrote previously. 

> 🆘 **Lost your code?** If your previous project is broken or missing, don't worry! You can download a clean starting point here: [Starter Project: topic_09_json_robust_apis.zip](/downloads/topic_09_json_robust_apis.zip). 

---

## Walkthrough: Building SkyCast

> 📁 **Target Project Reference (Completed Code)** — [topic_10_firebase.zip](/downloads/topic_10_firebase.zip)
>
> This project contains the complete, runnable SkyCast snapshot at Topic 10. Import into Android Studio and click Run.
>
> **Heads up:** The source files show the finished version of each step. Working through the walkthrough yourself first — then comparing to the download — is far more effective than reading the code directly.

SkyCast adds user accounts this topic so saved cities sync across all of a user's devices.

### Step 1: Firebase Setup

> **SkyCast Briefing:** Firebase is Google's Backend-as-a-Service platform. We will use Firebase Authentication (sign-in) and Cloud Firestore (database).

**Firebase Console Setup:**
1. Go to `console.firebase.google.com` and click **Add project**. Give it a name (e.g., `skycast-yourname`).
2. Click the Android icon to add an Android app. Enter your app's package name (from `app/build.gradle.kts` under `applicationId`).
3. Download `google-services.json` and place it in the `app/` directory of your project.
4. Go to **Authentication** → **Sign-in method** → enable **Email/Password**.
5. Go to **Firestore Database** → **Create Database** (start in test mode for now).

Now, update your Gradle files to pull in the Firebase SDKs using the BOM (Bill of Materials), which ensures all Firebase libraries are compatible versions.

```kotlin
// Project-level build.gradle.kts
plugins { 
    // Add the Google Services plugin
    id("com.google.gms.google-services") version "4.4.2" apply false 
}
```

```kotlin
// app-level build.gradle.kts
plugins { 
    id("com.google.gms.google-services") 
}

dependencies {
    implementation(platform("com.google.firebase:firebase-bom:33.5.1"))
    implementation("com.google.firebase:firebase-auth-ktx")
    implementation("com.google.firebase:firebase-firestore-ktx")
    implementation("org.jetbrains.kotlinx:kotlinx-coroutines-play-services:1.8.1")
}
```

---

### Step 2: Authentication Repository

> **SkyCast Briefing:** Firebase Auth handles user accounts. We will use email/password sign-in. To keep our code clean, we will wrap the callback-based Firebase listener in a Kotlin `Flow` inside a Repository.

Create `AuthRepository.kt` in your `data/` package:

```kotlin
package com.example.skycast.data

import com.google.firebase.auth.FirebaseAuth
import com.google.firebase.auth.FirebaseUser
import kotlinx.coroutines.channels.awaitClose
import kotlinx.coroutines.flow.Flow
import kotlinx.coroutines.flow.callbackFlow
import kotlinx.coroutines.tasks.await

class AuthRepository {
    private val auth = FirebaseAuth.getInstance()
    
    val currentUser: FirebaseUser? get() = auth.currentUser

    fun observeAuthState(): Flow<FirebaseUser?> = callbackFlow {
        val listener = FirebaseAuth.AuthStateListener { auth ->
            trySend(auth.currentUser)
        }
        auth.addAuthStateListener(listener)
        awaitClose { auth.removeAuthStateListener(listener) }
    }

    suspend fun signUp(email: String, password: String): Result<FirebaseUser> =
        runCatching { 
            auth.createUserWithEmailAndPassword(email, password).await().user!! 
        }

    suspend fun signIn(email: String, password: String): Result<FirebaseUser> =
        runCatching { 
            auth.signInWithEmailAndPassword(email, password).await().user!! 
        }

    fun signOut() = auth.signOut()
}
```

##### Code Breakdown: AuthRepository
- `callbackFlow` adapts the callback-based Firebase listener to a Kotlin Flow. 
- `awaitClose { }` cleans up the listener when the Flow is cancelled (e.g., when the app goes into the background).
- `runCatching` is a Kotlin standard library function that executes the block and returns a `Result.success` or `Result.failure`.

---

### Step 3: Auth ViewModel and State

> **SkyCast Briefing:** We need to expose this authentication state to the UI so we can gate access to the app (i.e., show the Login Screen if signed out, or the Dashboard if signed in).

Create `AuthViewModel.kt` in your `ui/auth/` package:

```kotlin
package com.example.skycast.ui.auth

import androidx.lifecycle.ViewModel
import androidx.lifecycle.viewModelScope
import com.example.skycast.data.AuthRepository
import kotlinx.coroutines.flow.SharingStarted
import kotlinx.coroutines.flow.StateFlow
import kotlinx.coroutines.flow.map
import kotlinx.coroutines.flow.stateIn
import kotlinx.coroutines.launch

sealed class AuthState {
    data object Loading   : AuthState()
    data object SignedOut : AuthState()
    data class SignedIn(val uid: String, val email: String?) : AuthState()
}

class AuthViewModel(
    private val repo: AuthRepository = AuthRepository()
) : ViewModel() {

    val authState: StateFlow<AuthState> = repo.observeAuthState()
        .map { user ->
            if (user == null) AuthState.SignedOut 
            else AuthState.SignedIn(user.uid, user.email)
        }
        .stateIn(
            scope = viewModelScope, 
            started = SharingStarted.WhileSubscribed(5_000), 
            initialValue = AuthState.Loading
        )

    fun signIn(email: String, password: String) = viewModelScope.launch {
        repo.signIn(email, password)
    }
    
    fun signUp(email: String, password: String) = viewModelScope.launch {
        repo.signUp(email, password)
    }
    
    fun signOut() = repo.signOut()
}
```

---

### Step 4: Storing Data in Cloud Firestore

> **SkyCast Briefing:** Firestore is a NoSQL document database organised as collections of documents. Think of a collection as a table and a document as a row. We want to save our users' favorite cities.

Create `SavedCitiesRepository.kt` in your `data/` package:

```kotlin
package com.example.skycast.data

import com.example.skycast.model.CityResult
import com.google.firebase.firestore.FirebaseFirestore
import com.google.firebase.firestore.Query
import com.google.firebase.firestore.ktx.firestore
import com.google.firebase.ktx.Firebase
import kotlinx.coroutines.channels.awaitClose
import kotlinx.coroutines.flow.Flow
import kotlinx.coroutines.flow.callbackFlow
import kotlinx.coroutines.tasks.await

data class SavedCity(
    val id:      String = "",
    val name:    String = "",
    val lat:     Double = 0.0,
    val lon:     Double = 0.0,
    val addedAt: Long   = System.currentTimeMillis()
)

class SavedCitiesRepository(private val uid: String) {
    // Structure: users / {uid} / savedCities / {cityDocument}
    private val collection = Firebase.firestore.collection("users")
        .document(uid).collection("savedCities")

    fun observeCities(): Flow<List<SavedCity>> = callbackFlow {
        val registration = collection.orderBy("addedAt", Query.Direction.ASCENDING)
            .addSnapshotListener { snapshot, error ->
                if (error != null) { 
                    close(error)
                    return@addSnapshotListener 
                }
                
                val cities = snapshot?.documents?.mapNotNull { doc ->
                    doc.toObject(SavedCity::class.java)?.copy(id = doc.id)
                }.orEmpty()
                
                trySend(cities)
            }
        awaitClose { registration.remove() }
    }

    suspend fun add(city: CityResult) {
        val newCity = SavedCity(name = city.name, lat = city.lat, lon = city.lon)
        collection.add(newCity).await()
    }

    suspend fun remove(cityId: String) {
        collection.document(cityId).delete().await()
    }
}
```

##### Code Breakdown: SavedCitiesRepository
- The `addSnapshotListener` fires immediately with the current data, then again whenever any document matching your query changes. You get real-time sync across all devices for free!

---

### Step 5: Securing the Database

> **SkyCast Briefing:** Security rules control who can read and write what in Firestore. Without rules, anyone who gets hold of your `google-services.json` can read and write your entire database!

Go to **Firestore** → **Rules** in the Firebase console. Write rules to ensure users can only access their own data:

```javascript
rules_version = '2';
service cloud.firestore {
  match /databases/{database}/documents {
    match /users/{uid}/savedCities/{cityId} {
      allow read, write: if request.auth != null && request.auth.uid == uid;
    }
  }
}
```

- Without this rule, any signed-in user could read or modify any other user's city list.
- `request.auth.uid == uid` ensures each user can only access their own path in the database.

---

## Guided Practice Challenges

Before diving into the full assignment, try these low-stakes practice challenges in Android Studio. They will build the exact muscle memory you need for interacting with Firebase.

### Challenge 1: The Bouncer (`FirebaseAuth`)
**The Scenario:** We need to know if the user is signed in so we can decide whether to show them the dashboard or the login screen.
**The Task:** 
1. Use `FirebaseAuth.getInstance()` to get the Auth instance.
2. Write a `val authState = callbackFlow { ... }` that listens to `AuthStateListener`.
3. Make sure to call `trySend(it.currentUser)` inside the listener.
4. Don't forget `awaitClose { auth.removeAuthStateListener(...) }` at the end!

### Challenge 2: The Live Database (`addSnapshotListener`)
**The Scenario:** When a user saves a city on their phone, it should immediately appear on their tablet.
**The Task:**
1. Given a Firestore collection reference `val col = Firebase.firestore.collection("savedCities")`.
2. Write a `callbackFlow` to observe real-time updates using `addSnapshotListener`.
3. Inside the listener, map the documents to a list of strings: `snapshot?.documents?.map { it.id }`.
4. Send the list to the flow.

### Challenge 3: Lockdown (`firestore.rules`)
**The Scenario:** Right now, anyone with our API key can delete everyone else's saved cities!
**The Task:**
1. Open the Firebase console and navigate to Firestore -> Rules.
2. Write a rule that ensures a user can only read/write documents in the `/users/{uid}/savedCities/{cityId}` path if `request.auth.uid == uid`.
3. Use the Rules Playground in the console to simulate a read with an incorrect UID. Verify it gets denied.

## References

1. [Add Firebase to your Android project](https://firebase.google.com/docs/android/setup)
2. [Firebase Authentication on Android](https://firebase.google.com/docs/auth/android/start)
3. [Get started with Cloud Firestore](https://firebase.google.com/docs/firestore/quickstart)
4. [Get started with Firebase Security Rules](https://firebase.google.com/docs/rules/get-started)

---

## Getting Help

Because this course is fully asynchronous, here's how to get unstuck:

- **Piazza** is the primary help channel. Every topic has a dedicated thread. When asking a question, include: (1) what you're trying to do, (2) what you've tried, (3) the exact error message or Logcat output. Most questions get answered within a few hours.
- **TA office hours** — each TA hosts 1–2 hours per timeline on Zoom. Schedule is posted on Canvas. These are open-form drop-in sessions: show up, share your screen, get help.
- **Instructor office hours** — by appointment for deeper issues (design questions, project direction, grading questions).
- **On using AI tools:** The use of AI is not recommended at least for the first 6 modules, until you understand the basics of the development cycle. I do not ban using AI, but when you use AI, you should be able to answer any conceptual questions asked by the TAs or the professor. See the Academic Integrity policy on Canvas for specifics.
"""

with open("/Users/nsm/cs4520/lessons/Topic_10_Firebase_Auth_Firestore.md", "w") as f:
    f.write(new_content)

print("Rewrote Topic 10 successfully!")
