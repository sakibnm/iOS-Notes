---
title: "Useful UI Elements"
weight: 40
---




<!-- Merged from 1.-hiding-keyboard-when-tapped-outside.md -->

# 1. Hiding Keyboard when tapped outside

When you are building iOS apps, you might have noticed that if you put some texts into TextFields, the emulator/phone keyboard doesn't disappear if you tap outside the keyboard automatically, like this:

<figure><img src="/gitbook-assets/KeyboardNotHiding (1).gif" alt=""><figcaption></figcaption></figure>

Now if we want to hide the keyboard, it is very simple. Inside the ViewController of a Screen, add the following code in `viewDidLoad()` method:

```swift
override func viewDidLoad() {
    super.viewDidLoad()
    
    //MARK: recognizing the taps on the app screen, not the keyboard...
    let tapRecognizer = UITapGestureRecognizer(target: self, action: #selector(hideKeyboardOnTap))
    tapRecognizer.cancelsTouchesInView = false
    view.addGestureRecognizer(tapRecognizer)

}


//MARK: Hide Keyboard...
@objc func hideKeyboardOnTap(){
    //MARK: removing the keyboard from screen...
    view.endEditing(true)
}
```

Here, we create a gesture recognizer that recognizes that the user taps on the app screen. Then we add the recognizer to the view. Then we add the action (`@objc func hideKeyboardOnTap()`) for reacting to that gesture that would hide the keyboard. The end result is:

<figure><img src="/gitbook-assets/KeyboardHiding (1).gif" alt=""><figcaption></figcaption></figure>



A great guide with other tricks can be found here: [https://kaushalelsewhere.medium.com/how-to-dismiss-keyboard-in-a-view-controller-of-ios-3b1bfe973ad1](https://kaushalelsewhere.medium.com/how-to-dismiss-keyboard-in-a-view-controller-of-ios-3b1bfe973ad1)&#x20;



<!-- Merged from 2.-slide-up-the-view-to-accommodate-the-on-screen-keyboard.md -->

# 2. Slide Up the View to Accommodate the On-screen Keyboard

It is a little complicated, watch the video below to understand the aspects of it:

{% embed url="https://www.youtube.com/watch?v=O4tP7egAV1I" %}

Source code: [https://github.com/jrasmusson/ios-professional-course/blob/main/Password-Reset/7-Dealing-Keyboards/README.md](https://github.com/jrasmusson/ios-professional-course/blob/main/Password-Reset/7-Dealing-Keyboards/README.md)



<!-- Merged from 3.-saving-small-data-when-the-app-is-not-running-session-or-other-state-variables.md -->

# 3. Saving small data when the App is not running (session or other state variables)

We can store any data type in the local storage as long as the App is installed. It means even if the app is not running, small values can be stored in the storage, and the app can access them whenever needed, like from a database. We use `UserDefaults` for that.

We can store key-value pairs using UserDefaults. For each key, the app can store a value. The value can be of many data types, like Bool, Float, Double, Int, String, URL, etc. You can also write more complex types such as arrays, dictionaries, and Date – and even Data values.

The syntax is very simple. You need to instantiate user defaults by writing something like:

```swift
let defaults = UserDefaults.standard
```

### Writing data

You can save data by writing something like:

```swift
let valueToBeSaved = "THIS_IS_THE_API_KEY"
defaults.set(valueToBeSaved, forKey: "apiKey")
```

In the above code, we are saving `valueToBeSaved` String to the local storage with the key "apiKey." The key is important to retrieve the data.

### Reading data

You can read data by accessing something like:

```swift
let apiKeySaved = defaults.object(forKey: "apiKey") as! String?
        
if let apiKey = apiKeySaved{
    //MARK: tasks if there is a key saved
    print("The Saved API Key: \(apiKey)")
}else{
    //MARK: tasks if there is no key saved
    print("No API Key saved at the moment!")
}
```

In the above code, we access the value saved using the key "apiKey."

**Please note,**

* **You should not be saving heavy data using UserDefaults. It is a slow transaction since the data is saved in the local storage, not in the RAM on your device.**
* **You should not use UserDefaults for inter-screen communications.**

**For more details, please read Paul Hudson's explanations here:** [**https://www.hackingwithswift.com/read/12/2/reading-and-writing-basics-userdefaults**](https://www.hackingwithswift.com/read/12/2/reading-and-writing-basics-userdefaults)



<!-- Merged from 4.-stack-view.md -->

# 4. Stack View

We often face a situation where we have more than two UI elements on a single row of the screen; then, it becomes really hard to align them proportionately with spacing using layout constraints. We can use UIStackView to deal with that situations.

For example, our goal is to have something like the following:

<figure><img src="/gitbook-assets/Screenshot 2023-06-08 at 1.05.38 PM (1).png" alt=""><figcaption></figcaption></figure>

There are three buttons, and we want to align them perfectly with each other without working with custom constraints.

### Designing View with UIStackView:

Let's create a new App and name it "StackViewDemo." Create a new file called StackView.swift, and put the following code there:

{% code lineNumbers="true" %}
```swift
//
//  StackView.swift
//  StackViewDemo
//
//  Created by Sakib Miazi on 6/6/23.
//

import UIKit

class StackView: UIView {
    //MARK: UI elements...
    var button1: UIButton!
    var button2: UIButton!
    var button3: UIButton!
    var stack: UIStackView!
    
    override init(frame: CGRect) {
        super.init(frame: frame)
        
        backgroundColor = .white
        
        setupHorizontalStack()
        setupButton1()
        setupButton2()
        setupButton3()
        
        initConstraints()
    }
    
    func setupHorizontalStack(){
        stack = UIStackView()
        stack.axis = .horizontal //the stack grows horizontally...
        //stack.alignment = .center // Useful for vertical stacks. The stack will be centrally aligned
        stack.distribution = .fillProportionally //make spaces in between UI elements proportionately and automatically...
        stack.translatesAutoresizingMaskIntoConstraints = false
        self.addSubview(stack)
    }
    func setupButton1(){
        button1 = UIButton(type: .system)
        button1.setImage(.add, for: .normal)
        button1.setTitle("Button 1", for: .normal)
        //button1.translatesAutoresizingMaskIntoConstraints = false
        stack.addArrangedSubview(button1)
    }
    func setupButton2(){
        button2 = UIButton(type: .infoDark)
        button2.setImage(.checkmark, for: .normal)
        button2.setTitle("Button 1", for: .normal)
        //button2.translatesAutoresizingMaskIntoConstraints = false
        stack.addArrangedSubview(button2)
    }
    func setupButton3(){
        button3 = UIButton(type: .infoDark)
        button3.setImage(.remove, for: .normal)
        button3.setTitle("Button 1", for: .normal)
        //button3.translatesAutoresizingMaskIntoConstraints = false
        stack.addArrangedSubview(button3)
    }
    
    func initConstraints(){
        NSLayoutConstraint.activate([
            stack.topAnchor.constraint(equalTo: self.safeAreaLayoutGuide.topAnchor, constant: 16),
            stack.leadingAnchor.constraint(equalTo: self.safeAreaLayoutGuide.leadingAnchor, constant: 16),
            stack.trailingAnchor.constraint(equalTo: self.safeAreaLayoutGuide.trailingAnchor, constant: -16),
        ])
    }
    
    required init?(coder: NSCoder) {
        fatalError("init(coder:) has not been implemented")
    }
}
```
{% endcode %}

In the above code, we have three buttons and a stack to hold these three buttons.

* On lines 11 through 15, we declare the buttons and the stack.
* On lines 30 through 37, we define the stack.
  * On line 32, we define the axis of the stack. There are two possible axes: horizontal and vertical. **The horizontal stack grows horizontally from left to right. The vertical stack grows downward, from top to bottom.**
  * Line 33 is commented out but important. If the stack is vertical, you might want to align the UI elements since we will have empty spaces on both sides.
  * Line 34 talks about empty space distribution. I used `filledProportionally`. It means the row is filled with the UI elements while keeping proportional spaces between them. It dynamically adjusts the empty spaces. You do not have to write complex constraints for them.
* On lines 38 through 57, we define three buttons, just as always. **However, the most important thing here is we are not adding the buttons as the sub-view of `self` here. We are adding the buttons as the arranged sub-views of the stack.**
* On lines 60 through 66, we are defining the constraints for the screen. See how easy it is to set up the layout constraints for stacks. **We define the stack view's top, leading, and trailing anchors here.** The stack height is automatically dealt with by the UI elements we added to the stack.

### Patching ViewController

Now, let's load the view we created in the ViewController.swift file.

### Run the App

If we run the app now, we will see:

<figure><img src="/gitbook-assets/24.one (1).gif" alt=""><figcaption></figcaption></figure>

If we change the axis to vertical ( `stack.axis = .vertical` ), the screen will look like:

<figure><img src="/gitbook-assets/24.two (3).gif" alt=""><figcaption></figcaption></figure>



<!-- Merged from embed-navigation-controller-from-code-not-storyboard.md -->

# Embed Navigation Controller from code (Not Storyboard)

So far you have noticed, we embed the Navigation Controller using the Storyboard (refer to [3.1.-navigation-controller.md](../3.-our-first-multi-screen-app/3.1.-navigation-controller.md "mention") ). What about we want to remove that process and want to add Navigation Controller by writing code? That way it'll be easy to change the name of the default "ViewController.swift" file to a more appropriate name.&#x20;

To start, we will create a new iOS project in Xcode named, "NavConFromCode."&#x20;

<figure><img src="/gitbook-assets/Screenshot 2025-10-09 at 1.22.15 PM.png" alt=""><figcaption></figcaption></figure>

We already know that it comes with a default view controller: **ViewController.swift**

So let's first change the name of it to a different name: **FirstScreenViewController.swift**

<figure><img src="/gitbook-assets/sdf.gif" alt=""><figcaption></figcaption></figure>

<mark style="color:$danger;background-color:red;">**Please note, we are also changing the name of the class.**</mark>&#x20;

Then just open SceneDelegate.swift file, and update the \
`func scene(_ scene: UIScene, willConnectTo session: UISceneSession, options connectionOptions: UIScene.ConnectionOptions)` function.

{% code lineNumbers="true" %}
```swift
func scene(_ scene: UIScene, willConnectTo session: UISceneSession, options connectionOptions: UIScene.ConnectionOptions) {
            
    guard let windowScene = (scene as? UIWindowScene) else { return }
    
    // Create your root view controller
    let rootViewController = FirstScreenViewController()
    
    // Embed it in a navigation controller
    let navigationController = UINavigationController(
                    rootViewController: rootViewController
            )
    
    // Create and configure the window
    window = UIWindow(windowScene: windowScene)
    window?.rootViewController = navigationController
    window?.makeKeyAndVisible()
}
```
{% endcode %}

On line 3, we define windowScene as a variable since we want to manipulate the window on the app.

On line 6, we define our root view controller for the navigation stack. (Our first/main screen).

On line 9, we define the navigation controller to be added. And set the root view controller to the main screen.

Then on lines 14 through 16, we setup the window of the app.&#x20;

Now, if we run the app, it should run as the FirstScreenViewController being the main view controller.



### Deleting the Main.storyboard

1. Delete the storyboard file from file explorer.
2. Open project's Info.plist
   1. Select your project in the Project Navigator
   2. Select your app target
   3. Go to the "Info" tab
   4. Expand "Application Scene Manifest"
   5. Expand "Scene Configuration"
   6. Expand "Application Session Role"
   7. Expand "Item 0"
   8. Delete the row: "Storyboard Name" (value: "Main")
   9. Find "Main storyboard file base name" or "Main Interface". Delete the value (set it to empty)

### Resource Files

{% file src="/gitbook-assets/NavConFromCode.zip" %}



## Table of Contents

{{< section >}}
