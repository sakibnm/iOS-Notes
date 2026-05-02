---
title: "Loops"
weight: 50
---

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

