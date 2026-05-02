---
title: "Clean Code & Async"
weight: 20
---

**Estimated effort:** 1-2 hours this topic
**Format:** Asynchronous online
**Prerequisites:** Previous iOS topics

{< hint info >}
**🎯 Topic Mission:** 
In this module, we will explore **Clean Code & Async** and learn how to integrate it into our iOS applications. Your mission is to understand the mechanics behind this concept and write robust Swift code.
{< /hint >}

---

## Learning Objectives

By the end of this session, you will be able to:
1. Understand the core concepts of Clean Code & Async.
2. Implement Clean Code & Async in an Xcode project.
3. Apply best practices to ensure clean and maintainable code.

---

## The Story So Far...

We have been progressively building our knowledge of iOS and Swift. In this module, we will expand our toolkit by diving into Clean Code & Async. 
Open your current Xcode project or start a new Playground to follow along with the hands-on material.

---

## Walkthrough: Exploring Clean Code & Async

> 📁 **Target Project** — Follow along by building the mini-app presented in the steps below, or integrate these concepts into your own ongoing projects.

<!-- Merged from 1.-writing-clean-code-for-asynchronous-operations.md -->

# 1. Writing clean code for Asynchronous operations

In this section, we will rewrite the code for App 11 (JSON API). We will have options for displaying, adding, deleting, and editing contacts using our same API (please refer to:[11.1.-the-json-api-for-the-contact-app.md](../11.-working-with-json/11.1.-the-json-api-for-the-contact-app.md "mention")). We took small steps in[useful-extra-11.8.-decluttering-codes-from-view-controller.md](../11.-working-with-json/useful-extra-11.8.-decluttering-codes-from-view-controller.md "mention") section to separate the API calls from the control code. This time, we will break the chain of nested asynchronous API calls with async-await blocks of code to make our code cleaner.&#x20;

## 1. Asynchronous calls

So far, what we have seen in our API calls is that, for a sequence of asynchronous tasks, we must wait for the previous task to complete before executing the next task. We wrote _**spaghetti**_ code there and made the next API call from the callback of the first API call (if the response was a 200-level code, refer to [11.5.-app11-add-a-new-contact.md](../11.-working-with-json/11.5.-app11-add-a-new-contact.md "mention") ). However, it renders our code largely unusable for future use. What if we could write the code such that we could call the async calls one after another, but the code would not execute in parallel? Wouldn't it be great to instruct the code to wait for the call to complete and then move to the next line? That way, we can keep our code cleaner and highly reusable for future use. &#x20;

Let's examine an example using pseudocode.

So far, we have dealt with sequential API calls by calling the second API from within the callback of the first API. For example, in our contacts API,  to add a new contact and display the updated list of contacts, what we are doing is:

{% code lineNumbers="true" %}
```swift
//MARK: It is a pseudocode, not Swift!!!

func addANewContact(contact:Contact){
    callAddContactAPI(){ in response //This is async callback
        if response.statusCode == 200 {
            //A ton of other code....
            callGetAllContactsAPI() // The next API call
            //A ton of remaining code....
        }
    }
}
```
{% endcode %}

In this pseudocode, when we call the callAddContactAPI() API, we must also call the callGetAllContactsAPI() API from its callback. It creates a spaghetti of code. Think about 3 or more sequential calls; How complex would that be!

If we could write it the following way, would you feel it's better?

```swift
//MARK: It is a pseudocode, not Swift!!!

func addANewContact(contact:Contact){
    await callAddContactAPI() //stop and wait until the call finishes
    await callGetAllContactsAPI() //when done it will have the updated list
}
```

See how much more readable and usable it becomes!

So, we will do the same for App 11 here.

## 2. Tasks with async await

Let's look at the following Swift code (you can run it in a Playground):

{% code lineNumbers="true" %}
```swift
import UIKit

import Foundation

// 1. An async function that waits and returns a String
func delayedGreeting() async -> String {
    try? await Task.sleep(nanoseconds: 5_000_000_000) // Suspend for 5 seconds
    return "Hello from the asynchronous world, I waited 5 seconds to print this!"
}

// 2. Start the Task in a synchronous context (e.g., main function)
func start() {
    Task { // Creates an asynchronous context
        print("Starting an asynchronous task...")
        let greeting = await delayedGreeting() // Await the result
        print(greeting)
    }
    print("Hello from synchronous world, I don't wait for the asyncs!")
}

start()
```
{% endcode %}

Let's look at what we have here:

1. On lines 6 through 9, we are writing a function that will asynchronously suspend for 5 seconds.
   1. To be able to run this asynchronous task and wait for it to complete, we need to  call this function from a special block named `Task{...}` .
2. On lines 13 to 17, we put the Task block.
   1. On line 14, we print the string, "Starting an asynchronous task..." to denote the start of the async task.
   2. On line 15, we are calling the async task, which will wait for the task to complete and fetch the greeting from the function. **`await`** notation means send this call to the background and wait in the scope of the Task block.
   3. On line 16, we print the greeting after the wait is over.
3. On line 18, outside the Task block, we print, "Hello from synchronous world, I don't wait for the asyncs!"

Now, if we run the code, you will see the following:

<figure><img src="/gitbook-assets/one (5).gif" alt=""><figcaption></figcaption></figure>

Now, if we change the code like this:

{% code lineNumbers="true" %}
```swift
import UIKit

import Foundation

// 1. An async function that waits and returns a String
func delayedGreeting() async -> String {
    try? await Task.sleep(nanoseconds: 5_000_000_000) // Suspend for 5 seconds
    return "Hello from the asynchronous world, I waited 5 seconds to print this!"
}

// 2. Start the Task in a synchronous context (e.g., main function)
func start() {
    Task { // Creates an asynchronous context
        print("Starting an asynchronous task...")
        let greeting = await delayedGreeting() // Await the result
        print(greeting)
        print("Now, I wait for the calls to complete!")
    } 
}

start()
```
{% endcode %}

We removed the print outside the Task block and put a new print statement in the block. It will ouput:

<pre><code>Starting an asynchronous task...
Hello from the asynchronous world, I waited 5 seconds to print this!
<a data-footnote-ref href="#user-content-fn-1">Now, I wait for the calls to complete!</a>
</code></pre>

So, within the **Task{...}** block, all asynchronous calls are sequenced one after another! For better clarity, run the following code in your playground:

{% code lineNumbers="true" %}
```swift
import UIKit

import Foundation

// 1. An async function that waits and returns a String
func delayedGreeting5() async -> String {
    try? await Task.sleep(nanoseconds: 5_000_000_000) // Suspend for 5 seconds
    return "Hello from the asynchrnous world, I waited 5 seconds to print this!"
}
// 2. An async function that waits and returns a String
func delayedGreeting3() async -> String {
    try? await Task.sleep(nanoseconds: 3_000_000_000) // Suspend for 5 seconds
    return "Hello from the asynchrnous world, I waited 3 seconds to print this!"
}

// 2. Start the Task in a synchronous context (e.g., main function)
func start() {
    Task { // Creates an asynchronous context
        print("Starting an asynchronous task...")
        let greeting5 = await delayedGreeting5() // Await the result
        print(greeting5)
        let greeting3 = await delayedGreeting3() // Await the result
        print(greeting3)
    }   
}
start()
```
{% endcode %}

### <mark style="color:red;">Important notes:</mark>

1. When we define an async function in Swift, we write async notation on the declaration.
2. When we call an async function, we call it using await notation.
3. **An await call can only be called from either another async function or from inside a Task{} block.**
   1. There are other ways of handling and sequencing async calls; please do your own research on them. This is the simplest way to start with async sequencing.

[^1]: The changed statement!



## Table of Contents

{{< section >}}

---

## Guided Practice Challenges

Before moving on to the next topic, try these low-stakes practice challenges in Xcode. They will build the exact muscle memory you need:

### Challenge 1: Experimentation
**The Scenario:** You've just learned about Clean Code & Async.
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

