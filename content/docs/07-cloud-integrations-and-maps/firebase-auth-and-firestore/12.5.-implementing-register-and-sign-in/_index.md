---
title: "12.5. Implementing Register and Sign In"
weight: 1500
---

# 12.5. Implementing Register and Sign In

Our next goal is to build the functionalities so that a user can register a new account and sign in to the account like the following:

<figure><img src="/gitbook-assets/12.two.gif" alt=""><figcaption></figcaption></figure>

* We need to add a right bar button to enable sign-in.
* If the user clicks on the bar button, the app should show an alert to give the user an option to put their email and password. It should also give them the option to register a new account.
* If the user clicks the 'Sign in' button, it should sign the user in using Firebase authentication.
* If the user clicks on the 'Register' button, it should open the registration screen to allow the user to create a new account.




<!-- Merged from 12.3.1.-building-the-right-bar-button-s-for-sign-in-and-logout.md -->

# 12.3.1. Building the Right Bar Button(s) for Sign In and Logout

We add two buttons on the right navigation bar, triggering the same action. We do it to display an image and text to explain to the user what to do. (This is not standard practice, you can design your own buttons.)

We will separate the logic of creating and handling the right bar button actions from the ViewController. So, let's create a new file `Main Screen -> RightBarButtonManager.swift` and write the following code there:

![](</gitbook-assets/Screenshot 2023-06-02 at 4.37.14 PM (1).png>)

{% code lineNumbers="true" %}
```swift
//
//  RightBarButtonManager.swift
//  App12
//
//  Created by Sakib Miazi on 6/2/23.
//

import UIKit
import FirebaseAuth

extension ViewController{
    func setupRightBarButton(isLoggedin: Bool){
        if isLoggedin{
            //MARK: user is logged in...
            let barIcon = UIBarButtonItem(
                image: UIImage(systemName: "rectangle.portrait.and.arrow.forward"),
                style: .plain,
                target: self,
                action: #selector(onLogOutBarButtonTapped)
            )
            let barText = UIBarButtonItem(
                title: "Logout",
                style: .plain,
                target: self,
                action: #selector(onLogOutBarButtonTapped)
            )
            
            navigationItem.rightBarButtonItems = [barIcon, barText]
            
        }else{
            //MARK: not logged in...
            let barIcon = UIBarButtonItem(
                image: UIImage(systemName: "person.fill.questionmark"),
                style: .plain,
                target: self,
                action: #selector(onSignInBarButtonTapped)
            )
            let barText = UIBarButtonItem(
                title: "Sign in",
                style: .plain,
                target: self,
                action: #selector(onSignInBarButtonTapped)
            )
            
            navigationItem.rightBarButtonItems = [barIcon, barText]
        }
    }
    
    @objc func onSignInBarButtonTapped(){
        
    }
    
    @objc func onLogOutBarButtonTapped(){
        
    }
    
}
```
{% endcode %}

## setupRightBarButton(isLoggedin: Bool)

In the above code:

* Depending on whether there is a signed-in user or not, we change the appearance and behavior of the right bar button. If the user is signed in, we display the logout button; else, we display the sign-in button.
* In both cases, we add two buttons to do the same tasks. If you look at lines 28 and 45, we add the pair of buttons together.
* For the logout buttons, the action would be `onLogOutBarButtonTapped()` method, and for the sign-in buttons, the action would be `onSignInBarButtonTapped()` method.

## onSignInBarButtonTapped()

When the sign-in bar button is tapped, we need to display an alert with the text fields to let the user sign in. It should have two buttons: 'SIgn In' and 'Logout.

So we will write the following logic inside the `onSignInBarButtonTapped()` method.

{% code lineNumbers="true" %}
```swift
@objc func onSignInBarButtonTapped(){
    let signInAlert = UIAlertController(
        title: "Sign In / Register",
        message: "Please sign in to continue.",
        preferredStyle: .alert)
    
    //MARK: setting up email textField in the alert...
    signInAlert.addTextField{ textField in
        textField.placeholder = "Enter email"
        textField.contentMode = .center
        textField.keyboardType = .emailAddress
    }
    
    //MARK: setting up password textField in the alert...
    signInAlert.addTextField{ textField in
        textField.placeholder = "Enter password"
        textField.contentMode = .center
        textField.isSecureTextEntry = true
    }
    
    //MARK: Sign In Action...
    let signInAction = UIAlertAction(title: "Sign In", style: .default, handler: {(_) in
        if let email = signInAlert.textFields![0].text,
           let password = signInAlert.textFields![1].text{
            //MARK: sign-in logic for Firebase...
            
        }
    })
    
    //MARK: Register Action...
    let registerAction = UIAlertAction(title: "Register", style: .default, handler: {(_) in
        //MARK: logic to open the register screen...
        
    })
    
    //MARK: action buttons...
    signInAlert.addAction(signInAction)
    signInAlert.addAction(registerAction)
    
    self.present(signInAlert, animated: true, completion: {() in
        //MARK: hide the alerton tap outside...
        signInAlert.view.superview?.isUserInteractionEnabled = true
        signInAlert.view.superview?.addGestureRecognizer(
            UITapGestureRecognizer(target: self, action: #selector(self.onTapOutsideAlert))
        )
    })
}
@objc func onTapOutsideAlert(){
    self.dismiss(animated: true)
}
```
{% endcode %}

In the above code:

* On lines 2 through 5, we set up the title and message of the alert controller. Then on lines 7 through 19, we add two TextFields for email and password. The text fields are added to an array of text fields inside the alert controller.
* Then we define two actions for the alert controllers: "Sign In" (lines 22-28) and "Register" (lines 31-34). We need to write the logic for signing in and registering in these closures. We will write the logic momentarily.
* Then we will add the actions to the alert controller (lines 37-38).
* Then we present the alert controller (lines 40-46). In the completion closure, we write logic to handle if the user taps outside the alert. We need to dismiss the alert if the user taps outside. So, we add a Gesture Recognizer on the `superview` (the screen which popped this alert) of the alert controller. If the user taps on the super view, the alert gets dismissed.

<mark style="color:orange;">**We will keep the sign-in and register logic empty and return to that momentarily.**</mark>

## onLogOutBarButtonTapped()

Now, when the user taps on the logout right bar button, we need to confirm that the user really wants to log out. So we need to show another alert to confirm the log-out operation. Let's write the following code in `onLogOutBarButtonTapped()` method:

```swift
@objc func onLogOutBarButtonTapped(){
    let logoutAlert = UIAlertController(title: "Logging out!", message: "Are you sure want to log out?", 
        preferredStyle: .actionSheet)
    logoutAlert.addAction(UIAlertAction(title: "Yes, log out!", style: .default, handler: {(_) in
            do{
                try Auth.auth().signOut()
            }catch{
                print("Error occured!")
            }
        })
    )
    logoutAlert.addAction(UIAlertAction(title: "Cancel", style: .cancel))
    
    self.present(logoutAlert, animated: true)
}
```

### **In the above code, we use a different alert controller style, ".actionSheet". An action sheet pops up from the bottom edge.**

* If the user taps on the action 'Yes, Log out!' we call the Firebase authentication service to log the current user out.
* If the user wats to stay logged in, they can tap 'Cancel.'

## Patching ViewController to display the Right Bar Buttons

We still need to display the Right Bar buttons on the Main Screen. So open up the ViewController.swift file and update the `handleAuth` closures to manage the sign-in and logout bar buttons:

```swift
//
//  ViewController.swift
//  App12
//
//  Created by Sakib Miazi on 6/1/23.
//
//codes omitted....
override func viewWillAppear(_ animated: Bool) {
    super.viewWillAppear(animated)
    
    //MARK: handling if the Authentication state is changed (sign in, sign out, register)...
    handleAuth = Auth.auth().addStateDidChangeListener{ auth, user in
        if user == nil{
            //MARK: not signed in...
            
            //codes omitted...
            //MARK: Sign in bar button...
            self.setupRightBarButton(isLoggedin: false)
            
        }else{
            //MARK: the user is signed in...
            
            //codes omitted...
            //MARK: Logout bar button...
            self.setupRightBarButton(isLoggedin: true)
            
        }
    }
}
```

See in the above code:

* If the user is not signed-in, we set up the right bar button with the parameter `isLoggedin` as false.
* Conversely, if the user is signed-in, we set up the right bar button with the parameter `isLoggedin` as true.

Now run the app again!

<figure><img src="/gitbook-assets/12.three (1).gif" alt=""><figcaption></figcaption></figure>



<!-- Merged from 12.3.2.-progress-activity-indicator.md -->

# 12.3.2. Progress Activity Indicator

If you noticed, when we clicked on the Register button, the UI was stuck for a few seconds as we were waiting for the create user operation to complete. In these cases, the user may get confused if we do not give the users a cue that the backend is working on their request. So we want to implement a loading screen with a progress indicator so that the user can understand the app is working in the backend to complete their request. Like this:

<figure><img src="/gitbook-assets/123.four (1).gif" alt=""><figcaption></figcaption></figure>

## Defining a Progress Activity Indicator

We will use a UI element in iOS called `UIActivityIndicatorView` to display the loading screen. Since we may reuse the same `UIActivityIndicatorView` for multiple backend tasks, we will write separate code to create the instance of it.

Let's create a new group called 'Progress Indicator' in the files navigator of Xcode. Then add two files in the group: ProgressSpinnerViewController.swift and ProgressSpinnerDelegate.swift.

![](</gitbook-assets/Screenshot 2023-06-02 at 9.23.32 PM (1).png>)

### ProgressSpinnerViewController.swift

Let's open ProgressSpinnerViewController.swift file and put the following code there:

{% code lineNumbers="true" %}
```swift
//
//  ProgressSpinnerViewController.swift
//  App12
//
//  Created by Sakib Miazi on 6/2/23.
//

import UIKit

class ProgressSpinnerViewController: UIViewController {
    
    var activityIndicator: UIActivityIndicatorView!

    override func viewDidLoad() {
        super.viewDidLoad()
        activityIndicator = UIActivityIndicatorView(style: .large)
        activityIndicator.color = .orange
        activityIndicator.translatesAutoresizingMaskIntoConstraints = false
        activityIndicator.startAnimating()
        
        view.backgroundColor = UIColor.lightGray.withAlphaComponent(0.25)
        view.addSubview(activityIndicator)
        
        activityIndicator.centerXAnchor.constraint(equalTo: view.centerXAnchor).isActive = true
        activityIndicator.centerYAnchor.constraint(equalTo: view.centerYAnchor).isActive = true
        
    }

}
```
{% endcode %}

In the above code:

* On line 12, we declare a variable of type `UIActivityIndicatorView`.
* On line 16, we create the instance of the indicator view and define its style as large. You can play with multiple different styles.
* On line 17, we define the color of the indicator as orange. (Yes, a weird choice, you can define any color you want to).
* On line 19, we say when this indicator view is loaded, start the 'loading' animation.
* We set the background color on lines 21 through 22 and attached the indicator to the current view.
* Then we anchor the indicator to the center of the screen.

Now that we set up the indicator view, we must define a protocol to control it from other screens.

### ProgressSpinnerDelegate.swift

Let's open ProgressSpinnerDelegate.swift file and put the following protocol there:

```swift
//
//  ProgressSpinnerDelegate.swift
//  App12
//
//  Created by Sakib Miazi on 6/2/23.
//

import Foundation

protocol ProgressSpinnerDelegate{
    func showActivityIndicator()
    func hideActivityIndicator()
}
```

So any class that wants to display the progress indicator view, must adopt `ProgressSpinnerDelegate` protocol and define the following two methods:

* showActivityIndicator()
* hideActivityIndicator()

## Displaying the Progress Indicator View while Registering a User

In our case, when a user clicks on the register button, the app should display the indicator view, and when the user is created, and their profile is updated, we will remove it.

We need to do a few tasks.

### **First**, open the 'RegisterViewController.swift' file.

Create an instance of `ProgressSpinnerViewController`.

<pre class="language-swift"><code class="lang-swift">//
//  RegisterViewController.swift
//  App12
//
//  Created by Sakib Miazi on 6/2/23.
//

<strong>//codes omitted...
</strong>
class RegisterViewController: UIViewController {
    
    //codes omitted...
    let childProgressView = ProgressSpinnerViewController()
    
    //codes omitted...
}

</code></pre>

### **Secondly,** let's create a new file, 'RegisterProgressIndicatorManager.swift' in the 'Register Screen' group.

![](</gitbook-assets/Screenshot 2023-06-02 at 9.58.51 PM (1).png>)

Add the following code there:

{% code lineNumbers="true" %}
```swift
//
//  RegisterProgressIndicatorManager.swift
//  App12
//
//  Created by Sakib Miazi on 6/2/23.
//

import Foundation

extension RegisterViewController:ProgressSpinnerDelegate{
    func showActivityIndicator(){
        addChild(childProgressView)
        view.addSubview(childProgressView.view)
        childProgressView.didMove(toParent: self)
    }
    
    func hideActivityIndicator(){
        childProgressView.willMove(toParent: nil)
        childProgressView.view.removeFromSuperview()
        childProgressView.removeFromParent()
    }
}
```
{% endcode %}

In the above code, we adopt the `ProgressSpinnerDelegate` protocol and define the show and hide methods.

* In the `showActivityIndicator()` method:
  * We add the indicator as a child view of the current view on lines 12 and 13.
  * Then we call `didMove(toParent: self)` method to attach and display the indicator on top of the current view.
* In the `hideActivityIndicator()` method:
  * We detach the indicator on line 18.
  * Then we remove the indicator views from their parent on lines 19 and 20.

### Thirdly, edit RegisterFirebaseManager.swift file

Remember the sequence of showing the progress indicator view?

* When a user clicks on the register button, the app should display the indicator view.
* And when the user is created and their profile is updated, we will remove it.

Where do we handle those tasks? - In RegisterFirebaseManager.swift file, right?

So let's edit the RegisterFirebaseManager.swift file and add a couple of lines like the following:

{% code lineNumbers="true" %}
```swift
//
//  RegisterFirebaseManager.swift
//  App12
//
//  Created by Sakib Miazi on 6/2/23.
//

import Foundation
import FirebaseAuth

extension RegisterViewController{
    
    func registerNewAccount(){
        //MARK: display the progress indicator...
        showActivityIndicator()
        //MARK: create a Firebase user with email and password...
        if let name = registerView.textFieldName.text,
           let email = registerView.textFieldEmail.text,
           let password = registerView.textFieldPassword.text{
            //Validations....
            Auth.auth().createUser(withEmail: email, password: password, completion: {result, error in
                if error == nil{
                    //MARK: the user creation is successful...
                    self.setNameOfTheUserInFirebaseAuth(name: name)
                }else{
                    //MARK: there is a error creating the user...
                    print(error)
                }
            })
        }
    }
    
    //MARK: We set the name of the user after we create the account...
    func setNameOfTheUserInFirebaseAuth(name: String){
        let changeRequest = Auth.auth().currentUser?.createProfileChangeRequest()
        changeRequest?.displayName = name
        changeRequest?.commitChanges(completion: {(error) in
            if error == nil{
                //MARK: the profile update is successful...
                
                //MARK: hide the progress indicator...
                self.hideActivityIndicator()
                
                //MARK: pop the current controller...
                self.navigationController?.popViewController(animated: true)
            }else{
                //MARK: there was an error updating the profile...
                print("Error occured: \(String(describing: error))")
            }
        })
    }
}
```
{% endcode %}

In the above code:

* On line 15, before we start creating the request for creating a user, we show the progress indicator.
* Online 42, after the profile update is done, we hide the progress indicator.

If you run the application now, you will see that the progress indicator is working!

<figure><img src="/gitbook-assets/12.five (1).gif" alt=""><figcaption></figcaption></figure>



<!-- Merged from 12.3.2.-register-screen-create-a-user-in-firebase.md -->

# 12.5.2. Register Screen: Create a user in Firebase

Let's design the Register Screen to let the user create an account. It will look like the following:

<figure><img src="/gitbook-assets/12.three.2 (1).gif" alt=""><figcaption></figcaption></figure>

The Register Screen design is very simple; we have three text fields to put the name, email, and password so that the user can create an account with them.

## RegisterView.swift

Let's create a new Group named "Register Screen." Create another group "Views" inside the "Register Screen" group. Add a file named "RegisterView.swift" in it.

![](</gitbook-assets/Screenshot 2023-06-02 at 5.55.46 PM (2).png>)

Put the following code to create the view for the Register screen:

```swift
//
//  RegisterView.swift
//  App12
//
//  Created by Sakib Miazi on 6/2/23.
//

import UIKit

class RegisterView: UIView {
    var textFieldName: UITextField!
    var textFieldEmail: UITextField!
    var textFieldPassword: UITextField!
    var buttonRegister: UIButton!
    
    override init(frame: CGRect){
        super.init(frame: frame)
        self.backgroundColor = .white
        setuptextFieldName()
        setuptextFieldEmail()
        setuptextFieldPassword()
        setupbuttonRegister()
        
        initConstraints()
    }
    
    func setuptextFieldName(){
        textFieldName = UITextField()
        textFieldName.placeholder = "Name"
        textFieldName.keyboardType = .default
        textFieldName.borderStyle = .roundedRect
        textFieldName.translatesAutoresizingMaskIntoConstraints = false
        self.addSubview(textFieldName)
    }
    
    func setuptextFieldEmail(){
        textFieldEmail = UITextField()
        textFieldEmail.placeholder = "Email"
        textFieldEmail.keyboardType = .emailAddress
        textFieldEmail.borderStyle = .roundedRect
        textFieldEmail.translatesAutoresizingMaskIntoConstraints = false
        self.addSubview(textFieldEmail)
    }
    
    func setuptextFieldPassword(){
        textFieldPassword = UITextField()
        textFieldPassword.placeholder = "Password"
        textFieldPassword.textContentType = .password
        textFieldPassword.isSecureTextEntry = true
        textFieldPassword.borderStyle = .roundedRect
        textFieldPassword.translatesAutoresizingMaskIntoConstraints = false
        self.addSubview(textFieldPassword)
    }
    
    func setupbuttonRegister(){
        buttonRegister = UIButton(type: .system)
        buttonRegister.setTitle("Register", for: .normal)
        buttonRegister.titleLabel?.font = .boldSystemFont(ofSize: 16)
        buttonRegister.translatesAutoresizingMaskIntoConstraints = false
        self.addSubview(buttonRegister)
    }
    
    func initConstraints(){
        NSLayoutConstraint.activate([
            textFieldName.topAnchor.constraint(equalTo: self.safeAreaLayoutGuide.topAnchor, constant: 32),
            textFieldName.centerXAnchor.constraint(equalTo: self.safeAreaLayoutGuide.centerXAnchor),
            textFieldName.widthAnchor.constraint(equalTo: self.safeAreaLayoutGuide.widthAnchor, multiplier: 0.9),
            
            textFieldEmail.topAnchor.constraint(equalTo: textFieldName.bottomAnchor, constant: 16),
            textFieldEmail.centerXAnchor.constraint(equalTo: self.safeAreaLayoutGuide.centerXAnchor),
            textFieldEmail.widthAnchor.constraint(equalTo: self.safeAreaLayoutGuide.widthAnchor, multiplier: 0.9),
            
            textFieldPassword.topAnchor.constraint(equalTo: textFieldEmail.bottomAnchor, constant: 16),
            textFieldPassword.centerXAnchor.constraint(equalTo: self.safeAreaLayoutGuide.centerXAnchor),
            textFieldPassword.widthAnchor.constraint(equalTo: self.safeAreaLayoutGuide.widthAnchor, multiplier: 0.9),
            
            buttonRegister.topAnchor.constraint(equalTo: textFieldPassword.bottomAnchor, constant: 32),
            buttonRegister.centerXAnchor.constraint(equalTo: self.safeAreaLayoutGuide.centerXAnchor),
        ])
    }
    
    required init?(coder: NSCoder) {
        fatalError("init(coder:) has not been implemented")
    }
}
```

The above code is very straightforward to display three text fields: name, email, password, and a register button.

## RegisterViewController.swift

Then let's create RegisterViewController.swift file to write code for controlling the Register screen.

{% code lineNumbers="true" %}
```swift
//
//  RegisterViewController.swift
//  App12
//
//  Created by Sakib Miazi on 6/2/23.
//

import UIKit
import FirebaseAuth
import FirebaseFirestore

class RegisterViewController: UIViewController {

    let registerView = RegisterView()
    
    override func loadView() {
        view = registerView
    }
    override func viewDidLoad() {
        super.viewDidLoad()
        navigationController?.navigationBar.prefersLargeTitles = true
        registerView.buttonRegister.addTarget(self, action: #selector(onRegisterTapped), for: .touchUpInside)
        title = "Register"
    }
    
    @objc func onRegisterTapped(){
        //MARK: creating a new user on Firebase...
        //registerNewAccount()
    }
    
    
}
```
{% endcode %}

In the above code:

* We have added the `onRegisterTapped()` method to handle if the Register button is tapped. We need to patch the Firebase code on line 30.

## RegisterFirebaseManager.swift

We will separate the code for Firebase from the controller. Let's create a new file `Register Screen -> RegisterFirebaseManager.swift`.

![](</gitbook-assets/Screenshot 2023-06-02 at 7.09.24 PM (1).png>)

In this file, we will handle the Firebase Authentication procedures.

### Firebase Authentication

Please visit the following documentation for using the Firebase Authentication service in iOS: [https://firebase.google.com/docs/auth/ios/start](https://firebase.google.com/docs/auth/ios/start). First look at their official documentation. If you are confused, ask us.

We have to do the following tasks:

* We need to register the user using email and password.
* Then we will update the profile's display name.

So, let's write the following code in RegisterFirebaseManager.swift file:

{% code lineNumbers="true" %}
```swift
//
//  RegisterFirebaseManager.swift
//  App12
//
//  Created by Sakib Miazi on 6/2/23.
//

import Foundation
import FirebaseAuth

extension RegisterViewController{
    
    func registerNewAccount(){
        //MARK: create a Firebase user with email and password...
        if let name = registerView.textFieldName.text,
           let email = registerView.textFieldEmail.text,
           let password = registerView.textFieldPassword.text{
            //Validations....
            Auth.auth().createUser(withEmail: email, password: password, completion: {result, error in
                if error == nil{
                    //MARK: the user creation is successful...
                    self.setNameOfTheUserInFirebaseAuth(name: name)
                }else{
                    //MARK: there is a error creating the user...
                    print(error)
                }
            })
        }
    }
    
    //MARK: We set the name of the user after we create the account...
    func setNameOfTheUserInFirebaseAuth(name: String){
        let changeRequest = Auth.auth().currentUser?.createProfileChangeRequest()
        changeRequest?.displayName = name
        changeRequest?.commitChanges(completion: {(error) in
            if error == nil{
                //MARK: the profile update is successful...
                self.navigationController?.popViewController(animated: true)
            }else{
                //MARK: there was an error updating the profile...
                print("Error occured: \(String(describing: error))")
            }
        })
    }
}

```
{% endcode %}

In the above code:

### <mark style="color:purple;">(Creating a new User in Firebase)</mark>

* The `registerNewAccount()` method creates a new account using Firebase Authentication service.
  * You have to import the authentication library `FirebaseAuth` (line 9).
  * Then on lines 14 through 17, we read the text fields to unwrap name, email, and password.
  * Then you need to validate the user inputs; I am omitting it here.
  * Then we call `Auth.auth().createUser(withEmail:...)` to send a request to the Firebase Authentication service to create a user with email and password.
  * In the `completion` closure, we will handle the response from the Firebase server.
    * There are two parameters of the response: result and error.
    * Then we check if the error is nil, meaning if there is no error. If there is no error, we decide that the response was successful, and the user is created.
      * Please note we cannot set the profile data in a FirebaseAuth account while creating the account. It can create just an account with the email and password. Then we have to update the profile with the name provided by the user in `setNameOfTheUserInFirebaseAuth()` method.
    * Else we have to handle the error.

### <mark style="color:purple;">(Updating a User Profile in Firebase)</mark>

* The `setNameOfTheUserInFirebaseAuth(name: String)` method updates the profile of the created user. (See [https://firebase.google.com/docs/auth/ios/manage-users#update\_a\_users\_profile](https://firebase.google.com/docs/auth/ios/manage-users#update\_a\_users\_profile)).
  * On line 33, we create a change request for the current FirebaseAuth user.
  * On line 34, we set the intended name of the user in the change request.
  * Then on line 35, we commit the changes with a request.
    * The `completion` closure handles what happens after the profile update.
    * If there is no error, the response returns a nil error. So, here we can certainly say that the profile has been updated.
    * Since all the tasks are done, we can close the register screen and return to the main screen (line 38).

<mark style="color:red;">**Very important:**</mark> <mark style="color:red;">Firebase calls are asynchronous, requiring network communications and server processing.</mark> <mark style="color:red;">**So the sequence of events is very important. You must wait until one operation is done, then conduct the next operation.**</mark> <mark style="color:red;">We cannot create a Firebase user and update profile operations together. We have to wait for the user to be created first. If the response is successful and the user is created, we update the profile. You must think carefully before writing codes and maintain the chain of Firebase calls correctly to avoid errors.</mark>

### RegisterViewController.swift

Now we need to handle when the user taps on the Register button. We need to call `registerNewAccount()` method from `onRegisterTapped()` method in RegisterViewMethod.swift file.\\

Open RegisterViewController.swift file, and update the `onRegisterTapped` method.

```swift
@objc func onRegisterTapped(){
    //MARK: creating a new user on Firebase...
    registerNewAccount()
}
```

## Patching the Main Screen to Show Register Screen

Open RightBarButtonManager.swift file. Now, we need to write the logic for opening the Register Screen in `registerAction` AlertAction. We will add the following codes:

```swift
//
//  RightBarButtonManager.swift
//  App12
//
//  Created by Sakib Miazi on 6/2/23.
//

//codes omitted...

extension ViewController{
    func setupRightBarButton(isLoggedin: Bool){
        //codes omitted...
    }
    
    @objc func onSignInBarButtonTapped(){
        //codes omitted...
        
        //MARK: Register Action...
        let registerAction = UIAlertAction(title: "Register", style: .default, handler: {(_) in
            //MARK: logic to open the register screen...
            let registerViewController = RegisterViewController()
            self.navigationController?.pushViewController(registerViewController, animated: true)
        })
        
        //codes omitted...
    }
    //codes omitted...   
}
```

If you run the app now, you will see:

<figure><img src="/gitbook-assets/12.three.3 (1).gif" alt=""><figcaption></figcaption></figure>

If you now look into the Firebase Authentication portal,

<figure><img src="/gitbook-assets/Screenshot 2023-06-02 at 9.06.25 PM (1).png" alt=""><figcaption></figcaption></figure>



<!-- Merged from 12.3.3.-implementing-sign-in.md -->

# 12.3.3. Implementing Sign In

Now it's time to sign in with an already created user.

We just need to add a few lines of code inside `RightBarButtonManager.swift` file inside the `signInAction` alert action:

{% code lineNumbers="true" %}
```swift
//
//  RightBarButtonManager.swift
//  App12
//
//  Created by Sakib Miazi on 6/2/23.
//

import UIKit
import FirebaseAuth

extension ViewController{
    func setupRightBarButton(isLoggedin: Bool){
        //code omitted...
    }
    
    @objc func onSignInBarButtonTapped(){
        //codes omitted...
        
        //MARK: Sign In Action...
        let signInAction = UIAlertAction(title: "Sign In", style: .default, handler: {(_) in
            if let email = signInAlert.textFields![0].text,
               let password = signInAlert.textFields![1].text{
                //MARK: sign-in logic for Firebase...
                self.signInToFirebase(email: email, password: password)
            }
        })
        //codes omitted...
    }
    //codes omitted...
    func signInToFirebase(email: String, password: String){
        //MARK: can you display progress indicator here?
        //MARK: authenticating the user...
        Auth.auth().signIn(withEmail: email, password: password, completion: {(result, error) in
            if error == nil{
                //MARK: user authenticated...
                //MARK: can you hide the progress indicator here?
            }else{
                //MARK: alert that no user found or password wrong...
            }      
        })
    }
}


```
{% endcode %}

Here:

* We add line 24 to call a method to sign in to an existing account.
* On lines 30 through 41, we define the `signInToFirebase` method. If there is no error, then great! We will load the homepage with the signed-in user. Else, display an alert to notify the user that the email or password was wrong.

If we run the app now, you will see:

<figure><img src="/gitbook-assets/12.six (1).gif" alt=""><figcaption></figcaption></figure>

_<mark style="color:purple;">**Can you display a progress indicator while the login operation is happening?**</mark>_

## App12 code so far:

{% file src="/gitbook-assets/App12_auth.zip" %}

