import os

new_content = """# Topic 11 — Firebase Storage I and Local Persistence with Room & DataStore

**Estimated effort:** 7–9 hours this topic
**Format:** Asynchronous online — work at your own pace
**Prerequisites:** Topics 1–9

---

## Learning Objectives

By the end of this session, students will be able to:

1. Upload and download files (especially images) using Firebase Cloud Storage.
2. Generate and display a download URL securely.
3. Define a Room database with entities, a DAO, and migrations.
4. Observe a Room table as a `Flow` to drive reactive UI.
5. Use DataStore Preferences for small key-value settings.
6. Decide when to use cloud (Firestore/Storage) vs local (Room/DataStore) persistence.

---

## Before You Start

Spread the work across the assigned time — don't leave it all for the day before the lab is due. A rough breakdown:

- **Walkthrough: Building SkyCast** — step-by-step lab building the real app while learning concepts. Budget about 90 minutes.

**Before you begin the lab, you should have:**

- Run every code example in Android Studio as you go.
- Completed the pre-topic quiz on Canvas (ungraded, just a self-check).

---

## The Story So Far...

In the previous topic, we integrated Firebase Authentication so users can log in, and Firestore to save their favorite cities in the cloud.

To continue the story, **open your existing Android Studio project from the previous topic**. We will be directly building upon the code you wrote previously. 

> 🆘 **Lost your code?** If your previous project is broken or missing, don't worry! You can download a clean starting point here: [Starter Project: topic_10_firebase.zip](/downloads/topic_10_firebase.zip). 

---

## Walkthrough: Building SkyCast

> 📁 **Target Project Reference (Completed Code)** — [topic_11_storage_room_datastore.zip](/downloads/topic_11_storage_room_datastore.zip)
>
> This project contains the complete, runnable SkyCast snapshot at Topic 11. Import into Android Studio and click Run.
>
> **Heads up:** The source files show the finished version of each step. Working through the walkthrough yourself first — then comparing to the download — is far more effective than reading the code directly.

SkyCast becomes offline-capable this topic. Room caches the last good API response; DataStore persists the user's unit preference. We also use Firebase Cloud Storage so users can upload an avatar!

### Step 1: Room Entities and DAO

> **SkyCast Briefing:** Room is Android's SQLite wrapper. It generates type-safe database code from annotations and integrates natively with Kotlin's `Flow` for reactive updates. We need to create **Entities** (the database tables) and a **DAO** (the interface for querying).

Create `RoomEntities.kt` in your `data/local/` package:

```kotlin
package com.example.skycast.data.local

import androidx.room.Entity
import androidx.room.PrimaryKey

@Entity(tableName = "cached_weather")
data class CachedWeatherEntity(
    @PrimaryKey val cityName: String,
    val lat:       Double,
    val lon:       Double,
    val tempC:     Double,
    val condition: String,
    val humidity:  Int,
    val windKph:   Double,
    val fetchedAt: Long = System.currentTimeMillis()
)

@Entity(tableName = "cached_forecast")
data class CachedForecastEntity(
    @PrimaryKey(autoGenerate = true) val id: Long = 0,
    val cityName:      String,
    val date:          String,
    val maxC:          Double,
    val minC:          Double,
    val conditionCode: Int
)
```

Now create `WeatherCacheDao.kt` in the same package:

```kotlin
package com.example.skycast.data.local

import androidx.room.Dao
import androidx.room.Insert
import androidx.room.OnConflictStrategy
import androidx.room.Query
import androidx.room.Transaction
import kotlinx.coroutines.flow.Flow

@Dao
interface WeatherCacheDao {
    @Query("SELECT * FROM cached_weather WHERE cityName = :city")
    suspend fun getWeather(city: String): CachedWeatherEntity?

    @Query("SELECT * FROM cached_forecast WHERE cityName = :city ORDER BY date ASC")
    fun observeForecast(city: String): Flow<List<CachedForecastEntity>>

    @Insert(onConflict = OnConflictStrategy.REPLACE)
    suspend fun saveWeather(w: CachedWeatherEntity)

    @Insert(onConflict = OnConflictStrategy.REPLACE)
    suspend fun saveForecast(days: List<CachedForecastEntity>)

    @Query("DELETE FROM cached_forecast WHERE cityName = :city")
    suspend fun clearForecast(city: String)

    @Transaction
    suspend fun replaceCache(w: CachedWeatherEntity, forecast: List<CachedForecastEntity>) {
        saveWeather(w)
        clearForecast(w.cityName)
        saveForecast(forecast)
    }
}
```

##### Code Breakdown: DAO
- `@Insert(onConflict = OnConflictStrategy.REPLACE)` acts as an "upsert" — insert if it's new, update if it already exists.
- `@Transaction` on `replaceCache` ensures the old forecast is atomically replaced. If the app crashes in the middle of this function, the database rolls back to the previous state, preventing partial updates.

---

### Step 2: The Room Database Singleton

> **SkyCast Briefing:** We need to tie our Entities and DAO together in a RoomDatabase class. Since creating the database is expensive, we use a singleton pattern.

Create `SkyCastDatabase.kt` in your `data/local/` package:

```kotlin
package com.example.skycast.data.local

import android.content.Context
import androidx.room.Database
import androidx.room.Room
import androidx.room.RoomDatabase

@Database(
    entities  = [CachedWeatherEntity::class, CachedForecastEntity::class],
    version   = 1,
    exportSchema = true
)
abstract class SkyCastDatabase : RoomDatabase() {
    abstract fun weatherCacheDao(): WeatherCacheDao

    companion object {
        @Volatile private var INSTANCE: SkyCastDatabase? = null
        
        fun get(context: Context) = INSTANCE ?: synchronized(this) {
            INSTANCE ?: Room.databaseBuilder(
                context.applicationContext, 
                SkyCastDatabase::class.java, 
                "skycast.db"
            ).build().also { INSTANCE = it }
        }
    }
}
```

Make sure to set `exportSchema = true` and configure the `schemas/` output directory in `build.gradle.kts` (we provided the Gradle snippet for this in the reference ZIP).

---

### Step 3: An Offline-First Repository

> **SkyCast Briefing:** We want a **Network-first, Cache-fallback** strategy. We will try to fetch the freshest data from Open-Meteo. If we get it, we save it to Room. If the network fails (e.g. the user is in a tunnel), we serve the stale cache from Room!

Update your `WeatherRepository.kt` to use the DAO:

```kotlin
package com.example.skycast.data

import com.example.skycast.data.local.WeatherCacheDao
import com.example.skycast.model.WeatherReport
import com.example.skycast.network.OpenMeteoApi
import java.io.IOException

class WeatherRepository(
    private val api:   OpenMeteoApi,
    private val cache: WeatherCacheDao
) {
    suspend fun fetchWeather(lat: Double, lon: Double, city: String): WeatherReport = try {
        // Try the network!
        val report = api.getForecast(lat, lon).toDomain(city)
        
        // Success! Save it to Room
        cache.replaceCache(
            report.current.toEntity(), 
            report.forecast.toEntities(city)
        )
        report
    } catch (e: IOException) {
        // Network unavailable — serve stale cache from Room
        val cached = cache.getWeather(city) 
            ?: throw IOException("No cached data for $city")
            
        cached.toDomain()
    }
}
```

---

### Step 4: DataStore Preferences

> **SkyCast Briefing:** DataStore replaces `SharedPreferences`. It's asynchronous (no ANR risk), transactional (no data corruption), and Flow-based. We will use it for small key-value settings that belong to one user on one device (like their preferred temperature unit).

Create `UserPreferencesRepository.kt` in your `data/local/` package:

```kotlin
package com.example.skycast.data.local

import android.content.Context
import androidx.datastore.preferences.core.booleanPreferencesKey
import androidx.datastore.preferences.core.edit
import androidx.datastore.preferences.core.stringPreferencesKey
import androidx.datastore.preferences.preferencesDataStore
import kotlinx.coroutines.flow.Flow
import kotlinx.coroutines.flow.map

val Context.prefsStore by preferencesDataStore("skycast_prefs")

object PrefKeys {
    val UNIT      = stringPreferencesKey("temp_unit")
    val DARK_MODE = booleanPreferencesKey("dark_mode")
    val HOME_CITY = stringPreferencesKey("home_city")
}

class UserPreferencesRepository(private val context: Context) {
    val unit:      Flow<String>  = context.prefsStore.data.map { it[PrefKeys.UNIT]      ?: "C"    }
    val darkMode:  Flow<Boolean> = context.prefsStore.data.map { it[PrefKeys.DARK_MODE] ?: false  }
    val homeCity:  Flow<String?> = context.prefsStore.data.map { it[PrefKeys.HOME_CITY]           }

    suspend fun setUnit(v: String)      = context.prefsStore.edit { it[PrefKeys.UNIT]      = v }
    suspend fun setDarkMode(v: Boolean) = context.prefsStore.edit { it[PrefKeys.DARK_MODE] = v }
    suspend fun setHomeCity(v: String)  = context.prefsStore.edit { it[PrefKeys.HOME_CITY] = v }
}
```

---

### Step 5: Firebase Cloud Storage (Avatars!)

> **SkyCast Briefing:** Firebase Cloud Storage stores arbitrary binary files — images, videos, documents. We will use it to let users upload a profile picture.

Create `AvatarRepository.kt` in your `data/` package:

```kotlin
package com.example.skycast.data

import android.net.Uri
import com.google.firebase.ktx.Firebase
import com.google.firebase.storage.ktx.storage
import kotlinx.coroutines.tasks.await

class AvatarRepository(private val userId: String) {
    private val storageRef = Firebase.storage.reference

    suspend fun upload(localUri: Uri): String {
        // We structure the storage folder as /users/{uid}/avatar.jpg
        val ref = storageRef.child("users/$userId/avatar.jpg")
        
        // Upload the file
        ref.putFile(localUri).await()
        
        // Retrieve the public download URL to load in our UI
        return ref.downloadUrl.await().toString()
    }
}
```

Go to **Storage** → **Rules** in the Firebase console. Write rules to ensure users can only upload images for themselves, and cap the file size to 5MB so malicious users don't bankrupt your Firebase bill!

```javascript
rules_version = '2';
service firebase.storage {
  match /b/{bucket}/o {
    match /users/{uid}/{allPaths=**} {
      allow read:  if request.auth != null && request.auth.uid == uid;
      allow write: if request.auth != null && request.auth.uid == uid
                   && request.resource.size < 5 * 1024 * 1024;  // 5 MB cap
    }
  }
}
```


---

## Guided Practice Challenges

Before diving into the full assignment, try these low-stakes practice challenges in Android Studio. They will build the exact muscle memory you need for persisting data across app restarts.

### Challenge 1: The Local Cache (Room `Entity` & `Dao`)
**The Scenario:** SkyCast users are complaining that their saved cities disappear when they enter a tunnel. We need an offline database.
**The Task:** 
1. Create a data class `SavedCityEntity` annotated with `@Entity(tableName = "saved_cities")`.
2. Give it a `val name: String` and a `@PrimaryKey(autoGenerate = true) val id: Long = 0`.
3. Create an `interface SavedCityDao` annotated with `@Dao`.
4. Add a function `@Query("SELECT * FROM saved_cities") fun getAll(): Flow<List<SavedCityEntity>>`.

### Challenge 2: Remembering User Choices (`DataStore`)
**The Scenario:** Users who prefer Fahrenheit are annoyed they have to toggle the switch every time they open the app.
**The Task:**
1. Create a `val Context.settingsStore by preferencesDataStore(name = "settings")`.
2. Define a key: `val UNIT_KEY = stringPreferencesKey("temp_unit")`.
3. Write a function to save the choice: `suspend fun saveUnit(unit: String) { context.settingsStore.edit { it[UNIT_KEY] = unit } }`.
4. Write a flow to read it: `val unitFlow = context.settingsStore.data.map { it[UNIT_KEY] ?: "C" }`.

### Challenge 3: Profile Pictures (`FirebaseStorage`)
**The Scenario:** SkyCast is getting social features, and users need avatars.
**The Task:**
1. Write a function `suspend fun uploadAvatar(uri: Uri, uid: String)`.
2. Get a reference to `Firebase.storage.reference.child("users/$uid/avatar.jpg")`.
3. Call `putFile(uri).await()` on the reference.
4. Retrieve the public URL by calling `downloadUrl.await()` and log it.

## References

1. [Get started with Cloud Storage on Android](https://firebase.google.com/docs/storage/android/start)
2. [Save data in a local database using Room](https://developer.android.com/training/data-storage/room)
3. [Store data with DataStore](https://developer.android.com/topic/libraries/architecture/datastore)
4. [Data and file storage overview](https://developer.android.com/training/data-storage)

---

## Getting Help

Because this course is fully asynchronous, here's how to get unstuck:

- **Piazza** is the primary help channel. Every topic has a dedicated thread. When asking a question, include: (1) what you're trying to do, (2) what you've tried, (3) the exact error message or Logcat output. Most questions get answered within a few hours.
- **TA office hours** — each TA hosts 1–2 hours per timeline on Zoom. Schedule is posted on Canvas. These are open-form drop-in sessions: show up, share your screen, get help.
- **Instructor office hours** — by appointment for deeper issues (design questions, project direction, grading questions).
- **On using AI tools:** The use of AI is not recommended at least for the first 6 modules, until you understand the basics of the development cycle. I do not ban using AI, but when you use AI, you should be able to answer any conceptual questions asked by the TAs or the professor. See the Academic Integrity policy on Canvas for specifics.
"""

with open("/Users/nsm/cs4520/lessons/Topic_11_Storage_Room_DataStore.md", "w") as f:
    f.write(new_content)

print("Rewrote Topic 11 successfully!")
