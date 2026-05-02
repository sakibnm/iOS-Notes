import os

new_content = """# Topic 07 — Lists with LazyColumn and Modern List Patterns

**Estimated effort:** 5–7 hours this topic
**Format:** Asynchronous online — work at your own pace
**Prerequisites:** Topics 1–5

---

## Learning Objectives

By the end of this session, students will be able to:

1. Build efficient scrolling lists with `LazyColumn` and `LazyRow`.
2. Use `items(list, key = ...)` correctly and explain why keys matter for performance and animations.
3. Handle add, update, and remove operations in a list-backed ViewModel.
4. Implement swipe-to-delete with `SwipeToDismissBox`.
5. Animate list changes with `animateItem` / `animateItemPlacement`.


---

## Before You Start

Spread the work across the assigned time — don't leave it all for the day before the lab is due. A rough breakdown:

- **Walkthrough: Building SkyCast** — step-by-step lab building the real app while learning concepts. Budget about 90 minutes.

**Before you begin the lab, you should have:**

- Run every code example in Android Studio as you go.
- Completed the pre-topic quiz on Canvas (ungraded, just a self-check).

---

## The Story So Far...

In the previous topic, we moved our weather data out of the UI and into a ViewModel to survive configuration changes and introduced StateFlow.

To continue the story, **open your existing Android Studio project from the previous topic**. We will be directly building upon the code you wrote previously. 

> 🆘 **Lost your code?** If your previous project is broken or missing, don't worry! You can download a clean starting point here: [Starter Project: topic_06_viewmodel_stateflow.zip](/downloads/topic_06_viewmodel_stateflow.zip). 

---

## Walkthrough: Building SkyCast

> 📁 **Target Project Reference (Completed Code)** — [topic_07_lists_lazycolumn.zip](/downloads/topic_07_lists_lazycolumn.zip)
>
> This project contains the complete, runnable SkyCast snapshot at Topic 7. Import into Android Studio and click Run.
>
> **Heads up:** The source files show the finished version of each step. Working through the walkthrough yourself first — then comparing to the download — is far more effective than reading the code directly.

SkyCast gains a 7-day forecast list and a saved-cities screen this topic.

### Step 1: ViewModel-backed List

> **SkyCast Briefing:** A list screen almost always needs a ViewModel to manage the list state (adding, deleting, or updating items). We'll start by building the logic for our saved cities list.

Create `SavedCitiesViewModel.kt` in your `ui/home/` package:

```kotlin
package com.example.skycast.ui.home

import androidx.lifecycle.ViewModel
import kotlinx.coroutines.flow.MutableStateFlow
import kotlinx.coroutines.flow.StateFlow
import kotlinx.coroutines.flow.asStateFlow
import kotlinx.coroutines.flow.update

class SavedCitiesViewModel : ViewModel() {
    // In Topic 11, we will replace this hardcoded list with a Room database!
    private val _cities = MutableStateFlow(
        listOf("Boston", "New York", "Chicago", "Miami")  
    )
    val cities: StateFlow<List<String>> = _cities.asStateFlow()

    fun addCity(city: String) {
        if (city.isBlank() || _cities.value.contains(city)) return
        _cities.update { it + city.trim() }
    }

    fun removeCity(city: String) {
        _cities.update { it.filter { c -> c != city } }
    }
}
```

##### Code Breakdown: SavedCitiesViewModel
- We use `_cities.update { ... }` which safely modifies the current list.
- We return a *new* list (e.g. `it + city.trim()` or `it.filter`) because `StateFlow` only emits if the object reference changes. If we used a `MutableList` and just called `.add()`, the UI would not update!

---

### Step 2: LazyColumn and Efficient Lists

> **SkyCast Briefing:** When a list has more items than fit on screen, you need a scrolling list. In Compose, the answer is `LazyColumn` — it only renders items currently visible on the screen, saving memory.

**Keys — the most important LazyColumn detail**
By default, Compose identifies items by their *position* in the list. If you remove item 2, Compose thinks items 3, 4, 5 all changed — so it recomposes them all. Fix this by providing stable, unique keys (`key = { day -> day.date }`).

Create `ForecastList.kt` and `ForecastDayCard.kt` in your `ui/common/` package:

```kotlin
package com.example.skycast.ui.common

import androidx.compose.foundation.layout.Arrangement
import androidx.compose.foundation.layout.PaddingValues
import androidx.compose.foundation.lazy.LazyColumn
import androidx.compose.foundation.lazy.items
import androidx.compose.runtime.Composable
import androidx.compose.ui.Modifier
import androidx.compose.ui.unit.dp
import com.example.skycast.model.DailyForecast

@Composable
fun ForecastList(
    forecast: List<DailyForecast>,
    isCelsius: Boolean,
    modifier: Modifier = Modifier
) {
    LazyColumn(
        modifier            = modifier,
        contentPadding      = PaddingValues(horizontal = 16.dp, vertical = 8.dp),
        verticalArrangement = Arrangement.spacedBy(8.dp)
    ) {
        // Provide a unique key (the date string) so Compose can track items during animations
        items(forecast, key = { day -> day.date }) { day ->
            ForecastDayCard(
                day = day, 
                isCelsius = isCelsius, 
                modifier = Modifier.animateItem()
            )
        }
    }
}
```

```kotlin
package com.example.skycast.ui.common

import androidx.compose.foundation.layout.*
import androidx.compose.material3.Card
import androidx.compose.material3.MaterialTheme
import androidx.compose.material3.Text
import androidx.compose.runtime.Composable
import androidx.compose.ui.Alignment
import androidx.compose.ui.Modifier
import androidx.compose.ui.unit.dp
import com.example.skycast.model.DailyForecast

@Composable
fun ForecastDayCard(
    day: DailyForecast,
    isCelsius: Boolean,
    modifier: Modifier = Modifier
) {
    val hi   = if (isCelsius) day.maxC else day.maxC * 9.0/5.0 + 32.0
    val lo   = if (isCelsius) day.minC else day.minC * 9.0/5.0 + 32.0
    val unit = if (isCelsius) "C" else "F"

    Card(modifier = modifier.fillMaxWidth()) {
        Row(Modifier.padding(16.dp), verticalAlignment = Alignment.CenterVertically) {
            Text(day.date, Modifier.width(48.dp),
                 style = MaterialTheme.typography.bodyMedium)
            Text(day.condition.emoji(),
                 style    = MaterialTheme.typography.headlineMedium,
                 modifier = Modifier.padding(horizontal = 12.dp))
            Spacer(Modifier.weight(1f))
            Text("${"%.0f".format(lo)}° / ${"%.0f".format(hi)}°$unit",
                 style = MaterialTheme.typography.bodyLarge)
        }
    }
}
```

##### Code Breakdown: ForecastList
- `Modifier.animateItem()` gives each row a slide-and-fade transition when added/removed. It *requires* stable keys to look correct.
- `contentPadding` adds padding around the scrollable content (so items don't appear flush against the edge).

---

### Step 3: Swipe to Dismiss

> **SkyCast Briefing:** Mobile users expect fluidity. Instead of putting a static "Delete" button next to every item in a list, implementing "Swipe to Dismiss" using `SwipeToDismissBox` is an HCI best practice.

Create `SwipeableCityRow.kt` in your `ui/common/` package:

```kotlin
package com.example.skycast.ui.common

import androidx.compose.foundation.background
import androidx.compose.foundation.clickable
import androidx.compose.foundation.layout.Box
import androidx.compose.foundation.layout.fillMaxSize
import androidx.compose.foundation.layout.padding
import androidx.compose.material.icons.Icons
import androidx.compose.material.icons.filled.ChevronRight
import androidx.compose.material.icons.filled.Delete
import androidx.compose.material.icons.filled.LocationOn
import androidx.compose.material3.*
import androidx.compose.runtime.Composable
import androidx.compose.ui.Alignment
import androidx.compose.ui.Modifier
import androidx.compose.ui.unit.dp

@OptIn(ExperimentalMaterial3Api::class)
@Composable
fun SwipeableCityRow(
    city: String,
    onClick: () -> Unit,
    onDelete: () -> Unit,
    modifier: Modifier = Modifier
) {
    val state = rememberSwipeToDismissBoxState(
        confirmValueChange = { swipeValue ->
            if (swipeValue == SwipeToDismissBoxValue.EndToStart) {
                // Remove the item from the ViewModel
                onDelete()
                true
            } else {
                false
            }
        }
    )
    
    SwipeToDismissBox(
        state                   = state,
        modifier                = modifier,
        enableDismissFromStartToEnd = false, // We only want right-to-left swipe
        backgroundContent = {
            // The red background revealed underneath as the user swipes
            Box(
                Modifier.fillMaxSize()
                    .background(MaterialTheme.colorScheme.errorContainer)
                    .padding(end = 24.dp),
                contentAlignment = Alignment.CenterEnd
            ) {
                Icon(Icons.Default.Delete, contentDescription = "Remove",
                     tint = MaterialTheme.colorScheme.onErrorContainer)
            }
        }
    ) {
        // The foreground content
        ListItem(
            headlineContent  = { Text(city) },
            leadingContent   = { Icon(Icons.Default.LocationOn, contentDescription = null) },
            trailingContent  = { Icon(Icons.Default.ChevronRight, contentDescription = null) },
            modifier         = Modifier.clickable(onClick = onClick)
        )
    }
}
```

##### Code Breakdown: SwipeableCityRow
- `EndToStart` indicates a swipe left (which triggers the delete).
- `onDelete()` is called inside `confirmValueChange` — the ViewModel removes the city from the StateFlow before the swipe animation even finishes.

---

### Step 4: The Saved Cities Screen

> **SkyCast Briefing:** Let's put everything together. We'll build the screen that displays the `LazyColumn` of `SwipeableCityRow` items, driven by our `SavedCitiesViewModel`.

Create `SavedCitiesScreen.kt` in your `ui/home/` package:

```kotlin
package com.example.skycast.ui.home

import androidx.compose.foundation.layout.padding
import androidx.compose.foundation.lazy.LazyColumn
import androidx.compose.foundation.lazy.items
import androidx.compose.material.icons.Icons
import androidx.compose.material.icons.filled.Add
import androidx.compose.material3.*
import androidx.compose.runtime.*
import androidx.compose.ui.Modifier
import androidx.lifecycle.compose.collectAsStateWithLifecycle
import androidx.lifecycle.viewmodel.compose.viewModel
import com.example.skycast.ui.common.SwipeableCityRow

@Composable
fun SavedCitiesScreen(
    onCityClick: (String) -> Unit,
    vm: SavedCitiesViewModel = viewModel()
) {
    val cities by vm.cities.collectAsStateWithLifecycle()
    var showAddDialog by remember { mutableStateOf(false) }

    Scaffold(
        topBar = { 
            @OptIn(ExperimentalMaterial3Api::class)
            TopAppBar(title = { Text("My Cities") }) 
        },
        floatingActionButton = {
            FloatingActionButton(onClick = { showAddDialog = true }) {
                Icon(Icons.Default.Add, contentDescription = "Add city")
            }
        }
    ) { padding ->
        LazyColumn(Modifier.padding(padding)) {
            items(cities, key = { it }) { city ->
                SwipeableCityRow(
                    city     = city,
                    onClick  = { onCityClick(city) },
                    onDelete = { vm.removeCity(city) },
                    modifier = Modifier.animateItem()
                )
            }
        }
    }
    
    // Using the AlertDialog pattern from Topic 05
    if (showAddDialog) {
        // Pseudo-code for brevity: A dialog to add a city
        // AddCityDialog(onAdd = { vm.addCity(it); showAddDialog = false }, onDismiss = { showAddDialog = false })
    }
}
```

You now have a fully functional, animated, swipe-to-delete list interface powered by a robust ViewModel architecture!

---

## Guided Practice Challenges

Before diving into the full assignment, try these low-stakes practice challenges in Android Studio. They will build the exact muscle memory you need for building SkyCast's list screens.

### Challenge 1: The Fast List (`LazyColumn`)
**The Scenario:** SkyCast needs to render a 14-day forecast without freezing the UI.
**The Task:** 
1. Create a `val days = (1..14).map { "Day $it" }`.
2. Write a `@Composable fun ForecastList()`.
3. Inside, use a `LazyColumn` to display the list of `days`.
4. Add a `contentPadding = PaddingValues(16.dp)` so it doesn't touch the edges of the screen.

### Challenge 2: The Identity Crisis (`key` and `animateItem`)
**The Scenario:** When users delete a saved city, the list instantly snaps without animation, jarring the user.
**The Task:**
1. Given a `data class City(val id: Int, val name: String)`.
2. Create a `LazyColumn` that iterates over a `List<City>`.
3. Set the `key` parameter to `{ city -> city.id }`.
4. Add `Modifier.animateItem()` to your row Composable. (Note: You can test this by adding a button that removes an item from a mutable state list and watching it slide smoothly).

### Challenge 3: Swiping Away (`SwipeToDismissBox`)
**The Scenario:** The UX team wants users to be able to delete cities with a swift swipe left.
**The Task:**
1. Look at the `SwipeableCityCard` code in Chapter 2.
2. Implement it in your `LazyColumn` from Challenge 2.
3. Configure the `backgroundContent` to show a red background and a trash icon.

---

## Mobile-First Interaction Patterns

As you build list-heavy applications, remember that a phone is not a tiny laptop. Users navigate primarily with their thumbs.

**The Thumb Zone:**
The bottom 40% of the screen is the most comfortable area for the thumb to reach. When building long lists, ensure that the most important actions (like a Floating Action Button to add an item) are within easy reach, while destructive actions are either hidden behind a gesture or placed further away to prevent accidental taps.

**Gestures vs. Buttons:**
Mobile users expect fluidity. Instead of putting a static "Delete" button next to every item in a list, implementing "Swipe to Dismiss" using `SwipeToDismissBox` is an HCI best practice. Swiping feels native, fast, and satisfying, reducing visual clutter and preventing accidental taps on a tiny button.

---

## References

1. [Lists and grids (Compose)](https://developer.android.com/jetpack/compose/lists)
2. [SwipeToDismissBox (Compose)](https://developer.android.com/reference/kotlin/androidx/compose/material3/package-summary)
3. [Save UI state in Compose](https://developer.android.com/topic/libraries/architecture/viewmodel/viewmodel-savedstate)

---

## Getting Help

Because this course is fully asynchronous, here's how to get unstuck:

- **Piazza** is the primary help channel. Every topic has a dedicated thread. When asking a question, include: (1) what you're trying to do, (2) what you've tried, (3) the exact error message or Logcat output. Most questions get answered within a few hours.
- **TA office hours** — each TA hosts 1–2 hours per timeline on Zoom. Schedule is posted on Canvas. These are open-form drop-in sessions: show up, share your screen, get help.
- **Instructor office hours** — by appointment for deeper issues (design questions, project direction, grading questions).
- **On using AI tools:** The use of AI is not recommended at least for the first 6 modules, until you understand the basics of the development cycle. I do not ban using AI, but when you use AI, you should be able to answer any conceptual questions asked by the TAs or the professor. See the Academic Integrity policy on Canvas for specifics.
"""

with open("/Users/nsm/cs4520/lessons/Topic_07_Lists_LazyColumn.md", "w") as f:
    f.write(new_content)

print("Rewrote Topic 07 successfully!")
