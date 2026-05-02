---
title: "Optionals"
weight: 80
---

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

