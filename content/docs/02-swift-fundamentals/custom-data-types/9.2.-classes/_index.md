---
title: "9.2. Classes"
weight: 570
---

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

