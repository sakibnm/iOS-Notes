---
title: "Closures"
weight: 70
---

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

