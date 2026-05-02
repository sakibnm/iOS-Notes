---
title: "3.3. Send data back from Screen 2 to Screen 1"
weight: 810
---

**Estimated effort:** 1-2 hours this topic
**Format:** Asynchronous online
**Prerequisites:** Previous iOS topics

{< hint info >}
**🎯 Topic Mission:** 
In this module, we will explore **3.3. Send data back from Screen 2 to Screen 1** and learn how to integrate it into our iOS applications. Your mission is to understand the mechanics behind this concept and write robust Swift code.
{< /hint >}

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

# 3.3. Send data back from Screen 2 to Screen 1

So, here is the goal for the extension of our current app:

* We will add a PickerView (selects one from a list of options) to the second screen (ShowViewController).
* The PickerView will show the user a list of moods: Happy, Meh, and Sad.
* The user selects a mood and sends the mood back to the first screen (ViewController).
* The first screen receives the mood and displays a corresponding image in an ImageView.

### Updating the screens with new UI elements.

**On ViewController,** we will add a new Label and an ImageView, as follows:

{% code lineNumbers="true" %}
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
{% endcode %}

The `labelMood` will show the mood the user selected on ShowViewController, and the ImageView `imageMood` will show an image corresponding to the mood.

**Now on ShowViewController,** we will add a new Label, a PickerView, and a Button, as follows:

{% code lineNumbers="true" %}
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
{% endcode %}

Here, `labelMoodInstructions` shows the message: "How are you feeling today?"

Then we place the `moodPicker` and finally put `buttonSendMood` at the bottom.

If we run the app now, we will see:

<figure><img src="/gitbook-assets/nine (1).gif" alt=""><figcaption></figcaption></figure>

Here, we do not see the two elements we added to ViewController, because `labelMood` and `imageMood` doesn't have anything to display.

On ShowViewController, we see there is an empty `moodPicker` and the newly added `buttonSendMood`.




<!-- Merged from 3.4.-send-data-back-from-screen-2-to-screen-1-part-2-uipickerview.md -->

# 3.3.1. Send data back from Screen 2 to Screen 1: UIPickerView

<figure><img src="/gitbook-assets/Screenshot 2023-05-11 at 12.13.48 PM (1).png" alt=""><figcaption></figcaption></figure>

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

We will choose the second option, where we can keep the code separated. So, let's implement or adopt the methods in the protocols and define them. You need to write code for three methods to properly set up the `moodPicker:`

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

{% code lineNumbers="true" %}
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
{% endcode %}

{% code lineNumbers="true" %}
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
{% endcode %}



<!-- Merged from 3.5.-send-data-back-from-screen-2-to-screen-1-part-3-delegating-to-viewcontroller.md -->

# 3.3.2. Send data back from Screen 2 to Screen 1: delegating to ViewController

Now, let's enable the action for `buttonSendMood` in ShowViewController.swift file. So let's update `viewDidLoad()` function and add a new selector method `onSendButtonTapped()`:

{% code lineNumbers="true" %}
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
{% endcode %}

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

{% code lineNumbers="true" %}
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
{% endcode %}

### Doing delegated tasks in ViewController

**Now, we need to add a method in ViewController** to conduct the delegated tasks from ShowViewController:

{% code lineNumbers="true" %}
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
{% endcode %}

Here, `delegateButtonSendMood(mood:String)` receives a String (mood) as a parameter. Let's just print the mood for now.

Now, let's switch back to ShowViewController. **We now need to call this `delegateButtonSendMood(mood:String)` method when the user taps on `onSendMoodButton`.** We can write:

{% code lineNumbers="true" %}
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
{% endcode %}

Since the instance of ShowViewController gets populated with the variable `delegate` already set to the instance of ViewController, we can call `delegateButtonSendMood()` method from ShowViewController. We are calling the method with `selectedMood` as the parameter. Now, let's run the app and check if ViewController can print the mood.

<figure><img src="/gitbook-assets/ten (1).gif" alt=""><figcaption></figcaption></figure>

We are yet to do another task. We need to pop the ShowViewController after we click on `buttonSendMood`. So we will add `navigationController?.popViewController(animated: true)` to `@objc func onSendMoodButtonTapped()`.

{% code lineNumbers="true" %}
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
{% endcode %}

Now let's run it again:

<figure><img src="/gitbook-assets/eleven.gif" alt=""><figcaption></figcaption></figure>

Yay! We now learned how to send data back and forth between two screens!

_Now, your task is to show the user's mood in `labelMood` at ViewController screen._

Next, we will discuss displaying an image related to the user's mood.



<!-- Merged from 3.6.-send-data-back-from-screen-2-to-screen-1-part-4-uiimageview.md -->

# 3.3.3. Send data back from Screen 2 to Screen 1: UIImageView

## Importing images into the project

Now, let's start working with ImageViews. We need three images for moods: happy, meh, and sad. We will be using the following images in three different sizes: 1x, 2x, and 3x.

![](</gitbook-assets/happy (1).png>) ![](</gitbook-assets/meh (1).png>) ![](</gitbook-assets/sad (1).png>)

Download the images from here:

{% file src="/gitbook-assets/images (1).zip" %}

If you extract the files, you will see something like the following:

<figure><img src="/gitbook-assets/Screenshot 2023-05-11 at 9.26.55 PM (2).png" alt=""><figcaption></figcaption></figure>

See each image has three versions: 1x, 2x, and 3x.

* 1x images have a resolution of 200x200
* 2x images have a resolution of 400x400
* 3x images have a resolution of 600x600

These are called image scaling. To understand the concept, read the following article: [https://www.appypie.com/image-scaling-ios-how-to](https://www.appypie.com/image-scaling-ios-how-to).

Long story short, in the early iOS devices before iPhone 8, the resolutions were very low, less than 640p. There you need to use smaller images (like 200x200). Comparatively, phones like iPhone 11 or later have more than 1024p, so modern screens can accommodate bigger images (like 600x600). iOS has a great feature to scale the images automatically if you provide images with all three scales. It will automatically use the appropriate image based on the device where you run the app.

**Pro tip:** now, you usually do not have to worry about 1x images anymore; those low-resolution devices are non-existent now.

Now, let's add the images to our project. Go to the project navigator on the left pane. Click on **Assets**. Right-click somewhere below the AppIcon, and select **New Folder.** Create a folder named "mood images."

_<mark style="color:blue;">(you can name it as you want; you do not need to create the folder; I am creating the folder to help myself organize the assets).</mark>_

Now, right-click on the "mood images" folder and select **Import.** Then select the images and **Open.**

<figure><img src="/gitbook-assets/thirteen (1).gif" alt=""><figcaption></figcaption></figure>

Looking at the Assets now, you'll see three image assets listed instead of nine. The project automatically indexed nine of them into three assets, each having 3 scales (1x, 2x, and 3x). ![](</gitbook-assets/Screenshot 2023-05-11 at 10.11.02 PM.png>)

## Setting the image into the ImageView through delegate

In ViewController, add the following line of code into `delegateButtonSendMood()` method:

```swift
imageMood.image = UIImage(named: mood.lowercased())
```

Here, we are creating an `UIImage` object from the project assets. We are looking for an image asset named as the mood we receive from ShowViewController through the delegate method. Now, the moods are "Happy," "Meh," and "Sad." But the image asset names are "happy," "meh," and "sad." So we convert the String to all lowercase by calling `lowercased()` method.

Let's run the app again.

<figure><img src="/gitbook-assets/fourteen (1).gif" alt=""><figcaption></figcaption></figure>

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

_<mark style="background-color:blue;">**Now, before you go, set the title of the app by writing**</mark><mark style="background-color:blue;">**&#x20;**</mark><mark style="background-color:blue;">**`title = "Learning Navigation"`**</mark><mark style="background-color:blue;">**&#x20;**</mark><mark style="background-color:blue;">**in**</mark><mark style="background-color:blue;">**&#x20;**</mark><mark style="background-color:blue;">**`viewDidLoad()`**</mark><mark style="background-color:blue;">**&#x20;**</mark><mark style="background-color:blue;">**method at ViewController. And run the app to see the changes!**</mark>_

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

