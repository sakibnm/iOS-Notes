---
title: "Operators"
weight: 30
---

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

