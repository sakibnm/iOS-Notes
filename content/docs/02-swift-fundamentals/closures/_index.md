---
title: "Closures"
weight: 70
---

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

