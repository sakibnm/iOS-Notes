---
title: "Conditionals"
weight: 40
---

# 4. Conditionals

Conditionals in Swift are used to make decisions in your code. They allow us to make different decisions based on the different circumstances. The condition is an expression that evaluates to a Boolean value, which can be either `true` or `false`. If the condition is true, the corresponding code block will execute; if false, that particular block won't execute. You can define a separate code block to execute if the condition is false.

There are three types of conditionals in Swift:

* `if` statements
* `if-else` statements
* `switch` statements




<!-- Merged from 4.1.-if-statements.md -->

# 4.1. If statements

**`if` statements** are the simplest type of conditional. They allow us to specify what should happen if a condition is `true`. For example, the following code prints "It is 5!" if the variable `myNum` is equal to 5:

```swift
let myNum = 5
//condition myNum==5 returns either true or false...
if myNum == 5 {
    //This code block executes if true...
    print("It is 5!")
}
```



<!-- Merged from 4.2.-if-else-statements.md -->

# 4.2. If-else statements

**`if-else` statements** allow us to specify what should happen if a condition is `true` or `false`. So, now we can add a code block if the condition is `false`. We can modify our previous example to print "It is not 5!", if `myNum` is not 5.

```swift
if myNum == 5 {
    print("It is 5!")
}else{
    print("It is not 5!")
}
```

You can build a `if-else if-else` chain if we are handling multiple `true` conditions. For example, the following code prints `myNum` if `myNum` is 1, 3, or 5. Else it prints "Not 1, 3, or 5!"

```swift
//if-else-if-else chain ...
if myNum == 1 {
    print("It is \(myNum)!")
}else if myNum == 3{
    print("It is \(myNum)!")
}else if myNum == 5{
    print("It is \(myNum)!")
}else{
    print("Not 1, 3, or 5!")
}
```

Here, the conditions are checked sequentially for each `if` and `else if`. If none of the conditions are true, the program switches to the `else` block.



<!-- Merged from 4.3.-switch-statements.md -->

# 4.3. Switch statements

Instead of `if-else if-else` chain, we can use `switch` statements if multiple statements are `true`. For example, the following code prints the name of the day of the week, depending on the value of the constant `day`. If the value of `day` is 1 through 7, the code prints the name of the day; else, it prints "Invalid!"

```swift
//switch statements...
let day = 5
switch day {
case 1:
    print("Sunday")
case 2:
    print("Monday")
case 3:
    print("Tuesday")
case 4:
    print("Wednesday")
case 5:
    print("Thursday")
case 6:
    print("Friday")
case 7:
    print("Saturday")
default:
    print("Invalid day")
}
```

**Please note:**

* Each `case` in a `switch` statement is the same as `if` or `else if` in `if-else if-else` chain.
* The `default` block in a `switch` statement is the same as the `else` block in `if-else` statements.



<!-- Merged from 4.4.-combining-operators.md -->

# 4.4. Combining operators

Swift has two operators that let us combine multiple conditions. They are `&&` (`and`), and `||` (or).

Let's look into an example:

```swift
let myAge = 24

if myAge >= 18 && myAge <= 65 {
    print("Eligible for the user study!")
}

if myAge < 18 || myAge > 65 {
    print("Not eligible!")
}
```

It means if `myAge` is more than or equal to 18 `and` less than or equal to 65, print "Eligible for the user study!"; if `myAge` is less than 18 `or` greater than 65, print "Not eligible!"



<!-- Merged from 4.5.-range-operators.md -->

# 4.5. Range operators

Swift can even represent a range of values. There are two kinds of range operators in Swift:

* Closed range operators (`...`) creates ranges up to and including the final value.
* Half-open range operators (`..<`) creates ranges up to and excluding the final value.

For example, the range `1..5` contains the numbers 1, 2, 3, 4, and 5. In contrast, the range `1..<5` contains the numbers 1, 2, 3, and 4.

The ranges are most useful in `switch` statements. For example, let's revisit the week example from before. We can write the following code:

```swift
let today = 8

switch today{
    case 1...5:
        print("Weekday!")
    case 6..<8:
        print("Weekend!")
    default:
        print("Invalid day!")
}
```

It means that if the value of `today` is in the range 1 to 5 (including 5), `today` is a weekday; if the value is in the range 6 to less than 8, `today` is a weekend; else it is an invalid day.



<!-- Merged from 4.6.-reference-code.md -->

# 4.6. Reference Code

{% file src="/gitbook-assets/MyPlayground4.playground.zip" %}

