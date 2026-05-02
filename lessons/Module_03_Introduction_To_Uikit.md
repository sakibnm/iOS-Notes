# Module 03: Introduction To UIKit

## Table of Contents




### Creating Our First App

## Table of Contents




### Designing Without Storyboards

**Estimated effort:** 1-2 hours this topic
**Format:** Asynchronous online
**Prerequisites:** Previous iOS topics


**🎯 Topic Mission:** 
In this module, we will explore **Designing Without Storyboards** and understand its fundamental mechanics. Your mission is to understand the mechanics behind this concept and write robust Swift code.


---

## Learning Objectives

By the end of this session, you will be able to:
1. Understand the core concepts of Designing Without Storyboards.
2. Implement Designing Without Storyboards in an Xcode project.
3. Apply best practices to ensure clean and maintainable code.

---

## The Story So Far...

We have been progressively building our knowledge of iOS and Swift. In this module, we will expand our toolkit by diving into Designing Without Storyboards. 
Open your current Xcode project or start a new Playground to follow along with the hands-on material.

---

## Walkthrough: Exploring Designing Without Storyboards

> 📁 **Target Project** — Follow along by building the mini-app presented in the steps below, or integrate these concepts into your own ongoing projects.

### Designing without Storyboards

In our first app, we dragged and dropped the UI elements on Storyboard and set up the constraints using the Interface Builder's tools. Now, I said we would ditch this approach and start designing the UI with codes.

### Why don't we use storyboards?

There are several reasons for it, as this blog post discusses: [https://kissdigital.com/blog/why-we-stopped-using-storyboards](https://kissdigital.com/blog/why-we-stopped-using-storyboards). However, long story short, Storyboards automatically create the XML tags for the UI elements. Since they are machine generated, the resource IDs of the UI elements change very frequently. So, if you run your friend's code on your computer, the IDs will change. Think about you are collaborating with a friend using GitHub. It will probably be fine if you do not work concurrently in different branches. However, it will be a massive pain if you work on the same project concurrently and want to merge the updates. Using codes to generate the UIs programmatically doesn't have this issue.

**Constraints and Attributes**

Before we start, let's have a quick look at the UI we had from 'App1':

![Educational illustration for iOS concept](</gitbook-assets/Screenshot 2023-05-09 at 10.25.49 PM.png>)

Let's look into the constraints of the UI:

![Educational illustration for iOS concept](</gitbook-assets/Screenshot 2023-05-09 at 10.50.48 PM (1) (1).png>)

So the Label ("Hello World!") has two constraints:

* Centered to the x-axis (horizontal axis).
* There is a gap of 32 points between the screen's top edge and the Label's top edge.

The TextField ("Put some text") has two constraints:

* Centered to the x-axis (horizontal axis).
* There is a gap of 16 points between the Label's bottom edge and the TextField's top edge.

Similarly, the Button ("Click me!") has two constraints:

* Centered to the x-axis (horizontal axis).
* There is a gap of 16 points between TextField's bottom edge and Button's top edge.

### Understanding the constraint notations

Let's look at the following grid:

<figure><img src="/gitbook-assets/grid (2).png" alt="Educational illustration for iOS concept"><figcaption><p>The grid on a screen</p></figcaption></figure>

The above grid is similar to a mobile screen. **The origin of the grid `(0, 0)` above is the top-left point,** unlike to the regular grid we use in our regular visualizations. So, when we want to anchor the object on the screen, there are four constraints we may need to set:

* Leading constraint - how far the object is from the reference point at its left.
* Trailing constraint - how far the object is from the reference point at its right.
* Top constraint - how far the object is from the reference point above it.
* Bottom constraint - how far the object is from the reference point below it.

Please note you do not need to add all four constraints to anchor an object on the screen. For example, the UI elements of 'App1' do not have all four anchors. They all have top, leading, and trailing anchors. _Centering an element takes care of two constraints: leading and trailing together._




### Converting the storyboard to code

Let's convert the Storyboard to Swift code!

The following image is how the grid on the device screen is defined.

<figure><img src="/gitbook-assets/grid (1) (1).png" alt="Educational illustration for iOS concept"><figcaption><p>Grid of a screen</p></figcaption></figure>

<figure><img src="/gitbook-assets/Screenshot 2023-05-09 at 10.50.48 PM (2).png" alt="Educational illustration for iOS concept" width="375"><figcaption><p>App1 design</p></figcaption></figure>

In the above image, we can see how the UI elements are placed on the device's screen in our App1.

We will add the code directly to ViewController.

### Understanding the attributes

### Label attributes

If you remember, In App1, we dragged and dropped a Label from the Objects Library and changed a few things. Let's go back to the Storyboard and click on the "Hello World!" label.

<figure><img src="/gitbook-assets/Screenshot 2023-05-10 at 10.09.48 AM.png" alt="Educational illustration for iOS concept"><figcaption></figcaption></figure>

* We changed the text to "Hello World!"
* The color of the text is Blue (accent color).
* The font is the system's default font, and the size is 24.

There are many other attributes we have in a Label that we can edit.

Okay, let's programmatically create a Label. And then set the Attributes. For this purpose, we will create a new project named "App\_NoStory." We will not touch the Main storyboard here.

Open the ViewController code directly and add a variable `labelHello` of the `UILabel.`

```swift
//
//  ViewController.swift
//  App1_NoStory
//
//  Created by Sakib Miazi on 5/9/23.
//

import UIKit

class ViewController: UIViewController {
    
    //MARK: declaring the UI elements...
    var labelHello:UILabel! //"Hello World!" Label...
 
    override func viewDidLoad() {
        super.viewDidLoad()
        // Do any additional setup after loading the view.
        
    }

}
```

Then inside `viewDidLoad()` we will have to define the attributes for `labelHello`.

```swift
import UIKit

class ViewController: UIViewController {
    
    //MARK: declaring the UI elements...
    var labelHello:UILabel! //"Hello World!" Label...
 
    override func viewDidLoad() {
        super.viewDidLoad()
        // Do any additional setup after loading the view.
        
        //MARK: call methods to setup the attributes of UI elements...
        setupLabelHello()
        
    }
    
    //Defining the Label attributes...
    func setupLabelHello(){
        labelHello = UILabel()
        labelHello.text = "Hello World!"
        labelHello.font = UIFont.systemFont(ofSize: 24)
        labelHello.textColor = .systemBlue
        labelHello.textAlignment = .center
        labelHello.translatesAutoresizingMaskIntoConstraints = false
        view.addSubview(labelHello)
    }

}
```

In the above code, we defined the attributes for the label:

* `labelHello.text` is the text inside the Label.
* `labelHello.font` is the font of the Label. We created a UIFont object with the system's default font of size `24.0`. Then set the Label's font to that object.
* `labelHello.textColor` is the color of the text of the Label. We set the color to system's default Blue color. You can put a `.` and choose other options.
* `labelHello.textAlignment` is the alignment of the text. We set the alignment to center. You can put a `.` and choose other options.
* `labelHello.translatesAutoresizingMaskIntoConstraints` is set to `false` which is a default and fail-safe attribute for all the UI elements. The storyboard sets it automatically. If you write codes to edit the attributes, you have to set it to `false` manually for every UI element. This attribute says to the iOS system that you are dynamically using your own constraints to display the contents on the screen. Otherwise, the system will try to pack all the UI elements together to display them on the screen without your choices.
* `view.addSubview(labelHello)` is where you add the logical view of `labelHello` you created as a subview of the screen. Here `view` is the logical view of the screen. Since `labelHello` is a child view of `view`, we write this line of code.

### Setting the constraints

Now that we have created a logical view of `labelHello`, we have to define the constraints. We can use `NSLayoutConstraint` system class to set the constraints. `NSLayoutConstraint.activate()` takes in an array of constraints and activate them on the current view. We know that `labelHello` has two constraints:

* Centered to the x-axis (horizontal axis).
* There is a gap of 32 points between the screen's top edge and the Label's top edge.

So, we can create the array of constraints with the above constraints and activate them by writing:

```swift
NSLayoutConstraint.activate(
    [
        labelHello.topAnchor.constraint(equalTo: view.safeAreaLayoutGuide.topAnchor, constant: 32),
        labelHello.centerXAnchor.constraint(equalTo: view.safeAreaLayoutGuide.centerXAnchor)
    ]
)
```

`labelHello.topAnchor.constraint(equalTo: view.safeAreaLayoutGuide.topAnchor, constant: 32)` means:

* Set the `labelHello`'s top anchor to the top anchor of the _**safe area.** (Remember,_ [_'safe area'_](../ios-development-with-uikit/1.-creating-our-first-app/1.2.-uilabel-our-first-ui-element.md)_?)_ We wanted to have a 32 points gap, `constant` is the gap here.
* Set the `centerXAnchor` (horizontal center point) of `labelHello` to the horizontal center point of the safe area.

Now let's see the entire code:

```swift
import UIKit

class ViewController: UIViewController {
    
    //MARK: declaring the UI elements...
    var labelHello:UILabel! //"Hello World!" Label...
 
    override func viewDidLoad() {
        super.viewDidLoad()
        // Do any additional setup after loading the view.
        
        //MARK: call methods to setup the attributes of UI elements...
        setupLabelHello()
        
        //MARK: initializing the constraints...
        initConstraints()
        
    }
    
    //Defining the Label attributes...
    func setupLabelHello(){
        labelHello = UILabel()
        labelHello.text = "Hello World!"
        labelHello.font = UIFont.systemFont(ofSize: 24)
        labelHello.textColor = .systemBlue
        labelHello.textAlignment = .center
        labelHello.translatesAutoresizingMaskIntoConstraints = false
        view.addSubview(labelHello)
    }
    
    //Initializing the constraints...
    func initConstraints(){
        NSLayoutConstraint.activate(
            [
                //Constraints for labelHello....
                labelHello.topAnchor.constraint(equalTo: view.safeAreaLayoutGuide.topAnchor, constant: 32),
                labelHello.centerXAnchor.constraint(equalTo: view.safeAreaLayoutGuide.centerXAnchor)
            ]
        )
    }

}
```

So we write a separate method `initConstraints()` to activate the constraints and call it from `viewDidLoad()`. Now let's run the app:

![Educational illustration for iOS concept](</gitbook-assets/Screenshot 2023-05-10 at 11.20.58 AM (1).png>)

So, our program rendered a "Hello World!" label on screen!

Now, let's add all the constraints for the other two UI elements.

Let's see the code after we add all the constraints:

```swift
//
//  ViewController.swift
//  App1_NoStory
//
//  Created by Sakib Miazi on 5/9/23.
//

import UIKit

class ViewController: UIViewController {
    
    //MARK: declaring the UI elements...
    var labelHello:UILabel! //"Hello World!" Label...
    var textFieldUser: UITextField! //TextField...
    var buttonClickMe: UIButton! //Button...
    

    override func viewDidLoad() {
        super.viewDidLoad()
        // Do any additional setup after loading the view.
        
        //MARK: setting up UI elements...
        setupLabelHello()
        setupTextFieldUser()
        setupButtonClickMe()
        
        //MARK: initializing the constraints...
        initConstraints()
    }
    
    //Defining the Label attributes...
    func setupLabelHello(){
        labelHello = UILabel()
        labelHello.text = "Hello World!"
        labelHello.font = UIFont.systemFont(ofSize: 24)
        labelHello.textColor = .systemBlue
        labelHello.textAlignment = .center
        labelHello.translatesAutoresizingMaskIntoConstraints = false
        view.addSubview(labelHello)
    }
    
    //Defining the TextField attributes...
    func setupTextFieldUser(){
        textFieldUser = UITextField()
        textFieldUser.placeholder = "Put some text"
        textFieldUser.borderStyle = .roundedRect
        textFieldUser.translatesAutoresizingMaskIntoConstraints = false
        view.addSubview(textFieldUser)
    }
    
    //Defining the Button attributes...
    func setupButtonClickMe(){
        buttonClickMe = UIButton(type: .system) //You need to set the type when you create a Button. We use default system button...
        buttonClickMe.setTitle("Click Me!", for: .normal)
        buttonClickMe.tintColor = .systemBlue
        buttonClickMe.translatesAutoresizingMaskIntoConstraints = false
        view.addSubview(buttonClickMe)
    }
    
    //MARK: Initializing the constraints...
    func initConstraints(){
        NSLayoutConstraint.activate(
            [
                //MARK: constraints for labelHello...
                labelHello.topAnchor.constraint(equalTo: view.safeAreaLayoutGuide.topAnchor, constant: 32),
                labelHello.centerXAnchor.constraint(equalTo: view.safeAreaLayoutGuide.centerXAnchor),
                
                //MARK: constraints for textFieldUser...
                textFieldUser.topAnchor.constraint(equalTo: labelHello.bottomAnchor, constant: 16),
                textFieldUser.centerXAnchor.constraint(equalTo: view.safeAreaLayoutGuide.centerXAnchor),
                
                //MARK: constraints for buttonClickMe...
                buttonClickMe.topAnchor.constraint(equalTo: textFieldUser.bottomAnchor, constant: 16),
                buttonClickMe.centerXAnchor.constraint(equalTo: view.safeAreaLayoutGuide.centerXAnchor)
            ]
        )
    }
    
}
```

So, we call the methods to define the attributes of UI elements first, then activate the constraints.

**Hint:** _You can still use the Storyboard to check what attributes to set up. When you are designing by coding for the first time, you can go to the Storyboard, place a UI element from the Objects Library on the Storyboard, and design it as you like. Then, use the attributes you edited to setup the design programmatically in ViewController. Then, delete the object from the storyboard. The Storyboard potentially becomes your draft design pad._

### Adding button action

Remember, we added an event listener for the button tap using `buttonClickMe.addtarget()`? Where do you think we should add that target?

We can do that in the `viewDidLoad()` method since that is the logical Controller of the app:

```swift
override func viewDidLoad() {
    super.viewDidLoad()
    // Do any additional setup after loading the view.
    
    //MARK: setting up UI elements...
    setupLabelHello()
    setupTextFieldUser()
    setupButtonClickMe()
    
    //MARK: adding action...
    buttonClickMe.addTarget(self, 
        action: #selector(onButtonClickMeTapped), 
        for: .touchUpInside
    )
    
    //MARK: initializing the constraints...
    initConstraints()
}
```

And then, we use the same methods we wrote in 'App1'.

So the full code is:

```swift
//
//  ViewController.swift
//  App1_NoStory
//
//  Created by Sakib Miazi on 5/9/23.
//

import UIKit

class ViewController: UIViewController {
    
    //MARK: declaring the UI elements...
    var labelHello:UILabel! //"Hello World!" Label...
    var textFieldUser: UITextField! //TextField...
    var buttonClickMe: UIButton! //Button...
    

    override func viewDidLoad() {
        super.viewDidLoad()
        // Do any additional setup after loading the view.
        
        //MARK: setting up UI elements...
        setupLabelHello()
        setupTextFieldUser()
        setupButtonClickMe()
        
        //MARK: adding action...
        buttonClickMe.addTarget(self, 
            action: #selector(onButtonClickMeTapped), 
            for: .touchUpInside
        )
           
        //MARK: initializing the constraints...
        initConstraints()
    }
    
    //Defining the Label attributes...
    func setupLabelHello(){
        labelHello = UILabel()
        labelHello.text = "Hello World!"
        labelHello.font = UIFont.systemFont(ofSize: 24)
        labelHello.textColor = .systemBlue
        labelHello.textAlignment = .center
        labelHello.translatesAutoresizingMaskIntoConstraints = false
        view.addSubview(labelHello)
    }
    
    //Defining the TextField attributes...
    func setupTextFieldUser(){
        textFieldUser = UITextField()
        textFieldUser.placeholder = "Put some text"
        textFieldUser.borderStyle = .roundedRect
        textFieldUser.translatesAutoresizingMaskIntoConstraints = false
        view.addSubview(textFieldUser)
    }
    
    //Defining the Button attributes...
    func setupButtonClickMe(){
        buttonClickMe = UIButton(type: .system) //You need to set the type when you create a Button. We use default system button...
        buttonClickMe.setTitle("Click Me!", for: .normal)
        buttonClickMe.tintColor = .systemBlue
        buttonClickMe.translatesAutoresizingMaskIntoConstraints = false
        view.addSubview(buttonClickMe)
    }
    
    //MARK: Initializing the constraints...
    func initConstraints(){
        NSLayoutConstraint.activate(
            [
                //MARK: constraints for labelHello...
                labelHello.topAnchor.constraint(equalTo: view.safeAreaLayoutGuide.topAnchor, constant: 32),
                labelHello.centerXAnchor.constraint(equalTo: view.safeAreaLayoutGuide.centerXAnchor),
                
                //MARK: constraints for textFieldUser...
                textFieldUser.topAnchor.constraint(equalTo: labelHello.bottomAnchor, constant: 16),
                textFieldUser.centerXAnchor.constraint(equalTo: view.safeAreaLayoutGuide.centerXAnchor),
                
                //MARK: constraints for buttonClickMe...
                buttonClickMe.topAnchor.constraint(equalTo: textFieldUser.bottomAnchor, constant: 16),
                buttonClickMe.centerXAnchor.constraint(equalTo: view.safeAreaLayoutGuide.centerXAnchor)
            ]
        )
    }
    
    //MARK: buttonClickMe tap action...
    @objc func onButtonClickMeTapped(){
        //print("Button Clicked!!")
        // MARK: fetching the text the user typed...
        let text = textFieldUser.text
        
        //Unwrapping the optional text...
        if let unwrappedText = text{
            //print(unwrappedText)
            
            if(unwrappedText.isEmpty){ //The user didn't put anything...
                showErrorAlert()
            } else{ //The user put some texts...
                showAlertText(text: unwrappedText)
            }
        }
    }
    
    //MARK: Alert controller logics...
    func showErrorAlert(){
        let alert = UIAlertController(title: "Error!", message: "Text Field must not be empty!", preferredStyle: .alert)
        
        alert.addAction(UIAlertAction(title: "OK", style: .default))
        
        self.present(alert, animated: true)
    }
    
    func showAlertText(text:String){
        let alert = UIAlertController(title: "You said:", message: "\(text)", preferredStyle: .alert)
        
        alert.addAction(UIAlertAction(title: "OK", style: .default))
        
        self.present(alert, animated: true)
    }
    
}
```

If you run the app, you can see that we replicated the whole App1 by just writing codes. You should start practicing this early since almost everyone in the industry got rid of Storyboards.



### Reference Code

[Download Project Archive](/gitbook-assets/App1_NoStory.zip)

---

## Guided Practice Challenges

Before moving on to the next topic, try these low-stakes practice challenges in Xcode. They will build the exact muscle memory you need:

### Challenge 1: Experimentation
**The Scenario:** You've just learned about Designing Without Storyboards.
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


### Multi-Screen Apps

**Estimated effort:** 1-2 hours this topic
**Format:** Asynchronous online
**Prerequisites:** Previous iOS topics


**🎯 Topic Mission:** 
In this module, we will explore **Multi-Screen Apps** and understand its fundamental mechanics. Your mission is to understand the mechanics behind this concept and write robust Swift code.


---

## Learning Objectives

By the end of this session, you will be able to:
1. Understand the core concepts of Multi-Screen Apps.
2. Implement Multi-Screen Apps in an Xcode project.
3. Apply best practices to ensure clean and maintainable code.

---

## The Story So Far...

We have been progressively building our knowledge of iOS and Swift. In this module, we will expand our toolkit by diving into Multi-Screen Apps. 
Open your current Xcode project or start a new Playground to follow along with the hands-on material.

---

## Walkthrough: Exploring Multi-Screen Apps

> 📁 **Target Project** — Follow along by building the mini-app presented in the steps below, or integrate these concepts into your own ongoing projects.

### Our first Multi-screen App

At this point, we will make a multi-screen application. After the end of lesson 3, we will understand the basics of Navigation Controller, UIImageViews, and Image Assets.

Let's create a new project named 'App3.'

I will be designing the interface without the Storyboard here.




### Navigation Controller

If you are an iPhone or iPad user, you must have used apps with multiple screens, where you go from one screen to another and return to the previous screen with a back button on the top left corner.

For example, the Settings app's navigation looks like this:

<figure><img src="/gitbook-assets/one_ (1).gif" alt="Educational illustration for iOS concept"><figcaption></figcaption></figure>

This is called the Navigation of the app, where you define how the screen transitions are managed in an app.

### Understanding the data Structure behind NavigationController

Navigation Controller is a Stack data structure. The user sees the screen from the top of the Stack. If we want to navigate from one screen to another screen, the user can call the `push()` method of the Navigation Controller to push Screen 2 on top of Screen 1. Since the user sees the Stack from above the Stack, the user will see Screen 2 now. Whenever the user is done dealing with screen 2, and they want to get back to screen 1, they have to basically use the Navigation Controller to `pop()` Screen 2 from the Stack. Then Screen 1 will be at the top of the Stack again

<div style="position: relative; padding-bottom: 56.25%; height: 0; overflow: hidden; margin-bottom: 1.5rem; border-radius: 8px; border: 1px solid var(--rule);">
  <iframe src="https://www.youtube.com/embed/JozvVb4QyvE" style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;" frameborder="0" allowfullscreen></iframe>
</div>
Navigation Controller Stack


In our case, the ViewController is Screen 1, and ShowViewController is Screen 2. We need to push ShowViewController on top of ViewController.

### Embedding the Navigation Controller

So let's create our new project, 'App3.' _**We will not entirely discard our Storyboard here. We will use it to attach the NavigationController to our app.**_ So, open the Main storyboard in your project, Select the ViewController (the preview screen), click on the Embed In button at the bottom right corner of the middle pane, and select 'Navigation Controller.'

<figure><img src="/gitbook-assets/two_ (1).gif" alt="Educational illustration for iOS concept"><figcaption></figcaption></figure>

Once you embed the ViewController into the NavigationController, our tasks with Storyboard are done.

### Adding UI elements on the ViewController

Let's add UI elements to our View Controller (ViewController.swift). Let's programmatically add two UI elements to the 'ViewController': a UITextField and a UIButton (often called as just 'TextField' and 'Button'). Our next goal is to build another screen, ShowViewController. Our app will do the following:

* The user puts a text in the TextField in the first ViewController and clicks on the Button.
* On clicking the Button, the screen switches from the ViewController to another screen, ShowViewController (which we will create momentarily), and displays the text the user put before.

Let's add the TextField and the Button programmatically. First, we initialize the UI elements and set proper attributes, like the following:


```swift
//
//  ViewController.swift
//  App3
//

class ViewController: UIViewController {

    var textFieldMessage: UITextField!
    var buttonSend: UIButton!
    
    override func viewDidLoad() {
        super.viewDidLoad()
        // Do any additional setup after loading the view.
        
        //MARK: initializing the UI elements...
        setupTextFieldMessage()
        setupButtonSend()
        
        //MARK: initializing the constraints...
        initConstraints()
    }
    
    func setupTextFieldMessage(){
        textFieldMessage = UITextField()
        textFieldMessage.placeholder = "Put your message here"
        textFieldMessage.borderStyle = .roundedRect
        textFieldMessage.translatesAutoresizingMaskIntoConstraints = false
        view.addSubview(textFieldMessage)
    }
    
    func setupButtonSend(){
        buttonSend = UIButton(type: .system)
        buttonSend.setTitle("Send", for: .normal)
        buttonSend.translatesAutoresizingMaskIntoConstraints = false
        view.addSubview(buttonSend)
    }
}
```


Then initialize the constraints:


```swift
func initConstraints(){
    
    NSLayoutConstraint.activate([
        // textFieldMessage constraints...
        textFieldMessage.centerXAnchor.constraint(equalTo: view.safeAreaLayoutGuide.centerXAnchor),
        textFieldMessage.topAnchor.constraint(equalTo: view.safeAreaLayoutGuide.topAnchor, constant: 32),
        // buttonSend constraints...
        buttonSend.centerXAnchor.constraint(equalTo: view.safeAreaLayoutGuide.centerXAnchor),
        buttonSend.topAnchor.constraint(equalTo: textFieldMessage.bottomAnchor, constant: 16),
        
    ])
    
}
```


Now let's run the app:

<figure><img src="/gitbook-assets/three (2) (1).gif" alt="Educational illustration for iOS concept"><figcaption></figcaption></figure>

### Creating ShowViewController and adding UI elements

Now, let's create the second View Controller, 'ShowViewController.'

* Click on **File -> New -> File.**
* Select Cocoa Touch Class, and click **Next.**
* Put ShowViewController as the Class name.
* Select UIViewController at Sublass of (it should be already selected).
* Language should be Swift.
* Click **Next.**
* Finally, click on **Create.**

<figure><img src="/gitbook-assets/four (3) (1).gif" alt="Educational illustration for iOS concept"><figcaption></figcaption></figure>

It should create a new ShowViewController swift file, where we will design our second screen.

Now let's add a Label in ShowViewController to display the message the user sent from the first screen (ViewController).

```swift
//
//  ShowViewController.swift
//  App3
//

import UIKit

class ShowViewController: UIViewController {
    var messageFromFirstScreen:String? = "No message received!" //First screen can set this variable...
    var labelMessage: UILabel!
    
    override func viewDidLoad() {
        super.viewDidLoad()
        
        setupLabelMessage()
        
        initConstraints()
    }
    

    func setupLabelMessage(){
        labelMessage = UILabel()
        labelMessage.textColor = .systemBlue
        labelMessage.text = messageFromFirstScreen
        labelMessage.translatesAutoresizingMaskIntoConstraints = false
        view.addSubview(labelMessage)
    }
    
    func initConstraints(){
        NSLayoutConstraint.activate([
            labelMessage.centerXAnchor.constraint(equalTo: view.safeAreaLayoutGuide.centerXAnchor),
            labelMessage.topAnchor.constraint(equalTo: view.safeAreaLayoutGuide.topAnchor, constant: 32)
        ])
    }

}
```

_In the above code, I also added a variable called `messageFromFirstScreen` to receive the message from the first screen. We set the variable's default value to "No message received!". This text will be displayed on the second screen if a user does not put anything on the first screen._

Now, it's time to patch the ShowViewController with the NavigationController.

### Pushing ShowViewController on the Button tap

So let's add an event action for `buttonSend` to push ShowViewController on the Stack. Open ViewController.swift file. Put the following code to `viewDidLoad()` method.&#x20;

```swift
//
//  ViewController.swift
//  App3
//    
override func viewDidLoad() {
    super.viewDidLoad()
    // Do any additional setup after loading the view.
    
    //MARK: initializing the UI elements...
    setupTextFieldMessage()
    setupButtonSend()
    
    //MARK: initializing the constraints...
    initConstraints()
    
    //MARK: on buttonSend tap...
    buttonSend.addTarget(self, action: #selector(onButtonSendTapped), 
                        for: .touchUpInside)
}
```

Then we define the `onButtonSendTapped()` method to delegate button tap events:

```swift
@objc func onButtonSendTapped(){
    //initializing a new screen with ShowViewController...
    var showViewController = ShowViewController()
    //push the screen to Stack...
    navigationController?.pushViewController(showViewController, animated: true)
}
```

In the above code, we create a new instance of ShowViewController, then push it to the navigation stack. Now, let's run the app:

<figure><img src="/gitbook-assets/six (1) (1).gif" alt="Educational illustration for iOS concept"><figcaption></figcaption></figure>

Now, there is a problem here. We can see that tapping the Send button opens the ShowViewController, but the background is black. Well, by default, iOS gives a ViewController a transparent background. The system has no background; the transparent background makes it look black. Now we can set the background color to white by writing `view.backgroundColor = .white` inside the `viewDidLoad()` method in **ShowViewController.swift** file.

```swift
//
//  ShowViewController.swift
//  App3
//
//  Created by Sakib Miazi on 5/10/23.
//
override func viewDidLoad() {
    super.viewDidLoad()
    //setting the view background to white...
    view.backgroundColor = .white
    
    setupLabelMessage()
    
    initConstraints()
}
```

Now let's run the app:

<figure><img src="/gitbook-assets/seven (1) (1).gif" alt="Educational illustration for iOS concept"><figcaption></figcaption></figure>

We can see that there is a Back button on the left top of the ShowViewController screen. When we tap on Back, the navigation controller automatically calls the `pop()` method, and pops ShowViewController.



### Send data from Screen 1 (ViewController) to Screen2 (ShowViewController)

Now it's time to send data from our first screen (ViewController) to the second screen (ShowViewController). Remember, we created a variable named `messageFromFirstScreen`? We have to access that variable from the first screen (ViewController) and set the text the user puts in `textFieldMessage` to `messageFromFirstScreen`.

Let's get back to ViewController.swift. Scroll down to the button event action method `onButtonSendTapped()`. And add the following code in `onButtonSendTapped()` after we initialize the ShowViewController:


```swift
//
//  ViewController.swift
//  App3
//
//  Created by Sakib Miazi on 5/10/23.
//
// MARK: On button tapped...
    @objc func onButtonSendTapped(){
        //initializing a new screen with ShowViewController...
        var showViewController = ShowViewController()
        
        //set the message to ShowViewController's messageFromFirstScreen variable...
        if let unwrappedMessage = textFieldMessage.text{
            if !unwrappedMessage.isEmpty{ // checking if the user has put any message...
                //Sending data...
                showViewController.messageFromFirstScreen = unwrappedMessage
                
                //push the screen to Stack...
                navigationController?.pushViewController(showViewController, animated: true)
            }else{
                //Alert the user to put message....
            }
            
        }
    }
```


Now let's run the code:

<figure><img src="/gitbook-assets/eight (1).gif" alt="Educational illustration for iOS concept"><figcaption></figcaption></figure>

So, we can see that we can send data from one screen to the next.



### Reference Code

[Download Project Archive](/gitbook-assets/App3 (1).zip)



## Table of Contents



---

## Guided Practice Challenges

Before moving on to the next topic, try these low-stakes practice challenges in Xcode. They will build the exact muscle memory you need:

### Challenge 1: Experimentation
**The Scenario:** You've just learned about Multi-Screen Apps.
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


### MVC Architecture

**Estimated effort:** 1-2 hours this topic
**Format:** Asynchronous online
**Prerequisites:** Previous iOS topics


**🎯 Topic Mission:** 
In this module, we will explore **MVC Architecture** and understand its fundamental mechanics. Your mission is to understand the mechanics behind this concept and write robust Swift code.


---

## Learning Objectives

By the end of this session, you will be able to:
1. Understand the core concepts of MVC Architecture.
2. Implement MVC Architecture in an Xcode project.
3. Apply best practices to ensure clean and maintainable code.

---

## The Story So Far...

We have been progressively building our knowledge of iOS and Swift. In this module, we will expand our toolkit by diving into MVC Architecture. 
Open your current Xcode project or start a new Playground to follow along with the hands-on material.

---

## Walkthrough: Exploring MVC Architecture

> 📁 **Target Project** — Follow along by building the mini-app presented in the steps below, or integrate these concepts into your own ongoing projects.

### Separating the View from the Controller code

A best practice in software design is to separate the Views (front-end codes) from the Controllers (back-end codes). That way, we can make ViewControllers less cluttered.

We have been keeping all the codes for a screen on a single file (ViewController.swift). We can easily separate the View codes from the ViewController. After we separate the Views, we willwillwillwillwillwillwillwill only have Control and Data access codes in ViewController.&#x20;

To be able to do that, we will create our App4. We will build something like the following:

<figure><img src="/gitbook-assets/Screenshot 2023-05-16 at 11.05.16 AM.png" alt="Educational illustration for iOS concept"><figcaption></figcaption></figure>

On our first screen, we will have a Label to display "App4." Then we will have a TextField to get a text from the user. Next, we will have another Label to say, "How are you feeling today?" And then, we will show a PickerView to select a mood from "Happy," "Meh," and "Sad." Finally, we will have a Button, Submit. If the user taps the Submit Button, it should take them to the second screen. The second screen displays the message and the mood of the user.&#x20;




### Creating a separate View code file

Now let's create a separate file, 'FirstScreenView.swift' in the project.&#x20;

* Click **File -> New -> File...**&#x20;
* Select **Cocoa Touch Class** and press **Next**
* The class name should be **FirstScreenView.**&#x20;
* Select **UIView** as for 'Subclass of.' And press **Next**.
* Press **Create.**

<figure><img src="/gitbook-assets/one (3).gif" alt="Educational illustration for iOS concept"><figcaption></figcaption></figure>

### Setting up the View

FirstScreenView will be our View (front end) code file. We will declare the UI elements in the file like the following:

```swift
class FirstScreenView: UIView {

    var labelAppName: UILabel!
    var textFieldMessage: UITextField!
    var labelMood: UILabel!
    var pickerMood: UIPickerView!
    var buttonSubmit: UIButton!
    
}
```

Now, we will override the `init()` method to initialize the View. So let's write:

```swift
class FirstScreenView: UIView {

    var labelAppName: UILabel!
    var textFieldMessage: UITextField!
    var labelMood: UILabel!
    var pickerMood: UIPickerView!
    var buttonSubmit: UIButton!
    
    override init(frame: CGRect) {
        super.init(frame: frame)
    }    

}
```

In the above code, we initialize the FirstScreenView with a rectangular frame. The frame comes from the view where we will patch this screen later.&#x20;

Now, Xcode will yell at you saying, 'required' initializer 'init(coder:)' must be provided by the subclass of 'UIView'. UIView adopts the [NSCoder](https://developer.apple.com/documentation/foundation/nscoder) protocol, so we must override the `init()` method with the coder parameter. Do not worry about it; just click on the red sign and click fix. That should automatically do the stuff for you. And you can keep the generated method untouched.

<figure><img src="/gitbook-assets/two (1).gif" alt="Educational illustration for iOS concept"><figcaption></figcaption></figure>

Let's start building the View now. We trivially add the following initializing methods like how we did before:&#x20;


```swift
//
//  FirstScreenView.swift
//  App4
//

import UIKit

class FirstScreenView: UIView {

    var labelAppName: UILabel!
    var textFieldMessage: UITextField!
    var labelMood: UILabel!
    var pickerMood: UIPickerView!
    var buttonSubmit: UIButton!
    
    override init(frame: CGRect) {
        super.init(frame: frame)
        
        //MARK: set the background color...
        self.backgroundColor = .white
        
        //MARK: initializing the UI elements and constraints...
        
        setupLabelAppName()
        setupTextFieldMessage()
        setupLabelMood()
        setupPickerMood()
        setupButtonSubmit()
        
    }
    
    //MARK: initializing the UI elements...
    func setupLabelAppName(){
        labelAppName = UILabel()
        labelAppName.text = "App4"
        labelAppName.translatesAutoresizingMaskIntoConstraints = false
        self.addSubview(labelAppName)
    }
    func setupTextFieldMessage(){
        textFieldMessage = UITextField()
        textFieldMessage.placeholder = "Put some text..."
        textFieldMessage.translatesAutoresizingMaskIntoConstraints = false
        self.addSubview(textFieldMessage)
    }
    func setupLabelMood(){
        labelMood = UILabel()
        labelMood.text = "How are you feeling today?"
        labelMood.translatesAutoresizingMaskIntoConstraints = false
        self.addSubview(labelMood)
    }
    func setupPickerMood(){
        pickerMood = UIPickerView()
        pickerMood.isUserInteractionEnabled = true
        pickerMood.translatesAutoresizingMaskIntoConstraints = false
        self.addSubview(pickerMood)
    }
    func setupButtonSubmit(){
        buttonSubmit = UIButton(type: .system)
        buttonSubmit.setTitle("Submit", for: .normal)
        buttonSubmit.translatesAutoresizingMaskIntoConstraints = false
        self.addSubview(buttonSubmit)
    }
    
    required init?(coder: NSCoder) {
        fatalError("init(coder:) has not been implemented")
    }
    
}

```


In the above code, notice that I am setting the 'backgroundColor' to white because it would, by default, populate a black screen without the background color. The `init(frame: CGRect)` method is used as the initializer of the instance of the FirstScreenView. If you look carefully at the setup methods, we are not saying `view.addSubView()` like before. This class is already a UIView, so we use `self.addSubView()` method.&#x20;

Now let's initialize the constraints:


```swift
class FirstScreenView: UIView {
    //codes omitted...    
    override init(frame: CGRect) {
        super.init(frame: frame)
        
        //MARK: set the background color...
        self.backgroundColor = .white
        
        //MARK: initializing the UI elements and constraints...
        
        //codes omitted...
        
        initConstraints()
    }
    
    //codes omitted...
    
    //MARK: initializing constraints...
    func initConstraints(){
        NSLayoutConstraint.activate([
            labelAppName.topAnchor.constraint(equalTo: self.safeAreaLayoutGuide.topAnchor, constant: 32),
            labelAppName.centerXAnchor.constraint(equalTo: self.safeAreaLayoutGuide.centerXAnchor),
            
            textFieldMessage.topAnchor.constraint(equalTo: labelAppName.bottomAnchor, constant: 16),
            textFieldMessage.centerXAnchor.constraint(equalTo: self.safeAreaLayoutGuide.centerXAnchor),
            
            labelMood.topAnchor.constraint(equalTo: textFieldMessage.bottomAnchor, constant: 16),
            labelMood.centerXAnchor.constraint(equalTo: self.safeAreaLayoutGuide.centerXAnchor),
            
            pickerMood.topAnchor.constraint(equalTo: labelMood.bottomAnchor, constant: 16),
            pickerMood.centerXAnchor.constraint(equalTo: self.safeAreaLayoutGuide.centerXAnchor),
            
            buttonSubmit.topAnchor.constraint(equalTo: pickerMood.bottomAnchor, constant: 16),
            buttonSubmit.centerXAnchor.constraint(equalTo: self.safeAreaLayoutGuide.centerXAnchor),
        ])
    }
    
    //codes omitted...
    
}

```


**Notice that here to set up the constraints, I am using****&#x20;****`self`****&#x20;****instead of****&#x20;****`view`****&#x20;****for the same reason, this FirstScreenView is a UIView itself. I am adding children of the****&#x20;****`self`****&#x20;****view.**



### Patching the View class with the ViewController

Now that we are done with the FirstScreenView file, we have to initialize the view in the ViewController. So open the ViewController.swift file. Let's create an instance of the FirstScreenView:

```swift
//
//  ViewController.swift
//  App4
//

import UIKit

class ViewController: UIViewController {
    
    //MARK: initializing the First Screen View...
    let firstScreen = FirstScreenView()

    override func viewDidLoad() {
        super.viewDidLoad()
        // Do any additional setup after loading the view.
    }
}
```

So, `firstScreen` is the instance of the View, FIrstScreenView. Now the view of the ViewController should be `firstScreen`, right? So, we need to define it when the view is loading (not when the view did load). So we can write the following:

```swift
//
//  ViewController.swift
//  App4
//

import UIKit

class ViewController: UIViewController {
    
    //MARK: initializing the First Screen View...
    let firstScreen = FirstScreenView()

    //MARK: add the view to this controller while the view is loading...
    override func loadView() {
        view = firstScreen
    }

    override func viewDidLoad() {
        super.viewDidLoad()
        // Do any additional setup after loading the view.
    }


}
```

Here we override the `loadView()` method so that we can patch the view with the controller while the view is loading.&#x20;

Now, let's run the app:&#x20;

<figure><img src="/gitbook-assets/five (1).gif" alt="Educational illustration for iOS concept"><figcaption></figcaption></figure>

### Adding the PickerView logic

Let's define the moods like the app, App3, which we built previously.

```swift
class ViewController: UIViewController {
    
    //codes omitted...
    
    //moods for firstScreen.pickerMood...
    let moods: [String] = ["Happy", "Meh", "Sad"]
    
    var selectedMood = "Happy"
    
    //codes omitted...
}
```

Now let's adopt the protocols UIPickerViewDelegate and UIPickerViewDataSource.

```swift
class ViewController: UIViewController {
    
    //codes omitted...

}

//MARK: implementing mood PickerView...
extension ViewController: UIPickerViewDelegate, UIPickerViewDataSource{
    //returns the number of columns/components in the Picker View...
    func numberOfComponents(in pickerView: UIPickerView) -> Int {
        return 1
    }
    
    //returns the number of rows in the current component...
    func pickerView(_ pickerView: UIPickerView, numberOfRowsInComponent component: Int) -> Int {
        return moods.count
    }
    
    //set the title of currently picked row...
    func pickerView(_ pickerView: UIPickerView, titleForRow row: Int, forComponent component: Int) -> String? {
        // on change selection, update selectedMood...
        selectedMood = moods[row]
        return moods[row]
    }
}
```

Now, it's time to patch the PickerView's (`pickerMood`) delegate and data source to the ViewController. Let's add the following to `viewDidLoad()` method:

```swift
class ViewController: UIViewController {
    
    //codes omitted...

    override func viewDidLoad() {
        super.viewDidLoad()
        
        //MARK: adding the PickerView delegate and data source...
        firstScreen.pickerMood.delegate = self
        firstScreen.pickerMood.dataSource = self
        
    }

}
//codes omitted...
```

**Notice that I am calling `pickerMood` by writing `firstScreen.pickerMood`** since the instance of the View where the PickerView resides is `firstScreen`.

The whole code so far is as follows:


```swift
//
//  ViewController.swift
//  App4
//

import UIKit

class ViewController: UIViewController {
    
    //MARK: initializing the First Screen View...
    let firstScreen = FirstScreenView()
    
    //moods for firstScreen.pickerMood...
    let moods: [String] = ["Happy", "Meh", "Sad"]
    
    var selectedMood = "Happy"
    
    //MARK: add the view to this controller while the view is loading...
    override func loadView() {
        view = firstScreen
    }

    override func viewDidLoad() {
        super.viewDidLoad()
        
        //MARK: adding the PickerView delegate and data source...
        firstScreen.pickerMood.delegate = self
        firstScreen.pickerMood.dataSource = self
        
    }

}

//MARK: implementing mood PickerView...
extension ViewController: UIPickerViewDelegate, UIPickerViewDataSource{
    //returns the number of columns/components in the Picker View...
    func numberOfComponents(in pickerView: UIPickerView) -> Int {
        return 1
    }
    
    //returns the number of rows in the current component...
    func pickerView(_ pickerView: UIPickerView, numberOfRowsInComponent component: Int) -> Int {
        return moods.count
    }
    
    //set the title of currently picked row...
    func pickerView(_ pickerView: UIPickerView, titleForRow row: Int, forComponent component: Int) -> String? {
        // on change selection, update selectedMood...
        selectedMood = moods[row]
        return moods[row]
    }
}

```


Now, let's run it.&#x20;

<figure><img src="/gitbook-assets/three (2).gif" alt="Educational illustration for iOS concept"><figcaption></figcaption></figure>

See, we patched the PickerView with data!



### Creating the Display Screen

Now, we need to create another screen to display the data the user sends from the first screen. We need to create two swift files here, one is for the view (DisplayView), and another is for the view controller (DisplayViewController).&#x20;

### DisplayView.swift

We have two Labels in the view:

* The first Label displays the message.
* The second Label displays the mood.

So create the 'DisplayView' file like before and add the codes as follows:


```swift
//
//  DisplayView.swift
//  App4
//
import UIKit

class DisplayView: UIView {

    var labelMessage: UILabel!
    var labelMood: UILabel!
    
    //MARK: View initializer...
    override init(frame: CGRect) {
        super.init(frame: frame)
        
        //setting the background color...
        self.backgroundColor = .white
        
        setupLabelMessage()
        setupLabelMood()
        
        initConstraints()
    }
    
    //MARK: initializing the UI elements...
    func setupLabelMessage(){
        labelMessage = UILabel()
        labelMessage.textAlignment = .left
        labelMessage.translatesAutoresizingMaskIntoConstraints = false
        self.addSubview(labelMessage)
    }
    func setupLabelMood(){
        labelMood = UILabel()
        labelMood.textAlignment = .left
        labelMood.translatesAutoresizingMaskIntoConstraints = false
        self.addSubview(labelMood)
    }
    
    //MARK: initializing the constraints...
    func initConstraints(){
        NSLayoutConstraint.activate([
            labelMessage.topAnchor.constraint(equalTo: self.safeAreaLayoutGuide.topAnchor, constant: 32),
            labelMessage.leadingAnchor.constraint(equalTo: self.safeAreaLayoutGuide.leadingAnchor, constant: 16),
            
            labelMood.topAnchor.constraint(equalTo: labelMessage.bottomAnchor, constant: 16),
            labelMood.leadingAnchor.constraint(equalTo: self.safeAreaLayoutGuide.leadingAnchor, constant: 16),
        ])
    }
    
    required init?(coder: NSCoder) {
        fatalError("init(coder:) has not been implemented")
    }
    
}

```


### Adding DisplayViewController

Now, let's add the view controller for the display screen to our project:

Now let's create a separate file, 'DisplayViewController.swift' in the project.&#x20;

* Click **File -> New -> File...**&#x20;
* Select **Cocoa Touch Class** and press **Next**
* The class name should be **DisplayViewController.**&#x20;
* Select **UIViewController** as for 'Subclass of.' And press **Next**.
* Press **Create.**

Now, we initialize DisplayView and patch the view to the controller:

```swift
//
//  DisplayViewController.swift
//  App4
//

import UIKit

class DisplayViewController: UIViewController {

    //MARK: creating instance of DisplayView...
    let displayScreen = DisplayView()
    
    //MARK: patch the view of the controller to the DisplayView...
    override func loadView() {
        view = displayScreen
    }
    
    override func viewDidLoad() {
        super.viewDidLoad()
       
    }

}

```



### Navigation Controller and sending data from screen 1 to screen 2

We will now use the navigation controller to switch between screens and send data from the first screen to the second screen.&#x20;

Embed the ViewController (controller of the first screen) to the Navigation Controller on Storyboard. &#x20;

Now, we need to send the data (message and mood) from the first screen (ViewController) to the second screen (DisplayViewController). We will create a public struct to create this package.&#x20;

### Adding a struct

So, open the ViewController.swift file, and add the struct there:

```swift
class ViewController: UIViewController {
    
    //codes omitted...
    
    //MARK: struct to create a package to send to the Display Screen...
    public struct Package {
        var message:String?
        var mood:String?
        
        init(message: String? = nil, mood: String? = nil) {
            self.message = message
            self.mood = mood
        }
    }
    //codes omitted...
}
//codes omitted...
```

Notice that I am writing `public` before declaring the struct `Package`. We are working with access control of Swift here. If we do not write `public`, `Package` cannot be accessed from outside the `ViewController` class. The keyword `public` means this struct `Package` will also be available to other classes outside this class. For more details about access control in Swift, read: [https://docs.swift.org/swift-book/documentation/the-swift-programming-language/accesscontrol/](https://docs.swift.org/swift-book/documentation/the-swift-programming-language/accesscontrol/).&#x20;

### Handling the Button Tap action

### **Sending Data**

Now that our struct is ready, we will create a data package of two strings (message and mood). And then, when the user taps on the Submit button, we should navigate to DisplayViewController and send this package there. So let's add an action to the button:


```swift
//  ViewController.swift
//  App4
//

class ViewController: UIViewController {
    //MARK: initializing the First Screen View...
    let firstScreen = FirstScreenView()

    //codes omitted...
    override func viewDidLoad() {
        super.viewDidLoad()
        //codes omitted...
        
        //MARK: adding action for firstScreen.
        firstScreen.buttonSubmit.addTarget(self, action: #selector(onButtonSubmitTapped), for: .touchUpInside)
        
    }
    
    
    //MARK: submit button tapped action...
    @objc func onButtonSubmitTapped(){
        let message = firstScreen.textFieldMessage.text
        if let unwrappedMessage = message{
            //if the message is not empty...
            if !unwrappedMessage.isEmpty{
                // creating a package to send to Display...
                let package = Package(message: unwrappedMessage, mood: selectedMood)
                
                //instantiating displayViewController...
                let displayViewController = DisplayViewController()
                
                //setting the to be sent package...
                displayViewController.receivedPackage = package
                
                //pushing displayController to navigation controller...
                navigationController?.pushViewController(displayViewController, animated: true)
            }else{
                //do your thing!
            }
        }
    }
}
//codes omitted...
```


In the above code, we add an action for `buttonSubmit` to handle if the user taps on it.&#x20;

> **Please note:** **`buttonSubmit`****&#x20;****is not a part of the ViewController, rather it's a part of the view (****`firstScreen`****). That is why we are adding the action to the button by calling****&#x20;****`firstScreen.buttonSubmit`****. We will always add actions for the buttons inside the ViewController, not the view. A view (FirstScreenView) class is just for setting up the front-end. You should not write back-end methods or actions there.**&#x20;

If the user puts in a message and selects their mood, the code will create a variable `package` of struct `Package` with the message and the mood. Then the code instantiates the DisplayViewController (`displayViewController`) and sets `package` as the value of the `receivedPackage` variable of `displayViewController`. Then, as usual, we push `displayViewController` to the navigation controller.

### **Receiving data at DisplayViewController**

We need to prepare the DisplayViewController to receive the package. So let's update DisplayViewController.swift as follows:


```swift
//
//  DisplayViewController.swift
//  App4
//
//  Created by Sakib Miazi on 5/16/23.
//

import UIKit

class DisplayViewController: UIViewController {

    //MARK: creating instance of DisplayView...
    let displayScreen = DisplayView()
    
    //MARK: patch the view of the controller to the DisplayView...
    override func loadView() {
        view = displayScreen
    }
    
    //MARK: message and mood from the first screen...
    var receivedPackage: ViewController.Package = ViewController.Package() // The first screen can set this variable...
    
    override func viewDidLoad() {
        super.viewDidLoad()
        
        //MARK: setting the Labels' texts...
        if let unwrappedMessage = receivedPackage.message{
            if !unwrappedMessage.isEmpty{
                displayScreen.labelMessage.text = "Your message: \(unwrappedMessage)"
            }
        }
        
        if let unwrappedMood = receivedPackage.mood{
            if !unwrappedMood.isEmpty{
                displayScreen.labelMood.text = "You are feeling \(unwrappedMood)"
            }
        }
    }
}

```


In the above code, see that we are creating a variable `receivedPackage` of type `ViewController.Package`. `Package` is a public struct in the `ViewController` class. So to access it from inside another class, we need to write the source class name, then dot(`.`), then the struct name.&#x20;

Then we process and display the data on DisplayView.

Let's run the app:

<figure><img src="/gitbook-assets/six (1).gif" alt="Educational illustration for iOS concept"><figcaption></figcaption></figure>

_**Here, we learned how to detach the front end (View) of a screen from the back end (ViewController) of it. It is a widely used technique in iOS development. And you should follow this pattern.**_



### Wrapping up: structuring the files

Now, your project structure should look like the following:

![Educational illustration for iOS concept](</gitbook-assets/Screenshot 2023-05-16 at 2.39.20 PM (1).png>)

Although we have separated the Views from the Controllers, we still may find this structure cluttered. So, we want to put the files in separate groups for better readability.&#x20;

* Select the files related to the first screen (FirstScreenView and ViewController). To select both files together, press **Command + click on the intended files.**&#x20;
* **Right-click** on the selected files and select **New Group From Selection**. Name the group as 'First Screen'
* Create the group of files (DisplayView and DisplayViewController) for the second screen similarly.

<figure><img src="/gitbook-assets/ten.gif" alt="Educational illustration for iOS concept"><figcaption></figcaption></figure>

**Now, the structure looks a lot better!!!** :tada:



### Reference Code

[Download Project Archive](/gitbook-assets/App4.zip)

---

## Guided Practice Challenges

Before moving on to the next topic, try these low-stakes practice challenges in Xcode. They will build the exact muscle memory you need:

### Challenge 1: Experimentation
**The Scenario:** You've just learned about MVC Architecture.
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


### Send data back from Screen 2 to Screen 1

**Estimated effort:** 1-2 hours this topic
**Format:** Asynchronous online
**Prerequisites:** Previous iOS topics


**🎯 Topic Mission:** 
In this module, we will explore **3.3. Send data back from Screen 2 to Screen 1** and understand its fundamental mechanics. Your mission is to understand the mechanics behind this concept and write robust Swift code.


---

## Learning Objectives

By the end of this session, you will be able to:
1. Understand the core concepts of 3.3. Send data back from Screen 2 to Screen 1.
2. Implement 3.3. Send data back from Screen 2 to Screen 1 in an Xcode project.
3. Apply best practices to ensure clean and maintainable code.

---

## The Story So Far...

We have been progressively building our knowledge of iOS and Swift. In this module, we will expand our toolkit by diving into 3.3. Send data back from Screen 2 to Screen 1. 
Open your current Xcode project or start a new Playground to follow along with the hands-on material.

---

## Walkthrough: Exploring 3.3. Send data back from Screen 2 to Screen 1

> 📁 **Target Project** — Follow along by building the mini-app presented in the steps below, or integrate these concepts into your own ongoing projects.

### Send data back from Screen 2 to Screen 1

So, here is the goal for the extension of our current app:

* We will add a PickerView (selects one from a list of options) to the second screen (ShowViewController).
* The PickerView will show the user a list of moods: Happy, Meh, and Sad.
* The user selects a mood and sends the mood back to the first screen (ViewController).
* The first screen receives the mood and displays a corresponding image in an ImageView.

### Updating the screens with new UI elements.

**On ViewController,** we will add a new Label and an ImageView, as follows:


```swift
//
//  ViewController.swift
//
import UIKit

class ViewController: UIViewController {
    
    var textFieldMessage: UITextField!
    var buttonSend: UIButton!
    var labelMood: UILabel!
    var imageMood: UIImageView!
    
    override func viewDidLoad() {
        super.viewDidLoad()
        // Do any additional setup after loading the view.
        
        //MARK: initializing the UI elements...
        
        // code in between is omitted...
        setupLabelMood()
        setupImageMood()
        
        //MARK: initializing the constraints...
        initConstraints()
        
        //MARK: on buttonSend tap...
        buttonSend.addTarget(self, action: #selector(onButtonSendTapped),
                             for: .touchUpInside)
    }
    
    // code in between is omitted...
    
    //labelMood...
    func setupLabelMood(){
        labelMood = UILabel()
        labelMood.translatesAutoresizingMaskIntoConstraints = false
        view.addSubview(labelMood)
    }
    
    //imageMood...
    func setupImageMood(){
        imageMood = UIImageView()
        imageMood.translatesAutoresizingMaskIntoConstraints = false
        view.addSubview(imageMood)
    }
    
    //updating constraints..
    func initConstraints(){
        NSLayoutConstraint.activate([
            // textFieldMessage constraints...
            textFieldMessage.centerXAnchor.constraint(equalTo: view.safeAreaLayoutGuide.centerXAnchor),
            textFieldMessage.topAnchor.constraint(equalTo: view.safeAreaLayoutGuide.topAnchor, constant: 32),
            
            // buttonSend constraints...
            buttonSend.centerXAnchor.constraint(equalTo: view.safeAreaLayoutGuide.centerXAnchor),
            buttonSend.topAnchor.constraint(equalTo: textFieldMessage.bottomAnchor, constant: 16),
            
            // labelMood constraints...
            labelMood.centerXAnchor.constraint(equalTo: view.safeAreaLayoutGuide.centerXAnchor),
            labelMood.topAnchor.constraint(equalTo: buttonSend.bottomAnchor, constant: 16),// labelMood constraints...
            
            // imageMood constraints...
            imageMood.centerXAnchor.constraint(equalTo: view.safeAreaLayoutGuide.centerXAnchor),
            imageMood.topAnchor.constraint(equalTo: labelMood.bottomAnchor, constant: 16),
        ])       
    }
}
```


The `labelMood` will show the mood the user selected on ShowViewController, and the ImageView `imageMood` will show an image corresponding to the mood.

**Now on ShowViewController,** we will add a new Label, a PickerView, and a Button, as follows:


```swift
//
//  ShowViewController.swift
//
import UIKit

class ShowViewController: UIViewController {
    var labelMessage: UILabel!
    var labelMoodInstructions: UILabel!
    var moodPicker: UIPickerView!
    var buttonSendMood: UIButton!
    
    override func viewDidLoad() {
        super.viewDidLoad()
        
        //omitting the code in between...
        
        setupLabelMoodInstructions()
        setupMoodPicker()
        setupButtonSendMood()
        
        // MARK: setting up constraints...
        initConstraints()
    }
    
    //omitting the code in between...
    
    // setting up labelMoodInstructions...
    func setupLabelMoodInstructions(){
        labelMoodInstructions = UILabel()
        labelMoodInstructions.text = "How are you feeling today?"
        labelMoodInstructions.translatesAutoresizingMaskIntoConstraints = false
        view.addSubview(labelMoodInstructions)
    }
    
    // setting up mood picker...
    func setupMoodPicker(){
        moodPicker = UIPickerView()
        moodPicker.isUserInteractionEnabled = true
        moodPicker.translatesAutoresizingMaskIntoConstraints = false
        view.addSubview(moodPicker)
    }
    
    // setting up buttonSendMood...
    func setupButtonSendMood(){
        buttonSendMood = UIButton(type: .system)
        buttonSendMood.setTitle("Send Mood back!", for: .normal)
        buttonSendMood.translatesAutoresizingMaskIntoConstraints = false
        view.addSubview(buttonSendMood)
    }
    
    //omitting the code in between...
    
    // MARK: setting up constraints...
    func initConstraints(){
        NSLayoutConstraint.activate([
            //labelMessage constraints...
            labelMessage.centerXAnchor.constraint(equalTo: view.safeAreaLayoutGuide.centerXAnchor),
            labelMessage.topAnchor.constraint(equalTo: view.safeAreaLayoutGuide.topAnchor, constant: 32),
            
            //labelMoodInstructions constraints...
            labelMoodInstructions.centerXAnchor.constraint(equalTo: view.safeAreaLayoutGuide.centerXAnchor),
            labelMoodInstructions.topAnchor.constraint(equalTo: labelMessage.bottomAnchor, constant: 16),
            
            //mood picker constraints...
            moodPicker.centerXAnchor.constraint(equalTo: view.safeAreaLayoutGuide.centerXAnchor),
            moodPicker.topAnchor.constraint(equalTo: labelMoodInstructions.bottomAnchor, constant: 16),
            
            //buttonSendMood constraints...
            buttonSendMood.centerXAnchor.constraint(equalTo: view.safeAreaLayoutGuide.centerXAnchor),
            buttonSendMood.topAnchor.constraint(equalTo: moodPicker.bottomAnchor, constant: 16),
            
        ])
    }
}    
```


Here, `labelMoodInstructions` shows the message: "How are you feeling today?"

Then we place the `moodPicker` and finally put `buttonSendMood` at the bottom.

If we run the app now, we will see:

<figure><img src="/gitbook-assets/nine (1).gif" alt="Educational illustration for iOS concept"><figcaption></figcaption></figure>

Here, we do not see the two elements we added to ViewController, because `labelMood` and `imageMood` doesn't have anything to display.

On ShowViewController, we see there is an empty `moodPicker` and the newly added `buttonSendMood`.




### Send data back from Screen 2 to Screen 1: UIPickerView

<figure><img src="/gitbook-assets/Screenshot 2023-05-11 at 12.13.48 PM (1).png" alt="Educational illustration for iOS concept"><figcaption></figcaption></figure>

Now let's open the second screen (ShowViewController). We are going to set up our PickerView `moodPicker` now. Let's define an array of Strings having three moods: "Happy," "Meh," and "Sad."

```swift
// moods for moodPicker...
let moods: [String] = ["Happy", "Meh", "Sad"] 
```

Also, let's declare a variable that keeps the selected mode:

```swift
var selectedMood = "Happy"
```

Now it's time to set up the PickerView. To activate a PickerView, the class ShowViewController needs to adopt two [Protocols](https://github.com/sakibnm/iOS/blob/main/10.-protocols): UIPickerViewDelegate, and UIPickerViewDataSource. UIPickerViewDelegate is the protocol to enable user interactions with the PickerView, and UIPickerViewDataSource is the protocol to access data to display on PickerView.

You can adopt it in two ways. The first way is the way we have seen in our Swift notes:

```swift
class ShowViewController: UIViewController,
                            UIPickerViewDelegate,
                            UIPickerViewDataSource {

    //codes omitted...

}
```

Or we can separate the code block from the class to make our code more readable by using `extension` keyword:

```swift
class ShowViewController: UIViewController {
    // codes omitted...
}


extension ShowViewController: UIPickerViewDelegate, UIPickerViewDataSource{
    //has the same scope of ShowViewController...
}
```

The keyword **`extension`** allows you to write code inside the same context of a class. You are writing code literally inside a class if you use an extension. &#x20;

We will choose the second option, where we can keep the code separated. Let's implement or adopt the methods in the protocols and define them. You need to write code for three methods to properly set up the `moodPicker:`

```swift
// MARK: Conforming required PickerView protocols...
extension ShowViewController: UIPickerViewDelegate, UIPickerViewDataSource{
    
    //returns the number of columns/components in the Picker View...
    func numberOfComponents(in pickerView: UIPickerView) -> Int {
        return 1
    }
    
    //returns the number of rows in the current component...
    func pickerView(_ pickerView: UIPickerView, numberOfRowsInComponent component: Int) -> Int {
        return moods.count
    }
    
    //set the title of currently picked row...
    func pickerView(_ pickerView: UIPickerView, titleForRow row: Int, forComponent component: Int) -> String? {
        // on change selection, update selectedMood...
        selectedMood = moods[row]
        return moods[row]
    }
    
}
```

Here, `numberOfComponents()` method expects you to return the number of columns in PickerView. In our `moodPicker` we only have one column, so we will return 1. (There could be scenarios with multiple components, like a date picker).

You see, there are two methods named `pickerView()`, it might get you confused at first glance, but really they are used as overridden methods for the protocols. The most important parts are `numberOfRowsInComponent` and `titleForRow` parameters.

The first `pickerView()` method with `numberOfRowsInComponent` should return the number of rows in the current component/column. We have to populate the Strings in the moods array. So, we return `moods.count`.

The second `pickerView()` method with `titleForRow` should return the title we want to set for the selected row. Here, we need to show the Strings in the moods array, each mood in each row. So we return `moods[row]`. Before we return, we update `selectedMood` variable's value to the corresponding String to the currently selected row, `moods[row]`.

Now, two more important tasks are yet to be done. We have to show the `moodPicker` the class where it can fetch the data from and enable user interaction. Add the following two lines of codes, in `setupMoodPicker()`:

```swift
moodPicker.delegate = self
moodPicker.dataSource = self
```

We are saying for enabling the user interactions (delegate), and as the data source `moodPicker` should use the ShowViewController class's current instance.

Now so far, the code files look like the following:


```swift
//
//  ShowViewController.swift
//  App3
//
//  Created by Sakib Miazi on 5/10/23.
//

import UIKit

class ShowViewController: UIViewController {

    var messageFromFirstScreen:String? = "No message received!" //First screen can set this variable...
    
    let moods: [String] = ["Happy", "Meh", "Sad"] // moods for moodPicker...
    
    var selectedMood = "Happy"
    
    var labelMessage: UILabel!
    var labelMoodInstructions: UILabel!
    var moodPicker: UIPickerView!
    var buttonSendMood: UIButton!
    
    override func viewDidLoad() {
        super.viewDidLoad()
        //setting the view background to white...
        view.backgroundColor = .white
        
        // MARK: initializing the UI elements...
        setupLabelMessage()
        setupLabelMoodInstructions()
        setupMoodPicker()
        setupButtonSendMood()
        
        // MARK: setting up constraints...
        initConstraints()
    }
    
    //setting up labelMessage...
    func setupLabelMessage(){
        labelMessage = UILabel()
        labelMessage.textColor = .systemBlue
        labelMessage.text = messageFromFirstScreen
        labelMessage.translatesAutoresizingMaskIntoConstraints = false
        view.addSubview(labelMessage)
    }
    
    // setting up labelMoodInstructions...
    func setupLabelMoodInstructions(){
        labelMoodInstructions = UILabel()
        labelMoodInstructions.text = "How are you feeling today?"
        labelMoodInstructions.translatesAutoresizingMaskIntoConstraints = false
        view.addSubview(labelMoodInstructions)
    }
    
    // setting up mood picker...
    func setupMoodPicker(){
        moodPicker = UIPickerView()
        moodPicker.isUserInteractionEnabled = true
        moodPicker.translatesAutoresizingMaskIntoConstraints = false
        view.addSubview(moodPicker)
        
        //patching the delegate and data source...
        moodPicker.delegate = self
        moodPicker.dataSource = self
    }
    
    // setting up buttonSendMood...
    func setupButtonSendMood(){
        buttonSendMood = UIButton(type: .system)
        buttonSendMood.setTitle("Send Mood back!", for: .normal)
        buttonSendMood.translatesAutoresizingMaskIntoConstraints = false
        view.addSubview(buttonSendMood)
    }
    
    // MARK: setting up constraints...
    func initConstraints(){
        NSLayoutConstraint.activate([
            //labelMessage constraints...
            labelMessage.centerXAnchor.constraint(equalTo: view.safeAreaLayoutGuide.centerXAnchor),
            labelMessage.topAnchor.constraint(equalTo: view.safeAreaLayoutGuide.topAnchor, constant: 32),
            
            //labelMoodInstructions constraints...
            labelMoodInstructions.centerXAnchor.constraint(equalTo: view.safeAreaLayoutGuide.centerXAnchor),
            labelMoodInstructions.topAnchor.constraint(equalTo: labelMessage.bottomAnchor, constant: 16),
            
            //mood picker constraints...
            moodPicker.centerXAnchor.constraint(equalTo: view.safeAreaLayoutGuide.centerXAnchor),
            moodPicker.topAnchor.constraint(equalTo: labelMoodInstructions.bottomAnchor, constant: 16),
            
            //buttonSendMood constraints...
            buttonSendMood.centerXAnchor.constraint(equalTo: view.safeAreaLayoutGuide.centerXAnchor),
            buttonSendMood.topAnchor.constraint(equalTo: moodPicker.bottomAnchor, constant: 16),
            
        ])
    }

}

// MARK: Conforming to required PickerView protocols...
extension ShowViewController: UIPickerViewDelegate, UIPickerViewDataSource{
    
    //returns the number of columns/components in the Picker View...
    func numberOfComponents(in pickerView: UIPickerView) -> Int {
        return 1
    }
    
    //returns the number of rows in the current component...
    func pickerView(_ pickerView: UIPickerView, numberOfRowsInComponent component: Int) -> Int {
        return moods.count
    }
    
    //set the title of currently picked row...
    func pickerView(_ pickerView: UIPickerView, titleForRow row: Int, forComponent component: Int) -> String? {
        // on change selection, update selectedMood...
        selectedMood = moods[row]
        return moods[row]
    }
    
}


```



```swift
//
//  ViewController.swift
//  App3
//
//  Created by Sakib Miazi on 5/10/23.
//

import UIKit

class ViewController: UIViewController {
    
    var textFieldMessage: UITextField!
    var buttonSend: UIButton!
    var labelMood: UILabel!
    var imageMood: UIImageView!

    override func viewDidLoad() {
        super.viewDidLoad()
        // Do any additional setup after loading the view.
        
        //MARK: initializing the UI elements...
        setupTextFieldMessage()
        setupButtonSend()
        setupLabelMood()
        setupImageMood()
        
        //MARK: initializing the constraints...
        initConstraints()
        
        //MARK: on buttonSend tap...
        buttonSend.addTarget(self, action: #selector(onButtonSendTapped),
                             for: .touchUpInside)
    }
    
    // textFieldMessage...
    func setupTextFieldMessage(){
        textFieldMessage = UITextField()
        textFieldMessage.placeholder = "Put your message here"
        textFieldMessage.borderStyle = .roundedRect
        textFieldMessage.translatesAutoresizingMaskIntoConstraints = false
        view.addSubview(textFieldMessage)
    }
    
    //buttonSend...
    func setupButtonSend(){
        buttonSend = UIButton(type: .system)
        buttonSend.setTitle("Send", for: .normal)
        buttonSend.translatesAutoresizingMaskIntoConstraints = false
        view.addSubview(buttonSend)
    }
    
    //labelMood...
    func setupLabelMood(){
        labelMood = UILabel()
        labelMood.translatesAutoresizingMaskIntoConstraints = false
        view.addSubview(labelMood)
    }
    
    //imageMood...
    func setupImageMood(){
        imageMood = UIImageView()
        imageMood.translatesAutoresizingMaskIntoConstraints = false
        view.addSubview(imageMood)
    }
    
    // MARK: On button tapped delegate...
    @objc func onButtonSendTapped(){
        //initializing a new screen with ShowViewController...
        var showViewController = ShowViewController()
        
        //set the message to ShowViewController's messageFromFirstScreen variable...
        if let unwrappedMessage = textFieldMessage.text{
            if !unwrappedMessage.isEmpty{ // checking if the user has put any message...
                showViewController.messageFromFirstScreen = unwrappedMessage
            }
        }
        
        //push the screen to Stack...
        navigationController?.pushViewController(showViewController, animated: true)
    }
    
    //MARK: initializing constraints...
    func initConstraints(){
        
        NSLayoutConstraint.activate([
            // textFieldMessage constraints...
            textFieldMessage.centerXAnchor.constraint(equalTo: view.safeAreaLayoutGuide.centerXAnchor),
            textFieldMessage.topAnchor.constraint(equalTo: view.safeAreaLayoutGuide.topAnchor, constant: 32),
            
            // buttonSend constraints...
            buttonSend.centerXAnchor.constraint(equalTo: view.safeAreaLayoutGuide.centerXAnchor),
            buttonSend.topAnchor.constraint(equalTo: textFieldMessage.bottomAnchor, constant: 16),
            
            // labelMood constraints...
            labelMood.centerXAnchor.constraint(equalTo: view.safeAreaLayoutGuide.centerXAnchor),
            labelMood.topAnchor.constraint(equalTo: buttonSend.bottomAnchor, constant: 16),// labelMood constraints...
            
            // imageMood constraints...
            imageMood.centerXAnchor.constraint(equalTo: view.safeAreaLayoutGuide.centerXAnchor),
            imageMood.topAnchor.constraint(equalTo: labelMood.bottomAnchor, constant: 16),
        ])
        
    }


}


```




### Send data back from Screen 2 to Screen 1: delegating to ViewController

Now, let's enable the action for `buttonSendMood` in ShowViewController.swift file. So let's update `viewDidLoad()` function and add a new selector method `onSendButtonTapped()`:


```swift
// setting up buttonSendMood...
override func viewDidLoad() {
        super.viewDidLoad()
        //setting the view background to white...
        view.backgroundColor = .white
        
        // MARK: initializing the UI elements...
        setupLabelMessage()
        setupLabelMoodInstructions()
        setupMoodPicker()
        setupButtonSendMood()
        
        // MARK: setting up constraints...
        initConstraints()
        
        //MARK: add a delegate to on 
        //button send mode tapped...
        buttonSendMood.addTarget(self, action: #selector(onSendMoodButtonTapped), for: .touchUpInside)
    }
// MARK: on send button tapped...
@objc func onSendMoodButtonTapped(){
    
}
```


### Declaring the delegate variable in ShowViewController.swift

**Before we write something in `onSendMoodButtonTapped()`,** we need to do a few more things. First, if we want to send the mood back to the first screen (ViewController), we need to ask the ViewController to receive the data and do the tasks afterward. We are delegating the tasks to VIewController after we click on `buttonSendMood`. So, we create a variable `delegate` in ShowViewController.swift file that can hold the reference to the instance of ViewController:

```swift
//
//  ShowViewController.swift
//  App3
//

class ShowViewController: UIViewController {

    var messageFromFirstScreen:String? = "No message received!" //First screen can set this variable...
    var delegate: ViewController! //delegate to ViewController...
    
    // codes omitted...
}
```

### Initializing delegate to the instance of ViewController (self)

**Now, let's go back to ViewController class** and ensure we set the `delegate`variable's value before pushing ShowViewController into the NavigationController. By doing that, we are ensuring that the instance of ShowViewController can have access to the instance of ViewController. So let's update the `@objc func onButtonSendTapped()` in ViewController:


```swift
//
//  ViewController.swift
//  App3
//

class ViewController: UIViewController {
    // codes omitted...
    // MARK: On button tapped delegate...
    @objc func onButtonSendTapped(){
        //initializing a new screen with ShowViewController...
        var showViewController = ShowViewController()
        
        //set the message to ShowViewController's messageFromFirstScreen variable...
        if let unwrappedMessage = textFieldMessage.text{
            if !unwrappedMessage.isEmpty{ // checking if the user has put any message...
                //Sending data...
                showViewController.messageFromFirstScreen = unwrappedMessage
            }
            //setting the delegate for receiving data...
            showViewController.delegate = self
        }
        
        //push the screen to Stack...
        navigationController?.pushViewController(showViewController, animated: true)
    }
    
    //codes omitted...

}
 
```


### Doing delegated tasks in ViewController

**Now, we need to add a method in ViewController** to conduct the delegated tasks from ShowViewController:


```swift
//
//  ViewController.swift
//  App3
//

class ViewController: UIViewController {
    // codes omitted...
    // MARK: On button tapped delegate...
    @objc func onButtonSendTapped(){
        //initializing a new screen with ShowViewController...
        var showViewController = ShowViewController()
        
        //set the message to ShowViewController's messageFromFirstScreen variable...
        if let unwrappedMessage = textFieldMessage.text{
            if !unwrappedMessage.isEmpty{ // checking if the user has put any message...
                //Sending data...
                showViewController.messageFromFirstScreen = unwrappedMessage
            }
            //setting the delegate for receiving data...
            showViewController.delegate = self
        }
        
        //push the screen to Stack...
        navigationController?.pushViewController(showViewController, animated: true)
    }
    
    //codes omitted...
    
    //MARK: delegated method from ShowViewController...
    func delegateButtonSendMood(mood: String){
        print("The user is \(mood)")
    }
    
    //codes omitted...
}
 
```


Here, `delegateButtonSendMood(mood:String)` receives a String (mood) as a parameter. Let's just print the mood for now.

Now, let's switch back to ShowViewController. **We now need to call this `delegateButtonSendMood(mood:String)` method when the user taps on `onSendMoodButton`.** We can write:


```swift
//
//  ShowViewController.swift
//  App3
//

class ShowViewController: UIViewController {
    // codes omitted in between...
    
    var delegate: ViewController! //delegate to ViewController...
    
    //codes omitted in between...
    // MARK: on send button tapped...
    @objc func onSendMoodButtonTapped(){
        delegate.delegateButtonSendMood(mood: selectedMood)
    }
    
    //codes omitted in between...

}

```


Since the instance of ShowViewController gets populated with the variable `delegate` already set to the instance of ViewController, we can call `delegateButtonSendMood()` method from ShowViewController. We are calling the method with `selectedMood` as the parameter. Now, let's run the app and check if ViewController can print the mood.

<figure><img src="/gitbook-assets/ten (1).gif" alt="Educational illustration for iOS concept"><figcaption></figcaption></figure>

We are yet to do another task. We need to pop the ShowViewController after we click on `buttonSendMood`. So we will add `navigationController?.popViewController(animated: true)` to `@objc func onSendMoodButtonTapped()`.


```swift
//
//  ShowViewController.swift
//  App3
//

class ShowViewController: UIViewController {
    // codes omitted in between...
    
    var delegate: ViewController! //delegate to ViewController...
    
    //codes omitted in between...
    // MARK: on send button tapped...
    @objc func onSendMoodButtonTapped(){
        delegate.delegateButtonSendMood(mood: selectedMood)
        navigationController?.popViewController(animated: true)
    }
    
    //codes omitted in between...

}
```


Now let's run it again:

<figure><img src="/gitbook-assets/eleven.gif" alt="Educational illustration for iOS concept"><figcaption></figcaption></figure>

Yay! We now learned how to send data back and forth between two screens!

_Now, your task is to show the user's mood in `labelMood` at ViewController screen._

Next, we will discuss displaying an image related to the user's mood.



### Send data back from Screen 2 to Screen 1: UIImageView

### Importing images into the project

Now, let's start working with ImageViews. We need three images for moods: happy, meh, and sad. We will be using the following images in three different sizes: 1x, 2x, and 3x.

![Educational illustration for iOS concept](</gitbook-assets/happy (1).png>) ![Educational illustration for iOS concept](</gitbook-assets/meh (1).png>) ![Educational illustration for iOS concept](</gitbook-assets/sad (1).png>)

Download the images from here:

[Download Project Archive](/gitbook-assets/images (1).zip)

If you extract the files, you will see something like the following:

<figure><img src="/gitbook-assets/Screenshot 2023-05-11 at 9.26.55 PM (2).png" alt="Educational illustration for iOS concept"><figcaption></figcaption></figure>

See each image has three versions: 1x, 2x, and 3x.

* 1x images have a resolution of 200x200
* 2x images have a resolution of 400x400
* 3x images have a resolution of 600x600

These are called image scaling. To understand the concept, read the following article: [https://www.appypie.com/image-scaling-ios-how-to](https://www.appypie.com/image-scaling-ios-how-to).

Long story short, in the early iOS devices before iPhone 8, the resolutions were very low, less than 640p. There you need to use smaller images (like 200x200). Comparatively, phones like iPhone 11 or later have more than 1024p, so modern screens can accommodate bigger images (like 600x600). iOS has a great feature to scale the images automatically if you provide images with all three scales. It will automatically use the appropriate image based on the device where you run the app.

**Pro tip:** now, you usually do not have to worry about 1x images anymore; those low-resolution devices are non-existent now.

Now, let's add the images to our project. Go to the project navigator on the left pane. Click on **Assets**. Right-click somewhere below the AppIcon, and select **New Folder.** Create a folder named "mood images."

_(you can name it as you want; you do not need to create the folder; I am creating the folder to help myself organize the assets)._

Now, right-click on the "mood images" folder and select **Import.** Then select the images and **Open.**

<figure><img src="/gitbook-assets/thirteen (1).gif" alt="Educational illustration for iOS concept"><figcaption></figcaption></figure>

Looking at the Assets now, you'll see three image assets listed instead of nine. The project automatically indexed nine of them into three assets, each having 3 scales (1x, 2x, and 3x). ![Educational illustration for iOS concept](</gitbook-assets/Screenshot 2023-05-11 at 10.11.02 PM.png>)

### Setting the image into the ImageView through delegate

In ViewController, add the following line of code into `delegateButtonSendMood()` method:

```swift
imageMood.image = UIImage(named: mood.lowercased())
```

Here, we are creating an `UIImage` object from the project assets. We are looking for an image asset named as the mood we receive from ShowViewController through the delegate method. Now, the moods are "Happy," "Meh," and "Sad." But the image asset names are "happy," "meh," and "sad." So we convert the String to all lowercase by calling `lowercased()` method.

Let's run the app again.

<figure><img src="/gitbook-assets/fourteen (1).gif" alt="Educational illustration for iOS concept"><figcaption></figcaption></figure>

Nice! We have learned a lot of things together from building this app:

* Designing an app without using the storyboard
* Working with multiple ViewControllers
* Navigation Controller and Navigation Stack
* Data exchange between two view controllers
* Basics of ImageViews

Thanks for bearing with me! :smile:

### A few notes:

* These are just the basics of these topics; we just scratched the surface, and many more things to explore, eventually.
* UIImageView and layout constraints do not go hand in hand. It's always better to use a UIImageView wrapped by a UIView. We will discuss it further down the road.

_**Now, before you go, set the title of the app by writing****&#x20;****`title = "Learning Navigation"`****&#x20;****in****&#x20;****`viewDidLoad()`****&#x20;****method at ViewController. And run the app to see the changes!**_

---

## Guided Practice Challenges

Before moving on to the next topic, try these low-stakes practice challenges in Xcode. They will build the exact muscle memory you need:

### Challenge 1: Experimentation
**The Scenario:** You've just learned about 3.3. Send data back from Screen 2 to Screen 1.
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


### 1.-creating-our-first-app

**Estimated effort:** 1-2 hours this topic
**Format:** Asynchronous online
**Prerequisites:** Previous iOS topics


**🎯 Topic Mission:** 
In this module, we will explore **this topic** and understand its fundamental mechanics. Your mission is to understand the mechanics behind this concept and write robust Swift code.


---

## Learning Objectives

By the end of this session, you will be able to:
1. Understand the core concepts of this topic.
2. Implement this topic in an Xcode project.
3. Apply best practices to ensure clean and maintainable code.

---

## The Story So Far...

We have been progressively building our knowledge of iOS and Swift. In this module, we will expand our toolkit by diving into this topic. 
Open your current Xcode project or start a new Playground to follow along with the hands-on material.

---

## Walkthrough: Exploring this topic

> 📁 **Target Project** — Follow along by building the mini-app presented in the steps below, or integrate these concepts into your own ongoing projects.

### Creating our first app

Press `Command (⌘) + Space` together on your Mac computer. It opens up Spotlight search. Search 'Xcode' there, and open Xcode. It opens the following window:

<figure><img src="/gitbook-assets/Screenshot 2023-05-09 at 10.51.51 AM (1).png" alt="Educational illustration for iOS concept"><figcaption></figcaption></figure>

Click on **'Create a new Xcode project.'** You will see the following:

**Make sure you select iOS from the top template chooser.&#x20;****Do not choose multiplatform or macOS.**

<figure><img src="/gitbook-assets/Screenshot 2023-05-09 at 10.55.45 AM (1).png" alt="Educational illustration for iOS concept"><figcaption></figcaption></figure>

Select **App** and press **Next.**

<figure><img src="/gitbook-assets/Screenshot 2023-05-09 at 10.57.39 AM (1).png" alt="Educational illustration for iOS concept"><figcaption></figcaption></figure>

Give your project a name. If you have not already signed in to an Apple ID, sign in here and then select your Personal Team. Put your preferred organization identifier (reversed domain name order). For example, you can put `com.nuios`. Select **'Storyboard'** as the interface (**do not select 'SwiftUI'**). Select the language **'Swift.'** And then press **Next**. You'll see:

<figure><img src="/gitbook-assets/Screenshot 2023-05-09 at 11.04.18 AM (1).png" alt="Educational illustration for iOS concept"><figcaption></figcaption></figure>

Here is where you'll choose where to save your project. Click on **Create.** It will create a new project for you, and you will see the following:

<figure><img src="/gitbook-assets/Screenshot 2023-05-09 at 11.05.36 AM (1).png" alt="Educational illustration for iOS concept"><figcaption></figcaption></figure>

Here, you need to select a simulator. Please click on the top middle panel as indicated in the following image:

<figure><img src="/gitbook-assets/1.1.1.png" alt="Educational illustration for iOS concept"><figcaption></figcaption></figure>

Select an iPhone simulator of your choice. **Do not select 'This Mac.'**

Now, your first project is ready to be built.

Press the Play :arrow\_forward: button from the top left corner.

<figure><img src="/gitbook-assets/Screenshot 2023-05-09 at 11.07.39 AM (1).png" alt="Educational illustration for iOS concept"><figcaption></figcaption></figure>

It will open up the Emulator with an empty screen.

<figure><img src="/gitbook-assets/Screenshot 2023-05-09 at 11.12.10 AM (1).png" alt="Educational illustration for iOS concept"><figcaption></figcaption></figure>

If you can see the emulator, you have successfully built your first app. We will start building on it.




### Project structure overview

The Xcode screen has three panes.

<figure><img src="/gitbook-assets/Screenshot 2023-05-09 at 11.22.24 AM (1).png" alt="Educational illustration for iOS concept"><figcaption></figcaption></figure>

### The left pane

In the left pane, you see the file structure of the codes and resources. If you right-click on the project directory, you can see that you can show the project directory in Finder:

![Educational illustration for iOS concept](</gitbook-assets/Screenshot 2023-05-09 at 11.27.41 AM.png>)

It will show you the project directory:

<figure><img src="/gitbook-assets/Screenshot 2023-05-09 at 11.30.52 AM.png" alt="Educational illustration for iOS concept"><figcaption></figcaption></figure>

Now we can see that the structure of the files and directories in your project directory match how you see the project structure in Xcode.

You will see three Swift files: **AppDelegate, SceneDelegate, and ViewController.**

**AppDelegate** is used to manage the application's lifecycle, like what happens after the app is launched, while populating the screens, when a screen is changing, and so on.

**SceneDelegate** is used to manage the lifecycle of the scenes you see while the app is running, like what happens when a window is populated, when the user sends the scene into the background, when it comes back from the background, and so on.

**ViewController** is the most important file where you define the Models, Views, and Controllers of the 'empty' screen you see. For each screen, you need to write a ViewController. This is the file where we will spend 90% of our time.

You'll also see two 'Storyboard' files as well. These are the design boards like prototype builders. **You should not touch the 'LaunchScreen' file if you do not have to (in fact, we do not need to touch this file in this course**).

**The Main storyboard is** where you can create the front end of your app by dragging and dropping UI elements on the screen, just like a prototyping tool. Storyboards are XML files defining the screen's UI elements, positional constraints, and user interactions.

_Even though it feels easier to design our app with storyboards, it comes with a significant caveat. It is very painful to work with when more than one developer works on the same project. So the industry shifted from using storyboards. Instead, we usually write code in the ViewController to design the screen programmatically and keep the storyboards empty. **For the first few practice exercises, we will design it in Storyboard and then switch to the design by coding.**_

### The middle pane

The middle pane is the work pane. Here we write code, design, change settings and preferences, debug, etc. For example, If we click on **ViewController** from the left pane, we will see the code in the middle pane:

<figure><img src="/gitbook-assets/Screenshot 2023-05-09 at 11.57.38 AM (1).png" alt="Educational illustration for iOS concept"><figcaption></figcaption></figure>

### The right pane

The right pane is the configuration and attributes explorer pane. For example, if you click on the Main Storyboard and click the screen preview, the right pane will display the attribute of the screen view:

<figure><img src="/gitbook-assets/Screenshot 2023-05-09 at 12.00.43 PM (1).png" alt="Educational illustration for iOS concept"><figcaption></figcaption></figure>

Once we start building apps, we will eventually get used to Xcode more.



### UILabel, our first UI element

Let's add a text pane, `UILabel` to our storyboard. Open the Main storyboard, and press `Command(⌘) + Shift + L` together. It opens up the Objects Library like this:

<figure><img src="/gitbook-assets/Screenshot 2023-05-09 at 12.09.01 PM.png" alt="Educational illustration for iOS concept"><figcaption></figcaption></figure>

Now, look for 'label'. **Press the intended UI element, (in this case, it shows as 'Label'), drag it, and drop it on the preview screen.**

<figure><img src="/gitbook-assets/six_ (1).gif" alt="Educational illustration for iOS concept"><figcaption></figcaption></figure>

It will now show:

<figure><img src="/gitbook-assets/Screenshot 2023-05-09 at 12.15.19 PM (1).png" alt="Educational illustration for iOS concept"><figcaption></figcaption></figure>

See, there is a left view pane where you can find all the elements. The newly added Label got added inside the View Controller tree. Inside the View Controller, you have a View. The View is actually the view of the entire screen, including the camera cut.

#### Safe area: Inside the View, we have a Safe area. A safe area is an area where there are no interruptions or obstacles like the camera cut. Click on the safe area; it will mark the safe area on the screen:

<figure><img src="/gitbook-assets/Screenshot 2023-05-09 at 12.24.52 PM.png" alt="Educational illustration for iOS concept"><figcaption></figcaption></figure>

The safe area comes in very handy designing the screen with constraints.

Now, let's add a few constraints and attributes for the Label we just added.

Click on the Label, either on the preview screen or the left view pane, and notice the right configuration pane:

<figure><img src="/gitbook-assets/Screenshot 2023-05-09 at 12.32.14 PM (1).png" alt="Educational illustration for iOS concept"><figcaption></figcaption></figure>

Change the label text, color, and font. You see, once you change the attributes, the changes reflect on the actual UI element.

#### Constraints and Alignments

Now, let's work on the constraints so that we can place the label on the screen, and it stays somewhere predictable, even if we rotate the screen. This is called anchoring.

Before we change anything for the Label, let's see where we will find the tools to work on constraints. Look at the bottom right corner of the Middle pane:

<figure><img src="/gitbook-assets/Screenshot 2023-05-09 at 12.40.55 PM (2).png" alt="Educational illustration for iOS concept"><figcaption></figcaption></figure>

Now let's click on the Label. Then click on the Alignment tool, and select both 'Horizontally in Container,' and 'Vertically in Container.' And add the constraints. It should put the Label in the center of the screen (center-aligned both horizontally and vertically):

<figure><img src="/gitbook-assets/Screenshot 2023-05-09 at 12.50.49 PM (1).png" alt="Educational illustration for iOS concept"><figcaption></figcaption></figure>

Now run the app. and rotate the screen:

![Educational illustration for iOS concept](</gitbook-assets/Screenshot 2023-05-09 at 12.51.58 PM (1).png>)

<figure><img src="/gitbook-assets/Screenshot 2023-05-09 at 12.52.07 PM (1).png" alt="Educational illustration for iOS concept"><figcaption></figcaption></figure>

See, for both cases, the alignment setup is keeping the Label on the screen nice and predictable.



### UITextField, and constraints

So far, we have added one UILabel, with the text "Hello World" in it. Now, we will add our second UI element on the screen, UITextField, below the Label. UITextField is used to get user inputs from the keyboard. We can type something in the TextField and use it in our app.

#### Housekeeping the constraints first

So far, the Label is center-aligned both horizontally and vertically. We will keep the horizontal alignment for the Label but remove the vertical alignment. Unfortunately, the storyboard can't clear one particular constraint from visual tools (or not easily). (That's another reason why we will move to write constraints programmatically). So, we will clear all the constraints from the Label. Click on the 'Reset constraints' tool, and select Clear Constraints for Selected Views to clear constraints for the Label:

<figure><img src="/gitbook-assets/Screenshot 2023-05-09 at 1.38.01 PM (1).png" alt="Educational illustration for iOS concept"><figcaption></figcaption></figure>

Now, we will put the Label at the top of the screen, having a 32 points margin from the top edge. Click the 'Add Constraints' tool, and set the top anchor constant to 32. Then click to 'Add 1 constraint':

<figure><img src="/gitbook-assets/Screenshot 2023-05-09 at 1.44.08 PM (1).png" alt="Educational illustration for iOS concept"><figcaption></figcaption></figure>

So you see that the Label is anchored to the top edge of the screen with a 32 points gap:

![Educational illustration for iOS concept](</gitbook-assets/Screenshot 2023-05-09 at 1.46.36 PM.png>)

Now, we will horizontally center the Label. Use the alignment tool to add the constraint:

<figure><img src="/gitbook-assets/Screenshot 2023-05-09 at 1.49.20 PM (1).png" alt="Educational illustration for iOS concept"><figcaption></figcaption></figure>

#### Adding UITextField below UILabel

We now add the UITextField using the Object library (`Command(⌘) + Shift + L`). Look for text, and drag and drop TextField on the screen.

![Educational illustration for iOS concept](</gitbook-assets/Screenshot 2023-05-09 at 1.55.41 PM (1).png>)

Now, let's center the TextField:

<figure><img src="/gitbook-assets/Screenshot 2023-05-09 at 1.58.10 PM (1).png" alt="Educational illustration for iOS concept"><figcaption></figcaption></figure>

Then add the 16 points constraint to the top so that the TextField is anchored to the bottom of the Label having a 16 points gap.

<figure><img src="/gitbook-assets/Screenshot 2023-05-09 at 2.01.02 PM (1).png" alt="Educational illustration for iOS concept"><figcaption></figcaption></figure>

For a TextField, you should give a user some hint of what kind of text the app is expecting. For example, we want to give the user a hint, "Put some text". So, we will use the 'Place holder' attribute in the right pane of the TextField to set it.

<figure><img src="/gitbook-assets/Screenshot 2023-05-09 at 2.02.40 PM (1).png" alt="Educational illustration for iOS concept"><figcaption></figcaption></figure>

Now run the app.

![Educational illustration for iOS concept](</gitbook-assets/Screenshot 2023-05-09 at 2.07.46 PM.png>)

You can see now, you can type something on the TextField.

Please note, you are using your computer keyboard to put the text inside. You can use the emulator (device) keyboard too. From the Simulator menu, click **I/O -> Keyboard -> Toggle Software Keyboard.**

<figure><img src="/gitbook-assets/Screenshot 2023-05-09 at 2.10.38 PM (1).png" alt="Educational illustration for iOS concept"><figcaption></figcaption></figure>



### UIButton, and UIAlertController

At this point, We have a TextField to get user inputs from the keyboard. Now, let's add a button below the TextField. Our goal is if a user types something on the TextField and presses the button, the app should echo the text back to the user with an alert.

We will use two UI elements for this purpose: UIButton, and UIAlertController.

### Adding a new button

Let's place a Button on the Screen, center it, and anchor it 16 points below the TextField.

<figure><img src="/gitbook-assets/Screenshot 2023-05-09 at 2.39.56 PM (1).png" alt="Educational illustration for iOS concept"><figcaption><p>Objects library</p></figcaption></figure>

<figure><img src="/gitbook-assets/Screenshot 2023-05-09 at 2.40.21 PM (1).png" alt="Educational illustration for iOS concept"><figcaption><p>Drag and drop button</p></figcaption></figure>

<figure><img src="/gitbook-assets/Screenshot 2023-05-09 at 2.40.40 PM (1).png" alt="Educational illustration for iOS concept"><figcaption><p>Center horizontally</p></figcaption></figure>

<figure><img src="/gitbook-assets/Screenshot 2023-05-09 at 2.40.57 PM (1).png" alt="Educational illustration for iOS concept"><figcaption><p>Add anchor to the bottom of the TextField</p></figcaption></figure>

<figure><img src="/gitbook-assets/Screenshot 2023-05-09 at 2.41.30 PM (1).png" alt="Educational illustration for iOS concept"><figcaption><p>Button is now placed</p></figcaption></figure>

Now, let's change the attributes of the Button. If you select the Button and look at the right pane, you will see the attributes of it. You can play with many different things, like the Style, Title, Background, and Foreground styling, etc. For now, we will just change the Title. Let's change the Title from "Button" to "Click me!"

<figure><img src="/gitbook-assets/Screenshot 2023-05-09 at 2.48.02 PM (1).png" alt="Educational illustration for iOS concept"><figcaption></figcaption></figure>

Now, run the app, and you will see that you have the button "Click me!", and can click on it!

### ViewController and AlertController

Now, we need to handle the click on the Button. So, we need to patch the frontend UI elements to our ViewController code.

_We will not use the following technique very much after this lesson since most people do not use Storyboards anymore. However, it's worth the knowledge._

So, we will open the Main storyboard and the ViewController code side by side. To do that, Go to the menu, **Editor -> Assistant.** After you click Assistant, it opens the Viewcontroller to right of the Storyboard:

<figure><img src="/gitbook-assets/Screenshot 2023-05-09 at 3.54.28 PM (2).png" alt="Educational illustration for iOS concept"><figcaption></figcaption></figure>

Basically, you have the front end on the left, and on the right, you have the back end.

<figure><img src="/gitbook-assets/Screenshot 2023-05-09 at 3.59.44 PM.png" alt="Educational illustration for iOS concept"><figcaption></figcaption></figure>

Let's patch the UI elements with the back-end code (ViewController).&#x20;

Think about what UI elements we need to handle from the backend here. We need the TextField and the Button. So, **press the 'control' key** on your keyboard (not the command key) and keep it pressed. While pressing the control button, click on the TextField from the storyboard, and do not release. Now, drag the mouse pointer to the right ViewController (keep both the control and mouse pointer pressed). A blue line should appear. Place it inside the class ViewController. An outlet connector appears; put the name of the logical TextField as "textFIeldUser."

<figure><img src="/gitbook-assets/one (2) (1).gif" alt="Educational illustration for iOS concept"><figcaption></figcaption></figure>

It creates a `@IBOutlet var textFieldUser: UITextField!` variable in your ViewController. `@IBOutlet` means it's an outlet from the Interface Builder (storyboard). In short, `textFieldUser` is the logical instance of the `TextField` from storyboard in the ViewController class.

Let's add the Button outlet to the ViewController the same way. And name the Button "buttonClickMe."

<figure><img src="/gitbook-assets/Screenshot 2023-05-09 at 5.35.35 PM (1).png" alt="Educational illustration for iOS concept"><figcaption></figcaption></figure>

### Adding button action

Now, we need to handle if the user taps on `buttonClickMe`. We need to handle the event when the view finishes loading. So, find the `viewDidLoad()` method. When the screen is done populating the UI elements and displaying them, this method is called by the system.

Let's type `buttonClickMe` in `viewDidLoad()` method, and press `.` and then you will see Xcode automatically shows you the possible usage of the button. Then find the `addTarget()` function.

<figure><img src="/gitbook-assets/two (3) (1).gif" alt="Educational illustration for iOS concept"><figcaption></figcaption></figure>

`addTarget()` has three parameters: target, action, and for.

* `target`: means where (view) we would listen for an event to happen. In our case, it is `self`. `self` is the current view, which is the View Controller screen.
* `action`: means which method to call if an event happens. Notice that it is asking for a Selector type function. 'Selector' is an API from the iOS system. iOS is built with Objective-C, and in the iOS system, Objective-C is heavily used. So, when an event occurs (the user taps on the Button), the system needs to delegate that to a method written in Swift to act based on the event. `@objc` means the Objective-C code of iOS can now read this method and delegate the event to the function to handle. We define a method `onButtonClickedMeTapped()` to handle the tap event.
* `for`: means what kind of event the system would wait for. For example, here we are using `.touchUpInside`. It means, If the button is tapped inside, catch the event, and delegate the event to the `onButtonClickedMeTapped()` method.

Let's define the `onButtonClickMeTapped()` method:

```swift
@objc func onButtonClickMeTapped(){
        print("Button Clicked!!")
}
```

Now, let's run the app and click the button.

<figure><img src="/gitbook-assets/three_ (1).gif" alt="Educational illustration for iOS concept"><figcaption></figcaption></figure>

You'll see that at the bottom right of Xcode, "Button clicked!!" is printed on the Output area.

### Displaying an Alert

Now, we will display an alert instead of just printing "Button clicked!!" Let's define an AlertController when the button is clicked. We want to display the text the user added in `textFieldUser`. So, we can write the code below to fetch what the user typed in the text field.

```swift
@objc func onButtonClickMeTapped(){
    //print("Button Clicked!!")
    // MARK: fetching the text the user typed...
    let text = textFieldUser.text
    
    print(text)

}
```

If you run the app, click the button, and check what's printed in the output, you will see:

`Optional("")`. That means `textFieldUser.text` is an Optional String. So you need to unwrap it and then use it.

<pre class="language-swift"><code class="lang-swift"><strong>@objc func onButtonClickMeTapped(){
</strong>        //print("Button Clicked!!")
        // MARK: fetching the text the user typed...
        let text = textFieldUser.text
        
        if let unwrappedText = text{
            print(unwrappedText)
        }
    }
</code></pre>

Now, it will print the string the user types. Let's show the alert.

If the text is empty, we want to show an error message saying the text field should not be empty. Otherwise, we will show the text typed.

Let's write the following code:

```swift
@objc func onButtonClickMeTapped(){
    //print("Button Clicked!!")
    // MARK: fetching the text the user typed...
    let text = textFieldUser.text
    
    //Unwrapping the optional text...
    if let unwrappedText = text{
        //print(unwrappedText)
        
        if(unwrappedText.isEmpty){ //The user didn't put anything...
            showErrorAlert()
        } else{ //The user put some texts...
            showAlertText(text: unwrappedText)
        }
    }
}

//MARK: Error alert...
func showErrorAlert(){
    let alert = UIAlertController(
        title: "Error!", message: "Text Field must not be empty!", 
        preferredStyle: .alert
    )
    
    alert.addAction(UIAlertAction(title: "OK", style: .default))
    
    self.present(alert, animated: true)
}

//MARK: text alert...
func showAlertText(text:String){
    let alert = UIAlertController(
        title: "You said:", 
        message: "\(text)", 
        preferredStyle: .alert
    )
    
    alert.addAction(UIAlertAction(title: "OK", style: .default))
    
    self.present(alert, animated: true)
}
```

In the above code, we first define a `UIAlertController`. The initializer of the alert controller requires three parameters.

* `title` is the title of the alert.
* `message` is the String the alert will display.
* and, `preferredStyle` is the way you want to display the alert. If it is a simple alert, use `.alert`.

Then you need to add action buttons for the alert, like "OK" or "Cancel." We just added an "OK" button here by calling `addAction()`.

Now let's run the app:

<figure><img src="/gitbook-assets/four (2).gif" alt="Educational illustration for iOS concept"><figcaption></figcaption></figure>

Now, we are almost done with our first app. The entire code in ViewController so far is:

```swift
//
//  ViewController.swift
//  App1
//
//  Created by Sakib Miazi on 5/9/23.
//

import UIKit

class ViewController: UIViewController {

    @IBOutlet var buttonClickMe: UIButton!
    @IBOutlet var textFieldUser: UITextField!
    override func viewDidLoad() {
        super.viewDidLoad()
        // Do any additional setup after loading the view.
        buttonClickMe.addTarget(self, action: #selector(onButtonClickMeTapped), for: .touchUpInside)
    }
    
    @objc func onButtonClickMeTapped(){
        //print("Button Clicked!!")
        // MARK: fetching the text the user typed...
        let text = textFieldUser.text
        
        //Unwrapping the optional text...
        if let unwrappedText = text{
            //print(unwrappedText)
            
            if(unwrappedText.isEmpty){ //The user didn't put anything...
                showErrorAlert()
            } else{ //The user put some texts...
                showAlertText(text: unwrappedText)
            }
        }
    }
    
    //MARK: Error alert...
    func showErrorAlert(){
        let alert = UIAlertController(
            title: "Error!", message: "Text Field must not be empty!", 
            preferredStyle: .alert
        )
        
        alert.addAction(UIAlertAction(title: "OK", style: .default))
        
        self.present(alert, animated: true)
    }
    
    //MARK: text alert...
    func showAlertText(text:String){
        let alert = UIAlertController(
            title: "You said:", 
            message: "\(text)", 
            preferredStyle: .alert
        )
        
        alert.addAction(UIAlertAction(title: "OK", style: .default))
        
        self.present(alert, animated: true)
    }

}


```



### Wrapping up: AppIcon

Before we complete the app, let's add an icon for the app. I generated a 1024x1024 pixels large icon:

![Educational illustration for iOS concept](</gitbook-assets/Screenshot 2023-05-09 at 7.05.08 PM (1).png>)

I will use it as my app icon for this app.

_You can generate AppIcons from here:_ [_https://www.appicon.co/_](https://www.appicon.co/)_._

Go to the project navigator from the left pane and click on Assets. In the middle pane, you will see the current assets are loaded. (There are no assets in your project yet). Click on AppIcon; you will see an empty canvas for a 1024x1024 image. Double-click on that, and select the icon from your files. Now your App Icon is set.

<figure><img src="/gitbook-assets/five (1) (1).gif" alt="Educational illustration for iOS concept"><figcaption></figcaption></figure>

Now, run the app again.

Now, go to the app drawer of the emulator. You will see that the icon for our 'App1' is set.

![Educational illustration for iOS concept](</gitbook-assets/Screenshot 2023-05-09 at 7.24.14 PM (1).png>)

Now, our first app 'App1' is complete!



### Reference Code and Video

[Download Project Archive](/gitbook-assets/App1_project.zip)

### TA Arpan created the video on this module for us:

<div style="position: relative; padding-bottom: 56.25%; height: 0; overflow: hidden; margin-bottom: 1.5rem; border-radius: 8px; border: 1px solid var(--rule);">
  <iframe src="https://www.youtube.com/embed/pEwhCh9j8wo" style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;" frameborder="0" allowfullscreen></iframe>
</div>

---

## Guided Practice Challenges

Before moving on to the next topic, try these low-stakes practice challenges in Xcode. They will build the exact muscle memory you need:

### Challenge 1: Experimentation
**The Scenario:** You've just learned about this topic.
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
