---
title: "Functions"
weight: 60
---

# 6. Functions

Functions are the best tools for writing reusable code blocks. Whenever we write codes, we often see that we need to execute the same task in multiple places in our program. What if we could separate the code for that particular task from the main code block and call it every time we need to do it instead of writing the same code again?

So, in short, a function is a code block where we can do certain tasks. We can provide it with data and receive a result from it.




<!-- Merged from 6.1.-writing-functions.md -->

# 6.1. Writing functions

To write a function in Swift, we use the keyword `func` followed by the function's name, parameter list, return data type, and body (the code block). A general structure of a Swift function is:

```
func functionName(parameter1:DataType, parameter2:DataType, ...) -> ReturnDataType{
    //code block
}
```

### Simple functions

For a function, the list of parameters can be empty, meaning if our function does not require any data from us to run, we do not need to define any parameters. For example, a function to print "Hello World" could be:

```swift
func printHelloWorld(){
    print("Hello World!")
}
```

You can call the function from your code like:

```swift
printHelloWorld()
```



<!-- Merged from 6.2.-functions-with-parameters.md -->

# 6.2. Functions with parameters

Now, let's write a function that accepts parameters and do some tasks. The following code accepts the name and age of a person as parameters and prints the details.

```swift
//function definition...
func printDetails(name:String, age:Int){
    print(
        """
        The user's name is: \(name).
        The user's age is: \(age).
        \(name) is awesome!
        """
    )
}


//calling the function...
printDetails(name: "Donald", age: 25)
```

It prints:

```
The user's name is: Donald.
The user's age is: 25.
Donald is awesome!
```



<!-- Merged from 6.3.-functions-that-return-a-value.md -->

# 6.3. Functions that return a value

Now, let's think about a function that accepts an array of integers as a parameter and returns the sum of the integers.

```swift
func sumOf(array:[Int]) -> Int{
    var sum = 0
    for item in array{
        sum += item
    }
    
    //returns the value...
    return sum
}

//calling the function with an integer array
print(sumOf(array: [1,2,3,4,5]))
```

It prints:

```
15
```

You can get the returned value and store it to a constant or variable:

```swift
let sum = sumOf(array: [1,2,3,4,5])
```



<!-- Merged from 6.4.-more-on-function-parameters.md -->

# 6.4. More on function parameters

## Parameter labels

Swift functions have the ability to have completely separate internal and external parameter names. Instead of having a single parameter name, the function below has two. The first one, `with` is an external parameter name, which is the name that will refer to the parameter when we call the function. The second one, `vehicle` is the internal parameter name which is the name we’ll use when we need to use the parameter within the function.

```swift
//function definition...
func navigate(with vehicle:String, from source:String, to destination:String) -> String{
    return "The user will use a \(vehicle) to travel from \(source) to \(destination)."
}

//calling the function
print(navigate(with: "car", from: "Boston", to: "NYC"))
```

It prints:

```
The user will use a car to travel from Boston to NYC.
```

Let's look at the first `String` parameter the `navigate` function accepts. Here, `with` is the external name or label, and `vehicle` is the internal label for the first parameter. When we are calling the function from outside, we are using `with`, and internally we are using `vehicle`.

We can use this feature to write and call a function creatively.

## Omitting parameter labels

We can also omit the external parameter name to call our function just by passing in a value without mentioning the parameter's name. We achieve this by simply replacing the external name with the underscore. Now we can call our function without using a parameter name at all. Instead, we can pass in a value that we want to use as the input.

Remember `underscores`? We can use it to define the external name of a parameter to omit the need to type the parameter name when we call the function:

```swift
//function definition...
func printHello(_ name:String){
    print("Hello \(name)!")
}

//Calling the function...
printHello("Sakib")
```

## Default parameters

Sometimes we want to have default values for our parameters. The default value gets activated if we do not pass any value through the parameters. We can set a default value by writing a `=` after the parameter's type followed by the default value. Like this:

```swift
//function definition
func printHello2(_ name:String = "Unknown"){
    print("Hello \(name)!")
}
//calling function...
printHello2()
```

It will print:

```
Hello Unknown!
```

Because the default is already set to "Unknown."

## <mark style="color:orange;">Why and where do we use internal and external names in Swift functions?</mark>

1.  **Improved Clarity in Function Calls:**

    When a function has descriptive external parameter names, it becomes clear what each argument represents when calling it. This helps understand each argument's purpose and makes the function call more readable.
2.  **Self-Documenting Code:**

    By providing meaningful external names, you can make your code self-documenting. This means that someone reading your code can understand the purpose and intent of the function just by looking at the function signature and the way it's called.
3. **Avoiding Ambiguity:** \
   In some cases, functions may have parameters with similar data types. Using external names allows you to disambiguate these parameters, making the function call unambiguous and reducing the risk of passing incorrect arguments.
4.  **Improved Readability and Maintenance:**

    By using external names, you can create functions with expressive, almost sentence-like function calls, which can be beneficial when reading and maintaining code.

### Scenarios where internal and external names are useful

1.  **Public API Design:**

    When designing public APIs, using external names helps ensure that the function calls are clear and self-explanatory for your framework or library users. You can find examples in Apple Documentation.
2.  **Functions with Multiple Parameters:**

    Functions with multiple parameters benefit from external names as they clarify the purpose of each parameter.
3.  **Methods in Classes and Structures:**

    In object-oriented programming, methods in classes and structures should use external names to indicate the role of each parameter in the context of the object.

In summary, using internal and external names in Swift functions is a good practice for writing clean, expressive, and self-documenting code, especially when designing public APIs or functions with multiple parameters. They enhance code readability and help prevent confusion and errors when calling functions.

_These are the very basics of functions in Swift. Eventually, we will learn more about functions and their various uses._



<!-- Merged from 6.5.-reference-code.md -->

# 6.5. Reference Code

{% file src="/gitbook-assets/MyPlayground6.playground (1).zip" %}

