# Collections


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

