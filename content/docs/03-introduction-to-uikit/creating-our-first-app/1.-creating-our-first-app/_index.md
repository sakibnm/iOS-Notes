---
coverY: 0
---

# 1. Creating our first app

Press `Command (⌘) + Space` together on your Mac computer. It opens up Spotlight search. Search 'Xcode' there, and open Xcode. It opens the following window:

<figure><img src="/gitbook-assets/Screenshot 2023-05-09 at 10.51.51 AM (1).png" alt=""><figcaption></figcaption></figure>

Click on **'Create a new Xcode project.'** You will see the following:

**Make sure you select iOS from the top template chooser.&#x20;**<mark style="color:red;">**Do not choose multiplatform or macOS.**</mark>

<figure><img src="/gitbook-assets/Screenshot 2023-05-09 at 10.55.45 AM (1).png" alt=""><figcaption></figcaption></figure>

Select **App** and press **Next.**

<figure><img src="/gitbook-assets/Screenshot 2023-05-09 at 10.57.39 AM (1).png" alt=""><figcaption></figcaption></figure>

Give your project a name. If you have not already signed in to an Apple ID, sign in here and then select your Personal Team. Put your preferred organization identifier (reversed domain name order). For example, you can put `com.nuios`. Select **'Storyboard'** as the interface (**do not select 'SwiftUI'**). Select the language **'Swift.'** And then press **Next**. You'll see:

<figure><img src="/gitbook-assets/Screenshot 2023-05-09 at 11.04.18 AM (1).png" alt=""><figcaption></figcaption></figure>

Here is where you'll choose where to save your project. Click on **Create.** It will create a new project for you, and you will see the following:

<figure><img src="/gitbook-assets/Screenshot 2023-05-09 at 11.05.36 AM (1).png" alt=""><figcaption></figcaption></figure>

Here, you need to select a simulator. Please click on the top middle panel as indicated in the following image:

<figure><img src="/gitbook-assets/1.1.1.png" alt=""><figcaption></figcaption></figure>

Select an iPhone simulator of your choice. **Do not select 'This Mac.'**

Now, your first project is ready to be built.

Press the Play :arrow\_forward: button from the top left corner.

<figure><img src="/gitbook-assets/Screenshot 2023-05-09 at 11.07.39 AM (1).png" alt=""><figcaption></figcaption></figure>

It will open up the Emulator with an empty screen.

<figure><img src="/gitbook-assets/Screenshot 2023-05-09 at 11.12.10 AM (1).png" alt=""><figcaption></figcaption></figure>

If you can see the emulator, you have successfully built your first app. We will start building on it.




<!-- Merged from 1.1.-project-structure-overview.md -->

# 1.1. Project structure overview

The Xcode screen has three panes.

<figure><img src="/gitbook-assets/Screenshot 2023-05-09 at 11.22.24 AM (1).png" alt=""><figcaption></figcaption></figure>

### The left pane

In the left pane, you see the file structure of the codes and resources. If you right-click on the project directory, you can see that you can show the project directory in Finder:

![](</gitbook-assets/Screenshot 2023-05-09 at 11.27.41 AM.png>)

It will show you the project directory:

<figure><img src="/gitbook-assets/Screenshot 2023-05-09 at 11.30.52 AM.png" alt=""><figcaption></figcaption></figure>

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

<figure><img src="/gitbook-assets/Screenshot 2023-05-09 at 11.57.38 AM (1).png" alt=""><figcaption></figcaption></figure>

### The right pane

The right pane is the configuration and attributes explorer pane. For example, if you click on the Main Storyboard and click the screen preview, the right pane will display the attribute of the screen view:

<figure><img src="/gitbook-assets/Screenshot 2023-05-09 at 12.00.43 PM (1).png" alt=""><figcaption></figcaption></figure>

Once we start building apps, we will eventually get used to Xcode more.



<!-- Merged from 1.2.-uilabel-our-first-ui-element.md -->

# 1.2. UILabel, our first UI element

Let's add a text pane, `UILabel` to our storyboard. Open the Main storyboard, and press `Command(⌘) + Shift + L` together. It opens up the Objects Library like this:

<figure><img src="/gitbook-assets/Screenshot 2023-05-09 at 12.09.01 PM.png" alt=""><figcaption></figcaption></figure>

Now, look for 'label'. **Press the intended UI element, (in this case, it shows as 'Label'), drag it, and drop it on the preview screen.**

<figure><img src="/gitbook-assets/six_ (1).gif" alt=""><figcaption></figcaption></figure>

It will now show:

<figure><img src="/gitbook-assets/Screenshot 2023-05-09 at 12.15.19 PM (1).png" alt=""><figcaption></figcaption></figure>

See, there is a left view pane where you can find all the elements. The newly added Label got added inside the View Controller tree. Inside the View Controller, you have a View. The View is actually the view of the entire screen, including the camera cut.

#### Safe area: Inside the View, we have a Safe area. A safe area is an area where there are no interruptions or obstacles like the camera cut. Click on the safe area; it will mark the safe area on the screen:

<figure><img src="/gitbook-assets/Screenshot 2023-05-09 at 12.24.52 PM.png" alt=""><figcaption></figcaption></figure>

The safe area comes in very handy designing the screen with constraints.

Now, let's add a few constraints and attributes for the Label we just added.

Click on the Label, either on the preview screen or the left view pane, and notice the right configuration pane:

<figure><img src="/gitbook-assets/Screenshot 2023-05-09 at 12.32.14 PM (1).png" alt=""><figcaption></figcaption></figure>

Change the label text, color, and font. You see, once you change the attributes, the changes reflect on the actual UI element.

#### Constraints and Alignments

Now, let's work on the constraints so that we can place the label on the screen, and it stays somewhere predictable, even if we rotate the screen. This is called anchoring.

Before we change anything for the Label, let's see where we will find the tools to work on constraints. Look at the bottom right corner of the Middle pane:

<figure><img src="/gitbook-assets/Screenshot 2023-05-09 at 12.40.55 PM (2).png" alt=""><figcaption></figcaption></figure>

Now let's click on the Label. Then click on the Alignment tool, and select both 'Horizontally in Container,' and 'Vertically in Container.' And add the constraints. It should put the Label in the center of the screen (center-aligned both horizontally and vertically):

<figure><img src="/gitbook-assets/Screenshot 2023-05-09 at 12.50.49 PM (1).png" alt=""><figcaption></figcaption></figure>

Now run the app. and rotate the screen:

![](</gitbook-assets/Screenshot 2023-05-09 at 12.51.58 PM (1).png>)

<figure><img src="/gitbook-assets/Screenshot 2023-05-09 at 12.52.07 PM (1).png" alt=""><figcaption></figcaption></figure>

See, for both cases, the alignment setup is keeping the Label on the screen nice and predictable.



<!-- Merged from 1.3.-uitextfield-and-constraints.md -->

# 1.3. UITextField, and constraints

So far, we have added one UILabel, with the text "Hello World" in it. Now, we will add our second UI element on the screen, UITextField, below the Label. UITextField is used to get user inputs from the keyboard. We can type something in the TextField and use it in our app.

#### Housekeeping the constraints first

So far, the Label is center-aligned both horizontally and vertically. We will keep the horizontal alignment for the Label but remove the vertical alignment. Unfortunately, the storyboard can't clear one particular constraint from visual tools (or not easily). (That's another reason why we will move to write constraints programmatically). So, we will clear all the constraints from the Label. Click on the 'Reset constraints' tool, and select Clear Constraints for Selected Views to clear constraints for the Label:

<figure><img src="/gitbook-assets/Screenshot 2023-05-09 at 1.38.01 PM (1).png" alt=""><figcaption></figcaption></figure>

Now, we will put the Label at the top of the screen, having a 32 points margin from the top edge. Click the 'Add Constraints' tool, and set the top anchor constant to 32. Then click to 'Add 1 constraint':

<figure><img src="/gitbook-assets/Screenshot 2023-05-09 at 1.44.08 PM (1).png" alt=""><figcaption></figcaption></figure>

So you see that the Label is anchored to the top edge of the screen with a 32 points gap:

![](</gitbook-assets/Screenshot 2023-05-09 at 1.46.36 PM.png>)

Now, we will horizontally center the Label. Use the alignment tool to add the constraint:

<figure><img src="/gitbook-assets/Screenshot 2023-05-09 at 1.49.20 PM (1).png" alt=""><figcaption></figcaption></figure>

#### Adding UITextField below UILabel

We now add the UITextField using the Object library (`Command(⌘) + Shift + L`). Look for text, and drag and drop TextField on the screen.

![](</gitbook-assets/Screenshot 2023-05-09 at 1.55.41 PM (1).png>)

Now, let's center the TextField:

<figure><img src="/gitbook-assets/Screenshot 2023-05-09 at 1.58.10 PM (1).png" alt=""><figcaption></figcaption></figure>

Then add the 16 points constraint to the top so that the TextField is anchored to the bottom of the Label having a 16 points gap.

<figure><img src="/gitbook-assets/Screenshot 2023-05-09 at 2.01.02 PM (1).png" alt=""><figcaption></figcaption></figure>

For a TextField, you should give a user some hint of what kind of text the app is expecting. For example, we want to give the user a hint, "Put some text". So, we will use the 'Place holder' attribute in the right pane of the TextField to set it.

<figure><img src="/gitbook-assets/Screenshot 2023-05-09 at 2.02.40 PM (1).png" alt=""><figcaption></figcaption></figure>

Now run the app.

![](</gitbook-assets/Screenshot 2023-05-09 at 2.07.46 PM.png>)

You can see now, you can type something on the TextField.

Please note, you are using your computer keyboard to put the text inside. You can use the emulator (device) keyboard too. From the Simulator menu, click **I/O -> Keyboard -> Toggle Software Keyboard.**

<figure><img src="/gitbook-assets/Screenshot 2023-05-09 at 2.10.38 PM (1).png" alt=""><figcaption></figcaption></figure>



<!-- Merged from 1.4.-uibutton-and-uialertcontroller.md -->

# 1.4. UIButton, and UIAlertController

At this point, We have a TextField to get user inputs from the keyboard. Now, let's add a button below the TextField. Our goal is if a user types something on the TextField and presses the button, the app should echo the text back to the user with an alert.

We will use two UI elements for this purpose: UIButton, and UIAlertController.

## Adding a new button

Let's place a Button on the Screen, center it, and anchor it 16 points below the TextField.

<figure><img src="/gitbook-assets/Screenshot 2023-05-09 at 2.39.56 PM (1).png" alt=""><figcaption><p>Objects library</p></figcaption></figure>

<figure><img src="/gitbook-assets/Screenshot 2023-05-09 at 2.40.21 PM (1).png" alt=""><figcaption><p>Drag and drop button</p></figcaption></figure>

<figure><img src="/gitbook-assets/Screenshot 2023-05-09 at 2.40.40 PM (1).png" alt=""><figcaption><p>Center horizontally</p></figcaption></figure>

<figure><img src="/gitbook-assets/Screenshot 2023-05-09 at 2.40.57 PM (1).png" alt=""><figcaption><p>Add anchor to the bottom of the TextField</p></figcaption></figure>

<figure><img src="/gitbook-assets/Screenshot 2023-05-09 at 2.41.30 PM (1).png" alt=""><figcaption><p>Button is now placed</p></figcaption></figure>

Now, let's change the attributes of the Button. If you select the Button and look at the right pane, you will see the attributes of it. You can play with many different things, like the Style, Title, Background, and Foreground styling, etc. For now, we will just change the Title. Let's change the Title from "Button" to "Click me!"

<figure><img src="/gitbook-assets/Screenshot 2023-05-09 at 2.48.02 PM (1).png" alt=""><figcaption></figcaption></figure>

Now, run the app, and you will see that you have the button "Click me!", and can click on it!

## ViewController and AlertController

Now, we need to handle the click on the Button. So, we need to patch the frontend UI elements to our ViewController code.

_<mark style="color:purple;">We will not use the following technique very much after this lesson since most people do not use Storyboards anymore. However, it's worth the knowledge.</mark>_

So, we will open the Main storyboard and the ViewController code side by side. To do that, Go to the menu, **Editor -> Assistant.** After you click Assistant, it opens the Viewcontroller to right of the Storyboard:

<figure><img src="/gitbook-assets/Screenshot 2023-05-09 at 3.54.28 PM (2).png" alt=""><figcaption></figcaption></figure>

Basically, you have the front end on the left, and on the right, you have the back end.

<figure><img src="/gitbook-assets/Screenshot 2023-05-09 at 3.59.44 PM.png" alt=""><figcaption></figcaption></figure>

Let's patch the UI elements with the back-end code (ViewController).&#x20;

Think about what UI elements we need to handle from the backend here. We need the TextField and the Button. So, **press the 'control' key** on your keyboard (not the command key) and keep it pressed. While pressing the control button, click on the TextField from the storyboard, and do not release. Now, drag the mouse pointer to the right ViewController (keep both the control and mouse pointer pressed). A blue line should appear. Place it inside the class ViewController. An outlet connector appears; put the name of the logical TextField as "textFIeldUser."

<figure><img src="/gitbook-assets/one (2) (1).gif" alt=""><figcaption></figcaption></figure>

It creates a `@IBOutlet var textFieldUser: UITextField!` variable in your ViewController. `@IBOutlet` means it's an outlet from the Interface Builder (storyboard). In short, `textFieldUser` is the logical instance of the `TextField` from storyboard in the ViewController class.

Let's add the Button outlet to the ViewController the same way. And name the Button "buttonClickMe."

<figure><img src="/gitbook-assets/Screenshot 2023-05-09 at 5.35.35 PM (1).png" alt=""><figcaption></figcaption></figure>

### Adding button action

Now, we need to handle if the user taps on `buttonClickMe`. We need to handle the event when the view finishes loading. So, find the `viewDidLoad()` method. When the screen is done populating the UI elements and displaying them, this method is called by the system.

Let's type `buttonClickMe` in `viewDidLoad()` method, and press `.` and then you will see Xcode automatically shows you the possible usage of the button. Then find the `addTarget()` function.

<figure><img src="/gitbook-assets/two (3) (1).gif" alt=""><figcaption></figcaption></figure>

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

<figure><img src="/gitbook-assets/three_ (1).gif" alt=""><figcaption></figcaption></figure>

You'll see that at the bottom right of Xcode, "Button clicked!!" is printed on the Output area.

### Displaying an Alert

Now, we will display an alert instead of just printing "Button clicked!!" So, let's define an AlertController when the button is clicked. We want to display the text the user added in `textFieldUser`. So, we can write the code below to fetch what the user typed in the text field.

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

<figure><img src="/gitbook-assets/four (2).gif" alt=""><figcaption></figcaption></figure>

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



<!-- Merged from 1.5.-wrapping-up-appicon.md -->

# 1.5. Wrapping up: AppIcon

Before we complete the app, let's add an icon for the app. I generated a 1024x1024 pixels large icon:

![](</gitbook-assets/Screenshot 2023-05-09 at 7.05.08 PM (1).png>)

I will use it as my app icon for this app.

_You can generate AppIcons from here:_ [_https://www.appicon.co/_](https://www.appicon.co/)_._

Go to the project navigator from the left pane and click on Assets. In the middle pane, you will see the current assets are loaded. (There are no assets in your project yet). Click on AppIcon; you will see an empty canvas for a 1024x1024 image. Double-click on that, and select the icon from your files. Now your App Icon is set.

<figure><img src="/gitbook-assets/five (1) (1).gif" alt=""><figcaption></figcaption></figure>

Now, run the app again.

Now, go to the app drawer of the emulator. You will see that the icon for our 'App1' is set.

![](</gitbook-assets/Screenshot 2023-05-09 at 7.24.14 PM (1).png>)

Now, our first app 'App1' is complete!



<!-- Merged from 1.6.-reference-code-and-video.md -->

# 1.6. Reference Code and Video

{% file src="/gitbook-assets/App1_project.zip" %}

### TA Arpan created the video on this module for us:

{% embed url="https://www.youtube.com/watch?v=pEwhCh9j8wo" %}

