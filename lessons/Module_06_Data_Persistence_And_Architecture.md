# Module 06: Data Persistence And Architecture

## Table of Contents




### Notification Center

**Estimated effort:** 1-2 hours this topic
**Format:** Asynchronous online
**Prerequisites:** Previous iOS topics


**🎯 Topic Mission:** 
In this module, we will explore **Notification Center** and learn how to integrate it into our iOS applications. Your mission is to understand the mechanics behind this concept and write robust Swift code.


---

## Learning Objectives

By the end of this session, you will be able to:
1. Understand the core concepts of Notification Center.
2. Implement Notification Center in an Xcode project.
3. Apply best practices to ensure clean and maintainable code.

---

## The Story So Far...

We have been progressively building our knowledge of iOS and Swift. In this module, we will expand our toolkit by diving into Notification Center. 
Open your current Xcode project or start a new Playground to follow along with the hands-on material.

---

## Walkthrough: Exploring Notification Center

> 📁 **Target Project** — Follow along by building the mini-app presented in the steps below, or integrate these concepts into your own ongoing projects.

### Notification Center

**(Do not confuse it with the push notifications)**

NotificationCenter is a very useful utility for iOS to handle data independent of the lifecycles of the screens.

According to Apple Developer: It is _a notification dispatch mechanism that enables the broadcast of information to registered observers._ Sounds confusing? Luckily, it is not that confusing, though.

Simply put, NotificationCenter is a central dispatcher of data to broadcast data from one part of the app to another. A 'part' of an app could be any Swift class.

For example, there are two screens in an app. Screen2 takes text input from the user, and it has to send the text to Screen1 and display the text in a Label. Here is how it can be handled using a NotificationCenter:

* NotificationCenter works as a separate mediator. A class can post data to or observe data from the NotificationCenter.
* Screen2 can post the text. And Screen1 can observe the text.
* When Screen2 posts a new text, the NotificationCenter detects an update of data been made and broadcasts the notifications to all the observers of that particular data.
* At this point, Screen1, as an observer of that particular text, receives the notification that the text has been updated.
* Finally, Screen1 reacts to the notification and updates it's local UI elements accordingly, such as updating it's Label with the updated text.

So, let's build a small App to test it out.




### Add an Observer

We are sending data from the second screen to the first screen. So, we need to observe the Notification Center for any notifications sent from the Second Screen.

### Initializing the Notification Center

We initialize the notification center in the first screen by adding the following line of code in ViewController.swift:


```swift
//
//  ViewController.swift
//  App7
//
//  Created by Sakib Miazi on 5/22/23.
//

import UIKit

class ViewController: UIViewController {
    let firstScreen = FirstScreenView()
    
    //MARK: instantiating the Notification center...
    let notificationCenter = NotificationCenter.default
    
    //codes omitted...
}
```


### Setting up an observer

Then we should start observing for a particular notification. We will use the following method: `notificationCenter.addObserver(observer: Any, selector: Selector, name: NSNotification.Name?, object: Any?)`

So let's add the following lines of code in `viewDidLoad()` method:


```swift
class ViewController: UIViewController {

    //codes omitted...
    
    override func viewDidLoad() {
        //codes omitted...
        
        //MARK: observing text if it is updated in NotificationCenter...
        notificationCenter.addObserver(
            self, 
            selector: #selector(notificationReceivedForTextChanged(notification:)),
            name: Notification.Name("textFromSecondScreen"),
            object: nil)
    }
    //codes omitted...
    @objc func notificationReceivedForTextChanged(notification: Notification){
        firstScreen.labelReceivedText.text = (notification.object as! String)
    }
}
```


Here what we are doing is:

* Setting the observer to self. This means this screen is observing for a notification.
* We need to add a selector method to handle the data we get back as part of the notification. Here, we define `notificationReceivedForTextChanged()` method to handle the notification. Inside that method, you can see that we are setting the `labelReceivedText`'s text to the received object.
* We also need to give an identifier to the notification using the `name` parameter. We set the identifier as "textFromSecondScreen." It means I am just observing a notification of the name: "textFromSecondScreen."
* The object parameter is `nil`. It means the first screen will not send any object; it will just listen.

Here is the entire code of the ViewController.swift:


```swift
//
//  ViewController.swift
//  App7
//
//  Created by Sakib Miazi on 5/22/23.
//

import UIKit

class ViewController: UIViewController {

    let firstScreen = FirstScreenView()
    
    //MARK: instantiating the Notification center...
    let notificationCenter = NotificationCenter.default
    
    override func loadView() {
        view = firstScreen
    }
    
    override func viewDidLoad() {
        super.viewDidLoad()
        title = "First Screen"
        
        //MARK: buttonSend target...
        firstScreen.buttonFetch.addTarget(self, action: #selector(onButtonFetchTapped), for: .touchUpInside)
        
        //MARK: observing text if it is updated in NotificationCenter...
        //MARK: observing text if it is updated in NotificationCenter...
        notificationCenter.addObserver(
            self, 
            selector: #selector(notificationReceivedForTextChanged(notification:)),
            name: Notification.Name("textFromSecondScreen"),
            object: nil)
    }
    
    @objc func onButtonFetchTapped(){
        let secondScrren = SecondScreenViewController()
        navigationController?.pushViewController(secondScrren, animated: true)
    }
    
    @objc func notificationReceivedForTextChanged(notification: Notification){
        firstScreen.labelReceivedText.text = (notification.object as! String)
    }
}


```


Now, our first screen will listen to any notification named "textFromSecondScreen" and deal with it in `notificationReceivedForTextChanged()` method.



### App 7

We will build the following app in this module.

<figure><img src="/gitbook-assets/app7.1.1.1.gif" alt="Educational illustration for iOS concept"><figcaption></figcaption></figure>

Here,

* The first screen contains a button to fetch text from the second screen.
* If the user taps the button, it takes the user to the second screen.
* The second screen contains a TextField where a user can put some text. This screen also contains a button.
* If the user puts some text and taps the button, it returns to the first screen, and the user will see the text on the first screen.
* So, we have to send the text back to the first screen from the second screen. We will use the Notification Center to do that.
* The first screen will observe the text, and the second screen will post updates to the text.

### Creating a new app, App7

Now, let's create a new app in Xcode and name it 'App7.' Add the views and controllers of two screens:

![Educational illustration for iOS concept](</gitbook-assets/Screenshot 2023-05-22 at 5.02.27 PM (1).png>)

### First Screen:

#### FirstScreenView.swift


```swift
//
//  FirstScreen.swift
//  App7
//
//  Created by Sakib Miazi on 5/22/23.
//

import UIKit

class FirstScreenView: UIView {
    var buttonFetch:UIButton!
    var labelReceivedText:UILabel!

    override init(frame: CGRect) {
        super.init(frame: frame)
        self.backgroundColor = .white
        
        setupButtonFetch()
        setupLabelReceivedText()
        
        initConstraints()
    }
    
    //MARK: initializing UI elements...
    func setupButtonFetch(){
        buttonFetch = UIButton(type: .system)
        buttonFetch.setTitle("Fetch Text from Second Screen", for: .normal)
        buttonFetch.translatesAutoresizingMaskIntoConstraints = false
        self.addSubview(buttonFetch)
    }
    
    func setupLabelReceivedText(){
        labelReceivedText = UILabel()
        labelReceivedText.text = "Will receive text from Screen 2"
        labelReceivedText.translatesAutoresizingMaskIntoConstraints = false
        self.addSubview(labelReceivedText)
    }
    
    //MARK: setting up constraints...
    func initConstraints(){
        NSLayoutConstraint.activate([
            buttonFetch.topAnchor.constraint(equalTo: self.safeAreaLayoutGuide.topAnchor, constant: 32),
            buttonFetch.centerXAnchor.constraint(equalTo: self.safeAreaLayoutGuide.centerXAnchor),
            
            labelReceivedText.topAnchor.constraint(equalTo: buttonFetch.bottomAnchor, constant: 32),
            labelReceivedText.centerXAnchor.constraint(equalTo: self.safeAreaLayoutGuide.centerXAnchor),
        ])
    }
    
    //MARK: unused methods...
    required init?(coder: NSCoder) {
        fatalError("init(coder:) has not been implemented")
    }
    
}

```


#### ViewController.swift


```swift
//
//  ViewController.swift
//  App7
//
//  Created by Sakib Miazi on 5/22/23.
//

import UIKit

class ViewController: UIViewController {

    let firstScreen = FirstScreenView()
    override func loadView() {
        view = firstScreen
    }
    
    override func viewDidLoad() {
        super.viewDidLoad()
        title = "First Screen"
        
        //MARK: buttonSend target...
        firstScreen.buttonFetch
            .addTarget(self, action: #selector(onButtonFetchTapped), for: .touchUpInside)
        
    }
    
    @objc func onButtonFetchTapped(){
        let secondScrren = SecondScreenViewController()
        navigationController?.pushViewController(secondScrren, animated: true)
    }
}
```


### Second Screen:

#### SecondScreenView.swift


```swift
//
//  SecondScreenView.swift
//  App7
//
//  Created by Sakib Miazi on 5/22/23.
//

import UIKit

class SecondScreenView: UIView {
    
    var labelInfo: UILabel!
    var textFieldSendBack: UITextField!
    var buttonSendBack: UIButton!

    override init(frame: CGRect) {
        super.init(frame: frame)
        
        self.backgroundColor = .white
        
        setupLabelInfo()
        setupTextFieldSendBack()
        setupButtonSendBack()
        
        initConstraints()
    }
    
    //MARK: setting up UI elements...
    func setupLabelInfo(){
        labelInfo = UILabel()
        labelInfo.text = "Type to send back:"
        labelInfo.translatesAutoresizingMaskIntoConstraints = false
        self.addSubview(labelInfo)
    }
    func setupTextFieldSendBack(){
        textFieldSendBack = UITextField()
        textFieldSendBack.placeholder = "Put text to send back to screen 1"
        textFieldSendBack.translatesAutoresizingMaskIntoConstraints = false
        self.addSubview(textFieldSendBack)
    }
    func setupButtonSendBack(){
        buttonSendBack = UIButton(type: .system)
        buttonSendBack.setTitle("Send Back", for: .normal)
        buttonSendBack.translatesAutoresizingMaskIntoConstraints = false
        self.addSubview(buttonSendBack)
    }
    
    //MARK: initializing constraints...
    func initConstraints(){
        NSLayoutConstraint.activate([
            labelInfo.topAnchor.constraint(equalTo: self.safeAreaLayoutGuide.topAnchor, constant: 32),
            labelInfo.centerXAnchor.constraint(equalTo: self.safeAreaLayoutGuide.centerXAnchor),
            
            textFieldSendBack.topAnchor.constraint(equalTo: labelInfo.bottomAnchor, constant: 16),
            textFieldSendBack.centerXAnchor.constraint(equalTo: self.safeAreaLayoutGuide.centerXAnchor),
            
            buttonSendBack.topAnchor.constraint(equalTo: textFieldSendBack.bottomAnchor, constant: 8),
            buttonSendBack.centerXAnchor.constraint(equalTo: self.safeAreaLayoutGuide.centerXAnchor),
        ])
    }
    
    required init?(coder: NSCoder) {
        fatalError("init(coder:) has not been implemented")
    }
    
}

```


#### SecondScreenViewController.swift


```swift
//
//  SecondScreenViewController.swift
//  App7
//
//  Created by Sakib Miazi on 5/22/23.
//

import UIKit

class SecondScreenViewController: UIViewController {
    let secondScreen = SecondScreenView()
    
    override func loadView() {
        view = secondScreen
    
    }
    
    override func viewDidLoad() {
        super.viewDidLoad()
        title = "Second Screen"
        
        secondScreen.buttonSendBack
            .addTarget(self, action: #selector(onButtonSendBackTapped), for: .touchUpInside)
        
    }
    
    @objc func onButtonSendBackTapped(){
        if let text = secondScreen.textFieldSendBack.text{
            //Send text to First Screen...
        }else{
            //Alert invalid input...
        }
        
    }

}
```




### Posting Data to Notification Center

Now, let's open up the SecondScreenViewController.swift file. We need to initialize the Notification Center here as well. Let's add the following code:


```swift
//
//  SecondScreenViewController.swift
//  App7
//
//  Created by Sakib Miazi on 5/22/23.
//

import UIKit

class SecondScreenViewController: UIViewController {
    //codes omitted...
    
    //MARK: instantiating the Notification center...
    let notificationCenter = NotificationCenter.default
    
   //codes omitted...

}

```


### Posting data to Notification Center

Now, when the user puts some text in `textFieldSendBack`, and taps `buttonSendBack`, we need to fetch the text and post the text to Notification Center. So, let's write the following codes in `onButtonSendBackTapped()` method:


```swift
//
//  SecondScreenViewController.swift
//  App7
//
//  Created by Sakib Miazi on 5/22/23.
//

import UIKit

class SecondScreenViewController: UIViewController {
    //codes omitted...
    
    override func viewDidLoad() {
        super.viewDidLoad()
        //codes omitted...
        
        secondScreen.buttonSendBack.addTarget(self, action: #selector(onButtonSendBackTapped), for: .touchUpInside)
        
    }
    
    @objc func onButtonSendBackTapped(){
        if let text = secondScreen.textFieldSendBack.text{
            //MARK: posting text to NotificationCenter...
            notificationCenter.post(
                name: Notification.Name("textFromSecondScreen"),
                object: text)
            navigationController?.popViewController(animated: true)
        }else{
            //Alert invalid input...
        }
        
    }

}

```


In `notificationCenter.post()` method, we are passing two parameters.

* **name:** The same identifier we used to observe the data.
* **object:** The object we are sending to Notification Center. Here, the object is the text the user puts in.

So now let's look into the whole code of SecondScreenViewController.swift:


```swift
//
//  SecondScreenViewController.swift
//  App7
//
//  Created by Sakib Miazi on 5/22/23.
//

import UIKit

class SecondScreenViewController: UIViewController {
    let secondScreen = SecondScreenView()
    
    //MARK: instantiating the Notification center...
    let notificationCenter = NotificationCenter.default
    
    override func loadView() {
        view = secondScreen
    
    }
    
    override func viewDidLoad() {
        super.viewDidLoad()
        title = "Second Screen"
        
        secondScreen.buttonSendBack.addTarget(self, action: #selector(onButtonSendBackTapped), for: .touchUpInside)
        
    }
    
    @objc func onButtonSendBackTapped(){
        if let text = secondScreen.textFieldSendBack.text{
            //MARK: posting text to NotificationCenter...
            notificationCenter.post(
                name: Notification.Name("textFromSecondScreen"),
                object: text)
            navigationController?.popViewController(animated: true)
        }else{
            //Alert invalid input...
        }
        
    }

}

```


Now let's run the app.

<figure><img src="/gitbook-assets/app7.1.1.1.gif" alt="Educational illustration for iOS concept"><figcaption></figcaption></figure>

### Notes:

* We can use Notification Center to send data between screens.
* We did not use delegates here. The observer method takes care of that.
* The Notification Center is just like a separate highway of data, independent of the lifecycle of the screens.
* It is a great way of data exchange, where you do not have to worry about handling data while carefully taking care of the Navigation Stack.

**There is a caveat, though. What if I want to send data from the first screen to the second screen?**

* The Notification Center is Asynchronous, so a real-time data transfer is desirable (almost always, the data transfer happens in real-time), yet not guaranteed.
* The Notification Center can broadcast data as long as the observer is alive. It cannot send the data before the observer is created or after it is killed.
* You need to set an observer before you send the data. So, when you create the second screen from the first screen, you logically (according to the lifecycle of a screen) post the data from the first screen even before the second screen is created, and the observer is set. So, even if the data is posted, the observer from the second screen can't receive it.
* Therefore, to send data from the parent screen to a child screen while creating the child screen, you should use the old way of sending data; usually Notification Center can't deliver the data.



### Defining the names (identifiers) of the Notifications in a Better Way

In real life, the Notification Center is used very frequently, especially when we fetch data from the internet and wait for data to update. Oftentimes, it's pretty common to create tens of observers in a single app. So, just writing the names/identifiers of the notifications, as we did before, is not a good way of dealing with it. If the names do not match on both sides, notifications won't work. So, keeping the names in a separate class as static variables is better.

So, let's create a new Swift file (not a Cocoa touch class) called NotificationNames.swift.

![Educational illustration for iOS concept](</gitbook-assets/Screenshot 2023-05-22 at 7.42.36 PM (1).png>)

Write the following code inside it:

```swift
//
//  NotificationNames.swift
//  App7
//
//  Created by Sakib Miazi on 5/22/23.
//

import Foundation
extension Notification.Name{
    static let textFromScondScreen = Notification.Name("textFromSecondScreen")
}
```

Here we are extending `Notification.Name` class, and defining new static names inside it. We used only one observer with the identity/name "textFromSecondScreen." `textFromSecondScreen` static constant is holding that identifier. So, now we will update the `addObserver()` and `post()` methods as follows:

### addObserver() method:

**Previously we had:**

```swift
//MARK: observing text if it is updated in NotificationCenter...
notificationCenter.addObserver(
    self, selector: #selector(notificationReceivedForTextChanged(notification:)),
    name: Notification.Name("textFromSecondScreen"),
    object: nil)
```

**We can now write:**

```swift
//MARK: observing text if it is updated in NotificationCenter...
notificationCenter.addObserver(
    self, selector: #selector(notificationReceivedForTextChanged(notification:)),
    name: .textFromScondScreen,
    object: nil)
```

### post() method:

**Previously we had:**

```swift
//MARK: posting text to NotificationCenter...
notificationCenter.post(
    name: Notification.Name("textFromSecondScreen"),
    object: text)
```

#### Now we can write:

```swift
//MARK: posting text to NotificationCenter...
notificationCenter.post(
    name: .textFromScondScreen,
    object: text)
```

_**This way, we can easily store multiple identifiers/names without worrying about fogetting and mismatching them.**_



### Reference Code

[Download Project Archive](/gitbook-assets/App7 (1).zip)

---

## Guided Practice Challenges

Before moving on to the next topic, try these low-stakes practice challenges in Xcode. They will build the exact muscle memory you need:

### Challenge 1: Experimentation
**The Scenario:** You've just learned about Notification Center.
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


### Clean Code & Async

**Estimated effort:** 1-2 hours this topic
**Format:** Asynchronous online
**Prerequisites:** Previous iOS topics


**🎯 Topic Mission:** 
In this module, we will explore **Clean Code & Async** and learn how to integrate it into our iOS applications. Your mission is to understand the mechanics behind this concept and write robust Swift code.


---

## Learning Objectives

By the end of this session, you will be able to:
1. Understand the core concepts of Clean Code & Async.
2. Implement Clean Code & Async in an Xcode project.
3. Apply best practices to ensure clean and maintainable code.

---

## The Story So Far...

We have been progressively building our knowledge of iOS and Swift. In this module, we will expand our toolkit by diving into Clean Code & Async. 
Open your current Xcode project or start a new Playground to follow along with the hands-on material.

---

## Walkthrough: Exploring Clean Code & Async

> 📁 **Target Project** — Follow along by building the mini-app presented in the steps below, or integrate these concepts into your own ongoing projects.

### Writing clean code for Asynchronous operations

In this section, we will rewrite the code for App 11 (JSON API). We will have options for displaying, adding, deleting, and editing contacts using our same API (please refer to:[11.1.-the-json-api-for-the-contact-app.md](../11.-working-with-json/11.1.-the-json-api-for-the-contact-app.md "mention")). We took small steps in[useful-extra-11.8.-decluttering-codes-from-view-controller.md](../11.-working-with-json/useful-extra-11.8.-decluttering-codes-from-view-controller.md "mention") section to separate the API calls from the control code. This time, we will break the chain of nested asynchronous API calls with async-await blocks of code to make our code cleaner.&#x20;

### Asynchronous calls

So far, what we have seen in our API calls is that, for a sequence of asynchronous tasks, we must wait for the previous task to complete before executing the next task. We wrote _**spaghetti**_ code there and made the next API call from the callback of the first API call (if the response was a 200-level code, refer to [11.5.-app11-add-a-new-contact.md](../11.-working-with-json/11.5.-app11-add-a-new-contact.md "mention") ). However, it renders our code largely unusable for future use. What if we could write the code such that we could call the async calls one after another, but the code would not execute in parallel? Wouldn't it be great to instruct the code to wait for the call to complete and then move to the next line? That way, we can keep our code cleaner and highly reusable for future use. &#x20;

Let's examine an example using pseudocode.

So far, we have dealt with sequential API calls by calling the second API from within the callback of the first API. For example, in our contacts API,  to add a new contact and display the updated list of contacts, what we are doing is:


```swift
//MARK: It is a pseudocode, not Swift!!!

func addANewContact(contact:Contact){
    callAddContactAPI(){ in response //This is async callback
        if response.statusCode == 200 {
            //A ton of other code....
            callGetAllContactsAPI() // The next API call
            //A ton of remaining code....
        }
    }
}
```


In this pseudocode, when we call the callAddContactAPI() API, we must also call the callGetAllContactsAPI() API from its callback. It creates a spaghetti of code. Think about 3 or more sequential calls; How complex would that be!

If we could write it the following way, would you feel it's better?

```swift
//MARK: It is a pseudocode, not Swift!!!

func addANewContact(contact:Contact){
    await callAddContactAPI() //stop and wait until the call finishes
    await callGetAllContactsAPI() //when done it will have the updated list
}
```

See how much more readable and usable it becomes!

So, we will do the same for App 11 here.

### Tasks with async await

Let's look at the following Swift code (you can run it in a Playground):


```swift
import UIKit

import Foundation

// 1. An async function that waits and returns a String
func delayedGreeting() async -> String {
    try? await Task.sleep(nanoseconds: 5_000_000_000) // Suspend for 5 seconds
    return "Hello from the asynchronous world, I waited 5 seconds to print this!"
}

// 2. Start the Task in a synchronous context (e.g., main function)
func start() {
    Task { // Creates an asynchronous context
        print("Starting an asynchronous task...")
        let greeting = await delayedGreeting() // Await the result
        print(greeting)
    }
    print("Hello from synchronous world, I don't wait for the asyncs!")
}

start()
```


Let's look at what we have here:

1. On lines 6 through 9, we are writing a function that will asynchronously suspend for 5 seconds.
   1. To be able to run this asynchronous task and wait for it to complete, we need to  call this function from a special block named `Task{...}` .
2. On lines 13 to 17, we put the Task block.
   1. On line 14, we print the string, "Starting an asynchronous task..." to denote the start of the async task.
   2. On line 15, we are calling the async task, which will wait for the task to complete and fetch the greeting from the function. **`await`** notation means send this call to the background and wait in the scope of the Task block.
   3. On line 16, we print the greeting after the wait is over.
3. On line 18, outside the Task block, we print, "Hello from synchronous world, I don't wait for the asyncs!"

Now, if we run the code, you will see the following:

<figure><img src="/gitbook-assets/one (5).gif" alt="Educational illustration for iOS concept"><figcaption></figcaption></figure>

Now, if we change the code like this:


```swift
import UIKit

import Foundation

// 1. An async function that waits and returns a String
func delayedGreeting() async -> String {
    try? await Task.sleep(nanoseconds: 5_000_000_000) // Suspend for 5 seconds
    return "Hello from the asynchronous world, I waited 5 seconds to print this!"
}

// 2. Start the Task in a synchronous context (e.g., main function)
func start() {
    Task { // Creates an asynchronous context
        print("Starting an asynchronous task...")
        let greeting = await delayedGreeting() // Await the result
        print(greeting)
        print("Now, I wait for the calls to complete!")
    } 
}

start()
```


We removed the print outside the Task block and put a new print statement in the block. It will ouput:

<pre><code>Starting an asynchronous task...
Hello from the asynchronous world, I waited 5 seconds to print this!
<a data-footnote-ref href="#user-content-fn-1">Now, I wait for the calls to complete!</a>
</code></pre>

So, within the **Task{...}** block, all asynchronous calls are sequenced one after another! For better clarity, run the following code in your playground:


```swift
import UIKit

import Foundation

// 1. An async function that waits and returns a String
func delayedGreeting5() async -> String {
    try? await Task.sleep(nanoseconds: 5_000_000_000) // Suspend for 5 seconds
    return "Hello from the asynchrnous world, I waited 5 seconds to print this!"
}
// 2. An async function that waits and returns a String
func delayedGreeting3() async -> String {
    try? await Task.sleep(nanoseconds: 3_000_000_000) // Suspend for 5 seconds
    return "Hello from the asynchrnous world, I waited 3 seconds to print this!"
}

// 2. Start the Task in a synchronous context (e.g., main function)
func start() {
    Task { // Creates an asynchronous context
        print("Starting an asynchronous task...")
        let greeting5 = await delayedGreeting5() // Await the result
        print(greeting5)
        let greeting3 = await delayedGreeting3() // Await the result
        print(greeting3)
    }   
}
start()
```


### Important notes:

1. When we define an async function in Swift, we write async notation on the declaration.
2. When we call an async function, we call it using await notation.
3. **An await call can only be called from either another async function or from inside a Task{} block.**
   1. There are other ways of handling and sequencing async calls; please do your own research on them. This is the simplest way to start with async sequencing.

[^1]: The changed statement!



## Table of Contents

{{< section >}}

---

## Guided Practice Challenges

Before moving on to the next topic, try these low-stakes practice challenges in Xcode. They will build the exact muscle memory you need:

### Challenge 1: Experimentation
**The Scenario:** You've just learned about Clean Code & Async.
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


### Writing Clean Code For Asynchronous Operations

**Estimated effort:** 1-2 hours this topic
**Format:** Asynchronous online
**Prerequisites:** Previous iOS topics


**🎯 Topic Mission:** 
In this module, we will explore **1. Writing Clean Code For Asynchronous Operations** and learn how to integrate it into our iOS applications. Your mission is to understand the mechanics behind this concept and write robust Swift code.


---

## Learning Objectives

By the end of this session, you will be able to:
1. Understand the core concepts of 1. Writing Clean Code For Asynchronous Operations.
2. Implement 1. Writing Clean Code For Asynchronous Operations in an Xcode project.
3. Apply best practices to ensure clean and maintainable code.

---

## The Story So Far...

We have been progressively building our knowledge of iOS and Swift. In this module, we will expand our toolkit by diving into 1. Writing Clean Code For Asynchronous Operations. 
Open your current Xcode project or start a new Playground to follow along with the hands-on material.

---

## Walkthrough: Exploring 1. Writing Clean Code For Asynchronous Operations

> 📁 **Target Project** — Follow along by building the mini-app presented in the steps below, or integrate these concepts into your own ongoing projects.

### Decluttering our App11 (Contacts App with JSON)

So far in [useful-extra-11.8.-decluttering-codes-from-view-controller.md](../../11.-working-with-json/useful-extra-11.8.-decluttering-codes-from-view-controller.md "mention") section, we learned how to write protocols and use extensions to modularize your code. Let's start there.&#x20;

So far, we have the following structure of the project:

* App 11
  * Data Models (Directory)
    * Contact.swift
    * ContactNames.swift
  * Contact API Coinfigs (Directory)
    * APIConfigs.swift
    * ContactsProtocol.swift
  * Edit Screen (Directory) _—_ _Added later for completeness_
    * Views (Directory)&#x20;
      * EditScreenView.swift
    * EditViewController.swift
  * Main Screen (Directory)
    * Views (Directory)
      * ContactsTableViewCell.swift
      * MainScreenView.swift
    * ContactListTableViewManager.swift _— Added later with extension magic!_
    * ContactsAPICalls.swift
    * ContactsViewController.swift — _Changed from ViewController using SceneDelegate_
  * _AppDelegate.swift_
  * _SceneDelegate.swift_

### Updating Contact API Protocol code

To be able to accommodate the async-await calls to remove the spaghetti code, we need a few changes in our Contact API protocol in ContactsProtocol.swift file:

```swift
import Foundation

protocol ContactsProtocol{
    func getAllContacts() async -> Bool
    func addANewContact(contact: Contact) async -> Bool
    func getContactDetails(name: String) async -> Contact?
    func deleteContact(name: String) async -> Bool
}

```

The basic differences here from before are:

1. We made all the API call functions asynchronous by adding the _**async**_ notation.&#x20;
2. We are also making the functions return something (Bool, Contact, etc.) so that it becomes easier when we sequence them from the controller.

### Making API calls async

So we will now rewrite (a little) the current code for the API calls (getall, add, delete, getdetails) to be able to call them asynchronously.

#### getAllContacts()

For example, the previous code for the getall API call in ContactAPICalls.swift file was:


```swift
//MARK: get all contacts call: getall endpoint...
func getAllContacts(){
    if let url = URL(string: APIConfigs.baseURL + "getall"){
        AF.request(url, method: .get).responseData(completionHandler: { response in
            //MARK: retrieving the status code...
            let status = response.response?.statusCode
            
            switch response.result{
            case .success(let data):
                //MARK: there was no network error...
                
                //MARK: status code is Optional, so unwrapping it...
                if let uwStatusCode = status{
                    switch uwStatusCode{
                        case 200...299:
                        //MARK: the request was valid 200-level...
                            self.contactNames.removeAll()
                            let decoder = JSONDecoder()
                            do{
                                let receivedData =
                                    try decoder
                                    .decode(ContactNames.self, from: data)
                                    
                                for item in receivedData.contacts{
                                    self.contactNames.append(item.name)
                                }
                                self.mainScreen.tableViewContacts.reloadData()
                            }catch{
                                print("JSON couldn't be decoded.")
                            }
                            break
                
                        case 400...499:
                        //MARK: the request was not valid 400-level...
                            print(data)
                            break
                
                        default:
                        //MARK: probably a 500-level error...
                            print(data)
                            break
                
                    }
                }
                break
                
            case .failure(let error):
                //MARK: there was a network error...
                print(error)
                break
            }
        })
    }
}
```


Here, our callback was on line 4, **completionHandler**. This closure gets returned when the network call is complete.&#x20;

Now, we need to get rid of the completionHandler since we will be managing the asynchronous operations ourselves.&#x20;

So, the updated code becomes something like:


```swift
//MARK: get all contacts...
func getAllContacts() async -> Bool{
    if let url = URL(string: APIConfigs.baseURL + "getall") {
        
        let response = await AF.request(url, method: .get)
            .serializingData()
            .response
        
        let statusCode = response.response?.statusCode
        
        switch response.result {
        case .success(let data):
            if let uwStatusCode = statusCode {
                switch uwStatusCode {
                case 200...299:
                    //MARK: the request was valid 200-level...
                    self.contactNames.removeAll()
                    let decoder = JSONDecoder()
                    do {
                        let receivedData = try decoder.decode(ContactNames.self, from: data)
                        for item in receivedData.contacts {
                            self.contactNames.append(item.name)
                        }
                        return true
                    } catch {
                        print("JSON couldn't be decoded.")
                        return false
                    }
                    
                case 400...499:
                    //MARK: the request was not valid 400-level...
                    print(data)
                    return false
                    
                default:
                    //MARK: probably a 500-level error...
                    print(data)
                    return false
                }
            }
            
        case .failure(let error):
            //MARK: there was a network error...
            print(error)
            return false
        }
    } else {
        return false
    }
    return false
}
```


Let's compare the two codes and check what happened here.

1. Instead of using the completionHandler, we are separating the AlamoFire call on line 5 with the await notation and retrieving the response asynchronously.
   1. Since we are sequencing the call, **await** will suspend execution until it receives the response.
2. Then, we retrieve the status code from the response on line 9, and subsequently write a switch-case block to filter cases with different status codes.
   1. We only return **true** if it is in the 200-level block. Every other case returns **false.**

It already looks less cluttered!&#x20;

### Control Code

Now, let's see how we can call getAllContacts using the Task{} block from the ViewController. Let's check the corresponding code in ContactsViewController.swift file:


```swift
import UIKit
import Alamofire

class ContactsViewController: UIViewController {
    
    //MARK: list to display the contact names in the TableView...
    var contactNames = [String]()
    
    let notificationCenter = NotificationCenter.default
    
    let mainScreen = MainScreenView()
    
    override func loadView() {
        view = mainScreen
    }
    
    override func viewDidLoad() {
        super.viewDidLoad()
        
        title = "Contacts JSON API"
        
        //Code reducted...
        
        //MARK: get all contact names when the main screen loads...
        callGetAllContacts()
        
        //Code reducted...
    }
    
    func callGetAllContacts(){
        Task{
            let getallSuccess = try await getAllContacts()
            if getallSuccess{
                mainScreen.tableViewContacts.reloadData()
            }
        }
    }
    
}
```


In the above code:

1. When the app loads, we want to load the list of current contacts, so we call callGetAllContacts() function on line 25. Lines 30 through 37 show the implementation of the function.
   1. You can see we have a Task{} block. Inside the block, everything will sequentially wait.
   2. On line 32, we call the API and wait for it to return the result. If the response was of 200-level, we reload the data in our table view.



### Decluttering continues...

Now we will look at an example where we will edit a contact. We would need to make two API calls sequentially: delete the contact, and then add a new contact with updated data.

For the sake of simplicity in this tutorial, I will skip most of the code; however, I will discuss the most important parts.

Let's look at the updated delete and add contact API calls:

#### addANewContact(contact: Contact)


```swift
//MARK: add a new contact call: add endpoint...
func addANewContact(contact: Contact) async -> Bool{
    if let url = URL(string: APIConfigs.baseURL + "add") {
        
        let response = await AF.request(
            url,
            method: .post,
            parameters: [
                "name": contact.name,
                "email": contact.email,
                "phone": contact.phone
            ]
        )
        .serializingData()
        .response
        
        let statusCode = response.response?.statusCode
        
        switch response.result {
        case .success(let data):
            if let uwStatusCode = statusCode {
                switch uwStatusCode {
                case 200...299:
                    return true
                    
                case 400...499:
                    return false
                    
                default:
                    return false
                }
            }
            return false
            
        case .failure(_):
            return false
        }
    } else {
        return false
    }
}
```


#### deleteContact(name: String)


```swift
//MARK: delete the selected contact...
func deleteContact(name: String) async -> Bool{
    
    if let url = URL(string: APIConfigs.baseURL + "delete") {
        
        let response = await AF.request(
            url,
            method: .get,
            parameters: ["name": name]
        )
        .serializingData()
        .response
        
        let statusCode = response.response?.statusCode
        
        switch response.result {
        case .success(let data):
            if let uwStatusCode = statusCode {
                switch uwStatusCode {
                case 200...299:
                    return true
                    
                case 400...499:
                    return false
                    
                default:
                    return false
                }
            }
            return false
            
        case .failure(_):
            return false
        }
    } else {
        return false
    }
}
```


Both calls were defined as asynchronous calls. Now, let's look into the code snippet where the user taps on the save button from the edit screen:


```swift
@objc func editContactSaveButtonPressed(notification: Notification){
    let tuple: (Contact, String) = notification.object as! (Contact, String)
    Task{
        let deleteSuccess = try await deleteContact(name: tuple.1)
        if deleteSuccess{
            let addSuccess = try await addANewContact(contact: tuple.0)
            if addSuccess{
                self.navigationController?.popViewController(animated: true)
                self.callGetAllContacts()
            }
        }
    }
}
```


In the above code:

1. I am sending a notification from the Edit Screen to the Main Screen to indicate that the user has tapped the Save button. The object in the notification contained a tuple that holds two values: the updated contact and the name from the old contact.
2. On lines 3 through 12, I am writing a Task{} block which enables sequential async operations.&#x20;
   1. First, on line 4, I am calling the delete API and waiting for it to complete.
   2. If the deletion is successful, I then call the add API.
   3. When deletion becomes successful, then I call the getall API and refresh the list.

The code looks certainly more readable now!

Please download the whole project and study that to understand the concepts.



### Reference Code

[Download Project Archive](/gitbook-assets/App 11 modular async.zip)

---

## Guided Practice Challenges

Before moving on to the next topic, try these low-stakes practice challenges in Xcode. They will build the exact muscle memory you need:

### Challenge 1: Experimentation
**The Scenario:** You've just learned about 1. Writing Clean Code For Asynchronous Operations.
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
