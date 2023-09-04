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
