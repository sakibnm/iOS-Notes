---
title: "Sorting Arrays"
weight: 110
---

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

