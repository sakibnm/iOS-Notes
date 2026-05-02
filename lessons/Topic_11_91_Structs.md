# 9.1. Structs


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

