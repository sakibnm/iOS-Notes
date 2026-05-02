import re

file_path = "/Users/nsm/cs4520/lessons/Week_02_Kotlin_Basics_II.md"
with open(file_path, "r", encoding="utf-8") as f:
    content = f.read()

# Chapter 1
ch1_old = r"""Let's start simple. Here's a class that represents a student:

```kotlin
class Student\(val name: String, val gpa: Double\) \{
    fun isHonours\(\): Boolean = gpa >= 3\.5

    override fun toString\(\): String = "Student\(\$name, GPA: \$gpa\)"
\}

fun main\(\) \{
    val alice = Student\("Alice", 3\.8\)
    println\(alice\.name\)        // Alice
    println\(alice\.isHonours\(\)\) // true
    println\(alice\)             // Student\(Alice, GPA: 3\.8\)
\}
```"""
ch1_new = """Let's start simple. Here's a class that represents a daily forecast:

```kotlin
class Forecast(val tempHigh: Double, val tempLow: Double) {
    fun tempRange(): Double = tempHigh - tempLow

    override fun toString(): String = "Forecast(High: $tempHigh, Low: $tempLow)"
}

fun main() {
    val today = Forecast(24.5, 12.0)
    println(today.tempHigh)    // 24.5
    println(today.tempRange()) // 12.5
    println(today)             // Forecast(High: 24.5, Low: 12.0)
}
```"""
content = re.sub(ch1_old, ch1_new, content, count=1, flags=re.DOTALL)

ch1_old2 = r"""```kotlin
class Student\(val name: String, val gpa: Double, val major: String = "CS"\)

val bob = Student\("Bob", 3\.2\)           // major defaults to "CS"
val cal = Student\("Cal", 3\.9, "Math"\)   // explicit major
```

\*\*Why `toString\(\)` matters\*\*

Notice the `override fun toString\(\)` in the first example\. By default, `println\(alice\)` would print something like `Student@6d06d69c`"""
ch1_new2 = """```kotlin
class Forecast(val tempHigh: Double, val tempLow: Double, val city: String = "Unknown")

val boston = Forecast(24.5, 12.0, "Boston")  // explicit city
val unknown = Forecast(20.0, 10.0)           // city defaults to "Unknown"
```

**Why `toString()` matters**

Notice the `override fun toString()` in the first example. By default, `println(today)` would print something like `Forecast@6d06d69c`"""
content = re.sub(ch1_old2, ch1_new2, content, count=1, flags=re.DOTALL)

ch1_old3 = r"""```kotlin
data class Student\(val name: String, val gpa: Double, val major: String = "CS"\)

fun main\(\) \{
    val alice = Student\("Alice", 3\.8\)

    // toString\(\) — automatic, based on all properties
    println\(alice\)   // Student\(name=Alice, gpa=3\.8, major=CS\)

    // equals\(\) — structural equality, not reference equality
    val alice2 = Student\("Alice", 3\.8\)
    println\(alice == alice2\)   // true  \(same values\)
    println\(alice === alice2\)  // false \(different objects in memory\)

    // copy\(\) — create a new instance changing only what you specify
    val aliceNextYear = alice\.copy\(gpa = 3\.9\)
    println\(aliceNextYear\)     // Student\(name=Alice, gpa=3\.9, major=CS\)
    println\(alice\)             // Student\(name=Alice, gpa=3\.8, major=CS\) — unchanged
\}
```"""
ch1_new3 = """```kotlin
data class WeatherSnapshot(val city: String, val tempC: Double, val condition: String = "Clear")

fun main() {
    val boston = WeatherSnapshot("Boston", 18.5)

    // toString() — automatic, based on all properties
    println(boston)   // WeatherSnapshot(city=Boston, tempC=18.5, condition=Clear)

    // equals() — structural equality, not reference equality
    val boston2 = WeatherSnapshot("Boston", 18.5)
    println(boston == boston2)   // true  (same values)
    println(boston === boston2)  // false (different objects in memory)

    // copy() — create a new instance changing only what you specify
    val updated = boston.copy(tempC = 21.0)
    println(updated)           // WeatherSnapshot(city=Boston, tempC=21.0, condition=Clear)
    println(boston)            // WeatherSnapshot(city=Boston, tempC=18.5, condition=Clear) — unchanged
}
```"""
content = re.sub(ch1_old3, ch1_new3, content, count=1, flags=re.DOTALL)

ch1_old4 = r"""```kotlin
data class Point\(val x: Int, val y: Int\)

val p = Point\(3, 7\)
val \(x, y\) = p       // x = 3, y = 7
println\("x=\$x, y=\$y"\)

// Also works in loops
val points = listOf\(Point\(1, 2\), Point\(3, 4\)\)
for \(\(x, y\) in points\) \{
    println\("\(\$x, \$y\)"\)
\}
```"""
ch1_new4 = """```kotlin
data class Coordinates(val lat: Double, val lon: Double)

val bostonLoc = Coordinates(42.36, -71.05)
val (lat, lon) = bostonLoc       // lat = 42.36, lon = -71.05
println("lat=$lat, lon=$lon")

// Also works in loops
val locations = listOf(Coordinates(42.36, -71.05), Coordinates(25.76, -80.19))
for ((l, ln) in locations) {
    println("($l, $ln)")
}
```"""
content = re.sub(ch1_old4, ch1_new4, content, count=1, flags=re.DOTALL)

ch1_old5 = r"""`Student`, `User`, `Product`, `Post` — all natural `data class` candidates."""
ch1_new5 = """`WeatherSnapshot`, `Coordinates`, `DailyForecast` — all natural `data class` candidates."""
content = re.sub(ch1_old5, ch1_new5, content, count=1)


# Chapter 2
ch2_old = r"""\*\*The problem it solves\*\*

Imagine you're writing a screen that loads data from a network\. At any moment the screen can be in one of three states:

- \*\*Loading\*\* — the request is in flight, show a spinner\.
- \*\*Success\*\* — the data arrived, show the list\.
- \*\*Error\*\* — something went wrong, show an error message\.

One naive approach is three separate boolean flags: `isLoading`, `hasError`, `hasData`\. That's fragile — you can have contradictory states like `isLoading = true` AND `hasData = true` simultaneously\. A better approach is a single value that can only ever be one of the three states at a time\.

```kotlin
sealed class UiState<out T> \{
    object Loading : UiState<Nothing>\(\)
    data class Success<T>\(val data: T\) : UiState<T>\(\)
    data class Error\(val message: String\) : UiState<Nothing>\(\)
\}
```

Let's unpack this:

- `sealed class` declares the hierarchy\. Every subtype must be in the same file\.
- `object Loading` is a singleton — there's only ever one `Loading` instance and it carries no data\.
- `data class Success<T>\(val data: T\)` is a generic subtype that carries the actual result\.
- `data class Error\(val message: String\)` carries an error message\.
- `out T` means the type parameter is covariant — don't worry about this now; it just allows `UiState<Nothing>` to be used where `UiState<T>` is expected\.

\*\*Exhaustive `when`\*\*

The real payoff comes when you use a `when` expression on a sealed class:

```kotlin
fun renderState\(state: UiState<List<String>>\): String = when \(state\) \{
    is UiState\.Loading  -> "Loading\.\.\."
    is UiState\.Success  -> "Got \$\{state\.data\.size\} items"
    is UiState\.Error    -> "Error: \$\{state\.message\}"
\}
```

Notice there's no `else` branch\. That's the key feature: because `sealed class` declares all possible subtypes at compile time, the compiler can verify the `when` is \*exhaustive\*\. If you add a fourth subtype later \(say, `Empty`\), your code won't compile until you handle it everywhere you use `when`\. This is a type-safe net that catches missing cases at compile time rather than at runtime as a crash\.

Try it: delete one branch and watch the compiler error\. Put it back\.

\*\*Smart casts\*\*

Inside each `when` branch, Kotlin automatically knows the type\. In the `is UiState\.Success` branch, `state` is automatically treated as `UiState\.Success<List<String>>`, so you can access `state\.data` without casting\. That's \*smart cast\* — the compiler is doing the type narrowing for you\.

\*\*A more concrete example\*\*

Let's model a login screen:

```kotlin
sealed class LoginState \{
    object Idle : LoginState\(\)
    object Loading : LoginState\(\)
    data class Success\(val userId: String\) : LoginState\(\)
    data class Failure\(val reason: String\) : LoginState\(\)
\}

fun handleLogin\(state: LoginState\) \{
    when \(state\) \{
        LoginState\.Idle    -> println\("Waiting for user input"\)
        LoginState\.Loading -> println\("Authenticating\.\.\."\)
        is LoginState\.Success -> println\("Welcome, user \$\{state\.userId\}"\)
        is LoginState\.Failure -> println\("Login failed: \$\{state\.reason\}"\)
    \}
\}

fun main\(\) \{
    handleLogin\(LoginState\.Idle\)
    handleLogin\(LoginState\.Loading\)
    handleLogin\(LoginState\.Success\("user_42"\)\)
    handleLogin\(LoginState\.Failure\("Invalid password"\)\)
\}
```

Notice `LoginState\.Idle` without `is` — because `Idle` is an `object` \(a singleton\), not a class you instantiate, you check equality rather than type\. `is` is for when the subtype has its own properties you want to access\.

You'll use this pattern in almost every screen you build in this course\. In Topic 5, `UiState` becomes the backbone of how ViewModels expose data to the UI\."""

ch2_new = """**The problem it solves**

Imagine you're building SkyCast's UI and need to determine the weather condition to display the correct icon. A weather condition could be:

- **Clear** — no data attached.
- **Rain** — carries data about mm per hour.
- **Snow** — carries data about cm per hour.

One naive approach is an enum combined with extra variables: `condition = RAIN`, `precipitationAmount = 2.5`. But what if `condition = CLEAR` and `precipitationAmount = 2.5`? That's an invalid state. A better approach is a single value that can only ever be one of these specific types.

```kotlin
sealed class WeatherCondition {
    object Clear : WeatherCondition()
    data class Rain(val mmPerHour: Double) : WeatherCondition()
    data class Snow(val cmPerHour: Double) : WeatherCondition()
}
```

Let's unpack this:

- `sealed class` declares the hierarchy. Every subtype must be in the same file.
- `object Clear` is a singleton — there's only ever one `Clear` instance and it carries no data.
- `data class Rain(val mmPerHour: Double)` is a subtype that carries the rain intensity.

**Exhaustive `when`**

The real payoff comes when you use a `when` expression on a sealed class:

```kotlin
fun renderIcon(condition: WeatherCondition): String = when (condition) {
    WeatherCondition.Clear -> "☀️"
    is WeatherCondition.Rain -> "🌧️ (${condition.mmPerHour}mm)"
    is WeatherCondition.Snow -> "❄️ (${condition.cmPerHour}cm)"
}
```

Notice there's no `else` branch. That's the key feature: because `sealed class` declares all possible subtypes at compile time, the compiler can verify the `when` is *exhaustive*. If you add a fourth subtype later (say, `Cloudy`), your code won't compile until you handle it everywhere you use `when`. This is a type-safe net that catches missing cases at compile time.

Try it: delete the `Snow` branch and watch the compiler error. Put it back.

**Smart casts**

Inside each `when` branch, Kotlin automatically knows the type. In the `is WeatherCondition.Rain` branch, `condition` is automatically treated as `WeatherCondition.Rain`, so you can access `condition.mmPerHour` without casting. That's *smart cast* — the compiler is doing the type narrowing for you.

Notice `WeatherCondition.Clear` without `is` — because `Clear` is an `object` (a singleton), not a class you instantiate, you check equality rather than type. `is` is for when the subtype has its own properties you want to access.

You'll use this pattern in almost every screen you build in this course. In Topic 5, a `UiState` sealed class becomes the backbone of how ViewModels expose data to the UI (Loading, Success, or Error)."""

content = re.sub(ch2_old, ch2_new, content, count=1, flags=re.DOTALL)

# Chapter 3
ch3_old = r"""```kotlin
data class Student\(val name: String, val gpa: Double, val major: String\)

val students = listOf\(
    Student\("Alice", 3\.8, "CS"\),
    Student\("Bob",   2\.9, "Math"\),
    Student\("Cal",   3\.6, "CS"\),
    Student\("Dana",  3\.9, "Physics"\),
    Student\("Eve",   3\.1, "Math"\)
\)
```

\*\*`filter`\*\* — keep only the items that match a predicate:

```kotlin
val honourStudents = students\.filter \{ it\.gpa >= 3\.5 \}
// \[Alice, Cal, Dana\]
```

\*\*`map`\*\* — transform every item into something else:

```kotlin
val names = students\.map \{ it\.name \}
// \["Alice", "Bob", "Cal", "Dana", "Eve"\]

val upperNames = students\.map \{ it\.name\.uppercase\(\) \}
// \["ALICE", "BOB", "CAL", "DANA", "EVE"\]
```

\*\*`sortedBy` / `sortedByDescending`\*\* — produce a new sorted list without modifying the original:

```kotlin
val byGpa = students\.sortedByDescending \{ it\.gpa \}
// \[Dana\(3\.9\), Alice\(3\.8\), Cal\(3\.6\), Eve\(3\.1\), Bob\(2\.9\)\]
```

\*\*`groupBy`\*\* — partition the list into a `Map<K, List<V>>` by a key:

```kotlin
val byMajor = students\.groupBy \{ it\.major \}
// \{
//   "CS"      → \[Alice, Cal\],
//   "Math"    → \[Bob, Eve\],
//   "Physics" → \[Dana\]
// \}
```

\*\*`mapValues`\*\* — transform the values in an existing map \(often used after `groupBy`\):

```kotlin
val averageGpaByMajor = students
    \.groupBy \{ it\.major \}
    \.mapValues \{ \(_, group\) -> group\.sumOf \{ it\.gpa \} / group\.size \}
// \{"CS" → 3\.7, "Math" → 3\.0, "Physics" → 3\.9\}
```

\*\*Chaining\*\*

The real power comes from chaining these operations\. Let's answer "what are the names of the top-2 students by GPA in the CS major\?":

```kotlin
val top2CS = students
    \.filter \{ it\.major == "CS" \}
    \.sortedByDescending \{ it\.gpa \}
    \.take\(2\)
    \.map \{ it\.name \}

println\(top2CS\)   // \[Alice, Cal\]
```

Read it top to bottom: filter to CS students → sort by GPA descending → take the first 2 → extract just the names\. Each step returns a new list; nothing is mutated\.

\*\*`fold` and `reduce`\*\*

For aggregating to a single value:

```kotlin
val totalGpa = students\.sumOf \{ it\.gpa \}            // 17\.3
val highestGpa = students\.maxOf \{ it\.gpa \}          // 3\.9
val count = students\.count \{ it\.gpa >= 3\.5 \}        // 3

// fold: accumulate with an explicit starting value
val nameString = students\.fold\("Students: "\) \{ acc, s -> "\$acc\$\{s\.name\} "\}
// "Students: Alice Bob Cal Dana Eve "
```"""

ch3_new = """```kotlin
data class DailyForecast(val day: String, val maxC: Double, val condition: String)

val week = listOf(
    DailyForecast("Mon", 21.0, "Sunny"),
    DailyForecast("Tue", 18.5, "Cloudy"),
    DailyForecast("Wed", 14.0, "Rain"),
    DailyForecast("Thu", 11.0, "Rain"),
    DailyForecast("Fri", 16.0, "Cloudy")
)
```

**`filter`** — keep only the items that match a predicate:

```kotlin
val niceDays = week.filter { it.maxC >= 18.0 }
// [Mon, Tue]
```

**`map`** — transform every item into something else:

```kotlin
val temperatures = week.map { it.maxC }
// [21.0, 18.5, 14.0, 11.0, 16.0]

val displays = week.map { "${it.day}: ${it.maxC}°C" }
// ["Mon: 21.0°C", "Tue: 18.5°C", ...]
```

**`sortedBy` / `sortedByDescending`** — produce a new sorted list without modifying the original:

```kotlin
val hottestDays = week.sortedByDescending { it.maxC }
// [Mon(21.0), Tue(18.5), Fri(16.0), Wed(14.0), Thu(11.0)]
```

**`groupBy`** — partition the list into a `Map<K, List<V>>` by a key:

```kotlin
val byCondition = week.groupBy { it.condition }
// {
//   "Sunny"  → [Mon],
//   "Cloudy" → [Tue, Fri],
//   "Rain"   → [Wed, Thu]
// }
```

**`mapValues`** — transform the values in an existing map (often used after `groupBy`):

```kotlin
val avgTempByCondition = week
    .groupBy { it.condition }
    .mapValues { (_, group) -> group.sumOf { it.maxC } / group.size }
// {"Sunny" → 21.0, "Cloudy" → 17.25, "Rain" → 12.5}
```

**Chaining**

The real power comes from chaining these operations. Let's answer "what are the names of the two hottest non-rainy days?":

```kotlin
val bestDays = week
    .filter { it.condition != "Rain" }
    .sortedByDescending { it.maxC }
    .take(2)
    .map { it.day }

println(bestDays)   // [Mon, Tue]
```

Read it top to bottom: filter out rain → sort by max temp descending → take the first 2 → extract just the day names. Each step returns a new list; nothing is mutated.

**`fold` and `reduce`**

For aggregating to a single value:

```kotlin
val totalTemp = week.sumOf { it.maxC }            // 80.5
val highestTemp = week.maxOf { it.maxC }          // 21.0
val countRain = week.count { it.condition == "Rain" } // 2

// fold: accumulate with an explicit starting value
val dayString = week.fold("Days: ") { acc, f -> "$acc${f.day} " }
// "Days: Mon Tue Wed Thu Fri "
```"""
content = re.sub(ch3_old, ch3_new, content, count=1, flags=re.DOTALL)

with open(file_path, "w", encoding="utf-8") as f:
    f.write(content)
print("Updated Week 2 successfully.")
