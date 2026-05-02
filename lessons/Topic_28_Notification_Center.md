# Notification Center


**Estimated effort:** 1-2 hours this topic
**Format:** Asynchronous online
**Prerequisites:** Previous iOS topics

{< hint info >}
**🎯 Topic Mission:** 
In this module, we will explore **Notification Center** and learn how to integrate it into our iOS applications. Your mission is to understand the mechanics behind this concept and write robust Swift code.
{< /hint >}

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

# 7. Notification Center

<mark style="color:purple;">**(Do not confuse it with the push notifications)**</mark>

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




<!-- Merged from 7.1.-add-an-observer.md -->

# 7.1. Add an Observer

We are sending data from the second screen to the first screen. So, we need to observe the Notification Center for any notifications sent from the Second Screen.

### Initializing the Notification Center

We initialize the notification center in the first screen by adding the following line of code in ViewController.swift:

{% code lineNumbers="true" %}
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
{% endcode %}

### Setting up an observer

Then we should start observing for a particular notification. We will use the following method: `notificationCenter.addObserver(observer: Any, selector: Selector, name: NSNotification.Name?, object: Any?)`

So let's add the following lines of code in `viewDidLoad()` method:

{% code lineNumbers="true" %}
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
{% endcode %}

Here what we are doing is:

* Setting the observer to self. This means this screen is observing for a notification.
* We need to add a selector method to handle the data we get back as part of the notification. Here, we define `notificationReceivedForTextChanged()` method to handle the notification. Inside that method, you can see that we are setting the `labelReceivedText`'s text to the received object.
* We also need to give an identifier to the notification using the `name` parameter. We set the identifier as "textFromSecondScreen." It means I am just observing a notification of the name: "textFromSecondScreen."
* The object parameter is `nil`. It means the first screen will not send any object; it will just listen.

Here is the entire code of the ViewController.swift:

{% code lineNumbers="true" %}
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
{% endcode %}

Now, our first screen will listen to any notification named "textFromSecondScreen" and deal with it in `notificationReceivedForTextChanged()` method.



<!-- Merged from 7.1.-app-7.md -->

# 7.1. App 7

We will build the following app in this module.

<figure><img src="/gitbook-assets/app7.1.1.1.gif" alt=""><figcaption></figcaption></figure>

Here,

* The first screen contains a button to fetch text from the second screen.
* If the user taps the button, it takes the user to the second screen.
* The second screen contains a TextField where a user can put some text. This screen also contains a button.
* If the user puts some text and taps the button, it returns to the first screen, and the user will see the text on the first screen.
* So, we have to send the text back to the first screen from the second screen. We will use the Notification Center to do that.
* The first screen will observe the text, and the second screen will post updates to the text.

### Creating a new app, App7

Now, let's create a new app in Xcode and name it 'App7.' Add the views and controllers of two screens:

![](</gitbook-assets/Screenshot 2023-05-22 at 5.02.27 PM (1).png>)

### First Screen:

#### FirstScreenView.swift

{% code lineNumbers="true" %}
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
{% endcode %}

#### ViewController.swift

{% code lineNumbers="true" %}
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
{% endcode %}

### Second Screen:

#### SecondScreenView.swift

{% code lineNumbers="true" %}
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
{% endcode %}

#### SecondScreenViewController.swift

{% code lineNumbers="true" %}
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
{% endcode %}



<!-- Merged from 7.2.-posting-data-to-notification-center.md -->

# 7.2. Posting Data to Notification Center

Now, let's open up the SecondScreenViewController.swift file. We need to initialize the Notification Center here as well. Let's add the following code:

{% code lineNumbers="true" %}
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
{% endcode %}

### Posting data to Notification Center

Now, when the user puts some text in `textFieldSendBack`, and taps `buttonSendBack`, we need to fetch the text and post the text to Notification Center. So, let's write the following codes in `onButtonSendBackTapped()` method:

{% code lineNumbers="true" %}
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
{% endcode %}

In `notificationCenter.post()` method, we are passing two parameters.

* **name:** The same identifier we used to observe the data.
* **object:** The object we are sending to Notification Center. Here, the object is the text the user puts in.

So now let's look into the whole code of SecondScreenViewController.swift:

{% code lineNumbers="true" %}
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
{% endcode %}

Now let's run the app.

<figure><img src="/gitbook-assets/app7.1.1.1.gif" alt=""><figcaption></figcaption></figure>

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



<!-- Merged from 7.3.-defining-the-names-identifiers-of-the-notifications-in-a-better-way.md -->

# 7.3. Defining the names (identifiers) of the Notifications in a Better Way

In real life, the Notification Center is used very frequently, especially when we fetch data from the internet and wait for data to update. Oftentimes, it's pretty common to create tens of observers in a single app. So, just writing the names/identifiers of the notifications, as we did before, is not a good way of dealing with it. If the names do not match on both sides, notifications won't work. So, keeping the names in a separate class as static variables is better.

So, let's create a new Swift file (not a Cocoa touch class) called NotificationNames.swift.

![](</gitbook-assets/Screenshot 2023-05-22 at 7.42.36 PM (1).png>)

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



<!-- Merged from 7.4.-reference-code.md -->

# 7.4. Reference Code

{% file src="/gitbook-assets/App7 (1).zip" %}

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

