---
title: "Module 2: Swift Fundamentals"
weight: 200
bookCollapseSection: false
---


## Table of Contents




## Variables & Data Types

## Table of Contents

{{< section >}}


## Collections

**Estimated effort:** 1-2 hours this topic
**Format:** Asynchronous online
**Prerequisites:** Previous iOS topics

{< hint info >}
**🎯 Topic Mission:** 
In this module, we will explore **Collections** and learn how to integrate it into our iOS applications. Your mission is to understand the mechanics behind this concept and write robust Swift code.
{< /hint >}

---

## Learning Objectives

By the end of this session, you will be able to:
1. Understand the core concepts of Collections.
2. Implement Collections in an Xcode project.
3. Apply best practices to ensure clean and maintainable code.

---

## The Story So Far...

We have been progressively building our knowledge of iOS and Swift. In this module, we will expand our toolkit by diving into Collections. 
Open your current Xcode project or start a new Playground to follow along with the hands-on material.

---

## Walkthrough: Exploring Collections

> 📁 **Target Project** — Follow along by building the mini-app presented in the steps below, or integrate these concepts into your own ongoing projects.

# 2. Collections

So far, we have discussed a few simple Data types like String, Int, Double, etc. **Now, we will move into learning a few useful Collections like Arrays, Sets, Tuples, and Dictionaries.**

We often work with a list of data in real life, meaning a list of items having similar properties; for example, we might need to display a list of similar hotels near a specific location. We use Collections like Arrays, Sets, Dictionaries, etc., to store a list or group of data items together. Collections are powerful tools to store, manage and order data while running the program.

Please browse to the next page to learn more about Swift Collections.




<!-- Merged from 2.1.-arrays.md -->

# 2.1. Arrays

An array is a _**data structure**_ that can store a collection of values of the same data type. An array is an ordered data structure, which means the elements are stored in a specific order, and an element stays at the same position/index until changed.

In Swift, we create arrays with `[DataType]`.

For example, the following code creates an empty array of strings that holds the name of car brands:

```swift
var carMakes = [String]()
```

Or, we can initialize an array with predefined values using an array literal, which is a list of values enclosed in square brackets. For example, the following code creates an array of strings to hold two initial car manufacturers, Toyota and Honda:

```swift
var carMakesSecond = ["Toyota", "Honda"]
```

Please note, in the above example, Swift automatically defines the variable type of `carMakesSecond` to an array of strings.

### **Adding a new element to an existing array:**

To add a new element in an array, we use `append()` function. For example, to add a new car brand in the carMakes array, we can write the following:

```swift
carMakes.append("Mazda")

// Print the current elements of the array...
print(carMakes)
```

If you run the code, it will print the following outputs:

```
["Mazda"]
```

Let's add a couple more brands:

```swift
carMakes.append("Toyota")
carMakes.append("Honda")

// Print the current elements of the array...
print("After appending: \(carMakes)")
```

The above code outputs:

```
After appending: ["Mazda", "Toyota", "Honda"]
```

### **Size of an existing array:**

We can get the size of an array by accessing the `count` attribute. `carMakes.count` is the size of `carMakes`. For example,

```swift
print("Number of elements in carMakes: \(carMakes.count)")
```

prints:

```
Number of elements in carMakes: 3
```

### **Accessing an element from a particular position:**

We can access an element of an array by it's index/position in the array. The indices start at `0`. So, the first element resides at position `0,` the second element resides at position `1`, and so on. For example, let's look at the following code:

```swift
// Accessing a particular element from the Array...
print("The first element of carMakes: \(carMakes[0])")
print("The second element of carMakes: \(carMakes[1])")
```

It will print the following output:

```
The first element of carMakes: Mazda
The second element of carMakes: Toyota
```

### **Removing an element from an existing array:**

We can remove an element from an element by calling `remove(at: index)` function. For example:

```swift
carMakes.remove(at: 1)

// Printing the current elements of the array...
print("After removing: \(carMakes)")
```

This code outputs:

```
After removing: ["Mazda", "Honda"]
```

So far, we have learned the basics about Swift arrays (declaring and initializing an array, adding and removing elements). We will explore more functionalities cumulatively further down the road.



<!-- Merged from 2.2.-sets.md -->

# 2.2. Sets

A Set in Swift is a similar data structure to an Array with two differences:

* No item in a set can appear twice. Each item must be unique in a set.
* A set is not ordered like an array, so we cannot access the items in a set using indices. The items are stored in random positions.

To create a set, we use the following literal:`Set<DataType>`. For example, the following code creates a new empty set of strings `colors`:

<pre class="language-swift"><code class="lang-swift"><strong>// Creating an empty set of strings...
</strong><strong>var colors = Set&#x3C;String>()
</strong></code></pre>

You can add a new item in a set using `insert()` function, like:

```swift
colors.insert("black")
// prints the current Set...
print(colors)
```

The print function prints:

```
["black"]
```

Let's add a couple more colors:

```swift
colors.insert("blue")
colors.insert("black")

// prints the current Set...
print(colors)
```

Now, if it were an array, the corresponding array would be `["black", "blue", "black"]`. However, the above code outputs:

```
["blue", "black"]
```

So, we can see that the set `colors` is not adding `black` again. It is holding one `black` and one `blue`. So, it holds unique elements. Also, the order of the set is not fixed since `blue` was added after `black`, but it displays it in the opposite order here.

Now, if you are working with a set where you will not change the elements in the future you should use `let` to create a set with predefined values.

For example,

```swift
let colors = Set(["blue", "black", "red"])
```

Note: you can remove an element from a set by calling `remove()` function. Try it yourself!



<!-- Merged from 2.3.-tuples.md -->

# 2.3. Tuples

A Tuple is a collection of different elements of different data types stored together in the same place. It may sound like an array, but it is not exactly an array. The differences are:

* An array contains values of the same data type. **However, a tuple can hold values of different data types together.**
* You can add and remove elements from an array. **However, you cannot add or remove elements once you create a tuple. You can change the elements, but you cannot change the types of the elements.**

### Creating a new tuple:

We can create a tuple by putting the elements into parenthesis, like:

```swift
// Simple tuple
var myTuple = ("Mark", 20)
// We can also define the names of the elements
var yourTuple = (name:"Julie", age:23)

//print tuples
print("myTuple: \(myTuple), yourTuple: \(yourTuple)")
```

It prints:

```
myTuple: ("Mark", 20), yourTuple: (name: "Julie", age: 23)
```

### Accessing elements in a tuple:

You can access the elements in a tuple using their positions (similar to an array) or using their names. For example,

```swift
// accessing tuple elements
print("yourTuple's elements:\n first element = \(yourTuple.0),\n second element = \(yourTuple.age)")
```

It outputs:

```
yourTuple's elements:
 first element = Julie,
 second element = 23
```

Here we can see that `yourTuple.0` is the first element of the tuple, which is the same as `yourTuple.name;` and `yourTuple.age` is the second element of the tuple.

### Changing values:

You can change the values of the elements of a Tuple, like:

```swift
yourTuple.age = 34
// or, yourTuple.1 = 34
print("yourTuple: \(yourTuple)")
```

It prints:

```
yourTuple: (name: "Julie", age: 34)
```

**Please note: you can modify the values of an element; however, you cannot change the data type.**

Try writing: `yourTuple.age="thirty four"` :wink:



<!-- Merged from 2.4.-dictionaries.md -->

# 2.4. Dictionaries

When we hear the word 'dictionary,' we imagine a book of words and their corresponding meanings where we search for the words and find their meanings. Each word has a meaning in a dictionary.

In Swift, a dictionary is a similar data structure to a real-life dictionary. It is a collection of `key-value` pairs. Where each `key` is similar to a word in a dictionary book, and the corresponding `value` is similar to the meaning of the word. A dictionary in Swift has the following properties:

* Each element in a dictionary is a pair of a key and a value.
* The keys can be of any type.
* The values can be of any type.
* Once a dictionary is created,
  * The type for all keys has to be the same.
  * The type for all values has to be the same.

### Creating a dictionary:

We can **create an empty dictionary** of `String-Int` pairs by writing the following code:

```swift
var carCounts = [String: Int]()
```

Or, you can **create a dictionary with predefined key-value pairs**, like:

```swift
var carCounts = [
    "Toyota": 2,
    "Mazda": 1,
    "Honda":10
]

print(carCounts)
```

It prints:

```
["Toyota": 2, "Mazda": 1, "Honda": 10]
```

### Adding a new key-value pair and updating a value for a particular key:

For both adding a pair and updating a current value for a particular key, we use `updateValue(value, forKey:key)` function. The `updateValue()` function finds if the `key` already exists or not. If the `key` is not in the dictionary, it adds the `key` with the `value` provided. If the `key` is found, it just updates the current value with the new `value`.

For example, we can add 5 more Chevy cars in `carCounts` by writing:

```swift
carCounts.updateValue(5, forKey: "Chevy")
print(carCounts)
```

_**Alternatively, we can add 5 Chevy cars by writing:**_

```swift
carCounts["Chevy"] = 5
```

It prints:

```
["Mazda": 1, "Toyota": 2, "Chevy": 5, "Honda": 10]
```

Now, if we want to sell one Honda car, we would write:

```swift
carCounts.updateValue(9, forKey: "Honda")
print(carCounts)
```

It prints:

```
["Honda": 9, "Chevy": 5, "Mazda": 1, "Toyota": 2]
```

Dictionaries are very useful and very often used in iOS development or any kind of software development.

### Accessing a value for a key:

We can fetch how many Mazda cars we have by:

```swift
let mazdaCount = carCounts["Mazda"]
```

**A small challenge:** can you try to remove all Honda cars? (Hint: there is a `removeValue()` function).



<!-- Merged from 2.5.-reference-code.md -->

# 2.5. Reference Code

{% file src="/gitbook-assets/MyPlayground2.playground.zip" %}

---

## Guided Practice Challenges

Before moving on to the next topic, try these low-stakes practice challenges in Xcode. They will build the exact muscle memory you need:

### Challenge 1: Experimentation
**The Scenario:** You've just learned about Collections.
**The Task:** Experiment with the code snippets provided above. Can you alter the behavior by changing the parameters or combining it with concepts from previous modules?

### Challenge 2: From Scratch
**The Task:** Try implementing the core feature of this module in a completely blank Xcode project without looking at the reference code. Rely on Xcode's autocomplete and standard Apple documentation.

---

## References

1. [Apple Developer Documentation](https://developer.apple.com/documentation/)
2. [Swift Language Guide](https://docs.swift.org/swift-book/)
3. [Human Interface Guidelines](https://developer.apple.com/design/human-interface-guidelines/)

---

## Getting Help

Because this course is fully asynchronous, here's how to get unstuck:

- **Piazza** is the primary help channel. When asking a question, include: (1) what you're trying to do, (2) what you've tried, (3) the exact Xcode error message.
- **TA office hours** — check the Canvas calendar. Show up, share your screen, and get help.
- **Instructor office hours** — by appointment for deeper issues (design questions, project direction).


## Operators

**Estimated effort:** 1-2 hours this topic
**Format:** Asynchronous online
**Prerequisites:** Previous iOS topics

{< hint info >}
**🎯 Topic Mission:** 
In this module, we will explore **Operators** and learn how to integrate it into our iOS applications. Your mission is to understand the mechanics behind this concept and write robust Swift code.
{< /hint >}

---

## Learning Objectives

By the end of this session, you will be able to:
1. Understand the core concepts of Operators.
2. Implement Operators in an Xcode project.
3. Apply best practices to ensure clean and maintainable code.

---

## The Story So Far...

We have been progressively building our knowledge of iOS and Swift. In this module, we will expand our toolkit by diving into Operators. 
Open your current Xcode project or start a new Playground to follow along with the hands-on material.

---

## Walkthrough: Exploring Operators

> 📁 **Target Project** — Follow along by building the mini-app presented in the steps below, or integrate these concepts into your own ongoing projects.

# 3. Operators

In this section, we will learn about the usage of operators (`+`,`-`,`/`, etc.) in Swift. Please continue reading the next pages to learn about them.




<!-- Merged from 3.1.-arithmetic-operations.md -->

# 3.1. Arithmetic Operations

Let's do some arithmetic operations using Swift now. For addition, subtraction, multiplication, and division, we use `+`,`-`,`*`, and `/` respectively. Let's look at the following code:

```swift
let num1 = 5
let num2 = 33

//Addition...
let sum = num1 + num2

//Subtraction...
let difference = num2 - num1

//Multiplication...
let product = num1 * num2

//Division (and remainder)...
let divided = num2 / num1
let remainder = num2 % num1

print(
    """
    Results:
    Sum = \(sum)
    Difference = \(difference)
    Product = \(product)
    Division result = \(divided)
    Division remainder = \(remainder)
    """
)
```

It prints:

```
Results:
Sum = 38
Difference = 28
Product = 165
Division result = 6
Division remainder = 3
```

From the above example, it feels very intuitive how you can directly use the operators `+`, `-`, `*`, and `/` do the arithmetic operations. The remainder of a divide operation can be done with the dedicated operator `%`.

However, there are a few caveats to these operations. Let's look into the following code:

```swift
let myInt:Int = 20
let myDouble:Double = 30.5

let sum:Int = myInt + myDouble
```

_What do you think will happen?_

It should show something like the following:

<figure><img src="/gitbook-assets/Screenshot 2023-05-02 at 3.34.04 PM (1).png" alt=""><figcaption></figcaption></figure>

Remember, `Double` is a 64-bits long number and `Int` is a 32-bits long number? We are trying to add an `Int`(`myInt`) and a `Double`(`myDouble`) together and put the result into an `Int`(`sum`). First of all, if you add an `Int` and a `Double` together, it results in a `Double` value, since `Double` has the largest capacity of the two. Now, we are trying to put that `Double` value into the constant `sum`, which is and `Int`. An `Int` doesn't have the capacity to hold a `Double`. So, it is yelling at us :man\_facepalming:

You should always be careful of the types of data before you use arithmetic operators in Swift. More on this later.



<!-- Merged from 3.2.-operator-overloading.md -->

# 3.2. Operator overloading

Operator overloading is a way of saying that an arithmetic operator like `+` has another meaning depending on different data types. For example, we can concatenate two strings, or join two arrays with `+` operator. For example,

```swift
let firstName = "Sakib"
let lastName = "Miazi"
let fullName = firstName + " " + lastName
print(fullName)

let listNumOne = [1,2,3]
let listNumTwo = [4,5,6]
let listNum = listNumOne + listNumTwo
print(listNum)
```

It prints:

```
Sakib Miazi
[1, 2, 3, 4, 5, 6]
```

Now a question: what if you write the following code:

```swift
let listOne = [1,2,3]
let listTwo = ["four", "five"]
let listOneTwo = listOne + listTwo
```

would it work? :wink:



<!-- Merged from 3.3.-more-on-operators.md -->

# 3.3. More on Operators

In Swift, you can take a few shortcuts when you are using operators (`+`, `-`, `*`, and `/`). For example,

```swift
var budget = 30_000
let expense = 5_000
```

In the above code, we want to deduct the `expense` from our `budget`. To update our remaining budget we would usually do:

```swift
budget = budget - expense
```

We can take a shortcut here. instead of writing the above code, we can write:

```
// Instead of budget = budget - expense 
budget -= expense
```

Other examples could be:

```swift
//Increment...
var count = 0
count += 1 
// count = 1

//Multiply...
var number = 5
number *= 4 
// number = 20

//Divide...
var number2 = 10
number2 /= 2 
// number2 = 5

//String operations (concatenation)...
var name = "Mark"
var surname = "Webber"
name += surname 
// name = "MarkWebber"
```



<!-- Merged from 3.4.-comparison-operators-and-booleans.md -->

# 3.4. Comparison Operators (and Booleans)

Swift uses many comparison operators like, `==`, `!=`, `<`, `>`, and so on. We use the following operators the most:

<table><thead><tr><th width="118.33333333333331">Operator</th><th width="217">Description</th><th width="129">Example</th><th>Meaning</th></tr></thead><tbody><tr><td><code>==</code></td><td>Equal to</td><td><code>a == b</code></td><td>is <code>a</code> equal to <code>b</code>?</td></tr><tr><td><code>!=</code></td><td>Not equal to</td><td><code>a != b</code></td><td>is <code>a</code> not equal to <code>b</code>?</td></tr><tr><td><code>&#x3C;</code></td><td>Less than</td><td><code>a &#x3C; b</code></td><td>is <code>a</code> less than <code>b</code>?</td></tr><tr><td><code>></code></td><td>Greater than</td><td><code>a > b</code></td><td>is <code>a</code> greater than <code>b</code>?</td></tr><tr><td><code>&#x3C;=</code></td><td>Less than or equal to</td><td><code>a &#x3C;= b</code></td><td>is <code>a</code> less than or equal to <code>b</code>?</td></tr><tr><td><code>>=</code></td><td>Greater than or equal to</td><td><code>a >= b</code></td><td>is <code>a</code> greater than or equal to <code>b</code>?</td></tr></tbody></table>

### Booleans:

Boolean is a very important data type in any programming language, and it's no different for Swift. Booleans can only have two values: `true`, and `false`. We can create a boolean variable in Swift by writing the following:

```swift
// Either with type annotations
var myBool: Bool = false
// Or without type annotations
var yourBool = true 
```

**Booleans are very closely related to Comparison Operators.** For example, let's look into the following code:

```swift
// Comparison operators and Booleans...
let a = 10
let b = 12

let isEqual = a == b

print(isEqual)
print(type(of: isEqual))
```

It prints:

```
false
Bool
```

It means `a==b` is comparing `a` with `b` to check if `a` is equal to `b,`and returning the decision in boolean. Since the decision is not true, it creates the constant `isEqual` with the value `false`.

Comparison operators are widely used in Conditionals, Loops, and many other places where we make binary decisions.



<!-- Merged from 3.5.-reference-code.md -->

# 3.5. Reference Code

{% file src="/gitbook-assets/MyPlayground3.playground (1).zip" %}

---

## Guided Practice Challenges

Before moving on to the next topic, try these low-stakes practice challenges in Xcode. They will build the exact muscle memory you need:

### Challenge 1: Experimentation
**The Scenario:** You've just learned about Operators.
**The Task:** Experiment with the code snippets provided above. Can you alter the behavior by changing the parameters or combining it with concepts from previous modules?

### Challenge 2: From Scratch
**The Task:** Try implementing the core feature of this module in a completely blank Xcode project without looking at the reference code. Rely on Xcode's autocomplete and standard Apple documentation.

---

## References

1. [Apple Developer Documentation](https://developer.apple.com/documentation/)
2. [Swift Language Guide](https://docs.swift.org/swift-book/)
3. [Human Interface Guidelines](https://developer.apple.com/design/human-interface-guidelines/)

---

## Getting Help

Because this course is fully asynchronous, here's how to get unstuck:

- **Piazza** is the primary help channel. When asking a question, include: (1) what you're trying to do, (2) what you've tried, (3) the exact Xcode error message.
- **TA office hours** — check the Canvas calendar. Show up, share your screen, and get help.
- **Instructor office hours** — by appointment for deeper issues (design questions, project direction).


## Conditionals

**Estimated effort:** 1-2 hours this topic
**Format:** Asynchronous online
**Prerequisites:** Previous iOS topics

{< hint info >}
**🎯 Topic Mission:** 
In this module, we will explore **Conditionals** and learn how to integrate it into our iOS applications. Your mission is to understand the mechanics behind this concept and write robust Swift code.
{< /hint >}

---

## Learning Objectives

By the end of this session, you will be able to:
1. Understand the core concepts of Conditionals.
2. Implement Conditionals in an Xcode project.
3. Apply best practices to ensure clean and maintainable code.

---

## The Story So Far...

We have been progressively building our knowledge of iOS and Swift. In this module, we will expand our toolkit by diving into Conditionals. 
Open your current Xcode project or start a new Playground to follow along with the hands-on material.

---

## Walkthrough: Exploring Conditionals

> 📁 **Target Project** — Follow along by building the mini-app presented in the steps below, or integrate these concepts into your own ongoing projects.

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

---

## Guided Practice Challenges

Before moving on to the next topic, try these low-stakes practice challenges in Xcode. They will build the exact muscle memory you need:

### Challenge 1: Experimentation
**The Scenario:** You've just learned about Conditionals.
**The Task:** Experiment with the code snippets provided above. Can you alter the behavior by changing the parameters or combining it with concepts from previous modules?

### Challenge 2: From Scratch
**The Task:** Try implementing the core feature of this module in a completely blank Xcode project without looking at the reference code. Rely on Xcode's autocomplete and standard Apple documentation.

---

## References

1. [Apple Developer Documentation](https://developer.apple.com/documentation/)
2. [Swift Language Guide](https://docs.swift.org/swift-book/)
3. [Human Interface Guidelines](https://developer.apple.com/design/human-interface-guidelines/)

---

## Getting Help

Because this course is fully asynchronous, here's how to get unstuck:

- **Piazza** is the primary help channel. When asking a question, include: (1) what you're trying to do, (2) what you've tried, (3) the exact Xcode error message.
- **TA office hours** — check the Canvas calendar. Show up, share your screen, and get help.
- **Instructor office hours** — by appointment for deeper issues (design questions, project direction).


## Loops

**Estimated effort:** 1-2 hours this topic
**Format:** Asynchronous online
**Prerequisites:** Previous iOS topics

{< hint info >}
**🎯 Topic Mission:** 
In this module, we will explore **Loops** and learn how to integrate it into our iOS applications. Your mission is to understand the mechanics behind this concept and write robust Swift code.
{< /hint >}

---

## Learning Objectives

By the end of this session, you will be able to:
1. Understand the core concepts of Loops.
2. Implement Loops in an Xcode project.
3. Apply best practices to ensure clean and maintainable code.

---

## The Story So Far...

We have been progressively building our knowledge of iOS and Swift. In this module, we will expand our toolkit by diving into Loops. 
Open your current Xcode project or start a new Playground to follow along with the hands-on material.

---

## Walkthrough: Exploring Loops

> 📁 **Target Project** — Follow along by building the mini-app presented in the steps below, or integrate these concepts into your own ongoing projects.

# 5. Loops

If you know any programming language, you probably have heard the word `loop` most frequently. Yes, Swift, too, has loops. Basically, the structure of a loop is simple, run a block of code repeatedly while a condition is true or until the condition is false.

There are three kinds of loops in Swift:

* For loops
* While loops
* Repeat-while loops




<!-- Merged from 5.1.-for-loops.md -->

# 5.1. For loops

For loops are the most common loops in Swift, and you'll probably use this loop for more than 90% of cases. We use `for` loops to iterate over a sequence of values or a range of values.

For example, the following code prints the integers in the range `1...10`.

```swift
let range = 1...10

for number in range{
    print(number)
}
```

Another example could be iterating through an array and printing the elements:

```swift
var carMakesSecond = ["Toyota", "Honda", "Mazda", "Chevy"]

for item in carMakesSecond{
    print(item)
}
```

In Swift, we have an extra feature. If we have a situation where we are not using the variable a for loop gives us (`number` or `item` in the above examples), we can skip creating the unnecessary values. For example, if we want to do the same task 10 times, we can write the following code:

```swift
for _ in 1...10{
    print("Doing the task!")
}
```

Here, underscore skips create unnecessary values.

### 5.1.2. Looping through other Collections (Dictionaries, Arrays of Struct Objects, etc.)

Let's think about the following Dictionary:

```swift
let dictCars: [String: Int] = ["Toyota": 10, "Honda": 20, "Ford": 30]
```

This a dictionary for a car dealership where the keys are car brands and the values are the number of cars of the corresponding brands in their inventory. We want to loop through the dictionary and print the values from the dictionary.

We will look at some of the example outputs:

**Code:**

```swift
print("We got:")
for (model, count) in dictCars {
    print("\(count) \(model)s")
}
print ("in our dealership.\n")
```

**Output:**

```
We got:
20 Hondas
30 Fords
10 Toyotas
in our dealership.
```

**Code:**

```swift
print("We got:")
//Omitting values from a dictionary...
for (model, _) in dictCars {
    print("\(model)s")
}
print ("in our dealership.\n")
```

**Output:**

```
We got:
Hondas
Fords
Toyotas
in our dealership.
```

**Code:**

```swift
//MARK: Omitting keys...
var total = 0
for (_, count) in dictCars {
    total += count
}
print ("We got \(total) cars in our dealership.\n")
```

**Output:**

```
We got 60 cars in our dealership.
```

**Long story short, we can use parenthesis to define which component to loop through selectively in a complex Collection.**



<!-- Merged from 5.2.-while-loops.md -->

# 5.2. While loops

The second most common loops in Swift are `while` loops. We use a while loop to run a code block repeatedly as long as a given condition is true. A general structure of a `while` loop is:

```swift
while condition {
    //code block
}
```

For example, the following code prints all the integers below 50:

```swift
var targetNum = 1
while targetNum <= 50{
    //code block
    print(targetNum)
    targetNum += 1
}
```

Here the condition is: if `targetNum` is less than or equal to 50.



<!-- Merged from 5.3.-repeat-loops.md -->

# 5.3. Repeat loops

The third way of writing loops is `repeat` loops. It is identical to a while loop, but the condition is checked at the end of the code block. If we use the same example from before, we can write:

```swift
var myNum = 1

repeat{
    //code block
    print(myNum)
    myNum += 1
} while myNum <= 50

```

The point is `repeat` loops will execute the code block at least once. So, you should be careful about the cases where the first iteration may result in errors.



<!-- Merged from 5.4.-break-and-continue.md -->

# 5.4. Break and continue

### Breaking/exiting loops

Sometimes we want to stop repeating the code block in a loop. We use the keyword `break` to do that. Let's look into the example below:

```swift
let breakPoint = 4
var countDown = 1
while breakPoint >= 0 {
    print("I will run!")
    
//  activating break point
    if countDown == breakPoint{
        print("I am tired now!")
        break
    }
    countDown += 1
}
```

Here the while loop is running infinitely if the value of `breakPoint` is greater than or equal to `0`. So, we need to break it when the `countDown` reaches the `breakPoint`. Thats where we user the keyword `break`.

### Skipping a block manually

Sometimes, we want to skip executing a repeated block for an iteration. Swift uses the keyword `continue` to do that. Let's look into the following example:

```swift
for number in 1...10 {
    //skipping the even numbers
    if number%2 == 0{
        continue
    }
    
    print("This an odd number:\(number)")
}
```

Here, we wanted to print the odd integers between 1 and 10. So, we are running a for loop from 1 to 10 and skipping the even numbers.



<!-- Merged from 5.5.-reference-code.md -->

# 5.5. Reference Code

{% file src="/gitbook-assets/MyPlayground5.playground.zip" %}

---

## Guided Practice Challenges

Before moving on to the next topic, try these low-stakes practice challenges in Xcode. They will build the exact muscle memory you need:

### Challenge 1: Experimentation
**The Scenario:** You've just learned about Loops.
**The Task:** Experiment with the code snippets provided above. Can you alter the behavior by changing the parameters or combining it with concepts from previous modules?

### Challenge 2: From Scratch
**The Task:** Try implementing the core feature of this module in a completely blank Xcode project without looking at the reference code. Rely on Xcode's autocomplete and standard Apple documentation.

---

## References

1. [Apple Developer Documentation](https://developer.apple.com/documentation/)
2. [Swift Language Guide](https://docs.swift.org/swift-book/)
3. [Human Interface Guidelines](https://developer.apple.com/design/human-interface-guidelines/)

---

## Getting Help

Because this course is fully asynchronous, here's how to get unstuck:

- **Piazza** is the primary help channel. When asking a question, include: (1) what you're trying to do, (2) what you've tried, (3) the exact Xcode error message.
- **TA office hours** — check the Canvas calendar. Show up, share your screen, and get help.
- **Instructor office hours** — by appointment for deeper issues (design questions, project direction).


## Functions

**Estimated effort:** 1-2 hours this topic
**Format:** Asynchronous online
**Prerequisites:** Previous iOS topics

{< hint info >}
**🎯 Topic Mission:** 
In this module, we will explore **Functions** and learn how to integrate it into our iOS applications. Your mission is to understand the mechanics behind this concept and write robust Swift code.
{< /hint >}

---

## Learning Objectives

By the end of this session, you will be able to:
1. Understand the core concepts of Functions.
2. Implement Functions in an Xcode project.
3. Apply best practices to ensure clean and maintainable code.

---

## The Story So Far...

We have been progressively building our knowledge of iOS and Swift. In this module, we will expand our toolkit by diving into Functions. 
Open your current Xcode project or start a new Playground to follow along with the hands-on material.

---

## Walkthrough: Exploring Functions

> 📁 **Target Project** — Follow along by building the mini-app presented in the steps below, or integrate these concepts into your own ongoing projects.

# 6. Functions

Functions are the best tools for writing reusable code blocks. Whenever we write codes, we often see that we need to execute the same task in multiple places in our program. What if we could separate the code for that particular task from the main code block and call it every time we need to do it instead of writing the same code again?

So, in short, a function is a code block where we can do certain tasks. We can provide it with data and receive a result from it.




<!-- Merged from 6.1.-writing-functions.md -->

# 6.1. Writing functions

To write a function in Swift, we use the keyword `func` followed by the function's name, parameter list, return data type, and body (the code block). A general structure of a Swift function is:

```
func functionName(parameter1:DataType, parameter2:DataType, ...) -> ReturnDataType{
    //code block
}
```

### Simple functions

For a function, the list of parameters can be empty, meaning if our function does not require any data from us to run, we do not need to define any parameters. For example, a function to print "Hello World" could be:

```swift
func printHelloWorld(){
    print("Hello World!")
}
```

You can call the function from your code like:

```swift
printHelloWorld()
```



<!-- Merged from 6.2.-functions-with-parameters.md -->

# 6.2. Functions with parameters

Now, let's write a function that accepts parameters and do some tasks. The following code accepts the name and age of a person as parameters and prints the details.

```swift
//function definition...
func printDetails(name:String, age:Int){
    print(
        """
        The user's name is: \(name).
        The user's age is: \(age).
        \(name) is awesome!
        """
    )
}


//calling the function...
printDetails(name: "Donald", age: 25)
```

It prints:

```
The user's name is: Donald.
The user's age is: 25.
Donald is awesome!
```



<!-- Merged from 6.3.-functions-that-return-a-value.md -->

# 6.3. Functions that return a value

Now, let's think about a function that accepts an array of integers as a parameter and returns the sum of the integers.

```swift
func sumOf(array:[Int]) -> Int{
    var sum = 0
    for item in array{
        sum += item
    }
    
    //returns the value...
    return sum
}

//calling the function with an integer array
print(sumOf(array: [1,2,3,4,5]))
```

It prints:

```
15
```

You can get the returned value and store it to a constant or variable:

```swift
let sum = sumOf(array: [1,2,3,4,5])
```



<!-- Merged from 6.4.-more-on-function-parameters.md -->

# 6.4. More on function parameters

## Parameter labels

Swift functions have the ability to have completely separate internal and external parameter names. Instead of having a single parameter name, the function below has two. The first one, `with` is an external parameter name, which is the name that will refer to the parameter when we call the function. The second one, `vehicle` is the internal parameter name which is the name we’ll use when we need to use the parameter within the function.

```swift
//function definition...
func navigate(with vehicle:String, from source:String, to destination:String) -> String{
    return "The user will use a \(vehicle) to travel from \(source) to \(destination)."
}

//calling the function
print(navigate(with: "car", from: "Boston", to: "NYC"))
```

It prints:

```
The user will use a car to travel from Boston to NYC.
```

Let's look at the first `String` parameter the `navigate` function accepts. Here, `with` is the external name or label, and `vehicle` is the internal label for the first parameter. When we are calling the function from outside, we are using `with`, and internally we are using `vehicle`.

We can use this feature to write and call a function creatively.

## Omitting parameter labels

We can also omit the external parameter name to call our function just by passing in a value without mentioning the parameter's name. We achieve this by simply replacing the external name with the underscore. Now we can call our function without using a parameter name at all. Instead, we can pass in a value that we want to use as the input.

Remember `underscores`? We can use it to define the external name of a parameter to omit the need to type the parameter name when we call the function:

```swift
//function definition...
func printHello(_ name:String){
    print("Hello \(name)!")
}

//Calling the function...
printHello("Sakib")
```

## Default parameters

Sometimes we want to have default values for our parameters. The default value gets activated if we do not pass any value through the parameters. We can set a default value by writing a `=` after the parameter's type followed by the default value. Like this:

```swift
//function definition
func printHello2(_ name:String = "Unknown"){
    print("Hello \(name)!")
}
//calling function...
printHello2()
```

It will print:

```
Hello Unknown!
```

Because the default is already set to "Unknown."

## <mark style="color:orange;">Why and where do we use internal and external names in Swift functions?</mark>

1.  **Improved Clarity in Function Calls:**

    When a function has descriptive external parameter names, it becomes clear what each argument represents when calling it. This helps understand each argument's purpose and makes the function call more readable.
2.  **Self-Documenting Code:**

    By providing meaningful external names, you can make your code self-documenting. This means that someone reading your code can understand the purpose and intent of the function just by looking at the function signature and the way it's called.
3. **Avoiding Ambiguity:** \
   In some cases, functions may have parameters with similar data types. Using external names allows you to disambiguate these parameters, making the function call unambiguous and reducing the risk of passing incorrect arguments.
4.  **Improved Readability and Maintenance:**

    By using external names, you can create functions with expressive, almost sentence-like function calls, which can be beneficial when reading and maintaining code.

### Scenarios where internal and external names are useful

1.  **Public API Design:**

    When designing public APIs, using external names helps ensure that the function calls are clear and self-explanatory for your framework or library users. You can find examples in Apple Documentation.
2.  **Functions with Multiple Parameters:**

    Functions with multiple parameters benefit from external names as they clarify the purpose of each parameter.
3.  **Methods in Classes and Structures:**

    In object-oriented programming, methods in classes and structures should use external names to indicate the role of each parameter in the context of the object.

In summary, using internal and external names in Swift functions is a good practice for writing clean, expressive, and self-documenting code, especially when designing public APIs or functions with multiple parameters. They enhance code readability and help prevent confusion and errors when calling functions.

_These are the very basics of functions in Swift. Eventually, we will learn more about functions and their various uses._



<!-- Merged from 6.5.-reference-code.md -->

# 6.5. Reference Code

{% file src="/gitbook-assets/MyPlayground6.playground (1).zip" %}

---

## Guided Practice Challenges

Before moving on to the next topic, try these low-stakes practice challenges in Xcode. They will build the exact muscle memory you need:

### Challenge 1: Experimentation
**The Scenario:** You've just learned about Functions.
**The Task:** Experiment with the code snippets provided above. Can you alter the behavior by changing the parameters or combining it with concepts from previous modules?

### Challenge 2: From Scratch
**The Task:** Try implementing the core feature of this module in a completely blank Xcode project without looking at the reference code. Rely on Xcode's autocomplete and standard Apple documentation.

---

## References

1. [Apple Developer Documentation](https://developer.apple.com/documentation/)
2. [Swift Language Guide](https://docs.swift.org/swift-book/)
3. [Human Interface Guidelines](https://developer.apple.com/design/human-interface-guidelines/)

---

## Getting Help

Because this course is fully asynchronous, here's how to get unstuck:

- **Piazza** is the primary help channel. When asking a question, include: (1) what you're trying to do, (2) what you've tried, (3) the exact Xcode error message.
- **TA office hours** — check the Canvas calendar. Show up, share your screen, and get help.
- **Instructor office hours** — by appointment for deeper issues (design questions, project direction).


## Closures

**Estimated effort:** 1-2 hours this topic
**Format:** Asynchronous online
**Prerequisites:** Previous iOS topics

{< hint info >}
**🎯 Topic Mission:** 
In this module, we will explore **Closures** and learn how to integrate it into our iOS applications. Your mission is to understand the mechanics behind this concept and write robust Swift code.
{< /hint >}

---

## Learning Objectives

By the end of this session, you will be able to:
1. Understand the core concepts of Closures.
2. Implement Closures in an Xcode project.
3. Apply best practices to ensure clean and maintainable code.

---

## The Story So Far...

We have been progressively building our knowledge of iOS and Swift. In this module, we will expand our toolkit by diving into Closures. 
Open your current Xcode project or start a new Playground to follow along with the hands-on material.

---

## Walkthrough: Exploring Closures

> 📁 **Target Project** — Follow along by building the mini-app presented in the steps below, or integrate these concepts into your own ongoing projects.

# 7. Closures

_<mark style="color:purple;">**This concept might look like a weird one. Do not worry, you'll understand it eventually, and I will keep it simple here.**</mark>_

Swift allows us to define a function just like a Data Type like `Int` , `String`, etc. It means you can define and use functions like constants or variables. These functions are called closures.&#x20;

On a different note, closures themselves are anonymous functions or functions with no name, they are essentially a self-contained package of functionality that we can pass around and use.\


A simple example could be:

```swift
let printHello = {
    print("Hello World!")
}
```

You can call it just like a function:

```swift
//calling closure...
printHello()
```




<!-- Merged from 7.1.-closures-with-parameters.md -->

# 7.1. Closures with parameters

We can take the help of `in` keyword to pass parameters in a closure. For example, in the following code, we define a closure to take a person's name as a parameter and say hello to them:

```swift
let sayHelloTo = { (name:String) in
    print("Hello \(name)!")
}

//calling closure with parameter...
sayHelloTo("Donald")
```

It prints:

```
Hello Donald!
```

Do you find a difference between functions and closure in handling the parameter labels? :wink:



<!-- Merged from 7.2.-closures-that-return-a-value.md -->

# 7.2. Closures that return a value

To return a value, we would use `->` followed by the return data type followed by `in` keyword. For example, let's convert the `sumOf` function into a closure to return the sum of integers in an array.

```swift
let sumOfArray = {(array:[Int]) -> Int in
    var sum = 0
    for item in array{
        sum += item
    }
    
    //returns the value...
    return sum
}

//calling the closure with an integer array
let sum = sumOfArray([1,2,3,4,5])
print(sum)
```

It prints:

```
15
```



<!-- Merged from 7.3.-closures-as-parameters.md -->

# 7.3. Closures as parameters

So far, we rewrote the functions as closures. So why write a closure when we can just define a function? Well, the beauty of closures is we can pass closures as parameters to a function. And iOS UIKit and SwiftUI libraries use it extensively.

Let's define two closures, one to fly and another to drive.

```swift
let drive = {
    print("I am driving!")
}

let fly = {
    print("I am taking a flight!")
}
```

Now let's recreate a previous scenario where the user could travel from one place to another. So we can write the function as:

```swift
//taking a closure as the parameter 'how'
func travel(from source:String, to destination:String, how: ()->Void){
    
    print("I need to travel from \(source) to \(destination).")
    how()
}
```

In function `travel`, we are accepting a closure (`how`) as the parameter. Notice that we are defining the data type of the parameter '`how`' as `()->Void`.

`()->Void` represents a closure data type where:

* `()` means the closure won't accept any parameters, and
* `-> Void` means the closure will return "nothing". `Void` means "nothing" in Swift.

Does the parameter data type for the closure (labeled as `how`) match with the definitions of the three closures we wrote before?

Now, let's call the travel function:

```swift
//calling the function
travel(from: "San Francisco", to: "Boston", how: fly)
```

It will print:

```
I need to travel from San Francisco to Boston.
I am taking a flight!
```

See, we are calling the closure we received as the parameter `how` from inside the function.

### When closures accept parameters themselves and return values

Let's define three closures to do addition, subtraction, and multiplication:

```swift
//defining three closures to add, subtract, and multiply two numbers
let add = {(num1:Int, num2:Int) -> Int in
    return num1+num2
}

let subtract = {(num1:Int, num2:Int) -> Int in
    return num1-num2
}

let multiply = {(num1:Int, num2:Int) -> Int in
    return num1*num2
}
```

Now, we will write a function `calculate` to do some operations on two integers and return the result:

```swift
// calculate function...
func calculate(operation: (_:Int, _:Int)-> Int, num1:Int, num2:Int) -> Int{
    
    let result = operation(num1, num2)
    
    return result
}
```

So, here we are accepting a closure and labeling it as `operation`. The `operation` closure can take two `Int` parameters and returns an `Int`.

* `(_:Int, _:Int)-> Int` is a closure data type.
* `(_:Int, _:Int)` means that the closure itself accepts two `Int` parameters. We do not need the labels for the `Int`s since the labels are not important when we call closures.
* `-> Int` means that the closure will return an `Int`.

Then the function `calculate` takes two more `Int` parameters `num1` and `num2` and finally returns an `Int`. We can call the function `calculate` as follows:

```swift
//calling function to multiply...
print(calculate(operation: multiply, num1: 2, num2: 23))
```

Which prints:

```
46
```

So far, we have covered the basics of closures. You need to get used to the closures. I would practice writing closures as much as I could, probably just starting with writing closures deliberately for every simple function. iOS libraries use it very extensively, so again, you need to understand the idea.



<!-- Merged from 7.4.-reference-code.md -->

# 7.4. Reference Code

{% file src="/gitbook-assets/MyPlayground7.playground.zip" %}

---

## Guided Practice Challenges

Before moving on to the next topic, try these low-stakes practice challenges in Xcode. They will build the exact muscle memory you need:

### Challenge 1: Experimentation
**The Scenario:** You've just learned about Closures.
**The Task:** Experiment with the code snippets provided above. Can you alter the behavior by changing the parameters or combining it with concepts from previous modules?

### Challenge 2: From Scratch
**The Task:** Try implementing the core feature of this module in a completely blank Xcode project without looking at the reference code. Rely on Xcode's autocomplete and standard Apple documentation.

---

## References

1. [Apple Developer Documentation](https://developer.apple.com/documentation/)
2. [Swift Language Guide](https://docs.swift.org/swift-book/)
3. [Human Interface Guidelines](https://developer.apple.com/design/human-interface-guidelines/)

---

## Getting Help

Because this course is fully asynchronous, here's how to get unstuck:

- **Piazza** is the primary help channel. When asking a question, include: (1) what you're trying to do, (2) what you've tried, (3) the exact Xcode error message.
- **TA office hours** — check the Canvas calendar. Show up, share your screen, and get help.
- **Instructor office hours** — by appointment for deeper issues (design questions, project direction).


## Optionals

**Estimated effort:** 1-2 hours this topic
**Format:** Asynchronous online
**Prerequisites:** Previous iOS topics

{< hint info >}
**🎯 Topic Mission:** 
In this module, we will explore **Optionals** and learn how to integrate it into our iOS applications. Your mission is to understand the mechanics behind this concept and write robust Swift code.
{< /hint >}

---

## Learning Objectives

By the end of this session, you will be able to:
1. Understand the core concepts of Optionals.
2. Implement Optionals in an Xcode project.
3. Apply best practices to ensure clean and maintainable code.

---

## The Story So Far...

We have been progressively building our knowledge of iOS and Swift. In this module, we will expand our toolkit by diving into Optionals. 
Open your current Xcode project or start a new Playground to follow along with the hands-on material.

---

## Walkthrough: Exploring Optionals

> 📁 **Target Project** — Follow along by building the mini-app presented in the steps below, or integrate these concepts into your own ongoing projects.

# 8. Optionals

So far, we have learned about the variables and constants that we always initialize with data. What about we declare a variable without any data in it and try to use it, like the following:

```swift
var myInt:Int
print(myInt)
```

It will give us an error:

<figure><img src="/gitbook-assets/Screenshot 2023-05-04 at 12.01.22 AM.png" alt="" width="563"><figcaption></figcaption></figure>

So, we cannot use a variable without initializing it, right?. Well, sort of. Swift allows us to keep the variables uninitialized. It is done using a special data structure called `Optional`. Optionals are declared by adding a `?` at the end, like the following:

```swift
var myInt:Int? //Optional Int
print(myInt)
```

It will print the following:

```
nil
```

First of all, `nil` means there is no value. It is equivalent to `null` in many other programming languages like Java. So we have to make sure we do not use an optional value if we haven't yet stored a value in it; otherwise, it might crash the program. Luckily, Swift handles optionals safely.

To understand the process, let's assign a value to `myInt` before we print it:

```swift
var myInt:Int?
//assigning a value...
myInt = 10
print(myInt) //prints Optional(10)
```

It prints `Optional(10)` instead of `10`. That means, the value of `myInt` is wrapped with the optional data type. By wrapping the value with Optional, Swift makes us unwrap the value before we use it. While unwrapping, we can detect if the unwrapped value is `nil` or not and take care of `nil` before we use it in the program to prevent crashes. There are three ways of unwrapping them.

* If-let
* Guard-let
* Forced

We will talk about `if-let` and forced for now. Eventually we will learn about `guard-let`.

### If-let

We can unwrap an optional value using `if-let` block. To unwrap `myInt` we can write:

```swift
var myInt:Int?
//assigning a value...
myInt = 10

//optional binding with if-let...
if let unwrappedMyInt = myInt{
    //value present
    print(unwrappedMyInt)
}else{
    // handling nil
    print("Optional value myInt must be initialized!")
}
```

It prints:

```
10
```

So here, we are binding the optional value by assigning it to `unwrappedMyInt` constant. If a value is present, the `unwrappedMyInt` will hold the unwrapped value from the optional `myInt`; else, we have to handle the condition where we have `nil` in our optional.

### Forced

Another way of unwrapping an optional is using forced unwrapping. We need to put a `!` after the optional variable to unwrap the value from it forcefully. For example, we can write:

```swift
//forced unwrapping...
print(myInt!)
// prints 10
```

<mark style="color:red;">**Which will unwrap the value of**</mark><mark style="color:red;">**&#x20;**</mark><mark style="color:red;">**`myInt`**</mark><mark style="color:red;">**&#x20;**</mark><mark style="color:red;">**forcefully, even if it is**</mark><mark style="color:red;">**&#x20;**</mark><mark style="color:red;">**`nil`**</mark><mark style="color:red;">**.**</mark> \ <mark style="color:red;">**So you should refrain from using**</mark><mark style="color:red;">**&#x20;**</mark><mark style="color:red;">**`!`**</mark><mark style="color:red;">**&#x20;**</mark><mark style="color:red;">**unless you are absolutely sure that the value is not**</mark><mark style="color:red;">**&#x20;**</mark><mark style="color:red;">**`nil`**</mark><mark style="color:red;">**.**</mark>

**The usage of optionals is very common in Swift, and eventually, we will have more examples down the road.**

### Source code

{% file src="/gitbook-assets/MyPlayground8.playground (1).zip" %}

---

## Guided Practice Challenges

Before moving on to the next topic, try these low-stakes practice challenges in Xcode. They will build the exact muscle memory you need:

### Challenge 1: Experimentation
**The Scenario:** You've just learned about Optionals.
**The Task:** Experiment with the code snippets provided above. Can you alter the behavior by changing the parameters or combining it with concepts from previous modules?

### Challenge 2: From Scratch
**The Task:** Try implementing the core feature of this module in a completely blank Xcode project without looking at the reference code. Rely on Xcode's autocomplete and standard Apple documentation.

---

## References

1. [Apple Developer Documentation](https://developer.apple.com/documentation/)
2. [Swift Language Guide](https://docs.swift.org/swift-book/)
3. [Human Interface Guidelines](https://developer.apple.com/design/human-interface-guidelines/)

---

## Getting Help

Because this course is fully asynchronous, here's how to get unstuck:

- **Piazza** is the primary help channel. When asking a question, include: (1) what you're trying to do, (2) what you've tried, (3) the exact Xcode error message.
- **TA office hours** — check the Canvas calendar. Show up, share your screen, and get help.
- **Instructor office hours** — by appointment for deeper issues (design questions, project direction).


## Custom Data Types

# 9. Creating your own data types

Swift allows you to create your own data types in two ways:

* Structs
* Classes

We will first talk about structs and then move into classes.


## Table of Contents

{{< section >}}


## Protocols

**Estimated effort:** 1-2 hours this topic
**Format:** Asynchronous online
**Prerequisites:** Previous iOS topics

{< hint info >}
**🎯 Topic Mission:** 
In this module, we will explore **Protocols** and learn how to integrate it into our iOS applications. Your mission is to understand the mechanics behind this concept and write robust Swift code.
{< /hint >}

---

## Learning Objectives

By the end of this session, you will be able to:
1. Understand the core concepts of Protocols.
2. Implement Protocols in an Xcode project.
3. Apply best practices to ensure clean and maintainable code.

---

## The Story So Far...

We have been progressively building our knowledge of iOS and Swift. In this module, we will expand our toolkit by diving into Protocols. 
Open your current Xcode project or start a new Playground to follow along with the hands-on material.

---

## Walkthrough: Exploring Protocols

> 📁 **Target Project** — Follow along by building the mini-app presented in the steps below, or integrate these concepts into your own ongoing projects.

# 10. Protocols

Protocols in Swift are similar to Interfaces in many other languages like Java.

Protocols are like 'standards,' 'guidelines,' or 'interfaces.' A real-life example of that could be the 'USB-C' interface. Think about your laptop, desktop, or phone having USB-C ports. See, the devices implementing these USB-C interfaces are all different, but they all have implemented a standard. The standard describes the physical properties of the interface to which a USB-C connector cable will get attached, how many channels for data communications and power will be there, and what functionalities the devices must implement to have this USB-C interface.

We will cover the very basics of protocols for Swift here. A general syntax of a protocol is:

```swift
protocol SomeProtocol{
    //protocol definition goes here...
}
```




<!-- Merged from 10.1.-adopting-a-protocol.md -->

# 10.1. Adopting a protocol

A protocol contains only the declarations of the properties and functions that are needed to be adopted and implemented by a struct or class. For example, let's define our own USB interface, `USBMad.`

We can define our own `USBMad` protocol with a few guidelines:

* We need an id of the device to implement this protocol.
* We have the option to support a display adapter through that port.
* We have the option to support audio through that interface.
* We must implement charging through the port.
* We must implement data transfer through the port.

So we define the protocol where we declare three variables, `id` - for the device ID, `supportsDisplayAdapter` - to decide whether we would implement the display feature, and `supportsAudio` - to decide whether we would implement the audio or not. We also declare two methods to say this `USBMad` protocol must provide functionalities to charge the accessories and transfer data.

```swift
protocol USBMad{
    var id:Int{get}
    var supportsDisplayAdapter:Bool{get}
    var supportsAudio:Bool{get}
    func chargeAccessories()
    func transferData()
}
```

_<mark style="color:orange;">You might be confused about</mark>_ _<mark style="color:orange;">`{get}`</mark>_ _<mark style="color:orange;">declarations you see in the code. It means the property is a gettable property when implemented. You can also declare a property both gettable and settable by declaring</mark>_ _<mark style="color:orange;">`{get set}`</mark><mark style="color:orange;">. I will not dig deeper into these declarations; for now, I will just use</mark>_ _<mark style="color:orange;">`{get}`</mark><mark style="color:orange;">. For more information,</mark>_ [_you can read this article_](https://chetan-aggarwal.medium.com/swift-protocols-properties-distinction-get-get-set-32a34a7f16e9)_._

Now, let's adopt our USBMad protocol in our `MyLaptop` struct:

```swift
struct MyLaptop: USBMad{
    //struct's own properties
    var name:String
    var architecture:String
    
    //adopted/conformed variables and methods
    var id: Int
    var supportsDisplayAdapter: Bool
    var supportsAudio: Bool
    
    //adopted and to be implemented methods
    func chargeAccessories() {
        //MyLaptop's implementation of adopted method
        print("I am able to charge the accessories!")
    }
    func transferData() {
        //MyLaptop's implementation of adopted method
        print("You can send/receive data to/from me!")
    }   
}
```

Here, we are defining our struct `MyLaptop` where we adopt the `USBMad` protocol. We wrote `MyLaptop : USBMad` to say that `MyLaptop` adopts `USBMad` protocol. `MyLaptop` has it's own variables, `name` and `architecture`. Also, since it adopts the `USBMad` protocol, it must adopt the properties and methods of `USBMad` and implement them.

So we can create an instance of `MyLaptop` like the following:

{% code overflow="wrap" %}
```swift
let myLaptop = MyLaptop(
    name: "Sakib's Macbook",
    architecture: "ARM64",
    id: 1,
    supportsDisplayAdapter: true,
    supportsAudio: true
)

myLaptop.chargeAccessories()
//prints: I am able to charge the accessories!

myLaptop.transferData()
//prints: You can send/receive data to/from me!
```
{% endcode %}

See, we not only have to initialize `MyLaptop`'s own properties but must also initialize the properties `MyLaptop` adopts from `USBMad`.

Let's add another method `describe()` to `MyLaptop`:

```swift
struct MyLaptop: USBMad{
    //struct's own properties
    var name:String
    var architecture:String
    
    //adopted/conformed variables and methods
    var id: Int
    var supportsDisplayAdapter: Bool
    var supportsAudio: Bool
    
    //adopted and to be implemented methods
    func chargeAccessories() {
        //MyLaptop's implementation of adopted method
        print("I am able to charge the accessories!")
    }
    func transferData() {
        //MyLaptop's implementation of adopted method
        print("You can send/receive data to/from me!")
    }
    
    //MyLaptop's own method...
    func describe(){
        print(
            """
            My name is \(name).
            I use \(architecture) architecture.
            I have a USBMad interface with id: \(id).
            """
        )
        self.chargeAccessories()
        self.transferData()
    }
}
```

Calling `myLaptop.describe()` prints:

```
My name is Sakib's Macbook.
I use ARM64 architecture.
I have a USBMad interface with id: 1.
I am able to charge the accessories!
You can send/receive data to/from me!
```

These are the CliffsNotes version of adopting/confirming a protocol. You will see extensive use of protocols in iOS development.

## Reference code

{% file src="/gitbook-assets/MyPlayground10.1.playground.zip" %}



<!-- Merged from 10.2.-creating-a-single-protocol-from-multiple-protocols.md -->

# 10.2. Creating a single protocol from multiple protocols

Let's assume we need to write a protocol for Teaching Assistants (TA). The TAs are paid, receive TA training, and are rated by the professors. Let's assume that we have protocols to pay people, conduct TA training, and rating TAs:

```swift
//protocol for payment...
protocol Payment{
    func biweeklyPayment() -> Double
}

//protocol for TA training...
protocol TATraining{
    func completeTraining()
}

//protocol for TA rating...
protocol RatedByProfessor{
    func rate() -> Int
}
```

Now, we can consolidate all the protocols into one for the TAs like:

```swift
// Some code//consolidating to a single protocol...
protocol TeachingAssistant: Payment, TATraining, RatedByProfessor{
    //properties and methods for TeachingAssistant protocol...
}
```



<!-- Merged from 10.3.-inheriting-a-super-class-and-adopting-protocols-together.md -->

# 10.3. Inheriting a super class and adopting protocols together

We are continuing with the previous example. Now let's expand on the idea. TAs are also students. A student can be either a graduate student or an undergrad student. Let's assume Alice is an undergrad TA. Let's see how we can write some code to define Alice:

First, we need to define a class `Student` that has property `name` and an initializer method to initialize the instance.

```swift
//super class Student...
class Student{
    var name: String
    init(name:String) {
        self.name = name
    }
}
```

Then we need to define the class `UndergradTA` that inherits `Student` class, and adopts or conforms `TeachingAssistant` protocol:

```swift
//UndergradTA inherits Student, and adopts/conforms TeachingAssistant protocol...

class UndergradTA: Student, TeachingAssistant{
    //own property course...
    var course:String
    
    //initializer for UndergradTA...
    init(name: String, course:String) {
        self.course = course
        super.init(name: name)
    }
    
    //defining adopted methods from TeachingAssistant...
    func biweeklyPayment() -> Double {
        return 1_500.00
    }
    
    func completeTraining() {
        print("\(name) completed the TA training.")
    }
    
    func rate() -> Int {
        return 5
    }
    
    // own describe method of UndergradTA...
    func describe(){
        print(
            """
            \(name) is a TA of \(course) course.
            They were rated \(self.rate())/5 by the professor.
            They are paid \(self.biweeklyPayment()) biweekly.
            """
        )
        self.completeTraining()
    }
}

```

<mark style="color:orange;">**Please note: a class can only inherit one superclass, but it can adopt as many protocols as it needs. So if there is a superclass to be inherited, the class is written as the first one after**</mark><mark style="color:orange;">\*\*</mark> `:` <mark style="color:orange;">**(like**</mark> <mark style="color:orange;">**`Student`**</mark> <mark style="color:orange;">**in this example)**</mark> <mark style="color:orange;">**followed by the protocols separated by**</mark> `,`(comma).\*\*

Here, in the above code, we can see `UndergradTA` the inherited `Student` class and adopted `TeachingAssistant` protocol. We have a new variable `course` in `UndergradTA`, so we write an `init()` method to initialize both the variable `course` and the variable `name` in the superclass `Student`.

Then we implement the adopted methods of the protocol `TeachingAssistant`. And finally we write `UndergradTA`'s own method `describe()`.

Let's create the TA `alice`:

```swift
let alice = UndergradTA(
    name: "Alice",
    course: "Mobile App Development"
)

alice.describe()

/*
 alice.describe() prints:
 Alice is a TA of Mobile App Development course.
 They were rated 5/5 by the professor.
 They are paid 1500.0 biweekly.
 Alice completed the TA training.
 */
```

**Please try the whole thing in your own playground.**

So now we have a basic understanding of how classes work with other classes and protocols. In iOS development, we will repeatedly face these concepts.

## Reference code

{% file src="/gitbook-assets/MyPlayground10.3.playground (1).zip" %}

---

## Guided Practice Challenges

Before moving on to the next topic, try these low-stakes practice challenges in Xcode. They will build the exact muscle memory you need:

### Challenge 1: Experimentation
**The Scenario:** You've just learned about Protocols.
**The Task:** Experiment with the code snippets provided above. Can you alter the behavior by changing the parameters or combining it with concepts from previous modules?

### Challenge 2: From Scratch
**The Task:** Try implementing the core feature of this module in a completely blank Xcode project without looking at the reference code. Rely on Xcode's autocomplete and standard Apple documentation.

---

## References

1. [Apple Developer Documentation](https://developer.apple.com/documentation/)
2. [Swift Language Guide](https://docs.swift.org/swift-book/)
3. [Human Interface Guidelines](https://developer.apple.com/design/human-interface-guidelines/)

---

## Getting Help

Because this course is fully asynchronous, here's how to get unstuck:

- **Piazza** is the primary help channel. When asking a question, include: (1) what you're trying to do, (2) what you've tried, (3) the exact Xcode error message.
- **TA office hours** — check the Canvas calendar. Show up, share your screen, and get help.
- **Instructor office hours** — by appointment for deeper issues (design questions, project direction).


## Sorting Arrays

**Estimated effort:** 1-2 hours this topic
**Format:** Asynchronous online
**Prerequisites:** Previous iOS topics

{< hint info >}
**🎯 Topic Mission:** 
In this module, we will explore **Sorting Arrays** and learn how to integrate it into our iOS applications. Your mission is to understand the mechanics behind this concept and write robust Swift code.
{< /hint >}

---

## Learning Objectives

By the end of this session, you will be able to:
1. Understand the core concepts of Sorting Arrays.
2. Implement Sorting Arrays in an Xcode project.
3. Apply best practices to ensure clean and maintainable code.

---

## The Story So Far...

We have been progressively building our knowledge of iOS and Swift. In this module, we will expand our toolkit by diving into Sorting Arrays. 
Open your current Xcode project or start a new Playground to follow along with the hands-on material.

---

## Walkthrough: Exploring Sorting Arrays

> 📁 **Target Project** — Follow along by building the mini-app presented in the steps below, or integrate these concepts into your own ongoing projects.

# 11. Sorting Arrays

Here we will talk about one of the most useful lessons while developing iOS apps, sorting. First, we will start with sorting a very simple array, and then we will look into how to sort arrays of custom struct/class objects.




<!-- Merged from 11.1.-increasing-order.md -->

# 11.1. Increasing order

We can call `sorted()` function to sort an array with the increasing order of it's values.

```swift
var arrayOfInt:[Int] = [1,56,89,23,4,6]

print(arrayOfInt.sorted())

// prints: [1, 4, 6, 23, 56, 89]
```

Let's try to sort an array of Strings.

```swift
//array of Strings ...

var arrayOfStrings = ["apple", "orange", "pineapple", "a", "b"]

print(arrayOfStrings.sorted())

//prints: ["a", "apple", "b", "orange", "pineapple"]
```

The above code sorted the array in a lexicographical order (like how the words in a dictionary are sorted).

###

###



<!-- Merged from 11.2.-decreasing-order.md -->

# 11.2. Decreasing order

Unfortunately, it is not as simple to sort an array in a reversed (decreasing) order as it is to sort it in an increasing order. We need to write a comparator function or closure and use `sort(by: <comparator>))` to do it.

Think about how you would sort an array of items.

* You'd probably iterate through the array and compare each item with the other items to see where to put the current item. You need to compare two values to figure out which one is bigger or which one is smaller.
* Now, sorting in increasing order is the default behavior, so you do not need to modify the comparator logic of Swift. However, sorting in decreasing is not a default behavior, so you need to specify how you would compare each pair of values.

Let's define our compare function `decreasing()` as follows:

```swift
//function to compare two values to find which if value1 is greater than value2...
func decreasing(value1:Int, value2:Int)->Bool{
    return value1 > value2
}
```

In increasing order, the comparator checks if the first value of a pair of values is smaller than the second value. If yes, then do not swap; else, swap. In the above code, we are reversing the order. So we are checking if the first value is greater than the second value, then do not swap; they are in the correct order.

Then we call the `sort(by: ..)` as follows:

```swift
var arrayOfInt:[Int] = [1,56,89,23,4,6]

//sort the array by using the comparator function decreasing...
arrayOfInt.sort(by: decreasing)

print(arrayOfInt)
//prints: [89, 56, 23, 6, 4, 1]
```

### Do it using closures (not functions)

We can concisely write code without writing a different function using closures. And it would be best if you got used to this style. As we have seen, we can use a function as a variable, or conversely, we can write code inline instead of a variable. So let's write a closure directly inside the `sort(by: ...)` as follows:

```swift
arrayOfIntC.sort(by: { (value1:Int, value2:Int) -> Bool in
    return value1 > value2
})
```

The difference between the previous code and the above code is that instead of writing a separate function `decreasing()`, we are writing the closure inside the `sort(by:..)` call.

Now let's see what happens:

```swift
var arrayOfIntC = [34,6,89,56,78,14]

print(arrayOfIntC)
//prints: [89, 78, 56, 34, 14, 6]
```

You can shorten it even more. I did not want to give you an overdose yet. :joy:



<!-- Merged from 11.-3.-sorting-an-array-of-custom-data.md -->

# 11. 3. Sorting an array of custom data

Let's look at the following example:

```swift
import UIKit

struct User{
    var name: String
    var age: Int
    var city: String
}

var users = [
    User(name: "Alice", age: 12, city: "Boston"),
    User(name: "Bob", age: 21, city: "Charlotte"),
    User(name: "Chris", age: 45, city: "NYC"),
    User(name: "David", age: 23, city: "Boston"),
    User(name: "Dillon", age: 89, city: "San Francisco"),
]

//MARK: sort by name in decreasing order
users.sort(by: { (user1:User, user2:User)-> Bool in
    return user1.name > user2.name
})

for user in users{
    print(user)
}
/*prints:
User(name: "Dillon", age: 89, city: "San Francisco")
User(name: "David", age: 23, city: "Boston")
User(name: "Chris", age: 45, city: "NYC")
User(name: "Bob", age: 21, city: "Charlotte")
User(name: "Alice", age: 12, city: "Boston")
 */

//MARK: sort by age in increasing order
users.sort(by: { (user1:User, user2:User)-> Bool in
    return user1.age < user2.age
})

for user in users{
    print(user)
}
/* prints:
User(name: "Alice", age: 12, city: "Boston")
User(name: "Bob", age: 21, city: "Charlotte")
User(name: "David", age: 23, city: "Boston")
User(name: "Chris", age: 45, city: "NYC")
User(name: "Dillon", age: 89, city: "San Francisco")
*/

```

This example is pretty self-explanatory. We have a struct to create our custom data type, `User`. Each user has `name`, `age`, and `city`.

We first want to sort the array of `User`s based on their name in decreasing order. So, wrote a closure that takes in a pair of `User` objects. Then compared their names.

The next task is to sort the users in increasing order of their age. The next closure takes care of it.

**That's pretty much it about the basics of sorting in Swift.**

---

## Guided Practice Challenges

Before moving on to the next topic, try these low-stakes practice challenges in Xcode. They will build the exact muscle memory you need:

### Challenge 1: Experimentation
**The Scenario:** You've just learned about Sorting Arrays.
**The Task:** Experiment with the code snippets provided above. Can you alter the behavior by changing the parameters or combining it with concepts from previous modules?

### Challenge 2: From Scratch
**The Task:** Try implementing the core feature of this module in a completely blank Xcode project without looking at the reference code. Rely on Xcode's autocomplete and standard Apple documentation.

---

## References

1. [Apple Developer Documentation](https://developer.apple.com/documentation/)
2. [Swift Language Guide](https://docs.swift.org/swift-book/)
3. [Human Interface Guidelines](https://developer.apple.com/design/human-interface-guidelines/)

---

## Getting Help

Because this course is fully asynchronous, here's how to get unstuck:

- **Piazza** is the primary help channel. When asking a question, include: (1) what you're trying to do, (2) what you've tried, (3) the exact Xcode error message.
- **TA office hours** — check the Canvas calendar. Show up, share your screen, and get help.
- **Instructor office hours** — by appointment for deeper issues (design questions, project direction).


## 9.1. Structs

**Estimated effort:** 1-2 hours this topic
**Format:** Asynchronous online
**Prerequisites:** Previous iOS topics

{< hint info >}
**🎯 Topic Mission:** 
In this module, we will explore **9.1. Structs** and learn how to integrate it into our iOS applications. Your mission is to understand the mechanics behind this concept and write robust Swift code.
{< /hint >}

---

## Learning Objectives

By the end of this session, you will be able to:
1. Understand the core concepts of 9.1. Structs.
2. Implement 9.1. Structs in an Xcode project.
3. Apply best practices to ensure clean and maintainable code.

---

## The Story So Far...

We have been progressively building our knowledge of iOS and Swift. In this module, we will expand our toolkit by diving into 9.1. Structs. 
Open your current Xcode project or start a new Playground to follow along with the hands-on material.

---

## Walkthrough: Exploring 9.1. Structs

> 📁 **Target Project** — Follow along by building the mini-app presented in the steps below, or integrate these concepts into your own ongoing projects.

# 9.1. Structs

Do you remember [tuples](../../2.-collections/2.3.-tuples.md)? We can store different types of data together in a tuple. Structs are very similar to that. We can have any kind of variables in it. For example, a simple struct to store a person's details would be:

```swift
struct Person{
    var name:String
    var age:Int
    var city:String
}
```

Here the struct `Person` holds three properties <mark style="color:purple;">(we call the variables inside structs properties)</mark>: two strings `name` and `city`, and one integer `age`. **Please note that** in Swift the name of a struct or class should start with an uppercase character, like <mark style="color:blue;">**P**</mark>**erson.**

Now since struct creates a custom data type for us, we can use `Person` as a data type everywhere. So, let's create a new variable (<mark style="color:purple;">or instance, more appropriately</mark>) of type `Person`.

```swift
var newPerson: Person = Person(name: "Bob Smith", age: 30, city: "Boston")

//print the variable person of type Person...
print(newPerson)
//print newPerson's name...
print(newPerson.name)
```

It will print:

```
Person(name: "Bob Smith", age: 30, city: "Boston")
Bob Smith
```

So we can create instances of our custom data type `Person` and once created, we can access the properties of the instances. Also, we can modify the properties of the instances, e.g. we can modify the `age` of `newPerson` like:

```swift
//modifying the inner variables of newPerson
newPerson.age = 36
//printing newPerson after changing the age...
print(newPerson)
```

It prints:

```
Person(name: "Bob Smith", age: 36, city: "Boston")
```

The value of `newPerson`'s age got changed to 36.

### Computed properties

Swift allows us to have special properties called computed properties in a struct. Basically, it means that we do not supply the value for that property. When we create a variable of a struct, the struct automatically calculates the value and sets it. For example, from the `age` property of a `Person` we can easily determine if the person is a minor or an adult, right?

Let's modify the `Person` struct to add a new computed property called `isMinor:`

```swift
struct Person{
    var name:String
    var age:Int
    var city:String
    
//    computed property .....
    var isMinor:Bool{
        if age < 18{
            return true
        }else{
            return false
        }
    }
}
```

Here, we are computing the value of the property `isMinor`. If the value of `age` is less than 18, we return `true`, that basically sets the value of `isMinor` to `true`. Else, it sets the value of the property to `false`. Now, let's add the following code:

```swift
print(newPerson)

if(newPerson.isMinor){
    print("\(newPerson.name) is a minor!")
}else{
    print("\(newPerson.name) is an adult!")
}
```

It prints:

```
Person(name: "Bob Smith", age: 36, city: "Boston")
Bob Smith is an adult!
```

So depending on different values of the property `age`, it automatically computes the value of the property `isMinor`.




<!-- Merged from 9.1.1.-functions-methods-inside-structs.md -->

# 9.1.1. Functions (methods) inside structs

We can write functions inside structs. In Swift, they're called methods. For example, we can have a `printProfile` method in our `Profile` struct:

```swift
struct Person{
    var name:String
    var age:Int
    var city:String
    
//    computed property .....
    var isMinor:Bool{
        if age < 18{
            return true
        }else{
            return false
        }
    }
//    method printProfile...
    
    func printProfile(){
        print(
            """
            Hi! I am \(name).
            I am \(age) years old.
            And I live in \(city)!
            Happy coding!
            """
        )
    }
}
```

Then we call the method from outside the struct:

```swift
//printing the profile intro using the method printProfile...
newPerson.printProfile()
```

It prints:

```
Hi! I am Bob Smith.
I am 36 years old.
And I live in Boston!
Happy coding!
```

### Struct initializers

We can set the default values for our structs using the initializer method `init()`. Let's add the `init()` method in `Person` where we set the `name` to "Unknown", `age` to `18`, and `city` to "Not Given".

```swift
struct Person{
    var name:String
    var age:Int
    var city:String
    
//    initializer method...
    init() {
        name = "Unknown"
        age = 18
        city = "Not Given"
    }
    
//    computed property .....
    var isMinor:Bool{
        if age < 18{
            return true
        }else{
            return false
        }
    }
    
//    method printProfile...
    
    func printProfile(){
        print(
            """
            Hi! I am \(name).
            I am \(age) years old.
            And I live in \(city)!
            Happy coding!
            """
        )
    }
}
```

Then we can create an instance of `Person` without providing any parameters, like:

```swift
//Creating an instance using the init()
var newPerson = Person()

//print the variable person of type Person...
print(newPerson) 

//modifying the properties of newPerson...
newPerson.name = "Bob Smith"
newPerson.age = 36
newPerson.city = "Boston"

//printing newPerson after modifying the properties...
print(newPerson)

//printing the computed property...
if(newPerson.isMinor){
    print("\(newPerson.name) is a minor!")
}else{
    print("\(newPerson.name) is an adult!")
    //prints 
}

//printing the profile intro using the method printProfile...
newPerson.printProfile()
```

It prints:

```
Person(name: "Unknown", age: 18, city: "Not Given")
Person(name: "Bob Smith", age: 36, city: "Boston")
Bob Smith is an adult!
Hi! I am Bob Smith.
I am 36 years old.
And I live in Boston!
Happy coding!
```

So, we can create an instance of a struct with default values by writing `init()` method. Then we have to set the values later.

<mark style="color:purple;">**Please note: you need to write**</mark><mark style="color:purple;">\*\*</mark> `init()` \*\*<mark style="color:purple;">**method before all the other methods and computed properties.**</mark>

## Source code

{% file src="/gitbook-assets/MyPlayground9.1.1.playground (1).zip" %}



<!-- Merged from 9.1.2.-initializing-structs-with-different-initializers.md -->

# 9.1.2. Initializing structs with different initializers

We can define multiple initializers in a struct. At this point, we will define a new struct `Car` to demonstrate this concept. Let's define `Car`:

```swift
struct Car{
    var make:String
    var model:String
    var year:Int
    
    init(){
        make = "Not set"
        model = "Not set"
        year = 0
    }
}

//creating an instance of Car...
var car = Car()

//printing the instance...
print(car)

```

It prints:

```
Car(make: "Not set", model: "Not set", year: 0)
```

Here, we can see that all the default values were set when we created the instance.

Now, let's define another custom `init()` method along with the default one. This custom `init()` will accept parameters when we are creating the instance.

```swift
struct Car{
    var make:String
    var model:String
    var year:Int
    
    //default init...
    init(){
        make = "Not set"
        model = "Not set"
        year = 0
    }
    //custom init...
    init(make:String, model:String, year:Int) {
        self.make = make
        self.model = model
        self.year = year
    }
}
```

_<mark style="color:purple;">Do you see the</mark>_ _<mark style="color:purple;">`self`</mark>_ _<mark style="color:purple;">keyword? What do you think it is? -</mark>_ `self` is used to refer to the current instance of `Car`. See, we are using the same names for the parameters the method accepts as the properties of `Car`. By writing `self.make = make`, we are instructing the program to set the value of the current instance's `make` property to the value of the parameter `make` accepted by the `init()` method.

Now, we can create an instance of `Car` by calling the new `init(make:String, model:String, year:Int)` method. Let's try:

```swift
//creating an instance of Car using the custom init()...
var car2 = Car(make: "Toyota", model: "Corolla", year: 2020)
print(car2)
```

It prints:

```
Car(make: "Toyota", model: "Corolla", year: 2020)
```

So yes! We can create instances of a struct using multiple `init()` methods.

### Struct initialization and Optionals

Let's continue with the same `Car` example. Let's assume that when we are creating an instance of `Car` struct, we only want to set the values for two parameters, `make` and `model`, and keep the value of `year` empty. We can write a new `init()` method like:

```swift
init(make:String, model:String){
    self.make = make
    self.model = model
    //year is left uninitialized...
}
```

If we add this method, we will see an error:

<figure><img src="/gitbook-assets/Screenshot 2023-05-04 at 2.01.14 PM (1).png" alt=""><figcaption></figcaption></figure>

So it is saying that we need to initialize all stored properties (`year` is not initialized). Now, how can we initialize `make` and `model` without initializing `year`?

Remember **Optional?**

Yes, we can declare `year` as an Optional like the following:

```swift
struct Car{
    var make:String
    var model:String
    var year:Int? //Optional
    
    //omitted other codes...
    init(make:String, model:String){
        self.make = make
        self.model = model
    }
}
```

Now that we do not have the error anymore, we can create an instance of `Car` and initialize it:

```swift
//creating an instance of Car...
var car3 = Car(make: "Honda", model: "Civic")
print(car3)
//prints: Car(make: "Honda", model: "Civic", year: nil)

//Assigning a value of year after we create the instance
car3.year = 2022
print(car3)
//prints: Car(make: "Honda", model: "Civic", year: Optional(2022))

```

Do you see an issue? `year` is wrapped with Optional. So if you want to use it anywhere, we should use an unwrapping technique like [if-let](../../8.-optionals.md).

## Source code

{% file src="/gitbook-assets/MyPlayground9.1.2.playground (1).zip" %}



<!-- Merged from 9.1.3.-manipulating-object-properties-inherently-in-a-struct.md -->

# 9.1.3. Manipulating object properties inherently in a struct

What about we try to update a property of an object and write a function **directly inside of the struct**? So, potentially we will use an inherent function to update a property of the current object.&#x20;

So, let's try to add a new function inside the struct `Car` , `updateYear()` to change the year of a car.

```swift
// updating a car's year...
func updateYear(_ year:Int){
    self.year = year
}
```

So if we put it in the struct, the entire code looks like:

```swift
struct Car{
    var make:String
    var model:String
    var year:Int?
    
    init(){
        make = "Not set"
        model = "Not set"
        year = 0
    }
    
    init(make:String, model:String, year:Int) {
        self.make = make
        self.model = model
        self.year = year
    }
    
    init(make:String, model:String){
        self.make = make
        self.model = model
    }
    
    func updateYear(_ year:Int){
        self.year = year
    }
}
```

If you write the updateYear function, you'll see the following error:

<figure><img src="/gitbook-assets/Screenshot 2025-09-09 at 5.00.06 PM.png" alt=""><figcaption></figcaption></figure>

It says that self is immutable. **Why?**

**struct** data type is a value type, it is not a reference type. It means, the objects are stored directly in their allocated memory space (RAM), if you access the objects with their variable names, you directly access them from the memory. If you pass a variable to a function through a parameter, it copies the whole object into the function, and never manipulates the original data.&#x20;

On the other hand, the variables of a **reference** data type like class do not directly store the objects in their allocated memory space. Rather, the variables will store a pointer (reference) to the objects, and the objects are stored in a separate memory location. So if you pass a reference type variable into a function through parameters, it will pass the reference to the original object. The function can manipulate the original data. It creates a shared **mutable** state.

_(In programming, a mutable object is one whose state or value can be changed after it is created.)_

**Long story short,** since Swift is a **safe** language, by default the objects of the **value data types** are not mutating. You have to purposefully make the manipulating functions mutating to allow the functions to mutate the object, or manipulate its original value. So we will change the function above to the following:

```swift
mutating func updateYear(_ year:Int){
    self.year = year
}
```

`mutating`  keyword defines that this function can update the original data for the object.&#x20;

So let's use the new method:

```swift
import UIKit

//MARK: 9.1.2 initializers...
struct Car{
    var make:String
    var model:String
    var year:Int?
    
    init(){
        make = "Not set"
        model = "Not set"
        year = 0
    }
    
    init(make:String, model:String, year:Int) {
        self.make = make
        self.model = model
        self.year = year
    }
    
    init(make:String, model:String){
        self.make = make
        self.model = model
    }
    
    mutating func updateYear(_ year:Int){
        self.year = year
    }
}

//creating an instance of Car using the custom init()...
var car2 = Car(make: "Toyota", model: "Corolla", year: 2020)
print(car2)
car2.updateYear(2025)
print(car2)
```

It prints:

```
Car(make: "Toyota", model: "Corolla", year: Optional(2020))
Car(make: "Toyota", model: "Corolla", year: Optional(2025))
```

**So, if the object you are using is of a value type, any inherent manipulator needs to be explicitly defined as mutating.**&#x20;

---

## Guided Practice Challenges

Before moving on to the next topic, try these low-stakes practice challenges in Xcode. They will build the exact muscle memory you need:

### Challenge 1: Experimentation
**The Scenario:** You've just learned about 9.1. Structs.
**The Task:** Experiment with the code snippets provided above. Can you alter the behavior by changing the parameters or combining it with concepts from previous modules?

### Challenge 2: From Scratch
**The Task:** Try implementing the core feature of this module in a completely blank Xcode project without looking at the reference code. Rely on Xcode's autocomplete and standard Apple documentation.

---

## References

1. [Apple Developer Documentation](https://developer.apple.com/documentation/)
2. [Swift Language Guide](https://docs.swift.org/swift-book/)
3. [Human Interface Guidelines](https://developer.apple.com/design/human-interface-guidelines/)

---

## Getting Help

Because this course is fully asynchronous, here's how to get unstuck:

- **Piazza** is the primary help channel. When asking a question, include: (1) what you're trying to do, (2) what you've tried, (3) the exact Xcode error message.
- **TA office hours** — check the Canvas calendar. Show up, share your screen, and get help.
- **Instructor office hours** — by appointment for deeper issues (design questions, project direction).


## 9.2. Classes

**Estimated effort:** 1-2 hours this topic
**Format:** Asynchronous online
**Prerequisites:** Previous iOS topics

{< hint info >}
**🎯 Topic Mission:** 
In this module, we will explore **9.2. Classes** and learn how to integrate it into our iOS applications. Your mission is to understand the mechanics behind this concept and write robust Swift code.
{< /hint >}

---

## Learning Objectives

By the end of this session, you will be able to:
1. Understand the core concepts of 9.2. Classes.
2. Implement 9.2. Classes in an Xcode project.
3. Apply best practices to ensure clean and maintainable code.

---

## The Story So Far...

We have been progressively building our knowledge of iOS and Swift. In this module, we will expand our toolkit by diving into 9.2. Classes. 
Open your current Xcode project or start a new Playground to follow along with the hands-on material.

---

## Walkthrough: Exploring 9.2. Classes

> 📁 **Target Project** — Follow along by building the mini-app presented in the steps below, or integrate these concepts into your own ongoing projects.

# 9.2. Classes

At first glance, a `class` looks the same as a `struct`. However, there are a few major differences between them.

We will discuss classes using the differences they have.

An example of a class is as follows:

```swift
class Vehicle{
    var type:String
}
```

If you just write the above block of code, you'll get an error:

<figure><img src="/gitbook-assets/Screenshot 2023-05-04 at 5.08.56 PM (1).png" alt="" width="563"><figcaption></figcaption></figure>

So, it is not like a `struct` where you do not need to have an initializer method. You must have your own initializer to be able to create an instance of a `class`. <mark style="color:orange;">**This is the first difference between a**</mark><mark style="color:orange;">\*\*</mark> `struct` <mark style="color:orange;">**and a**</mark> `class`.\*\*

Now let's define our `init()` method and create a variable:

```swift
class Vehicle{
    var type:String
    
    //mandatory init() method
    init(type:String){
        self.type = type
    }
    
}

var car1 = Vehicle(type: "Car")
var car2 = Vehicle(type: "Truck")
var car3 = Vehicle(type: "Minivan")
print(car1.type) //prints: Car
```




<!-- Merged from 9.2.1.-inheritance.md -->

# 9.2.1. Inheritance

**One of the most critical capabilities that a class has but a struct doesn't have is inheritance.** Inheritance is the ability of a class to inherit the properties of another existing class and add more functionalities along with it. In other words, we can build a new class based on another existing class. For example, we can build a new class `Car` based on the `Vehicle` class we have:

```swift
//The Vehicle class....
class Vehicle{
    var type:String
    
    init(type:String){
        self.type = type
    }
    
}
// defining a new class inheriting Vehicle class
class Car:Vehicle{
    var make:String
    var model:String
    
    init(type:String, make:String, model:String) {
        //initializing this instance's properties...
        self.make = make
        self.model = model
        
        //Calling super class's initializer...
        super.init(type: type)
    }
}
```

Here, we are doing a few things:

* Using `:` we are saying that `Car` inherits properties from an existing class `Vehicle`. In this case, `Vehicle` is the super class of `Car`.
* We added two properties `make` and `model` in `Car` class. Hence, we now have three properties in `Car` class: `type` (inherited from `Vehicle`), `make`, and `model`.
* We need to write our own `init()` method for each class we write. So, `Car` and `Vehicle` both have their own initializers. Think about the initializer of class `Car`. The `Car` class has it's own properties, so we need to initialize them. Also, we need to initialize the super class `Vehicle` inside `Car`'s initializer. That is what we are doing in the `init()` function inside `Car`. We use `super` keyword is used to access the super class `Vehicle`'s properties.

### Overriding methods

Let's define a method `describe()` inside the class `Vehicle` which prints a string.

```swift
class Vehicle{
    var type:String
    
    init(type:String){
        self.type = type
    }
    
    //method describing a Vehicle...
    func describe(){
        print("This is a \(type).")
    }
    
}
// creating an instance of class Vehicle...
var vehicle = Vehicle(type: "Car")

vehicle.describe() // prints: This is a Car.
```

Now, let's create an instance of the `Car` class, and call `describe()` method it inherited from `Vehicle`.

```swift
//creating an instance of Car...
var car = Car(type: "Car", make: "Toyota", model: "Rav4")

car.describe() //prints: This is a Car.
```

The thing is, it still just prints, "This is a Car." However, we have more information in class `Car,` like the `make` and `model` of the instance. What if we want to print more information?

We can override the method we inherited from the super class `Vehicle`. For example,

```swift
class Car:Vehicle{
    var make:String
    var model:String
    
    init(type:String, make:String, model:String) {
        //initializing this instance's properties...
        self.make = make
        self.model = model
        
        //Calling super class's initializer...
        super.init(type: type)
    }
    
    //overriding super.describe()...
    override func describe() {
        print(
            """
            This is a \(type).
            It is a \(make) \(model).
            """
        )
    }
}

//creating an instance of Car...
var car = Car(type: "Car", make: "Toyota", model: "Rav4")
car.describe()
```

It prints:

```
This is a Car.
It is a Toyota Rav4.
```

This is called method overriding. A class not only can inherit a method from the superclass but also can change (override) it.

## Source code

{% file src="/gitbook-assets/MyPlayground9.2.1.playground (1).zip" %}



<!-- Merged from 9.2.2.-value-vs.-reference.md -->

# 9.2.2. Value vs. Reference

Another major difference between a struct and a class is how they behave when copied. Structs are 'value types,' and classes are 'reference types.'

<mark style="color:purple;">**(Structs)**</mark> When you copy an instance of a struct from an existing instance, both instances work independently. For example:

```swift
struct User{
    var name:String
}

//creating an instance of User...
var user1 = User(name: "John Smith")

//copying the instance to a new instance...
var user2 = user1

//changing the name in the copied instance...
user2.name = "Bob Smith"

print(
    """
    User name of user1 = \(user1.name)
    User name of user2 = \(user2.name)
    """
)

```

It prints:

```
User name of user1 = John Smith
User name of user2 = Bob Smith
```

We copied the instance `user1` to another instance `user2`. When I changed the `name` in `user2` it did not have any effect on `user1`. They worked independent to each other. The data of the instances are independent and separate to each other.

<mark style="color:purple;">**(Classes)**</mark> However, classes are reference types. For example,

```swift
class Person{
    var name:String
    init(name:String){
        self.name = name
    }
}

//creating an instance of Person...
var person1 = Person(name: "John Snow")

//copying the instance to a new instance...
var person2 = person1

//changing the name in the copied instance...
person2.name = "Arya Stark"

print(
    """
    Name of person1 = \(person1.name)
    Name of person2 = \(person2.name)
    """
)
```

It prints:

```
Name of person1 = Arya Stark
Name of person2 = Arya Stark
```

Do you find the difference?

Here, we copied `person1` to `person2`. But when we changed the name of `person2`, it also changed the `name` of `person1`. So basically, the data is not separate for the two instances, they share the same data reference.

## Reference Code

{% file src="/gitbook-assets/MyPlayground9.2.2.playground (1).zip" %}

---

## Guided Practice Challenges

Before moving on to the next topic, try these low-stakes practice challenges in Xcode. They will build the exact muscle memory you need:

### Challenge 1: Experimentation
**The Scenario:** You've just learned about 9.2. Classes.
**The Task:** Experiment with the code snippets provided above. Can you alter the behavior by changing the parameters or combining it with concepts from previous modules?

### Challenge 2: From Scratch
**The Task:** Try implementing the core feature of this module in a completely blank Xcode project without looking at the reference code. Rely on Xcode's autocomplete and standard Apple documentation.

---

## References

1. [Apple Developer Documentation](https://developer.apple.com/documentation/)
2. [Swift Language Guide](https://docs.swift.org/swift-book/)
3. [Human Interface Guidelines](https://developer.apple.com/design/human-interface-guidelines/)

---

## Getting Help

Because this course is fully asynchronous, here's how to get unstuck:

- **Piazza** is the primary help channel. When asking a question, include: (1) what you're trying to do, (2) what you've tried, (3) the exact Xcode error message.
- **TA office hours** — check the Canvas calendar. Show up, share your screen, and get help.
- **Instructor office hours** — by appointment for deeper issues (design questions, project direction).


## 1.-variables-data-types-and-more.

**Estimated effort:** 1-2 hours this topic
**Format:** Asynchronous online
**Prerequisites:** Previous iOS topics

{< hint info >}
**🎯 Topic Mission:** 
In this module, we will explore **this topic** and learn how to integrate it into our iOS applications. Your mission is to understand the mechanics behind this concept and write robust Swift code.
{< /hint >}

---

## Learning Objectives

By the end of this session, you will be able to:
1. Understand the core concepts of this topic.
2. Implement this topic in an Xcode project.
3. Apply best practices to ensure clean and maintainable code.

---

## The Story So Far...

We have been progressively building our knowledge of iOS and Swift. In this module, we will expand our toolkit by diving into this topic. 
Open your current Xcode project or start a new Playground to follow along with the hands-on material.

---

## Walkthrough: Exploring this topic

> 📁 **Target Project** — Follow along by building the mini-app presented in the steps below, or integrate these concepts into your own ongoing projects.

# 1. Variables, Data types, and more.

This is where we begin our journey with Swift. In this book section, we will go through the simple data types in Swift and see how to work with them. Please go to the next page to start!!!




<!-- Merged from 1.1.-creating-a-swift-playground.md -->

# 1.1. Creating a Swift Playground

Open Xcode from your Launchpad. You should be seeing something like the following:

<figure><img src="/gitbook-assets/Screenshot 2023-05-01 at 11.46.52 AM (1).png" alt=""><figcaption><p>Xcode launch screen</p></figcaption></figure>

Do not create an Xcode project yet; click on _**File -> New -> Playground**_. Select _**Blank**,_ click _**Next**_, give the playground a name, and click on _Create._ If you see something like the following, you are good to go! That is the first step toward learning Swift!!!

<figure><img src="/gitbook-assets/Screenshot 2023-05-01 at 12.01.56 PM (2).png" alt=""><figcaption><p>Playground</p></figcaption></figure>

## Video

{% embed url="https://www.youtube.com/watch?v=IG9nba_A7Z4" %}
Demo
{% endembed %}



<!-- Merged from 1.2.-variables.md -->

# 1.2. Variables

We will write our "Hello World" code here. In very short, variables are the places in your code where you can store program data while the program is running. They are called variables because you can change (vary) their values.

Now the Playground you created comes with a line of code:

```swift
var greeting = "Hello, playground"
```

It creates a new variable called _greeting_, and gives it the value "Hello, playground".

<figure><img src="/gitbook-assets/Screenshot 2023-05-01 at 12.31.15 PM (1).png" alt=""><figcaption></figcaption></figure>

After you click on the play button, you'll see "Hello, playground" on the right side, which is the output area of the Playground.

Since greeting is a variable, we can always change it from the code, right? So let's change the value to something else like:

```swift
greeting = "Hello, Bonobos!!!!"
```

Now, you can see the new values showing on the output area!

<figure><img src="/gitbook-assets/Screenshot 2023-05-01 at 12.35.08 PM (1).png" alt=""><figcaption></figcaption></figure>

Since greeting is a variable, we can change the values without creating a new variable for the new value!

## Video

{% embed url="https://youtu.be/_a2NJAJg-WM" %}



<!-- Merged from 1.3.-type-safety.md -->

# 1.3. Type safety

Swift is a type-safe language. It means that once you create a variable, it is stuck with a specific data type, and you cannot change the data type of it. Every variable has to have a particular data type.

So far in our code, we have a variable _**greeting**_ having the value "Hello, Bonobos!!!". What if we try to set the value of _**greeting**_ to 12? Let's try it!

```swift
greeting = 12
```

And click on play! We will see something like the following:

<figure><img src="/gitbook-assets/Screenshot 2023-05-01 at 1.06.02 PM (1).png" alt=""><figcaption></figcaption></figure>

It says, "Cannot assign the value of type **'Int'** to **'String'**. So it means that Swift automatically sets the type of the variable _**greeting**_ to a String when it creates the variable with a String. Now that the type is already assigned, when I wanted to change the value to an integer 12, it yelled at me.

Ok, let's create another variable to hold the integer.

```swift
var count = 12
```

Here it creates a variable named count, then finds that the value I am initially setting (12) is of type **Int** (integer). So, _**count**_ can only hold **Int**s after the creation.

There is a _swift_ and usable trick for large integers. For example, if you want to store 1 million (1000000) in a variable, It is hard to read/type when you deal with a stream of consecutive zeroes together. Swift uses underscores as thousand separators. Like this:

```swift
var million = 1_000_000
```

**To sum up, you need to be very careful about the data types of variables. You must not mix up data types for a particular variable.**

## Video

{% embed url="https://youtu.be/XrHRxOiLX_o" %}



<!-- Merged from 1.4.-strings-and-print-to-console.md -->

# 1.4. Strings and print to console

Swift allows you to write strings in two ways. The first one is, of course, the age-old String we declare inside **" "**. The next one is multiline strings which you can write inside **""" """** (triple quotes on both sides).

An example of the first type is the _**greeting**_ variable we have. Let's try to see what a multi-line string is.

Let's create a string like the following:

```swift
var multiline = """
I am a multiline String.
I might look weird, but I am really very simple.
At times I could be very useful!
"""
```

After you define the String, if you look at the output area, you'll see that a character **'\n' is** added between two lines. **'\n'** denotes a new line. It means that the variable multiline contains a String that will be logically multiline and follows the exact format the user put in.

Now, you can use the command **print()** to display the output to the console. Let's put the following line of code:

```swift
print(multiline)
```

It should display the following at the bottom (console output) of Xcode:

<figure><img src="/gitbook-assets/Screenshot 2023-05-01 at 1.55.07 PM (1).png" alt=""><figcaption></figcaption></figure>

Now you get the full view of how a multiline String would get displayed.

## Video

{% embed url="https://youtu.be/FEoQh4CarpM" %}



<!-- Merged from 1.5.-floating-point-numbers-and-type-annotation.md -->

# 1.5. Floating point numbers and Type annotation

Two basic data types in Swift handle the floating point numbers (fractional values): **Double** and **Float.**

**Double** is short for "double-precision floating point number." It is a 64-bit floating point number. Long story short, it can hold very large fractional values. Swift uses **Double** as its default data type for floating point literals.

On the other hand, **Float** is a 32-bit floating point number, which is less precise than **Double,** and you do not need to use it unless you are building games or graphics applications.

So now, let's write a Double variable:

```swift
var myNum = 12.5
print(myNum)
print(type(of: myNum))
```

Here Swift automatically sets the type of the variable myNum to **Double** since I put a fractional value to it. The above code outputs the following:

<figure><img src="/gitbook-assets/Screenshot 2023-05-01 at 3.21.10 PM (1) (1).png" alt=""><figcaption></figcaption></figure>

The first print() outputs the value of _**myNum**_, and the second print outputs the type of the variable _**myNum**_.

Now, if you need to define a **Float** at some point\*\*,\*\* how would you do it? Remember, Swift, by default, uses **Double** for fractional values. That's where we will learn how to create a variable with a predefined type. For example, in the following code, I am creating a **Float** variable:

```swift
var myFloat:Float = 13
print(myFloat)
print(type(of: myFloat))
```

Here, I am writing 'var' to say the next one is a variable, as earlier. I give the variable a name, 'myFloat', and then I put a colon(:), **followed by the type of the variable (Float),** and finally, I assign a value, 13. This is a standard way of defining a variable in Swift. We will eventually learn about a more concrete way of declaring and defining the variables. Now the output of the code is:

<figure><img src="/gitbook-assets/Screenshot 2023-05-01 at 3.34.11 PM (3).png" alt=""><figcaption></figcaption></figure>

One thing to note is that I put the value as 13 for myFloat, which would be interpreted as an Int if I did not specifically predefine it as a **Float.** If you look at the output, 13 became 13.0, which is a fractional number.

## Video

{% embed url="https://youtu.be/TU-5-RWzJMs" %}



<!-- Merged from 1.6.-more-print-string-interpolation.md -->

# 1.6. More print, String interpolation

Swift allows you to insert values of variables into a String. String interpolation is useful for creating dynamic texts (labels, error messages, debug information, etc.) and formatting texts.

In Swift, String interpolation is done using `\(...)` notation. Let's look into an example. So far, what we have in our playground are a few variables, such as `myNum`, `myFloat`, and `multiline`. (`myNum` is a Double, `myFloat` is a Float, and `multiline` is a string.)

So let's add the following lines of code to your Playground:

```swift
var myString = 
    "My Double number is \(myNum). My Float number is \(myFloat). And, my multiline string is \(multiline)"
print(myString)
```

If you run the code, the output would be:

```
My Double number is 12.5. My Float number is 13.0. And, my multiline string is I am a multiline String.
I might look weird, but I am really very simple.
At times I could be very useful!
```

**Here, You can see that `myNum`(a Double), `myFloat` (a Float), and `multiline` (even a String) have been interpolated into `myString`.**

Now, If we change the code to the following:

```swift
var myString = """
My Double number is \(myNum).
My Float number is \(myFloat).
And, my multiline string is
\(multiline)
"""

print(myString)
```

The output becomes:

```
My Double number is 12.5.
My Float number is 13.0.
And, my multiline string is
I am a multiline String.
I might look weird, but I am really very simple.
At times I could be very useful!
```

Here we see how multiline Strings and String interpolation can be used together to format the texts.

**Question:**

* _Can you print the same output by calling the `print()` function without creating the `myString` variable?_



<!-- Merged from 1.7.-constants.md -->

# 1.7. Constants

So far, we talked about variables. Just as a refresher, you can always change the values of a variable, maintaining the **type-safety**. However, in many cases, you would not want a value to be changeable and keep it unchanged while the program runs. These are called **constants.**

To write a constant in Swift, you need to use the keyword `let`. You write, `let` `variableName` : `DataType` = `value`. (Recall Type annotations?)

For example, let's add the following line of code in our Playground:

```swift
let myConstant:Int = 14
print("My constant is \(myConstant)")
```

It will output the following:

```
My constant is 14
```

Now, let's try to set a new value `20` to `myConstant`.

```swift
myConstant = 20
```

But now you will see the following error:

<figure><img src="/gitbook-assets/Screenshot 2023-05-01 at 10.56.02 PM.png" alt=""><figcaption></figcaption></figure>

**So, `myConstant` is not changeable (not mutable).**

\*\*Please note: when you will be building iOS apps, \*\*<mark style="color:red;">**use constants as much as possible.**</mark> It is suggested that you should declare everything as constants using `let` and then selectively change them to variables when needed.



<!-- Merged from 1.8.-type-annotations-revisited.md -->

# 1.8. Type annotations (revisited)

As we have already discussed a couple of times, we can predefine the data type for a variable when you are creating it. This is called **Type annotations.**

The general format of type annotations is as follows: `let` `variableName` : `DataType` = `value`.

A few examples could be:

```swift
let myName:String = "Sakib Miazi"
var myAge:Int = 10
let iUseIPhone:Bool = false
```



<!-- Merged from 1.9.-comments.md -->

# 1.9. Comments

We often need to write texts that are not executable programming instructions, just plain text instructions or documentation of our code. These are called comments. In swift, we can write comments in two ways.

* For a single-line comment, we use `//`.
* For multiline comments, we use `/* ... */`

For example,

```swift
// This is a single-line comment before I create a variable...
var str:String = "Nothing"

/* This is a multi-line comment describing the following:
 myNum is a Double.
 myFloat is a Float.
*/
var myNum = 12.5
var myFloat:Float = 13
```



<!-- Merged from 1.10.-reference-code.md -->

# 1.10. Reference Code

{% file src="/gitbook-assets/MyPlayground.playground (1).zip" %}

---

## Guided Practice Challenges

Before moving on to the next topic, try these low-stakes practice challenges in Xcode. They will build the exact muscle memory you need:

### Challenge 1: Experimentation
**The Scenario:** You've just learned about this topic.
**The Task:** Experiment with the code snippets provided above. Can you alter the behavior by changing the parameters or combining it with concepts from previous modules?

### Challenge 2: From Scratch
**The Task:** Try implementing the core feature of this module in a completely blank Xcode project without looking at the reference code. Rely on Xcode's autocomplete and standard Apple documentation.

---

## References

1. [Apple Developer Documentation](https://developer.apple.com/documentation/)
2. [Swift Language Guide](https://docs.swift.org/swift-book/)
3. [Human Interface Guidelines](https://developer.apple.com/design/human-interface-guidelines/)

---

## Getting Help

Because this course is fully asynchronous, here's how to get unstuck:

- **Piazza** is the primary help channel. When asking a question, include: (1) what you're trying to do, (2) what you've tried, (3) the exact Xcode error message.
- **TA office hours** — check the Canvas calendar. Show up, share your screen, and get help.
- **Instructor office hours** — by appointment for deeper issues (design questions, project direction).
