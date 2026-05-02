---
title: "UIScrollView"
weight: 20
---

# 8. UIScrollView

So far, we have worked with screens that do not scroll. I think all of you faced a similar issue: if you rotate the screen, the UI elements get outside the bottom edge. The reason behind it is that the screen is not scrollable. So here, we will implement a scrollable view.

Let's build a small app App8 to implement a ScrollView. The app should look like this:

<figure><img src="/gitbook-assets/8.11 (1).gif" alt=""><figcaption></figcaption></figure>

**So there will be the following UI elements:**

* One text field at the top (`textField1`).
* Next, we will have a large image covering almost the whole screen.
* Then two more text fields at the bottom (`textField1` and `textField2`).




<!-- Merged from 8.1.-creating-the-view-of-the-screen.md -->

# 8.1. Creating the View of the Screen

Let's declare the UI elements:

```swift
//
//  ScrollScreenView.swift
//  App8_scroller
//
//  Created by Sakib Miazi on 5/24/23.
//

import UIKit

class ScrollScreenView: UIView {
    var contentWrapper:UIScrollView!
    var largeImageView:UIImageView!
    var textField1:UITextField!
    var textField2:UITextField!
    var textField3:UITextField!
    
    override init(frame: CGRect) {
        super.init(frame: frame)
        self.backgroundColor = .white
        
        setupContentWrapper()
        setupLargeImageView()
        setuptextField1()
        setuptextField2()
        setuptextField3()
        
        initConstraints()
    }
    
    //MARK: unused...
    required init?(coder: NSCoder) {
        fatalError("init(coder:) has not been implemented")
    }
}
```

If you noticed, I have declared a variable called `contentWrapper` of type `UIScrollView`. We will wrap the elements we want to include in the scrollable part of the screen.

We also need a large image. I used the following image to load inside the screen:

![](</gitbook-assets/image@3x (1).jpg>)

So, let's import the image into the project:

<figure><img src="/gitbook-assets/Screenshot 2023-05-24 at 10.59.28 AM (1).png" alt=""><figcaption></figcaption></figure>

Let's initialize the UI elements:

```swift
//MARK: setting up UI elements...
func setupContentWrapper(){
    contentWrapper = UIScrollView()
    contentWrapper.translatesAutoresizingMaskIntoConstraints = false
    self.addSubview(contentWrapper)
}

func setuptextField1(){
    textField1 = UITextField()
    textField1.placeholder = "First Text Field"
    textField1.translatesAutoresizingMaskIntoConstraints = false
    contentWrapper.addSubview(textField1)
}

func setupLargeImageView(){
    largeImageView = UIImageView()
    largeImageView.image = UIImage(named: "image")
    largeImageView.contentMode = .scaleAspectFill
    largeImageView.clipsToBounds = true
    largeImageView.translatesAutoresizingMaskIntoConstraints = false
    contentWrapper.addSubview(largeImageView)
}

func setuptextField2(){
    textField2 = UITextField()
    textField2.placeholder = "Second Text Field"
    textField2.translatesAutoresizingMaskIntoConstraints = false
    contentWrapper.addSubview(textField2)
}

func setuptextField3(){
    textField3 = UITextField()
    textField3.placeholder = "Third Text Field"
    textField3.translatesAutoresizingMaskIntoConstraints = false
    contentWrapper.addSubview(textField3)
}
```

As you can see in the image view, I set the image when I initialize it. I also set the content mode to scale aspect fit; and set the clips to bounds to true so that the image view clips the image outside the image view.

### Constraints:

```swift
//MARK: initializing constraints...
func initConstraints(){
    NSLayoutConstraint.activate([
        //MARK: contentWrapper constraints...
        contentWrapper.topAnchor.constraint(equalTo: self.safeAreaLayoutGuide.topAnchor),
        contentWrapper.leadingAnchor.constraint(equalTo: self.safeAreaLayoutGuide.leadingAnchor),
        contentWrapper.widthAnchor.constraint(equalTo:self.safeAreaLayoutGuide.widthAnchor),
        contentWrapper.heightAnchor.constraint(equalTo: self.safeAreaLayoutGuide.heightAnchor),
        
        //MARK: textField1 constraints...
        textField1.topAnchor.constraint(equalTo: contentWrapper.topAnchor, constant: 32),
        textField1.centerXAnchor.constraint(equalTo: contentWrapper.centerXAnchor),
        
        //MARK: largeImageView constraints...
        largeImageView.heightAnchor.constraint(equalToConstant: 800),
        largeImageView.widthAnchor.constraint(equalTo: contentWrapper.widthAnchor),
        largeImageView.topAnchor.constraint(equalTo: textField1.bottomAnchor, constant: 8),
        largeImageView.centerXAnchor.constraint(equalTo: contentWrapper.centerXAnchor),
        
        //MARK: textField2 constraints...
        textField2.topAnchor.constraint(equalTo: largeImageView.bottomAnchor, constant: 8),
        textField2.centerXAnchor.constraint(equalTo: contentWrapper.centerXAnchor),
        
        
        //MARK: textField3 constraints...
        textField3.topAnchor.constraint(equalTo: textField2.bottomAnchor, constant: 8),
        textField3.centerXAnchor.constraint(equalTo: contentWrapper.centerXAnchor),
        textField3.bottomAnchor.constraint(equalTo: contentWrapper.bottomAnchor)
        

    ])
}
```

**ImageView constraints:** We should always set the height and weight using constraints for the image view. **The height should be a constant; otherwise, it might ruin your layout.**

**ScrollView constraints:** Here, we need to be careful when setting constraints of the scroll view. There are **four** constraints we must set for the scroll view:

* **topAnchor:** set it where the scrollable view starts (top edge of the safe area in this case).
* **leadingAnchor:** the left edge of the scrollable view (leading edge of the safe area here).
* **widthAnchor:** it is very important to set the width of the ScrollView; otherwise scroll view may behave in uncanny ways.
* **heightAnchor:** also, it is absolutely necessary to set the height; otherwise, it might not even scroll. **It might become tricky where we have UI elements outside the scroller.**

**The most important constraints that you must set correctly are**: **the topAnchor** of the topmost UI element and **the bottomAnchor** of the bottom element.

* The topAnchor of the topmost element should be set to the topAnchor of the scroll view.
* The bottomAnchor of the bottom element should be set to the bottomAnchor of the scroll view.
* Please note the scroll view wraps the elements. So, it is important that you use these anchors of the UI elements the scroll view is wrapping.

Now we need to patch the screen to the controller.



<!-- Merged from 8.2.-creating-the-controller.md -->

# 8.2. Creating the Controller

Let's put the following code in the ViewController.swift:

```swift
//
//  ViewController.swift
//  App8_scroller
//
//  Created by Sakib Miazi on 5/24/23.
//

import UIKit

class ViewController: UIViewController {

    let homeScreen = ScrollScreenView()
    
    override func loadView() {
        view = homeScreen
    }
    override func viewDidLoad() {
        super.viewDidLoad()
        
        //MARK: hide Keyboard on tapping the screen...
        hideKeyboardOnTapOutside()
    }
    
    //MARK: hide keyboard logic...
    func hideKeyboardOnTapOutside(){
        //MARK: recognizing the taps on the app screen, not the keyboard...
        let tapRecognizer = UITapGestureRecognizer(target: self, action: #selector(hideKeyboardOnTap))
        view.addGestureRecognizer(tapRecognizer)
    }
    
    @objc func hideKeyboardOnTap(){
        //MARK: removing the keyboard from screen...
        view.endEditing(true)
    }
}


```

Here, we are loading the view on `loadView()` method; and also including the methods to hide the iOS keyboard by tapping outside ([1.-hiding-keyboard-when-tapped-outside.md](../useful-tools-and-ui-elements/1.-hiding-keyboard-when-tapped-outside.md "mention")).

Let's run the app now.

<figure><img src="/gitbook-assets/8.11 (1).gif" alt=""><figcaption></figcaption></figure>

_<mark style="color:purple;">Now that you know how to use scrollable views. Use it carefully when you use it.</mark>_



<!-- Merged from 8.3.-reference-code.md -->

# 8.3. Reference Code

{% file src="/gitbook-assets/App8 (1).zip" %}

