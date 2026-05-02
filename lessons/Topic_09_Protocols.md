# Protocols


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

