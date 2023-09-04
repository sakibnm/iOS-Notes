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

<figure><img src="../../.gitbook/assets/Screenshot 2023-05-04 at 5.08.56 PM (1).png" alt="" width="563"><figcaption></figcaption></figure>

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
