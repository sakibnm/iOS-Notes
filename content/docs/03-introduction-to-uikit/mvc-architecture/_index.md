---
title: "MVC Architecture"
weight: 40
---

# 4. Separating the View from the Controller code

One of the better ways of coding is to separate the Views (front-end codes) from the Controllers (back-end codes). That way, we can make ViewControllers less cluttered.

We have been keeping all the codes for a screen on a single file (ViewController.swift). We can easily separate the View codes from the ViewController. After we separate the Views, we willwillwillwillwillwillwillwill only have Control and Data access codes in ViewController.&#x20;

To be able to do that, we will create our App4. We will build something like the following:

<figure><img src="/gitbook-assets/Screenshot 2023-05-16 at 11.05.16 AM.png" alt=""><figcaption></figcaption></figure>

On our first screen, we will have a Label to display "App4." Then we will have a TextField to get a text from the user. Next, we will have another Label to say, "How are you feeling today?" And then, we will show a PickerView to select a mood from "Happy," "Meh," and "Sad." Finally, we will have a Button, Submit. If the user taps the Submit Button, it should take them to the second screen. The second screen displays the message and the mood of the user.&#x20;




<!-- Merged from 4.1.-creating-a-separate-view-code-file.md -->

# 4.1. Creating a separate View code file

Now let's create a separate file, 'FirstScreenView.swift' in the project.&#x20;

* Click **File -> New -> File...**&#x20;
* Select **Cocoa Touch Class** and press **Next**
* The class name should be **FirstScreenView.**&#x20;
* Select **UIView** as for 'Subclass of.' And press **Next**.
* Press **Create.**

<figure><img src="/gitbook-assets/one (3).gif" alt=""><figcaption></figcaption></figure>

## Setting up the View

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

Now, Xcode will yell at you saying, <mark style="color:red;">'required' initializer 'init(coder:)' must be provided by the subclass of 'UIView'.</mark> UIView adopts the [NSCoder](https://developer.apple.com/documentation/foundation/nscoder) protocol, so we must override the `init()` method with the coder parameter. Do not worry about it; just click on the red sign and click fix. That should automatically do the stuff for you. And you can keep the generated method untouched.

<figure><img src="/gitbook-assets/two (1).gif" alt=""><figcaption></figcaption></figure>

Let's start building the View now. We trivially add the following initializing methods like how we did before:&#x20;

{% code lineNumbers="true" %}
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
{% endcode %}

In the above code, notice that I am setting the 'backgroundColor' to white because it would, by default, populate a black screen without the background color. The `init(frame: CGRect)` method is used as the initializer of the instance of the FirstScreenView. If you look carefully at the setup methods, we are not saying `view.addSubView()` like before. This class is already a UIView, so we use `self.addSubView()` method.&#x20;

Now let's initialize the constraints:

{% code lineNumbers="true" %}
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
{% endcode %}

<mark style="color:purple;background-color:red;">**Notice that here to set up the constraints, I am using**</mark><mark style="color:purple;background-color:red;">**&#x20;**</mark><mark style="color:purple;background-color:red;">**`self`**</mark><mark style="color:purple;background-color:red;">**&#x20;**</mark><mark style="color:purple;background-color:red;">**instead of**</mark><mark style="color:purple;background-color:red;">**&#x20;**</mark><mark style="color:purple;background-color:red;">**`view`**</mark><mark style="color:purple;background-color:red;">**&#x20;**</mark><mark style="color:purple;background-color:red;">**for the same reason, this FirstScreenView is a UIView itself. I am adding children of the**</mark><mark style="color:purple;background-color:red;">**&#x20;**</mark><mark style="color:purple;background-color:red;">**`self`**</mark><mark style="color:purple;background-color:red;">**&#x20;**</mark><mark style="color:purple;background-color:red;">**view.**</mark>



<!-- Merged from 4.2.-patching-the-view-class-with-the-viewcontroller.md -->

# 4.2. Patching the View class with the ViewController

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

<figure><img src="/gitbook-assets/five (1).gif" alt=""><figcaption></figcaption></figure>

## Adding the PickerView logic

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

{% code lineNumbers="true" %}
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
{% endcode %}

Now, let's run it.&#x20;

<figure><img src="/gitbook-assets/three (2).gif" alt=""><figcaption></figcaption></figure>

See, we patched the PickerView with data!



<!-- Merged from 4.3.-creating-the-display-screen.md -->

# 4.3. Creating the Display Screen

Now, we need to create another screen to display the data the user sends from the first screen. We need to create two swift files here, one is for the view (DisplayView), and another is for the view controller (DisplayViewController).&#x20;

## DisplayView.swift

We have two Labels in the view:

* The first Label displays the message.
* The second Label displays the mood.

So create the 'DisplayView' file like before and add the codes as follows:

{% code lineNumbers="true" %}
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
{% endcode %}

## Adding DisplayViewController

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



<!-- Merged from 4.4.-navigation-controller-and-sending-data-from-screen-1-to-screen-2.md -->

# 4.4. Navigation Controller and sending data from screen 1 to screen 2

We will now use the navigation controller to switch between screens and send data from the first screen to the second screen.&#x20;

Embed the ViewController (controller of the first screen) to the Navigation Controller on Storyboard. &#x20;

Now, we need to send the data (message and mood) from the first screen (ViewController) to the second screen (DisplayViewController). We will create a public struct to create this package.&#x20;

## Adding a struct

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

## Handling the Button Tap action

### **Sending Data**

Now that our struct is ready, we will create a data package of two strings (message and mood). And then, when the user taps on the Submit button, we should navigate to DisplayViewController and send this package there. So let's add an action to the button:

{% code lineNumbers="true" %}
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
{% endcode %}

In the above code, we add an action for `buttonSubmit` to handle if the user taps on it.&#x20;

**Please note:** <mark style="color:purple;">**`buttonSubmit`**</mark><mark style="color:purple;">**&#x20;**</mark><mark style="color:purple;">**is not a part of the ViewController, rather it's a part of the view (**</mark><mark style="color:purple;">**`firstScreen`**</mark><mark style="color:purple;">**). That is why we are adding the action to the button by calling**</mark><mark style="color:purple;">**&#x20;**</mark><mark style="color:purple;">**`firstScreen.buttonSubmit`**</mark><mark style="color:purple;">**. We will always add actions for the buttons inside the ViewController, not the view. A view (FirstScreenView) class is just for setting up the front-end. You should not write back-end methods or actions there.**</mark>&#x20;

If the user puts in a message and selects their mood, the code will create a variable `package` of struct `Package` with the message and the mood. Then the code instantiates the DisplayViewController (`displayViewController`) and sets `package` as the value of the `receivedPackage` variable of `displayViewController`. Then, as usual, we push `displayViewController` to the navigation controller.

### **Receiving data at DisplayViewController**

We need to prepare the DisplayViewController to receive the package. So let's update DisplayViewController.swift as follows:

{% code lineNumbers="true" %}
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
{% endcode %}

In the above code, see that we are creating a variable `receivedPackage` of type `ViewController.Package`. `Package` is a public struct in the `ViewController` class. So to access it from inside another class, we need to write the source class name, then dot(`.`), then the struct name.&#x20;

Then we process and display the data on DisplayView.

Let's run the app:

<figure><img src="/gitbook-assets/six (1).gif" alt=""><figcaption></figcaption></figure>

_<mark style="color:purple;">**Here, we learned how to detach the front end (View) of a screen from the back end (ViewController) of it. It is a widely used technique in iOS development. And you should follow this pattern.**</mark>_



<!-- Merged from 4.5.-wrapping-up-structuring-the-files.md -->

# 4.5. Wrapping up: structuring the files

Now, your project structure should look like the following:

![](</gitbook-assets/Screenshot 2023-05-16 at 2.39.20 PM (1).png>)

Although we have separated the Views from the Controllers, we still may find this structure cluttered. So, we want to put the files in separate groups for better readability.&#x20;

* Select the files related to the first screen (FirstScreenView and ViewController). To select both files together, press **Command + click on the intended files.**&#x20;
* **Right-click** on the selected files and select **New Group From Selection**. Name the group as 'First Screen'
* Create the group of files (DisplayView and DisplayViewController) for the second screen similarly.

<figure><img src="/gitbook-assets/ten.gif" alt=""><figcaption></figcaption></figure>

**Now, the structure looks a lot better!!!** :tada:



<!-- Merged from 4.6.-reference-code.md -->

# 4.6. Reference Code

{% file src="/gitbook-assets/App4.zip" %}

