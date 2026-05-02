---
coverY: 0
---

# 5. Tab Bar Controller

We often see apps with bottom navigation bars, where you can tap on an icon from the bottom bar, and the app loads different screens for different buttons pressed like the following:

<figure><img src="/gitbook-assets/5.one (1).gif" alt=""><figcaption></figcaption></figure>

iOS gives us an easy-to-use and customizable tool called UITabBarController to build such screens. In this module, we will create an app that uses a Tab Bar.

## The TabControllerDemo app

Let's create an app called TabControllerDemo in XCode. The app will have:

* A bottom Tab Bar having three Tab Bar buttons: red, green, and blue.
* Tapping the "red" button opens the Red Screen.
* Tapping the "blue" button opens the Blue Screen.
* Tapping the "green" button opens the Green Screen.
* Each screen has
  * A color box displaying the corresponding color.
  * A button to send data to other screens.
  * A label to display the received data from other screens.




<!-- Merged from 5.1.-views-of-the-screens.md -->

# 5.1. Views of the Screens

## Views

The design of the screens is the same except for the background color of the color box. So, let's create the views of Red, Blue, and Green screens.

### RedView.swift

Let's create a swift file called RedView.swift and put the following code:

```swift
//
//  RedView.swift
//  TabControllerDemo
//
//  Created by Sakib Miazi on 6/6/23.
//

import UIKit

class RedView: UIView {
    var boxView: UIView!
    var buttonSend: UIButton!
    var labelReceived: UILabel!
    override init(frame: CGRect) {
        super.init(frame: frame)
        
        boxView = UIView()
        boxView.backgroundColor = .red
        boxView.translatesAutoresizingMaskIntoConstraints = false
        self.addSubview(boxView)
        
        buttonSend = UIButton(type: .system)
        buttonSend.setTitle("Send Hello", for: .normal)
        buttonSend.translatesAutoresizingMaskIntoConstraints = false
        self.addSubview(buttonSend)
        
        labelReceived = UILabel()
        labelReceived.text = "Waiting for Notification!"
        labelReceived.translatesAutoresizingMaskIntoConstraints = false
        self.addSubview(labelReceived)
        
        
        NSLayoutConstraint.activate([
            boxView.topAnchor.constraint(equalTo: self.safeAreaLayoutGuide.topAnchor, constant: 32),
            boxView.widthAnchor.constraint(equalToConstant: 200),
            boxView.heightAnchor.constraint(equalToConstant: 200),
            boxView.centerXAnchor.constraint(equalTo: self.safeAreaLayoutGuide.centerXAnchor),
            
            buttonSend.topAnchor.constraint(equalTo: self.boxView.bottomAnchor, constant: 8),
            buttonSend.centerXAnchor.constraint(equalTo: self.safeAreaLayoutGuide.centerXAnchor),
            
            labelReceived.topAnchor.constraint(equalTo: self.buttonSend.bottomAnchor, constant: 8),
            labelReceived.centerXAnchor.constraint(equalTo: self.safeAreaLayoutGuide.centerXAnchor),
        ])
    }
    
    required init?(coder: NSCoder) {
        fatalError("init(coder:) has not been implemented")
    }
}

```

In the above code, we create a boxView to display the corresponding color of the screen, a button to send data to other screens, and a label to display the received data.

### GreenView.swift and BlueView.swift

The only thing different in these files compared to RedView.swift is the background color of the boxView. For GreenView.swift, it is `.green`, and for BlueView.swift, it is `.blue`.



<!-- Merged from 5.2.-controllers-of-the-screens.md -->

# 5.2. Controllers of the Screens

For each different screen (red, blue, and green), we need to have different Controllers. Let's create three controller files.

## RedViewController.swift

```swift
//
//  RedViewController.swift
//  TabControllerDemo
//
//  Created by Sakib Miazi on 6/6/23.
//

import UIKit

class RedViewController: UIViewController {
    let redView = RedView()
    
    override func loadView() {
        view = redView
    }
    
    override func viewDidLoad() {
        super.viewDidLoad()
        view.backgroundColor = .white
        title = "Red"
    }
}

```

## BlueViewController.swift

```swift
//
//  BlueViewController.swift
//  TabControllerDemo
//
//  Created by Sakib Miazi on 6/6/23.
//

import UIKit

class BlueViewController: UIViewController {
    let blueView = BlueView()
    
    override func loadView() {
        view = blueView
    }
    
    override func viewDidLoad() {
        super.viewDidLoad()
        view.backgroundColor = .white
        title = "Blue"
    }
}

```

## GreenViewController.swift

```swift
//
//  GreenViewController.swift
//  TabControllerDemo
//
//  Created by Sakib Miazi on 6/6/23.
//

import UIKit

class GreenViewController: UIViewController {
    let greenView = GreenView()
    
    override func loadView() {
        view = greenView
    }
    
    override func viewDidLoad() {
        super.viewDidLoad()
        view.backgroundColor = .white
        title = "Green"
    }
}

```



<!-- Merged from 5.3.-patching-the-screens-in-the-tab-bar.md -->

# 5.3. Patching the Screens in the Tab Bar

We have three screens. Now we want to patch these three screens in a Tab Bar Controller. Now it's time to use our main ViewController.swift file.

Let's look into the logical structure of a Tab Bar:

<figure><img src="/gitbook-assets/Screenshot 2023-06-12 at 12.41.40 PM (1).png" alt=""><figcaption></figcaption></figure>

* The Tab Bar is the UI component that displays the bottom tabs.
* So it needs a controller to control the UI. In our case, we will use the main ViewController as the Tab Bar Controller.
* The Tab Bar contains the bar items. In our case, we will use three bar items: red, green, and blue.
  * Each bar item represents a screen; for example, the red item represents the Red Screen.
  * **Since each screen is independent of other tab bar screens, they should also have their own Navigation Controllers. (Do you remember that we have been embedding Navigation Controllers through the Storyboards? We can also do that by writing codes)**
  * For each screen, we define its Navigation Controller, then embed it in the corresponding view controller.
  * We have already patched the screen views to their view controllers.

### Setting up the Tab Bar: ViewController.swift

Let's open the ViewController.swift file and put the following code there:

{% code lineNumbers="true" %}
```swift
//
//  ViewController.swift
//  TabControllerDemo
//
//  Created by Sakib Miazi on 6/6/23.
//

import UIKit

class ViewController: UITabBarController, UITabBarControllerDelegate {

    override func viewWillAppear(_ animated: Bool) {
        super.viewWillAppear(animated)
        
        //MARK: setting up red tab bar...
        let tabRed = UINavigationController(rootViewController: RedViewController())
        let tabRedBarItem = UITabBarItem(
            title: "Red",
            image: UIImage(systemName: "r.square")?.withRenderingMode(.alwaysOriginal),
            selectedImage: UIImage(systemName: "r.square.fill")
        )
        tabRed.tabBarItem = tabRedBarItem
        tabRed.title = "Red"
        
        //MARK: setting up green tab bar...
        let tabGreen = UINavigationController(rootViewController: GreenViewController())
        let tabGreenBarItem = UITabBarItem(
            title: "Green",
            image: UIImage(systemName: "g.square")?.withRenderingMode(.alwaysOriginal),
            selectedImage: UIImage(systemName: "g.square.fill")
        )
        tabGreen.tabBarItem = tabGreenBarItem
        tabGreen.title = "Green"
        
        //MARK: setting up blue tab bar...
        let tabBlue = UINavigationController(rootViewController: BlueViewController())
        let tabBlueBarItem = UITabBarItem(
            title: "Blue",
            image: UIImage(systemName: "b.square")?.withRenderingMode(.alwaysOriginal),
            selectedImage: UIImage(systemName: "b.square.fill")
        )
        tabBlue.tabBarItem = tabBlueBarItem
        tabBlue.title = "Blue"
        
        //MARK: setting up this view controller as the Tab Bar Controller...
        self.viewControllers = [tabRed, tabGreen, tabBlue]
    }
    
    override func viewDidLoad() {
        super.viewDidLoad()
        
    }
}
```
{% endcode %}

In the above code:

* We first need to adopt two protocols related to the Tab Bar Controller: `UITabBarController and UITabBarControllerDelegate` (line 10).
* We should write the logic for setting up the tab bar controller just before the view appears. So we will write the code in `viewWillAppear()` method.
* On lines 15 through 23, we set up the Tab Bar Button for the Red Screen.
  * On line 16, we define the Navigation Controller, `tabRed` for the Red Screen.
  * Then we define the tab bar item.
    * We used two images from the SF Symbols app for two behaviors of the bar item: 'not selected' and 'selected'. It means when the user taps on an item, it should change its appearance with a different image. (Tab bar items are very similar to buttons).
  * On line 22, we set the tab bar item in the navigation controller, `tabRed`.
  * On line 23, we set the screen title for the red screen using the navigation controller.
* We do the same steps for the other two screens from lines 25 through 43.
* On line 46, we finally embed all three navigation controllers into this view controller.

If we run the app now, we will see:

<figure><img src="/gitbook-assets/5.two (1).gif" alt=""><figcaption></figcaption></figure>



<!-- Merged from 5.4.-sending-data-from-one-tab-to-another.md -->

# 5.4. Sending data From one Tab to Another

We will use Notification Center to send data between the tabs. If the user taps on the "Send Hello" button from the Red Screen, it will send all the other tabs a message, "Hello From Red Screen." The other screens will display the message on the labels.

We now have to write code in the view controllers to enable this feature. Let's open RedViewController.swift file and write the following code:

{% code lineNumbers="true" %}
```swift
//
//  RedViewController.swift
//  TabControllerDemo
//
//  Created by Sakib Miazi on 6/6/23.
//

import UIKit

class RedViewController: UIViewController {
    let redView = RedView()
    
    let notificationCenter = NotificationCenter.default
    
    override func loadView() {
        view = redView
    }
    
    override func viewDidLoad() {
        super.viewDidLoad()
        view.backgroundColor = .white
        title = "Red"
        
        //MARK: setting observers...
        observeBlue()
        observeGreen()

        //MARK: send hello button...
        redView.buttonSend.addTarget(self, action: #selector(onButtonSendTapped), for: .touchUpInside)
    }
    
    //MARK: observing blue...
    func observeBlue(){
        notificationCenter.addObserver(
            self,
            selector: #selector(notificationReceived(notification:)),
            name: .fromBlue, object: nil
        )
    }
    
    //MARK: observing green...
    func observeGreen(){
        notificationCenter.addObserver(
            self,
            selector: #selector(notificationReceived(notification:)),
            name: .fromGreen, object: nil
        )
    }
    
    //MARK: handling notifications...
    @objc func notificationReceived(notification: Notification){
        redView.labelReceived.text = notification.object as! String
    }
    
    //MARK: sending hello to other screens...
    @objc func onButtonSendTapped(){
        notificationCenter.post(
            name: .fromRed,
            object: "Hello from Red!"
        )
    }
}
```
{% endcode %}

In the above code:

* On line 13, we define the notification center.
* We create a separate file `NotificationNames.swift` to set the names of the notifications.
  * `static let fromRed = Notification.Name("fromRed")`
  * `static let fromGreen = Notification.Name("fromGreen")`
  * `static let fromBlue = Notification.Name("fromBlue")`
* Since this is the red screen, we will observe the notifications from the blue and green screens.
  * On lines 25 and 26, we call two methods (`observeBlue()` and `observeGreen()`) to set up the observers.
  * `observeBlue()` method observes the notifications from the Blue Screen. When a new notification from the Blue Screen is received, we handle the notification in `notificationReceived(notification: Notification)` method.
    * On lines 51 through 53, we handle the notification. In the method, we set the label's text to the notification's text.
* On line 29, we add the target for `buttonSend`.
  * On tapping `buttonSend` we post the notification with the string: "Hello from Red!" (lines 56 through 61).

We write the other two view controllers regarding the Blue and Green screens similarly.

Now, if we run the app now, we will see:

<figure><img src="/gitbook-assets/5.four (1).gif" alt=""><figcaption></figcaption></figure>



<!-- Merged from 5.5.-reference-code.md -->

# 5.5. Reference Code

{% file src="/gitbook-assets/TabControllerDemo.zip" %}



<!-- Merged from 5.6.-notes-for-tab-bar-controller.md -->

# 5.6. Notes for Tab Bar Controller

* **Tab Bar Controller is a powerful tool.**
* **Each tab has its own Navigation Controller. So, you can build a separate tree of screens for each tab with its navigation.**
* **So, each tab can potentially work like a separate multiscreen app module.**
* **You can play around with the UI style elements of the tab bar items to design them as you like.**

