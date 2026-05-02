---
coverY: 0
---

# 1. Variables, Data types, and more.

This is where we begin our journey with Swift. In this book section, we will go through the simple data types in Swift and see how to work with them. Please go to the next page to start!!!




<!-- Merged from 1.1.-creating-a-swift-playground.md -->

# 1.1. Creating a Swift Playground

Open Xcode from your Launchpad. You should be seeing something like the following:

<figure><img src="/gitbook-assets/Screenshot 2023-05-01 at 11.46.52 AM (1).png" alt=""><figcaption><p>Xcode launch screen</p></figcaption></figure>

Do not create an Xcode project yet; click on _**File -> New -> Playground**_. Select _**Blank**,_ click _**Next**_, give the playground a name, and click on _Create._ If you see something like the following, you are good to go! That is the first step toward learning Swift!!!

<figure><img src="/gitbook-assets/Screenshot 2023-05-01 at 12.01.56 PM (2).png" alt=""><figcaption><p>Playground</p></figcaption></figure>

## Video

{% embed url="https://www.youtube.com/watch?v=IG9nba_A7Z4" %}
Demo
{% endembed %}



<!-- Merged from 1.2.-variables.md -->

# 1.2. Variables

We will write our "Hello World" code here. In very short, variables are the places in your code where you can store program data while the program is running. They are called variables because you can change (vary) their values.

Now the Playground you created comes with a line of code:

```swift
var greeting = "Hello, playground"
```

It creates a new variable called _greeting_, and gives it the value "Hello, playground".

<figure><img src="/gitbook-assets/Screenshot 2023-05-01 at 12.31.15 PM (1).png" alt=""><figcaption></figcaption></figure>

After you click on the play button, you'll see "Hello, playground" on the right side, which is the output area of the Playground.

Since greeting is a variable, we can always change it from the code, right? So let's change the value to something else like:

```swift
greeting = "Hello, Bonobos!!!!"
```

Now, you can see the new values showing on the output area!

<figure><img src="/gitbook-assets/Screenshot 2023-05-01 at 12.35.08 PM (1).png" alt=""><figcaption></figcaption></figure>

Since greeting is a variable, we can change the values without creating a new variable for the new value!

## Video

{% embed url="https://youtu.be/_a2NJAJg-WM" %}



<!-- Merged from 1.3.-type-safety.md -->

# 1.3. Type safety

Swift is a type-safe language. It means that once you create a variable, it is stuck with a specific data type, and you cannot change the data type of it. Every variable has to have a particular data type.

So far in our code, we have a variable _**greeting**_ having the value "Hello, Bonobos!!!". What if we try to set the value of _**greeting**_ to 12? Let's try it!

```swift
greeting = 12
```

And click on play! We will see something like the following:

<figure><img src="/gitbook-assets/Screenshot 2023-05-01 at 1.06.02 PM (1).png" alt=""><figcaption></figcaption></figure>

It says, "Cannot assign the value of type **'Int'** to **'String'**. So it means that Swift automatically sets the type of the variable _**greeting**_ to a String when it creates the variable with a String. Now that the type is already assigned, when I wanted to change the value to an integer 12, it yelled at me.

Ok, let's create another variable to hold the integer.

```swift
var count = 12
```

Here it creates a variable named count, then finds that the value I am initially setting (12) is of type **Int** (integer). So, _**count**_ can only hold **Int**s after the creation.

There is a _swift_ and usable trick for large integers. For example, if you want to store 1 million (1000000) in a variable, It is hard to read/type when you deal with a stream of consecutive zeroes together. Swift uses underscores as thousand separators. Like this:

```swift
var million = 1_000_000
```

**To sum up, you need to be very careful about the data types of variables. You must not mix up data types for a particular variable.**

## Video

{% embed url="https://youtu.be/XrHRxOiLX_o" %}



<!-- Merged from 1.4.-strings-and-print-to-console.md -->

# 1.4. Strings and print to console

Swift allows you to write strings in two ways. The first one is, of course, the age-old String we declare inside **" "**. The next one is multiline strings which you can write inside **""" """** (triple quotes on both sides).

An example of the first type is the _**greeting**_ variable we have. Let's try to see what a multi-line string is.

Let's create a string like the following:

```swift
var multiline = """
I am a multiline String.
I might look weird, but I am really very simple.
At times I could be very useful!
"""
```

After you define the String, if you look at the output area, you'll see that a character **'\n' is** added between two lines. **'\n'** denotes a new line. It means that the variable multiline contains a String that will be logically multiline and follows the exact format the user put in.

Now, you can use the command **print()** to display the output to the console. Let's put the following line of code:

```swift
print(multiline)
```

It should display the following at the bottom (console output) of Xcode:

<figure><img src="/gitbook-assets/Screenshot 2023-05-01 at 1.55.07 PM (1).png" alt=""><figcaption></figcaption></figure>

Now you get the full view of how a multiline String would get displayed.

## Video

{% embed url="https://youtu.be/FEoQh4CarpM" %}



<!-- Merged from 1.5.-floating-point-numbers-and-type-annotation.md -->

# 1.5. Floating point numbers and Type annotation

Two basic data types in Swift handle the floating point numbers (fractional values): **Double** and **Float.**

**Double** is short for "double-precision floating point number." It is a 64-bit floating point number. Long story short, it can hold very large fractional values. Swift uses **Double** as its default data type for floating point literals.

On the other hand, **Float** is a 32-bit floating point number, which is less precise than **Double,** and you do not need to use it unless you are building games or graphics applications.

So now, let's write a Double variable:

```swift
var myNum = 12.5
print(myNum)
print(type(of: myNum))
```

Here Swift automatically sets the type of the variable myNum to **Double** since I put a fractional value to it. The above code outputs the following:

<figure><img src="/gitbook-assets/Screenshot 2023-05-01 at 3.21.10 PM (1) (1).png" alt=""><figcaption></figcaption></figure>

The first print() outputs the value of _**myNum**_, and the second print outputs the type of the variable _**myNum**_.

Now, if you need to define a **Float** at some point\*\*,\*\* how would you do it? Remember, Swift, by default, uses **Double** for fractional values. That's where we will learn how to create a variable with a predefined type. For example, in the following code, I am creating a **Float** variable:

```swift
var myFloat:Float = 13
print(myFloat)
print(type(of: myFloat))
```

Here, I am writing 'var' to say the next one is a variable, as earlier. I give the variable a name, 'myFloat', and then I put a colon(:), **followed by the type of the variable (Float),** and finally, I assign a value, 13. This is a standard way of defining a variable in Swift. We will eventually learn about a more concrete way of declaring and defining the variables. Now the output of the code is:

<figure><img src="/gitbook-assets/Screenshot 2023-05-01 at 3.34.11 PM (3).png" alt=""><figcaption></figcaption></figure>

One thing to note is that I put the value as 13 for myFloat, which would be interpreted as an Int if I did not specifically predefine it as a **Float.** If you look at the output, 13 became 13.0, which is a fractional number.

## Video

{% embed url="https://youtu.be/TU-5-RWzJMs" %}



<!-- Merged from 1.6.-more-print-string-interpolation.md -->

# 1.6. More print, String interpolation

Swift allows you to insert values of variables into a String. String interpolation is useful for creating dynamic texts (labels, error messages, debug information, etc.) and formatting texts.

In Swift, String interpolation is done using `\(...)` notation. Let's look into an example. So far, what we have in our playground are a few variables, such as `myNum`, `myFloat`, and `multiline`. (`myNum` is a Double, `myFloat` is a Float, and `multiline` is a string.)

So let's add the following lines of code to your Playground:

```swift
var myString = 
    "My Double number is \(myNum). My Float number is \(myFloat). And, my multiline string is \(multiline)"
print(myString)
```

If you run the code, the output would be:

```
My Double number is 12.5. My Float number is 13.0. And, my multiline string is I am a multiline String.
I might look weird, but I am really very simple.
At times I could be very useful!
```

**Here, You can see that `myNum`(a Double), `myFloat` (a Float), and `multiline` (even a String) have been interpolated into `myString`.**

Now, If we change the code to the following:

```swift
var myString = """
My Double number is \(myNum).
My Float number is \(myFloat).
And, my multiline string is
\(multiline)
"""

print(myString)
```

The output becomes:

```
My Double number is 12.5.
My Float number is 13.0.
And, my multiline string is
I am a multiline String.
I might look weird, but I am really very simple.
At times I could be very useful!
```

Here we see how multiline Strings and String interpolation can be used together to format the texts.

**Question:**

* _Can you print the same output by calling the `print()` function without creating the `myString` variable?_



<!-- Merged from 1.7.-constants.md -->

# 1.7. Constants

So far, we talked about variables. Just as a refresher, you can always change the values of a variable, maintaining the **type-safety**. However, in many cases, you would not want a value to be changeable and keep it unchanged while the program runs. These are called **constants.**

To write a constant in Swift, you need to use the keyword `let`. You write, `let` `variableName` : `DataType` = `value`. (Recall Type annotations?)

For example, let's add the following line of code in our Playground:

```swift
let myConstant:Int = 14
print("My constant is \(myConstant)")
```

It will output the following:

```
My constant is 14
```

Now, let's try to set a new value `20` to `myConstant`.

```swift
myConstant = 20
```

But now you will see the following error:

<figure><img src="/gitbook-assets/Screenshot 2023-05-01 at 10.56.02 PM.png" alt=""><figcaption></figcaption></figure>

**So, `myConstant` is not changeable (not mutable).**

\*\*Please note: when you will be building iOS apps, \*\*<mark style="color:red;">**use constants as much as possible.**</mark> It is suggested that you should declare everything as constants using `let` and then selectively change them to variables when needed.



<!-- Merged from 1.8.-type-annotations-revisited.md -->

# 1.8. Type annotations (revisited)

As we have already discussed a couple of times, we can predefine the data type for a variable when you are creating it. This is called **Type annotations.**

The general format of type annotations is as follows: `let` `variableName` : `DataType` = `value`.

A few examples could be:

```swift
let myName:String = "Sakib Miazi"
var myAge:Int = 10
let iUseIPhone:Bool = false
```



<!-- Merged from 1.9.-comments.md -->

# 1.9. Comments

We often need to write texts that are not executable programming instructions, just plain text instructions or documentation of our code. These are called comments. In swift, we can write comments in two ways.

* For a single-line comment, we use `//`.
* For multiline comments, we use `/* ... */`

For example,

```swift
// This is a single-line comment before I create a variable...
var str:String = "Nothing"

/* This is a multi-line comment describing the following:
 myNum is a Double.
 myFloat is a Float.
*/
var myNum = 12.5
var myFloat:Float = 13
```



<!-- Merged from 1.10.-reference-code.md -->

# 1.10. Reference Code

{% file src="/gitbook-assets/MyPlayground.playground (1).zip" %}

