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
