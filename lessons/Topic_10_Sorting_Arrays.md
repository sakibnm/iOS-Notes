# Sorting Arrays


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

