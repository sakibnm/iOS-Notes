# Module 07: Cloud Integrations And Maps

## Table of Contents




### CocoaPods

**Estimated effort:** 1-2 hours this topic
**Format:** Asynchronous online
**Prerequisites:** Previous iOS topics


**🎯 Topic Mission:** 
In this module, we will explore **CocoaPods** and learn how to integrate it into our iOS applications. Your mission is to understand the mechanics behind this concept and write robust Swift code.


---

## Learning Objectives

By the end of this session, you will be able to:
1. Understand the core concepts of CocoaPods.
2. Implement CocoaPods in an Xcode project.
3. Apply best practices to ensure clean and maintainable code.

---

## The Story So Far...

We have been progressively building our knowledge of iOS and Swift. In this module, we will expand our toolkit by diving into CocoaPods. 
Open your current Xcode project or start a new Playground to follow along with the hands-on material.

---

## Walkthrough: Exploring CocoaPods

> 📁 **Target Project** — Follow along by building the mini-app presented in the steps below, or integrate these concepts into your own ongoing projects.

### Cocoa Pods

UIKit has thousands of modules, and we cannot learn all of them (you don't even need to). You only need to learn the most important, common, and useful ones. Then you can learn the others if you need them to solve a problem you are facing in real life.

Also, many developers build third-party modules that give generalized solutions to tricky problems, like making HTTP connections to talk to remote APIs over the Internet, building reactive screens that can deal with different sensors, etc. So, these community-built modules are also shared with others through Cocoa Pods, so you do not have to reinvent the wheels. ([https://cocoapods.org/](https://cocoapods.org/)).

**Caution: You must be cautious since CocoaPods are not developed and released by Apple.**

* The cocoa pods are usually general-purpose modules, meaning they are the Jacks of all trades, masters of none. So, for a large application, they might create slight performance issues. For example, you might have just needed to read the byte stream from a remote API. If you use a fancy general-purpose cocoa pod library that can do many more tasks and would implement a lot of abstractions before it gives you the stream, it might be overkill for you. And if your app is time and performance sensitive, you better build your own module.
* Not all of the modules can be trusted since community members openly share these, and not many of us test all of them. **Only use the most common and reputed ones. (Google might help you find them).**
* **Only use the ones that get updated often.** Many of the modules in Cocoa Pods seem useful, yet weren't been updated in the last couple of years. **Do not use them.** First, Swift gets updates very _**swiftly**_, so even if the module works today, the underlying libraries are probably deprecated. So, if they stop working tomorrow, you need to build your own module anyway. \ Secondly, older modules risk being vulnerable regarding security, privacy, and overall code safety.

(Enough of being cautious) However, Cocoa Pods have some of the very best modules; those are even used in the industry. For example, AlamoFire is a beginner-friendly module that can be used to connect your app to the Internet and talk to the API servers. It is a general-purpose module that is used by millions of developers and very often gets updates and support from many contributors worldwide.

Here we will see how to integrate Cocoa Pod modules into our app.




### Installing Cocoa Pods

Let's visit the web page [https://cocoapods.org/](https://cocoapods.org/).

[View Resource](https://cocoapods.org/)

It should open a page like this:

<figure><img src="/gitbook-assets/Screenshot 2023-05-24 at 12.27.12 PM (1).png" alt="Educational illustration for iOS concept"><figcaption></figcaption></figure>

Now let's open the Terminal app on your Mac.

* Press `command` ⌘ `+` `Space` and it'll open the Spotlight search.
* Type "Terminal," and it should find the Terminal app for you.
* Press the return key to open it.

<figure><img src="/gitbook-assets/9.1 (1).gif" alt="Educational illustration for iOS concept"><figcaption></figcaption></figure>

### **There are two ways of installing CocoaPods on your Mac:**

### Using the command in cocoapods.org:

* Copy the command (`sudo gem install cocoapods`) from the CocoaPods webpage and paste it into the Terminal. Put in your password and press return. It should install CocoaPods. After installation is done, put the command `pod --version` into your terminal. It should show something like: `1.12.1`. If you see that, you are done installing CocoaPods on your Mac.

#### **2. If the above method doesn't work and your Terminal is not responding, try the following (more stable) method:**

* **Install Homebrew on your Mac:** **Homebrew** is an alternative (Linux-like) package manager for Mac. It is very widely used and quite useful to install open-sourced software packages.
  * Visit: [https://github.com/Homebrew/install](https://github.com/Homebrew/install)
  * Copy the terminal command posted there: `/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"`.
  * Paste it into your Terminal.
  * Press the return key.
  * Put in your Mac password.
  * It should install **homebrew** on your Mac.
* **Install CocoaPods using Homebrew:**
  * Open your Terminal and put the following command there:
    * `brew install cocoapods`
  * Press the return key.
  * It should be installing **CocoaPods** on your Mac.
  * After it's done, put the following command `pod --version` into your terminal. It should show something like the following: `1.12.1`. If you see that, you are done installing CocoaPods on your Mac.

<figure><img src="/gitbook-assets/9.two (2).gif" alt="Educational illustration for iOS concept"><figcaption></figcaption></figure>



### Integrating CocoaPods into a Project

Let's create a new project App9 in Xcode. We will not write any code here; we will just use it to see how we can integrate cocoa pods into the project.

**The setup part might look a little bit tricky, but it's really easy.**

* **After you create the project, remember the directory you store the project into.**
* Open the directory using FInder (file browser on Mac). Browse to the directory (folder) where you saved the project. Do not get into the directory yet. So, you should be in the parent directory of the project directory now.
* Open Terminal.
* Type `cd` and put a space. **Do not press return yet.**
* Drag and drop the project directory onto the Terminal. You will see the path to the directory is pasted on the Terminal after `cd`.
* Press return. Now you should be in the project directory through Terminal.
* Type `ls` and press return. You will see the project files in the Terminal.

<figure><img src="/gitbook-assets/9.one (1).gif" alt="Educational illustration for iOS concept"><figcaption></figcaption></figure>

* Now, type in `pod init` command on Terminal.
* Open Finder again. You will see that there is a file called **Podfile** has been created.

<figure><img src="/gitbook-assets/9.4 (1).gif" alt="Educational illustration for iOS concept"><figcaption></figcaption></figure>

* Now open the Podfile with your favorite text editor.
* You will see a line `# Pods for App9`. You can add modules after the line.

<figure><img src="/gitbook-assets/9.5 (1).gif" alt="Educational illustration for iOS concept"><figcaption></figcaption></figure>

### Adding a CocoaPod module, Alamofire, to our project

As I said before, Alamofire is a widely used module for beginners to manage Internet data transmission. We will integrate Alamofire to App9.

* Visit [https://cocoapods.org](https://cocoapods.org).
* Search for Alamofire. On top of the search results, you will see something like '**Alamofire 5.6.4.'**
* Click on the button to the right, 'Site.'
* It will load the main project site in Github.

<figure><img src="/gitbook-assets/9.6 (2).gif" alt="Educational illustration for iOS concept"><figcaption></figcaption></figure>

* If you scroll down to **Installation,** you will see the instructions of how to install Alamofire using CocoaPods. Copy the line that says: `pod 'Alamofire'`.
* Open the Podfile we have seen before.
* Paste the line after `# Pods for App9`.

<figure><img src="/gitbook-assets/9.7.gif" alt="Educational illustration for iOS concept"><figcaption></figcaption></figure>

* Now go back to the Terminal again. Go to the project directory if you are not there (see above if you forgot how to).
* Put the following command onto the Terminal: `pod install`.
* You will see, depending on the modules you added to the Podfile, it will install them. When it's done installing the pods, in this case, it is Alamofire, your project can use this CocoaPod module.

**Now, the final step is to be able to use the module. The following part is very important. We often forget to do that and the modules do not work in code.**

* Now, what you have to do is, **close the Xcode project.**
* Open the project directory again.
* **Do not open the .xcodeproj file.** **Open the .xcworkspace file for this project.**
* **Once you install a third-party module using CocoaPods, you must always use the workspace file (.****xcworkspace****) to open the project. Otherwise, you can't use the third-party modules.**

<figure><img src="/gitbook-assets/9.9 (1).gif" alt="Educational illustration for iOS concept"><figcaption></figcaption></figure>

**Now, we have completed adding the 'Alamofire' module to our project using CocoaPods.**

### Reference Code

[Download Project Archive](/gitbook-assets/App9_cocoapods (1).zip)

---

## Guided Practice Challenges

Before moving on to the next topic, try these low-stakes practice challenges in Xcode. They will build the exact muscle memory you need:

### Challenge 1: Experimentation
**The Scenario:** You've just learned about CocoaPods.
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


### Firebase Auth & Firestore

**Estimated effort:** 1-2 hours this topic
**Format:** Asynchronous online
**Prerequisites:** Previous iOS topics


**🎯 Topic Mission:** 
In this module, we will explore **Firebase Auth & Firestore** and learn how to integrate it into our iOS applications. Your mission is to understand the mechanics behind this concept and write robust Swift code.


---

## Learning Objectives

By the end of this session, you will be able to:
1. Understand the core concepts of Firebase Auth & Firestore.
2. Implement Firebase Auth & Firestore in an Xcode project.
3. Apply best practices to ensure clean and maintainable code.

---

## The Story So Far...

We have been progressively building our knowledge of iOS and Swift. In this module, we will expand our toolkit by diving into Firebase Auth & Firestore. 
Open your current Xcode project or start a new Playground to follow along with the hands-on material.

---

## Walkthrough: Exploring Firebase Auth & Firestore

> 📁 **Target Project** — Follow along by building the mini-app presented in the steps below, or integrate these concepts into your own ongoing projects.

### Firebase Authentication and Firestore

Firebase is a Google service portal through which Google provides users with many useful Cloud services. Firebase services are very fast, reliable, and easy to use. They have comprehensive guides for developers to integrate and build systems using their services on a plethora of platforms, like, iOS, Android, NodeJS, Flutter, Unity, etc.

**The landing portal of Firebase services is:** [https://firebase.google.com/](https://firebase.google.com/)

### Getting started with Firebase

[View Resource](https://youtu.be/1I9KMcQ_XCg)

### Enabling Authentication, Firestore, and Storage

[View Resource](https://youtu.be/gdQDxqoTT5U)

### Adding Firebase to our App

[View Resource](https://youtu.be/W0RGrDo4Bv4)

### Firestore Data Structure

[View Resource](https://youtu.be/eqW7KNChx5A)

### Firebase Official Documentation

* [**Firebase Authentication for iOS**](https://firebase.google.com/docs/auth/ios/start)
* [**Firebase Firestore for iOS**](https://firebase.google.com/docs/firestore/quickstart#ios+)
* [**Firebase Storage for iOS**](https://firebase.google.com/docs/storage/ios/start)




### App 12 with Firebase

In this module, we will build App 12, which will be a contacts list app using,

* Firebase Authentication
* Firebase Firestore

### App12: My Contacts app

The overall goal is to build an app like the following:

<figure><img src="/gitbook-assets/12.one (1).gif" alt="Educational illustration for iOS concept"><figcaption></figcaption></figure>

The app has the following features:

* The user can create an account.
* The user can sign in.
* The user can store their contacts in a database.
* They can log out.
* Each authenticated user will have a separate contacts list.

### Setting up your Firebase project in Firebase's Console

* Please set up your own Firebase project.
* Create your own App12 in Xcode.
* Add your app to Firebase project.
* Download and add the GoogleService-Info.plist to your Xcode project.
* Configure Firebase in AppDelegate.
* Patch up Firebase libraries, Auth, Firestore, FirestoreSwift, and Storage using Swift Package manager.
* Then use the code provided.
* **Otherwise, you cannot see what is happening in Firebase.**



### Setting up the Main Screen View

In this Project, we will keep the codes as modular as possible. So, let's create a new Group called 'Main Screen.' Put ViewController.swift file inside 'Main Screen.'

Then we create a new Group called 'Views' inside 'Main Screen.' Add a new file named MainScreenView.swift inside 'Views.' The structure looks like this:

![Educational illustration for iOS concept](</gitbook-assets/Screenshot 2023-06-02 at 2.39.45 PM.png>)

### MainScreenView.swift

Then open MainScreenView.swift, and the following code there:


```swift
class MainScreenView: UIView {
    var profilePic: UIImageView!
    var labelText: UILabel!
    var floatingButtonAddContact: UIButton!
    var tableViewContacts: UITableView!
    
    override init(frame: CGRect) {
        super.init(frame: frame)
        self.backgroundColor = .white
        
        setupProfilePic()
        setupLabelText()
        setupFloatingButtonAddContact()
        setupTableViewContacts()
        initConstraints()
    }
    
    //MARK: initializing the UI elements...
    func setupProfilePic(){
        profilePic = UIImageView()
        profilePic.image = UIImage(systemName: "person.circle")?.withRenderingMode(.alwaysOriginal)
        profilePic.contentMode = .scaleToFill
        profilePic.clipsToBounds = true
        profilePic.layer.masksToBounds = true
        profilePic.translatesAutoresizingMaskIntoConstraints = false
        self.addSubview(profilePic)
    }
    
    func setupLabelText(){
        labelText = UILabel()
        labelText.font = .boldSystemFont(ofSize: 14)
        labelText.translatesAutoresizingMaskIntoConstraints = false
        self.addSubview(labelText)
    }
    
    func setupTableViewContacts(){
        tableViewContacts = UITableView()
        tableViewContacts.register(ContactsTableViewCell.self, forCellReuseIdentifier: Configs.tableViewContactsID)
        tableViewContacts.translatesAutoresizingMaskIntoConstraints = false
        self.addSubview(tableViewContacts)
    }
    
    func setupFloatingButtonAddContact(){
        floatingButtonAddContact = UIButton(type: .system)
        floatingButtonAddContact.setTitle("", for: .normal)
        floatingButtonAddContact.setImage(UIImage(systemName: "person.crop.circle.fill.badge.plus")?.withRenderingMode(.alwaysOriginal), for: .normal)
        floatingButtonAddContact.contentHorizontalAlignment = .fill
        floatingButtonAddContact.contentVerticalAlignment = .fill
        floatingButtonAddContact.imageView?.contentMode = .scaleAspectFit
        floatingButtonAddContact.layer.cornerRadius = 16
        floatingButtonAddContact.imageView?.layer.shadowOffset = .zero
        floatingButtonAddContact.imageView?.layer.shadowRadius = 0.8
        floatingButtonAddContact.imageView?.layer.shadowOpacity = 0.7
        floatingButtonAddContact.imageView?.clipsToBounds = true
        floatingButtonAddContact.translatesAutoresizingMaskIntoConstraints = false
        self.addSubview(floatingButtonAddContact)
    }
    
    
    //MARK: setting up constraints...
    func initConstraints(){
        NSLayoutConstraint.activate([
            profilePic.widthAnchor.constraint(equalToConstant: 32),
            profilePic.heightAnchor.constraint(equalToConstant: 32),
            profilePic.topAnchor.constraint(equalTo: self.safeAreaLayoutGuide.topAnchor, constant: 8),
            profilePic.leadingAnchor.constraint(equalTo: self.safeAreaLayoutGuide.leadingAnchor, constant: 16),
            
            labelText.topAnchor.constraint(equalTo: profilePic.topAnchor),
            labelText.bottomAnchor.constraint(equalTo: profilePic.bottomAnchor),
            labelText.leadingAnchor.constraint(equalTo: profilePic.trailingAnchor, constant: 8),
            
            tableViewContacts.topAnchor.constraint(equalTo: profilePic.bottomAnchor, constant: 8),
            tableViewContacts.bottomAnchor.constraint(equalTo: self.safeAreaLayoutGuide.bottomAnchor, constant: -8),
            tableViewContacts.leadingAnchor.constraint(equalTo: self.safeAreaLayoutGuide.leadingAnchor, constant: 16),
            tableViewContacts.trailingAnchor.constraint(equalTo: self.safeAreaLayoutGuide.trailingAnchor, constant: -16),
            
            floatingButtonAddContact.widthAnchor.constraint(equalToConstant: 48),
            floatingButtonAddContact.heightAnchor.constraint(equalToConstant: 48),
            floatingButtonAddContact.bottomAnchor.constraint(equalTo: self.safeAreaLayoutGuide.bottomAnchor, constant: -16),
            floatingButtonAddContact.trailingAnchor.constraint(equalTo: self.safeAreaLayoutGuide.trailingAnchor, constant: -16),
            
        ])
    }
    
    required init?(coder: NSCoder) {
        fatalError("init(coder:) has not been implemented")
    }
}
```


In the above code, you should have already worked with all the elements in your previous assignments. The only new concept here is to build a floating add button at the bottom right corner of the screen. If you look at lines 77 through 80, we are setting up the constraints for that button.

* It is a regular button; we make it appear floating on the screen.
* We first fix the height and width of the floating button. (Lines 77 and 78).
* Then we fix the bottom and right anchors of the floating button to the bottom and right anchors of the safe area.
* Later, in the controller code, we will force this button to appear over all the UI elements to make it float.
* In lines 43 through 56, we add some shadow effects to make this button look like it is over the other elements.

### ContactsTableViewCell.swift

We are displaying a table view for the contacts the user saves, so we need to design a cell layout for the table view. Let's create a new file inside `Main Screen -> Views ->` named 'ContactsTableViewCell.swift.' Then add the following code there:


```swift
//
//  ContactsTableViewCell.swift
//  App12
//
//  Created by Sakib Miazi on 6/2/23.
//

import UIKit

import UIKit

class ContactsTableViewCell: UITableViewCell {
    
    var wrapperCellView: UIView!
    var labelName: UILabel!
    var labelEmail: UILabel!
    var labelPhone: UILabel!
    
    override init(style: UITableViewCell.CellStyle, reuseIdentifier: String?){
        super.init(style: style, reuseIdentifier: reuseIdentifier)
        
        setupWrapperCellView()
        setupLabelName()
        setupLabelEmail()
        setupLabelPhone()
        
        initConstraints()
    }
    
    required init?(coder: NSCoder) {
        fatalError("init(coder:) has not been implemented")
    }
    
    func setupWrapperCellView(){
        wrapperCellView = UITableViewCell()
        
        //working with the shadows and colors...
        wrapperCellView.backgroundColor = .white
        wrapperCellView.layer.cornerRadius = 6.0
        wrapperCellView.layer.shadowColor = UIColor.gray.cgColor
        wrapperCellView.layer.shadowOffset = .zero
        wrapperCellView.layer.shadowRadius = 4.0
        wrapperCellView.layer.shadowOpacity = 0.4
        wrapperCellView.translatesAutoresizingMaskIntoConstraints = false
        self.addSubview(wrapperCellView)
    }
    
    func setupLabelName(){
        labelName = UILabel()
        labelName.font = UIFont.boldSystemFont(ofSize: 20)
        labelName.translatesAutoresizingMaskIntoConstraints = false
        wrapperCellView.addSubview(labelName)
    }
    
    func setupLabelEmail(){
        labelEmail = UILabel()
        labelEmail.font = UIFont.boldSystemFont(ofSize: 14)
        labelEmail.translatesAutoresizingMaskIntoConstraints = false
        wrapperCellView.addSubview(labelEmail)
    }
    
    func setupLabelPhone(){
        labelPhone = UILabel()
        labelPhone.font = UIFont.boldSystemFont(ofSize: 14)
        labelPhone.translatesAutoresizingMaskIntoConstraints = false
        wrapperCellView.addSubview(labelPhone)
    }
    
    func initConstraints(){
        NSLayoutConstraint.activate([
            wrapperCellView.topAnchor.constraint(equalTo: self.topAnchor,constant: 10),
            wrapperCellView.leadingAnchor.constraint(equalTo: self.leadingAnchor, constant: 10),
            wrapperCellView.bottomAnchor.constraint(equalTo: self.bottomAnchor, constant: -10),
            wrapperCellView.trailingAnchor.constraint(equalTo: self.trailingAnchor, constant: -10),
            
            labelName.topAnchor.constraint(equalTo: wrapperCellView.topAnchor, constant: 8),
            labelName.leadingAnchor.constraint(equalTo: wrapperCellView.leadingAnchor, constant: 16),
            labelName.heightAnchor.constraint(equalToConstant: 20),
            labelName.widthAnchor.constraint(lessThanOrEqualTo: wrapperCellView.widthAnchor),
            
            labelEmail.topAnchor.constraint(equalTo: labelName.bottomAnchor, constant: 2),
            labelEmail.leadingAnchor.constraint(equalTo: labelName.leadingAnchor),
            labelEmail.heightAnchor.constraint(equalToConstant: 16),
            labelEmail.widthAnchor.constraint(lessThanOrEqualTo: labelName.widthAnchor),
            
            labelPhone.topAnchor.constraint(equalTo: labelEmail.bottomAnchor, constant: 2),
            labelPhone.leadingAnchor.constraint(equalTo: labelEmail.leadingAnchor),
            labelPhone.heightAnchor.constraint(equalToConstant: 16),
            labelPhone.widthAnchor.constraint(lessThanOrEqualTo: labelName.widthAnchor),
            
            wrapperCellView.heightAnchor.constraint(equalToConstant: 72)
        ])
    }

    override func awakeFromNib() {
        super.awakeFromNib()
        // Initialization code
    }

    override func setSelected(_ selected: Bool, animated: Bool) {
        super.setSelected(selected, animated: animated)

        // Configure the view for the selected state
    }

}

```


The above code is pretty straightforward; we have used the same code before. However, we still need to set up an identifier for the cell to use in the table view.

### Configs.swift

Let's create a new file named 'Configs.swift' in the project directory. We will add a static constant defining the ID of the cell. The Configs.swift file would look like this:

```swift
//
//  Configs.swift
//  App12
//
//  Created by Sakib Miazi on 6/2/23.
//

import Foundation
class Configs{
    static let tableViewContactsID = "tableViewContactsID"
}
```

The file structure looks like the following:

![Educational illustration for iOS concept](</gitbook-assets/Screenshot 2023-06-02 at 2.59.59 PM (1).png>)

Great! Now that our view is set up, we can start patching the ViewController.



### Setting up the ViewController with TableView

Now we will patch up the view to the controller. Let's open up `MainScreen -> ViewController.swift` file, and add the following code there:


```swift
//
//  ViewController.swift
//  App12
//
//  Created by Sakib Miazi on 6/1/23.
//

import UIKit

class ViewController: UIViewController {

    let mainScreen = MainScreenView()
    
    override func loadView() {
        view = mainScreen
    }
    
    override func viewDidLoad() {
        super.viewDidLoad()
        
        title = "My Contacts"
        
        //MARK: Make the titles look large...
        navigationController?.navigationBar.prefersLargeTitles = true
        
        //MARK: Put the floating button above all the views...
        view.bringSubviewToFront(mainScreen.floatingButtonAddContact)
    }
}
```


In the above code,

* On line 21, we set the title to "My Contacts."
* On line 24, we tell the navigation controller that we prefer large titles, not the default smaller ones.
* On line 27, we bring the floating button on top of all the views.

If you run the app now, it'd look like this:

![Educational illustration for iOS concept](</gitbook-assets/Screenshot 2023-06-02 at 3.09.07 PM (1).png>)

### Patching the Table View

We need to create a data model for the contacts to display them. Let's create a data model (a struct) Contact in `Data Models -> Contact.swift` file.

Create a new Group named 'Data Models' and add Contact.swift file inside.

![Educational illustration for iOS concept](</gitbook-assets/Screenshot 2023-06-02 at 3.17.58 PM (2).png>)

```swift
//
//  Contact.swift
//  App12
//
//  Created by Sakib Miazi on 6/2/23.
//

import Foundation

struct Contact: Codable{
    var name: String
    var email: String
    var phone: Int
    
    init(name: String, email: String, phone: Int) {
        self.name = name
        self.email = email
        self.phone = phone
    }
}
```

Now let's open the ViewController.swift file, and add an array of Contacts for the table view.

```swift
//
//  ViewController.swift
//  App12
//
//  Created by Sakib Miazi on 6/1/23.
//

import UIKit

class ViewController: UIViewController {
    //codes omitted...    
    
    var contactsList = [Contact]()
    //codes omitted...
}
```

### Adopting TableView protocols

Let's separate the adoption of the protocols from ViewController.swift. So, let's create a file `Main Screen -> ContactsTableViewManager.swift` and write the following code there:

![Educational illustration for iOS concept](</gitbook-assets/Screenshot 2023-06-02 at 3.24.55 PM (1).png>)

```swift
//
//  ContactsTableViewManager.swift
//  App12
//
//  Created by Sakib Miazi on 6/2/23.
//

import Foundation
import UIKit

extension ViewController: UITableViewDelegate, UITableViewDataSource{
    func tableView(_ tableView: UITableView, numberOfRowsInSection section: Int) -> Int {
        return contactsList.count
    }
    
    func tableView(_ tableView: UITableView, cellForRowAt indexPath: IndexPath) -> UITableViewCell {
        let cell = tableView.dequeueReusableCell(withIdentifier: Configs.tableViewContactsID, for: indexPath) as! ContactsTableViewCell
        cell.labelName.text = contactsList[indexPath.row].name
        cell.labelEmail.text = contactsList[indexPath.row].email
        cell.labelPhone.text = "\(contactsList[indexPath.row].phone)"
        return cell
    }
}
```

Here we are extending ViewController and adopting UITableViewDelegate and UITableViewDataSource protocols in a separate file.

Then open up ViewController.swift again, and patch the delegate and data source of the table view in ViewController.

```swift
//
//  ViewController.swift
//  App12
//
//  Created by Sakib Miazi on 6/1/23.
//

import UIKit

class ViewController: UIViewController {

    //codes omitted...        
    override func viewDidLoad() {
       //codes omitted...
        
        //MARK: patching table view delegate and data source...
        mainScreen.tableViewContacts.delegate = self
        mainScreen.tableViewContacts.dataSource = self
        
        //MARK: removing the separator line...
        mainScreen.tableViewContacts.separatorStyle = .none
        
        //codes omitted...
    }
}
```



### Authentication State Handler

Now, it's time to set up the authentication for the app. We will use the right navigation bar buttons to manage the sign-in, register, and logout operations. Before we set up those buttons, let's write the logic to handle the authentication states in the app. Let's open ViewCOntroller.swift file and write the following code there:


```swift
//
//  ViewController.swift
//  App12
//
//  Created by Sakib Miazi on 6/1/23.
//

import UIKit
import FirebaseAuth

class ViewController: UIViewController {

    //codes omitted...
    
    var handleAuth: AuthStateDidChangeListenerHandle?
    var currentUser:FirebaseAuth.User?
    
    override func loadView() {
        view = mainScreen
    }
    
    override func viewWillAppear(_ animated: Bool) {
        super.viewWillAppear(animated)
        
        //MARK: handling if the Authentication state is changed (sign in, sign out, register)...
        handleAuth = Auth.auth().addStateDidChangeListener{ auth, user in
            if user == nil{
                //MARK: not signed in...
                
            }else{
                //MARK: the user is signed in...
            }
        }
    }
    
    override func viewDidLoad() {
        super.viewDidLoad()
        //codes omitted...
    }
    
    override func viewWillDisappear(_ animated: Bool) {
        super.viewWillDisappear(animated)
        Auth.auth().removeStateDidChangeListener(handleAuth!)
    }
}
```


In the above code:

* On line 15, we create an authentication state change listener called `handleAuth`. We will use this listener to track whether any user is signed in.
* On line 16, we create a variable to keep an instance of the current signed-in Firebase user.
* Now, you can see that we are overriding two methods that we did not use before.
  * `viewWillAppear`: is a lifecycle method where you can handle the logic before the screen is loaded.
  * `viewWillDisappear`: is another lifecycle method where you can handle the logic right before the screen disappears.
* In `viewWillAppear` method, we define `handleAuth` handler with a closure to handle the authentication state changes. This closure will be automatically called every time a user signs in or logs out. In the closure, you see that we have two parameters: `auth`, and `user`. If the user is nil, there is no authenticated user; else, there is a signed-in user in the app.
* In `viewWillDisappear` method, we remove the listener from the app so that we do not run the listener infinitely.

### if user == nil

If the user is nil, meaning there is no signed-in user, we will write the following logic:

```swift
handleAuth = Auth.auth().addStateDidChangeListener{ auth, user in
    if user == nil{
        //MARK: not signed in...
        self.currentUser = nil
        self.mainScreen.labelText.text = "Please sign in to see the notes!"
        self.mainScreen.floatingButtonAddContact.isEnabled = false
        self.mainScreen.floatingButtonAddContact.isHidden = true
        
        //MARK: Reset tableView...
        self.contactsList.removeAll()
        self.mainScreen.tableViewContacts.reloadData()
        
    }else{
        //MARK: the user is signed in...
    }
}
```

In the above code,

* We hide and disable the floating add contact button because if there is no signed-in user, there is no point in having the option to add a contact.
* Then we also need to clear the local array for contacts by removing all the array elements.
* Then finally, we reload the table view to reflect the authentication state change.

### else (the user is logged in)

To handle if the user is signed in, we write logic inside the `else` closure:

```swift
handleAuth = Auth.auth().addStateDidChangeListener{ auth, user in
    if user == nil{
        //MARK: not signed in...
        //codes omitted...
        
    }else{
        //MARK: the user is signed in...
        self.currentUser = user
        self.mainScreen.labelText.text = "Welcome \(user?.displayName ?? "Anonymous")!"
        self.mainScreen.floatingButtonAddContact.isEnabled = true
        self.mainScreen.floatingButtonAddContact.isHidden = false   
    }
}
```

Here we update the local `currentUser` instance with the signed-in user. We then update the label to display the signed-in user's name and enable and display the floating add contact button.



### Firestore Structure for Storing Contacts

At this point, our authentication service is working great. Now have to design our Firestore structure to accommodate a contacts list for each user.

So, we can design the Firestore database with the following structure:

* Root Document
  * users (collection)
    * user1 (document)
      * contacts (collection)
        * contact1 (document)
        * contact2 (document)
        * contact3 (document)
        * ...
    * user2 (document)
    * user3 (document)
    * ...

We have multiple users, and each user has a list of contacts. Hence, in the above structure:

1. We have a collection named "users" in our root document, where we store the users (authenticated with FirebaseAuth) as documents.
2. Each user document will hold a collection named "contacts" to store that user's contact.
3. In the "contacts" collection, we have all the contact documents.
4. If you are confused, please revisit the video here: [#firestore-data-structure](./#firestore-data-structure "mention").

When we implement the functionalities in our app, we need to make sure we store and retrieve data following the above Firestore structure.



### Adding a New Contact

Let's focus on building the functionalities to add a new contact for a signed-in user in the app.

Let's add a new group in the file navigator, 'Add Contact Screen.' Create a file named 'AddContactViewController.swift' inside it.

Create a sub-group of 'Add Contact Screen' named 'Views' and create 'AddContactView.swift' file inside it.

![Educational illustration for iOS concept](</gitbook-assets/Screenshot 2023-06-02 at 11.30.10 PM (1).png>)

### AddContactView.swift

Let's open 'AddContactView.swift' file and write the following code there:

```swift
//
//  AddContactView.swift
//  App12
//
//  Created by Sakib Miazi on 6/2/23.
//
import UIKit

class AddContactView: UIView {
    var textFieldName: UITextField!
    var textFieldEmail: UITextField!
    var textFieldPhone: UITextField!
    var buttonAdd: UIButton!
    
    override init(frame: CGRect) {
        super.init(frame: frame)
        self.backgroundColor = .white
        
        setupTextFieldName()
        setupTextFieldEmail()
        setupTextFieldPhone()
        setupButtonAdd()
        
        initConstraints()
    }
    
    func setupTextFieldName(){
        textFieldName = UITextField()
        textFieldName.placeholder = "Name"
        textFieldName.borderStyle = .roundedRect
        textFieldName.translatesAutoresizingMaskIntoConstraints = false
        self.addSubview(textFieldName)
    }
    
    func setupTextFieldEmail(){
        textFieldEmail = UITextField()
        textFieldEmail.placeholder = "Email"
        textFieldEmail.borderStyle = .roundedRect
        textFieldEmail.translatesAutoresizingMaskIntoConstraints = false
        self.addSubview(textFieldEmail)
    }
    
    func setupTextFieldPhone(){
        textFieldPhone = UITextField()
        textFieldPhone.placeholder = "Phone"
        textFieldPhone.borderStyle = .roundedRect
        textFieldPhone.translatesAutoresizingMaskIntoConstraints = false
        self.addSubview(textFieldPhone)
    }
    
    func setupButtonAdd(){
        buttonAdd = UIButton(type: .system)
        buttonAdd.setTitle("Add", for: .normal)
        buttonAdd.setImage(.add, for: .normal)
        buttonAdd.titleLabel?.font = UIFont.boldSystemFont(ofSize: 20)
        buttonAdd.translatesAutoresizingMaskIntoConstraints = false
        self.addSubview(buttonAdd)
    }
    
    func initConstraints(){
        NSLayoutConstraint.activate([
            textFieldName.topAnchor.constraint(equalTo: self.safeAreaLayoutGuide.topAnchor, constant: 8),
            textFieldName.leadingAnchor.constraint(equalTo: self.safeAreaLayoutGuide.leadingAnchor, constant: 16),
            textFieldName.trailingAnchor.constraint(equalTo: self.safeAreaLayoutGuide.trailingAnchor, constant: -16),
            
            textFieldEmail.topAnchor.constraint(equalTo: textFieldName.bottomAnchor, constant: 8),
            textFieldEmail.leadingAnchor.constraint(equalTo: self.safeAreaLayoutGuide.leadingAnchor, constant: 16),
            textFieldEmail.trailingAnchor.constraint(equalTo: self.safeAreaLayoutGuide.trailingAnchor, constant: -16),
            
            textFieldPhone.topAnchor.constraint(equalTo: textFieldEmail.bottomAnchor, constant: 8),
            textFieldPhone.leadingAnchor.constraint(equalTo: self.safeAreaLayoutGuide.leadingAnchor, constant: 16),
            textFieldPhone.trailingAnchor.constraint(equalTo: self.safeAreaLayoutGuide.trailingAnchor, constant: -16),
            
            buttonAdd.topAnchor.constraint(equalTo: textFieldPhone.bottomAnchor, constant: 8),
            buttonAdd.leadingAnchor.constraint(equalTo: self.safeAreaLayoutGuide.leadingAnchor, constant: 16),
            buttonAdd.trailingAnchor.constraint(equalTo: self.safeAreaLayoutGuide.trailingAnchor, constant: -16),
        ])
    }
    
    required init?(coder: NSCoder) {
        fatalError("init(coder:) has not been implemented")
    }
    
}
```

The above code is straightforward as well. We have four UI elements, three text fields for the contact's name, email, and phone, and an add button to store the contact.

### AddContactViewController.swift

Open the 'AddContactViewController.swift' file. Now let's put the following code there:


```swift
//
//  AddContactViewController.swift
//  App12
//
//  Created by Sakib Miazi on 6/2/23.
//

import UIKit
import FirebaseAuth
import FirebaseFirestore
import FirebaseFirestoreSwift

class AddContactViewController: UIViewController {
    var currentUser:FirebaseAuth.User?
    
    let addContactScreen = AddContactView()
    
    override func loadView() {
        view = addContactScreen
    }
    override func viewDidLoad() {
        super.viewDidLoad()
        navigationController?.navigationBar.prefersLargeTitles = false
        title = "Add a New Contact"
        
        addContactScreen.buttonAdd.addTarget(self, action: #selector(onAddButtonTapped), for: .touchUpInside)
    }
    
    //MARK: on add button tapped....
    @objc func onAddButtonTapped(){
        let name = addContactScreen.textFieldName.text
        let email = addContactScreen.textFieldEmail.text
        let phoneText = addContactScreen.textFieldPhone.text
        
        if name == "" || email == "" || phoneText == ""{
            //alert..
        }else{
            if let phone = Int(phoneText!) {
                let contact = Contact(name: name!, email: email!, phone: phone)
                
                saveContactToFireStore(contact: contact)
            }
        }
        
    }
    
    //MARK: logic to add a contact to Firestore...
    func saveContactToFireStore(contact: Contact){
        
    }
        
}
```


In the above code:

* We import the necessary libraries:
  * FirebaseAuth - to access the details of the current user
  * FirebaseFirestore - to store data
  * FirebaseFirestoreSwift - to upload/read data using Swift Codable structs.
* On line 23, we say we prefer a small-sized title, not a large one.
* On line 26, we add an action to the add button, and the action is defined in `@objc func onAddButtonTapped()` method.
* On lines 30 through 45, we define `@objc func onAddButtonTapped()` method.
  * First, we validate the name, email, and phone number the user put in. Then we call `func saveContactToFireStore(contact: Contact)` method to upload the contact to Firestore.
* We now have to update the Contact struct a little bit to conform to the Firestore structure.
* Then we will define `func saveContactToFireStore(contact: Contact)` method.

### Updating Contact.swift

Open `DataModels -> Contact.swift` and update it like the following:


```swift
//
//  Contact.swift
//  App12
//
//  Created by Sakib Miazi on 6/2/23.
//

import Foundation
import FirebaseFirestoreSwift

struct Contact: Codable{
    @DocumentID var id: String?
    var name: String
    var email: String
    var phone: Int
    
    init(name: String, email: String, phone: Int) {
        self.name = name
        self.email = email
        self.phone = phone
    }
}

```


In the above code:

* We import FirebaseFirestoreSwift to encode and decode Swift objects to and from Firestore document objects. Each Swift Contact object will represent a contact document in Firestore.
* We adopt the Codable protocol to enable encoding and decoding.
* On line 12, you see that we added `@DocumentID var id: String?`. Do you remember that Firebase has two options for setting a document ID? You can either give an ID manually or auto-generate an ID. We need to put that declaration line to enable both to conform properly to the Firestore document structure. We are saying that the document ID of the Firestore document will be an optional string. For more clarification visit: [https://firebase.google.com/docs/firestore/solutions/swift-codable-data-mapping](https://firebase.google.com/docs/firestore/solutions/swift-codable-data-mapping).

### Uploading the Contact to Firestore

Now, let's put the following code to AddContactViewController.swift file:


```swift
//
//  AddContactViewController.swift
//  App12
//
//  Created by Sakib Miazi on 6/2/23.
//

import UIKit
import FirebaseAuth
import FirebaseFirestore
import FirebaseFirestoreSwift

class AddContactViewController: UIViewController {
    //code omitted...
    let database = Firestore.firestore()
    //code omitted...
    
    //MARK: logic to add a contact to Firestore...
    func saveContactToFireStore(contact: Contact){
        if let userEmail = currentUser!.email{
            let collectionContacts = database
                .collection("users")
                .document(userEmail)
                .collection("contacts")  
            do{
                try collectionContacts.addDocument(from: contact, completion: {(error) in
                    if error == nil{
                        self.navigationController?.popViewController(animated: true)
                    }
                })
            }catch{
                print("Error adding document!")
            }
        }
    }       
}
```


In the above code:

* On line 15, we instantiate constant `database` with the Firestore database. `database` now points to the root document in Firestore.
* We are creating a reference to the collection for the contacts of the current user on lines 21 through 24. We are trying to access
  * On lines 21-22, `database.collection("users")` to access the `users` collection where we have all the users.
    * On line 23, `.document(userEmail)` tries to access the document regarding the current user. We name (DocumentID) the document with their email address since the email will be unique to each user.
      * On line 24, `.collection("contacts")` tries to access the 'contacts' collection for that user document.
* So basically "users" collection holds all the documents regarding the users. Each document refers to a user authenticated through FirebaseAuth. Inside each user document, we have another collection named "contacts" to hold all the contacts for that user. `collectionContacts` refers to this "contacts" collection.
* From lines 25 through 33, we handle storing the contact to Firebase. Here the do-try-catch block is necessary since this is a network call, and it might create errors when adding something to Firebase if we write data with a wrong structure.
* On line 26, we call `collectionContacts.addDocument(from: contact, completion:...)` to add a contact document to `collectionContacts` reference. If you notice, we are directly uploading the data from a Swift Contact object.
* If there is no error, the add is successful, and we can now close this screen and go back to Main Screen.

### Adding Progress Activity Indicator

We can easily add the progress indicator view when storing the contact in Firestore. Let's add the following code to AddContactViewController.swift:


```swift
//
//  AddContactViewController.swift
//  App12
//
//  Created by Sakib Miazi on 6/2/23.
//

//codes omitted...

class AddContactViewController: UIViewController {
    //codes omitted...
    
    let childProgressView = ProgressSpinnerViewController()
    //codes omitted...
    
    //MARK: logic to add a contact to Firestore...
    func saveContactToFireStore(contact: Contact){
        if let userEmail = currentUser!.email{
            let collectionContacts = database
                .collection("users")
                .document(userEmail)
                .collection("contacts")
            
            //MARK: show progress indicator...
            showActivityIndicator()
            
            do{
                try collectionContacts.addDocument(from: contact, completion: {(error) in
                    if error == nil{
                        //MARK: hide progress indicator...
                        self.hideActivityIndicator()
                        
                        self.navigationController?.popViewController(animated: true)
                    }
                })
            }catch{
                print("Error adding document!")
            }
        }
    
    }
        
}

//MARK: adopting progress indicator protocol...
extension AddContactViewController:ProgressSpinnerDelegate{
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


In the above code:

* On lines 46 through 58, we are adopting the `ProgressSpinnerDelegate` protocol to display the progress indicator.
* On line 25, we show the indicator before we start storing the contact in Firestore.
* On line 31, we hide the indicator after we complete storing the contact.

### Patching with the Main Screen

Once the floating add contact button is tapped, we need to display the add contact screen. So, let's add the following lines of code to ViewController.swift file:


```swift
//
//  ViewController.swift
//  App12
//
//  Created by Sakib Miazi on 6/1/23.
//

import UIKit
import FirebaseAuth

class ViewController: UIViewController {

    //codes omitted...
    
    override func viewDidLoad() {
        super.viewDidLoad()
        
        //codes omitted...
        
        //MARK: tapping the floating add contact button...
        mainScreen.floatingButtonAddContact.addTarget(self, action: #selector(addContactButtonTapped), for: .touchUpInside)
    }
    
    //codes omitted...
    
    @objc func addContactButtonTapped(){
        let addContactController = AddContactViewController()
        addContactController.currentUser = self.currentUser
        navigationController?.pushViewController(addContactController, animated: true)
    }
}
```


In the above code:

* In `viewDidLoad()` method, we add an action to `floatingButtonAddContact` button. The action is defined in `addContactButtonTapped()` method.
* On lines 26 through 30, we populate the Add Contact screen.

Now, if we run the app, we will see:

<figure><img src="/gitbook-assets/12.seven (1).gif" alt="Educational illustration for iOS concept"><figcaption></figcaption></figure>

If we look at the Firestore console, we will see the following:

<figure><img src="/gitbook-assets/Screenshot 2023-06-03 at 1.06.35 AM (1).png" alt="Educational illustration for iOS concept"><figcaption></figcaption></figure>

<figure><img src="/gitbook-assets/Screenshot 2023-06-03 at 1.06.45 AM (1).png" alt="Educational illustration for iOS concept"><figcaption></figcaption></figure>

You can see that:

* The "users" collection contains a document called "alice@email.com". Because the current user's email is "alice@email.com."
* The "alice@email.com" document contains a collection named "contacts."
* Inside the "contacts" collection, we have contact documents (with auto-generated IDs).
* Inside each contact document, we have details of that contact as fields.



### Observing Firestore Updates: Updating the TableView

We need to update our local array of contacts if anything changes in Firestore, right? If the user adds or removes a contact, we need to update the TableView.

So we need to add an observer for Firestore contacts list updates when there is a logged-in user. The observer for Firestore data change is called a `SnapshotListener`. ([https://firebase.google.com/docs/firestore/query-data/listen?hl=en\&authuser=0#swift](https://firebase.google.com/docs/firestore/query-data/listen?hl=en\&authuser=0#swift)).

We need to update `handleAuth` (the handler to handle authentication state changes) in ViewController.swift to add an observer. Open ViewController.swift and add the following code:


```swift
//
//  ViewController.swift
//  App12
//
//  Created by Sakib Miazi on 6/1/23.
//

import UIKit
import FirebaseAuth
import FirebaseFirestore

class ViewController: UIViewController {

    //code omitted...
    let database = Firestore.firestore()
    
    override func loadView() {
        view = mainScreen
    }
    
    override func viewWillAppear(_ animated: Bool) {
        super.viewWillAppear(animated)
        
        //MARK: handling if the Authentication state is changed (sign in, sign out, register)...
        handleAuth = Auth.auth().addStateDidChangeListener{ auth, user in
            if user == nil{
               //code omitted...
                
            }else{
                //code omitted...
                
                //MARK: Observe Firestore database to display the contacts list...
                self.database.collection("users")
                    .document((self.currentUser?.email)!)
                    .collection("contacts")
                    .addSnapshotListener(includeMetadataChanges: false, listener: {querySnapshot, error in
                        if let documents = querySnapshot?.documents{
                            self.contactsList.removeAll()
                            for document in documents{
                                do{
                                    let contact  = try document.data(as: Contact.self)
                                    self.contactsList.append(contact)
                                }catch{
                                    print(error)
                                }
                            }
                            self.contactsList.sort(by: {$0.name < $1.name})
                            self.mainScreen.tableViewContacts.reloadData()
                        }
                    })
                
            }
        }
    }
    
    //code omitted...
}


```


In the above code:

* On line 10, we import `FirebaseFirestore` library.
* On line 15, we create the instance of the Firestore database.
* Inside the handleAuth's closure when a user is signed in, we add a `SnapshotListener` on lines 33 through 50.
  * Here we observe the "contacts" collection of the current user document. If anything is changed in that collection, the closure gets triggered and `querySnapshot` contains the updates.
  * Basically the `querySnapshot` contains all the current documents inside the collection we are observing.
  * We then empty our current local contacts array on line 38.
  * Then we append all the current contacts from the `querySnapshot`. in lines 39 through 47.
    * On line 41, we parse the received document and decode that according to the Contact struct (which is Codable).
  * On line 47, we sort the contacts in the alphabetic order of names.
  * Finally, on line 48, we reload the table view data.

Now let's run the app again.

<figure><img src="/gitbook-assets/12.ten (1).gif" alt="Educational illustration for iOS concept"><figcaption></figcaption></figure>

### **YAY!!! We built our first app using Firebase!!!**



### Reference Code

[Download Project Archive](/gitbook-assets/App12 (1).zip)



## Table of Contents

{{< section >}}

---

## Guided Practice Challenges

Before moving on to the next topic, try these low-stakes practice challenges in Xcode. They will build the exact muscle memory you need:

### Challenge 1: Experimentation
**The Scenario:** You've just learned about Firebase Auth & Firestore.
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


### Firebase Storage

**Estimated effort:** 1-2 hours this topic
**Format:** Asynchronous online
**Prerequisites:** Previous iOS topics


**🎯 Topic Mission:** 
In this module, we will explore **Firebase Storage** and learn how to integrate it into our iOS applications. Your mission is to understand the mechanics behind this concept and write robust Swift code.


---

## Learning Objectives

By the end of this session, you will be able to:
1. Understand the core concepts of Firebase Storage.
2. Implement Firebase Storage in an Xcode project.
3. Apply best practices to ensure clean and maintainable code.

---

## The Story So Far...

We have been progressively building our knowledge of iOS and Swift. In this module, we will expand our toolkit by diving into Firebase Storage. 
Open your current Xcode project or start a new Playground to follow along with the hands-on material.

---

## Walkthrough: Exploring Firebase Storage

> 📁 **Target Project** — Follow along by building the mini-app presented in the steps below, or integrate these concepts into your own ongoing projects.

### Firebase Storage

In this module, we will extend App12 to store images in FIrebase storage. Please review [https://github.com/sakibnm/iOS/blob/main/12.-firebase-authentication-and-firestore](https://github.com/sakibnm/iOS/blob/main/12.-firebase-authentication-and-firestore "mention") section to set up your Firebase Storage service in your Firebase services.

### App 12 extended for storage

We will extend App 12 to store images in Firestore Storage. We will do the following:

* In the Register Screen, we will have the option to pick a profile photo.
* Once we create the profile, we have to store the profile photo in Firebase Storage.
* Then, when we are on the main screen, we should see the profile photo loaded on the Screen. Like the following:

<figure><img src="/gitbook-assets/13.one (1).gif" alt="Educational illustration for iOS concept"><figcaption></figcaption></figure>




### Integrating Photo Pickers

### Updating RegisterView.swift

Let's open App 12

We need to update the Register Screen's view to accommodate the profile photo. Let's open the `Register Screen -> RegisterView.swift` file. Let's add a couple of UI elements to the view:

* labelPhoto
* buttonTakePhoto

And then update the constraints to accommodate the new elements on the screen.


```swift
//
//  RegisterView.swift
//  App12
//
//  Created by Sakib Miazi on 6/2/23.
//

import UIKit

class RegisterView: UIView {
    //codes omitted...
    var labelPhoto:UILabel!
    var buttonTakePhoto: UIButton!
    
    //codes omitted...
    
    override init(frame: CGRect){
        super.init(frame: frame)
        self.backgroundColor = .white
        //codes omitted...
        
        setuplabelPhoto()
        setupbuttonTakePhoto()
        
        //codes omitted...
        
        initConstraints()
    }
    
    //codes omitted...
    
    func setuplabelPhoto(){
        labelPhoto = UILabel()
        labelPhoto.text = "Add Profile Photo"
        labelPhoto.font = UIFont.boldSystemFont(ofSize: 14)
        labelPhoto.translatesAutoresizingMaskIntoConstraints = false
        self.addSubview(labelPhoto)
    }
    
    func setupbuttonTakePhoto(){
        buttonTakePhoto = UIButton(type: .system)
        buttonTakePhoto.setTitle("", for: .normal)
        buttonTakePhoto.setImage(UIImage(systemName: "camera.fill")?.withRenderingMode(.alwaysOriginal), for: .normal)
        //buttonTakePhoto.setImage(UIImage(systemName: "camera.fill")?.withRenderingMode(.alwaysOriginal), for: .normal)
        buttonTakePhoto.contentHorizontalAlignment = .fill
        buttonTakePhoto.contentVerticalAlignment = .fill
        buttonTakePhoto.imageView?.contentMode = .scaleAspectFit
        buttonTakePhoto.showsMenuAsPrimaryAction = true
        buttonTakePhoto.translatesAutoresizingMaskIntoConstraints = false
        self.addSubview(buttonTakePhoto)
    }
    
    //codes omitted...
    
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
            
            buttonTakePhoto.topAnchor.constraint(equalTo: textFieldPassword.bottomAnchor, constant: 16),
            buttonTakePhoto.centerXAnchor.constraint(equalTo: self.safeAreaLayoutGuide.centerXAnchor),
            //MARK: setting buttonTakePhoto's height and width..
            buttonTakePhoto.widthAnchor.constraint(equalToConstant: 100),
            buttonTakePhoto.heightAnchor.constraint(equalToConstant: 100),
            
            labelPhoto.topAnchor.constraint(equalTo: buttonTakePhoto.bottomAnchor),
            labelPhoto.centerXAnchor.constraint(equalTo: self.safeAreaLayoutGuide.centerXAnchor),
            
            buttonRegister.topAnchor.constraint(equalTo: labelPhoto.bottomAnchor, constant: 32),
            buttonRegister.centerXAnchor.constraint(equalTo: self.safeAreaLayoutGuide.centerXAnchor)
        ])
    }
    
    //codes omitted...
}

```


### Patching RegisterViewController to Pick Photo

Now we update the RegisterViewController.swift:


```swift
//
//  RegisterViewController.swift
//  App12
//
//  Created by Sakib Miazi on 6/2/23.
//

import UIKit
import PhotosUI

class RegisterViewController: UIViewController {
    
    //codes omitted...
    
    //MARK: variable to store the picked Image...
    var pickedImage:UIImage?
    //codes omitted...
    
    override func viewDidLoad() {
        super.viewDidLoad()
        //codes omitted...
        registerView.buttonTakePhoto.menu = getMenuImagePicker()
        //codes omitted...
    }
    
    //MARK: menu for buttonTakePhoto setup...
    func getMenuImagePicker() -> UIMenu{
        let menuItems = [
            UIAction(title: "Camera",handler: {(_) in
                self.pickUsingCamera()
            }),
            UIAction(title: "Gallery",handler: {(_) in
                self.pickPhotoFromGallery()
            })
        ]
        
        return UIMenu(title: "Select source", children: menuItems)
    }
    
    //MARK: take Photo using Camera...
    func pickUsingCamera(){
        let cameraController = UIImagePickerController()
        cameraController.sourceType = .camera
        cameraController.allowsEditing = true
        cameraController.delegate = self
        present(cameraController, animated: true)
    }
    
    //MARK: pick Photo using Gallery...
    func pickPhotoFromGallery(){
        //MARK: Photo from Gallery...
        var configuration = PHPickerConfiguration()
        configuration.filter = PHPickerFilter.any(of: [.images])
        configuration.selectionLimit = 1
        
        let photoPicker = PHPickerViewController(configuration: configuration)
        
        photoPicker.delegate = self
        present(photoPicker, animated: true, completion: nil)
    }
    //codes omitted...
}

```


In the above code:

* We import PhotosUI library to implement photo pickers.
* We declare a UIImage variable `pickedImage` on line 16 to keep the picked photo.
* We set up the menu items for two options: Camera and Gallery (line 22 and lines 26 through 38).
* Then as we did in [https://github.com/sakibnm/iOS/blob/main/6.-uimenu-picking-images-from-gallery-and-camera-and-uiimageview](https://github.com/sakibnm/iOS/blob/main/6.-uimenu-picking-images-from-gallery-and-camera-and-uiimageview "mention"), we define `pickUsingCamera()` and `pickPhotoFromGallery()` methods.

We still need to adopt the protocols related to PHPickerView, and UIImagePicker. We will separate the adoption of protocols from RegisterViewController.swift file.

### PhotoManager.swift

Let's create a new file PhotoManager.swift in `Register Screen` group and put the following code in it:


```swift
//
//  PhotoManager.swift
//  App12
//
//  Created by Sakib Miazi on 6/5/23.
//

import UIKit
import PhotosUI

//MARK: adopting required protocols for PHPicker...
extension RegisterViewController:PHPickerViewControllerDelegate{
    func picker(_ picker: PHPickerViewController, didFinishPicking results: [PHPickerResult]) {
        dismiss(animated: true)
        
        print(results)
        
        let itemprovider = results.map(\.itemProvider)
        
        for item in itemprovider{
            if item.canLoadObject(ofClass: UIImage.self){
                item.loadObject(
                    ofClass: UIImage.self,
                    completionHandler: { (image, error) in
                        DispatchQueue.main.async{
                            if let uwImage = image as? UIImage{
                                self.registerView.buttonTakePhoto.setImage(
                                    uwImage.withRenderingMode(.alwaysOriginal),
                                    for: .normal
                                )
                                self.pickedImage = uwImage
                            }
                        }
                    }
                )
            }
        }
    }
}

//MARK: adopting required protocols for UIImagePicker...
extension RegisterViewController: UINavigationControllerDelegate, UIImagePickerControllerDelegate{
    func imagePickerController(_ picker: UIImagePickerController, didFinishPickingMediaWithInfo info: [UIImagePickerController.InfoKey : Any]) {
        picker.dismiss(animated: true)
        
        if let image = info[.editedImage] as? UIImage{
            self.registerView.buttonTakePhoto.setImage(
                image.withRenderingMode(.alwaysOriginal),
                for: .normal
            )
            self.pickedImage = image
        }else{
            // Do your thing for No image loaded...
        }
    }
}
```


In the above code, we save the selected image in `pickedImage` variable (on lines 31 and 51).

Now that the Photo Pickers are integrated let's run the app. We should see the following:

<figure><img src="/gitbook-assets/13.two (1).gif" alt="Educational illustration for iOS concept"><figcaption></figcaption></figure>

**Note: we are making 'pick a profile photo' for the new user optional. So, a user can be created without even picking a photo.**



### Uploading the Picked Photo to Firebase Storage

We need to update the RegisterFirebaseManager.swift file to upload the picked photo to Firebase Storage.

**Firebase operations are asynchronous network calls. So we have to be very careful about the sequence of operations. We need to maintain the following sequence:**

1. Upload the picked image to Firebase Storage. We have to wait until the upload is successful and fetch the download URL of that photo.
2. Once the image upload is successful, we create the account with the email and password. We have to wait until the account is successfully created.
3. Once the account is created, we update the profile with the user's name and photo URL.

So we will overhaul the whole RegisterFirebaseManager.swift file. But before we do, we need to import the `FirebaseStorage` library and create a Firebase Storage instance in RegisterViewController.swift file, like the following:

```swift
//
//  RegisterViewController.swift
//  App12
//
//  Created by Sakib Miazi on 6/2/23.
//

import FirebaseStorage

class RegisterViewController: UIViewController {
    //codes omitted...
    let storage = Storage.storage()
    //codes omitted...
}
```

### Uploading a File to Storage: RegisterFirebaseManager.swift

Let's open the RegisterFirebaseManager.swift file and write the following code:


```swift
//
//  RegisterFirebaseManager.swift
//  App12
//
//  Created by Sakib Miazi on 6/2/23.
//

import Foundation
import FirebaseAuth
import FirebaseStorage

extension RegisterViewController{    
    func uploadProfilePhotoToStorage(){
        var profilePhotoURL:URL?
        
        //MARK: Upload the profile photo if there is any...
        if let image = pickedImage{
            if let jpegData = image.jpegData(compressionQuality: 80){
                let storageRef = storage.reference()
                let imagesRepo = storageRef.child("imagesUsers")
                let imageRef = imagesRepo.child("\(NSUUID().uuidString).jpg")
                
                let uploadTask = imageRef.putData(jpegData, completion: {(metadata, error) in
                    if error == nil{
                        imageRef.downloadURL(completion: {(url, error) in
                            if error == nil{
                                profilePhotoURL = url
                                self.registerUser(photoURL: profilePhotoURL)
                            }
                        })
                    }
                })
            }
        }else{
            registerUser(photoURL: profilePhotoURL)
        }
    }
    
    func registerUser(photoURL: URL?){
        if let name = registerView.textFieldName.text,
           let email = registerView.textFieldEmail.text,
           let password = registerView.textFieldPassword.text{
            Auth.auth().createUser(withEmail: email, password: password, completion: {result, error in
                if error == nil{
                    self.setNameAndPhotoOfTheUserInFirebaseAuth(name: name, email: email, photoURL: photoURL)
                }
            })
        }
    }
    
    func setNameAndPhotoOfTheUserInFirebaseAuth(name: String, email: String, photoURL: URL?){
        let changeRequest = Auth.auth().currentUser?.createProfileChangeRequest()
        changeRequest?.displayName = name
        changeRequest?.photoURL = photoURL
        
        print("\(photoURL)")
        changeRequest?.commitChanges(completion: {(error) in
            if error != nil{
                print("Error occured: \(String(describing: error))")
            }else{
                self.hideActivityIndicator()
                self.navigationController?.popViewController(animated: true)
            }
        })
    }
}

```


In the above code:

* We are following the sequence we talked about before.
* We extend RegisterViewController class.
* On line 10, we import the FirebaseStorage library.
* **On lines 13 through 37**, we upload the `pickedImage`.
  * Since picking a profile photo is optional for the user, we might not have a selected image. So if there is no image selected (lines 34 through 36), we directly jump to `registerUser(photoURL: profilePhotoURL)` method.
  * If the user picked an image (lines 18 through 33):
    * **Line 18:** We first get a jpeg image from the picked image. (I set the compression quality to 80%, but you can set it anywhere between 70-95%. The higher the number is, the more space it takes in the storage).
    * **Line 19:** We initiate the Firebase Storage.
    * **Line 20**: We create a folder named `imagesUsers` in the storage bucket.
    * **Line 21:** We want to add a new file in the `imageUsers` folder, right? The file new file is the image we picked. We must provide the file's name when we upload it to Firebase Storage. Here we create a unique name for the file using `NSUUID().uuidString`. `NSUUID()` is the iOS's default Universal Unique Identifier (UUID) generator. It generates 128-bit long unique IDs. We get the string value of that random UUID and name the jpeg file with it.
    * **Lines 23 through 32:** we upload the image to the Storage.
      * We are uploading the file using `putData()` method on line 23. The completion closure deals with the response from Firebase Storage.
      * On line 24, we check if the response is successful or not.
        * Now on line 25, we make a separate network call to fetch the download URL of the uploaded image.
        * On line 26, we check whether the `downloadURL()` call returns an error or not.
          * If the download URL is returned successfully, then we save the URL locally in variable `profilePhotoURL`.
          * And then, to maintain the sequence of operations correctly, we call the `registerUser()` method to register the new user with the uploaded photo.
* **Lines 39 through 49:** we create the user as before. Then on success, we call the `setNameAndPhotoOfTheUserInFirebaseAuth(name: name, email: email, photoURL: photoURL)` method to update the user profile.
* **Lines 51 through 65:** Then we create a `changeRequest` as before to update the current user profile. We set the value of `photoURL` parameter of the user profile to the download URL we fetched.
  * Lines 60 through 63: If the profile update is successful, we pop the current screen from the navigation controller.
  * (We also hide the progress activity indicator).

Now uploading files to Firebase Storage code is ready!

We must patch the RegisterViewController.swift file to call these sequence operations correctly.

### RegisterViewController.swift

Let's open the RegisterViewController.swift file again, and scroll down to `@objc func onRegisterTapped()` method. Let's put the following code in the method:

```swift
@objc func onRegisterTapped(){
    //MARK: creating a new user on Firebase with photo...
    showActivityIndicator()
    uploadProfilePhotoToStorage()
}
```

Here we are just displaying the progress activity indicator, and then calling the first method of the sequence of operations.

Now! If you run the app again, you'll see:

<figure><img src="/gitbook-assets/13.four (1).gif" alt="Educational illustration for iOS concept"><figcaption></figcaption></figure>

Let's look into the FirebaseStorage console:

<figure><img src="/gitbook-assets/13.five (2).gif" alt="Educational illustration for iOS concept"><figcaption></figcaption></figure>

So the files are getting uploaded. Now we need to display the images, and then it's done.



### Displaying Images Hosted in Cloud

Now, we know the download URL of the profile photo of the logged-in user. We will now display it in an ImageView.

We first add a custom utility for the UIImageView class using `extension` keyword. Let's create a file named 'ImageViewUtils.swift'.

<figure><img src="/gitbook-assets/Screenshot 2023-06-05 at 6.52.34 PM (1).png" alt="Educational illustration for iOS concept" width="345"><figcaption></figcaption></figure>

Put the following code there:


```swift
//
//  ImageViewUtils.swift
//  App12
//
//  Created by Sakib Miazi on 6/5/23.
//

import Foundation
import UIKit

extension UIImageView {
    //MARK: Borrowed from: https://www.hackingwithswift.com/example-code/uikit/how-to-load-a-remote-image-url-into-uiimageview
    
    func loadRemoteImage(from url: URL) {
        DispatchQueue.global().async { [weak self] in
            if let data = try? Data(contentsOf: url) {
                if let image = UIImage(data: data) {
                    DispatchQueue.main.async {
                        self?.image = image
                    }
                }
            }
        }
    }
}
```


In the above code:

* We are extending the default UIImageView class and adding `loadRemoteImage(from url: URL)` method.
* On line 15: We are creating a background task to load the cloud image. It has to be through an asynchronous background thread because it is a network call. We cannot guarantee the image getting downloaded instantly.
* If the data from the remote URL is a valid image, then we load the data as image into the UIImageView.

Now, we need to open ViewController.swift file and scroll down to `handleAuth`.

Let's add the following couple of lines of code in the file:


```swift
//
//  ViewController.swift
//  App12
//
//  Created by Sakib Miazi on 6/1/23.
//

//codes omitted...

class ViewController: UIViewController {

   //codes omitted...
    
    override func viewWillAppear(_ animated: Bool) {
        super.viewWillAppear(animated)
        
        //MARK: handling if the Authentication state is changed (sign in, sign out, register)...
        handleAuth = Auth.auth().addStateDidChangeListener{ auth, user in
            if user == nil{
               //codes omitted...
                
            }else{
                //codes omitted...
                
                //MARK: setting the profile photo...
                if let url = self.currentUser?.photoURL{
                    self.mainScreen.profilePic.loadRemoteImage(from: url)
                }
                
                //codes omitted...
                
            }
        }
    }
    
    //codes omitted...
}


```


In the above code:

* If the user is logged in on lines 26 through 28, we are checking whether the user's profile photo is nil. If it's not nil, we set the `profilePic`'s image using our custom utility.

Let's run the app now.

<figure><img src="/gitbook-assets/13.seven (1).gif" alt="Educational illustration for iOS concept"><figcaption></figcaption></figure>

### Great!!! We now know how to store and retrieve an image using Firebase Storage.

### What data can you store in a FirebaseAuth user object?

* Firebase users have a fixed set of basic properties—a unique ID, a primary email address, a name and a photo URL—stored in the project's user database, that can be updated by the user (iOS, Android, web). **You cannot add other properties to the user object directly; instead, you can store the additional properties in any other storage services, like Google Cloud Firestore.**



### Reference Code

[Download Project Archive](/gitbook-assets/App13(App 12 extension with Storage) (1).zip)

---

## Guided Practice Challenges

Before moving on to the next topic, try these low-stakes practice challenges in Xcode. They will build the exact muscle memory you need:

### Challenge 1: Experimentation
**The Scenario:** You've just learned about Firebase Storage.
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


### MapKit & Location

**Estimated effort:** 1-2 hours this topic
**Format:** Asynchronous online
**Prerequisites:** Previous iOS topics


**🎯 Topic Mission:** 
In this module, we will explore **MapKit & Location** and learn how to integrate it into our iOS applications. Your mission is to understand the mechanics behind this concept and write robust Swift code.


---

## Learning Objectives

By the end of this session, you will be able to:
1. Understand the core concepts of MapKit & Location.
2. Implement MapKit & Location in an Xcode project.
3. Apply best practices to ensure clean and maintainable code.

---

## The Story So Far...

We have been progressively building our knowledge of iOS and Swift. In this module, we will expand our toolkit by diving into MapKit & Location. 
Open your current Xcode project or start a new Playground to follow along with the hands-on material.

---

## Walkthrough: Exploring MapKit & Location

> 📁 **Target Project** — Follow along by building the mini-app presented in the steps below, or integrate these concepts into your own ongoing projects.

### UIMapKit: Working with Location and Maps

In this module, we will learn how to use location services in iOS and build a few basic utilities of UIMapKit. Our end goal is to search places nearby on a Map View and navigate to the selected place using Apple Maps.

Let's create a new project on XCode and name it App14.




### Phase 1: Displaying Map View and Current Location

### Setting up the Map View

Our landing screen will be a Map screen. In the first step, we will have a button to show the current location on the map.&#x20;

Let's create a file named MapView.swift.&#x20;

![Educational illustration for iOS concept](</gitbook-assets/Screenshot 2023-06-14 at 11.20.25 AM (1).png>)

Let's put the following code in the file:


```swift
//
//  MapView.swift
//  App14
//
//  Created by Sakib Miazi on 6/14/23.
//

import UIKit
import MapKit

class MapView: UIView {
    var mapView:MKMapView!
    var buttonLoading:UIButton!
    var buttonCurrentLocation:UIButton!
    
    override init(frame: CGRect) {
        super.init(frame: frame)
        backgroundColor = .white
        setupMapView()
        setupButtonLoading()
        setupButtonCurrentLocation()
        initConstraints()
    }
    
    func setupMapView(){
        mapView = MKMapView()
        mapView.translatesAutoresizingMaskIntoConstraints = false
        mapView.layer.cornerRadius = 10
        self.addSubview(mapView)
    }
    
    func setupButtonLoading(){
        buttonLoading = UIButton(type: .system)
        buttonLoading.setTitle(" Fetching Location...  ", for: .normal)
        buttonLoading.titleLabel?.font = UIFont.boldSystemFont(ofSize: 20)
        buttonLoading.setImage(UIImage(systemName: "circle.dotted"), for: .normal)
        buttonLoading.layer.backgroundColor = UIColor.black.cgColor
        buttonLoading.tintColor = .white
        buttonLoading.layer.cornerRadius = 10
        
        buttonLoading.layer.shadowOffset = .zero
        buttonLoading.layer.shadowRadius = 4
        buttonLoading.layer.shadowOpacity = 0.7
        
        buttonLoading.translatesAutoresizingMaskIntoConstraints = false
        
        buttonLoading.isEnabled = false
        self.addSubview(buttonLoading)
    }
    
    func setupButtonCurrentLocation(){
        buttonCurrentLocation = UIButton(type: .system)
        buttonCurrentLocation.setImage(UIImage(systemName: "location.circle"), for: .normal)
        buttonCurrentLocation.layer.backgroundColor = UIColor.lightGray.cgColor
        buttonCurrentLocation.tintColor = .blue
        buttonCurrentLocation.layer.cornerRadius = 10
        
        buttonCurrentLocation.layer.shadowOffset = .zero
        buttonCurrentLocation.layer.shadowRadius = 4
        buttonCurrentLocation.layer.shadowOpacity = 0.7
        
        buttonCurrentLocation.translatesAutoresizingMaskIntoConstraints = false
        
        self.addSubview(buttonCurrentLocation)
    }
    
    func initConstraints(){
        NSLayoutConstraint.activate([
            mapView.centerXAnchor.constraint(equalTo: self.safeAreaLayoutGuide.centerXAnchor),
            mapView.centerYAnchor.constraint(equalTo: self.safeAreaLayoutGuide.centerYAnchor),
            mapView.widthAnchor.constraint(equalTo: self.safeAreaLayoutGuide.widthAnchor, multiplier: 0.95),
            mapView.heightAnchor.constraint(equalTo: self.safeAreaLayoutGuide.heightAnchor, multiplier: 0.95),
            
            buttonLoading.centerXAnchor.constraint(equalTo: mapView.centerXAnchor),
            buttonLoading.centerYAnchor.constraint(equalTo: mapView.centerYAnchor),
            buttonLoading.widthAnchor.constraint(equalToConstant: 240),
            buttonLoading.heightAnchor.constraint(equalToConstant: 40),
            
            buttonCurrentLocation.trailingAnchor.constraint(equalTo: mapView.trailingAnchor, constant: -16),
            buttonCurrentLocation.bottomAnchor.constraint(equalTo: self.mapView.bottomAnchor, constant: -8),
            buttonCurrentLocation.heightAnchor.constraint(equalToConstant: 36),
            buttonCurrentLocation.widthAnchor.constraint(equalToConstant: 36)
        ])
    }
    
    required init?(coder: NSCoder) {
        fatalError("init(coder:) has not been implemented")
    }
}
```


In the above code:

* We import MapKit first.
* We have a MKMapView, and two UIButtons (`buttonLoading` and `buttonCurrentLocation`).
  * `buttonLoading` is just a dumb button to display the status when the location is getting fetched. You can use a Progress Activity Dialog instead of this.
* On lines 25 through 29, we initialize the map view.
  * On line 28, we set the corner radius of the map view.
* On lines 32 through 49, we define the `buttonLoading` button.
* On lines 51 through 65, we define the `buttonCurrentLocation` button.
* And finally, we initialize the constraints on lines 67 through 84.
  * Make sure you define the height and width of the map view using constraints.

### Patching the View with the Controller

Let's open the ViewController.swift file and put the following code there:

```swift
//
//  ViewController.swift
//  App14
//
//  Created by Sakib Miazi on 6/14/23.
//

import UIKit

class ViewController: UIViewController {
    let mapView = MapView()
    
    override func loadView() {
        view = mapView
    }

    override func viewDidLoad() {
        super.viewDidLoad()
        // Do any additional setup after loading the view.
    }

}

```

Let's run the app now.

<figure><img src="/gitbook-assets/Screenshot 2023-06-14 at 11.38.02 AM.png" alt="Educational illustration for iOS concept" width="188"><figcaption></figcaption></figure>

### Location Manager

Now we will work on fetching the current location and moving the camera (map frame) to that location. Let's create a new file named LocationManager.swift. ![Educational illustration for iOS concept](</gitbook-assets/Screenshot 2023-06-14 at 12.15.25 PM.png>)

Let's add the following code to the file:


```swift
//
//  LocationManager.swift
//  App14
//
//  Created by Sakib Miazi on 6/14/23.
//

import Foundation
import CoreLocation

//MARK: setting up location manager delegate...
extension ViewController: CLLocationManagerDelegate{
    func setupLocationManager(){
        //MARK: setting up location manager to get the current location...
        locationManager.delegate = self
        locationManager.desiredAccuracy = kCLLocationAccuracyBest
        locationManager.requestWhenInUseAuthorization()
        locationManager.startUpdatingLocation()
    }
    
    func locationManagerDidChangeAuthorization(_ manager: CLLocationManager) {
        //MARK: if the user either allows location while using the app or always...
        if manager.authorizationStatus == .authorizedWhenInUse
            || manager.authorizationStatus == .authorizedAlways{
            manager.requestLocation()
        }
    }
    
    func locationManager(_ manager: CLLocationManager, didUpdateLocations locations: [CLLocation]) {
        if let location = locations.first{
            mapView.buttonLoading.isHidden = true
            
        }
    }
    func locationManager(_ manager: CLLocationManager, didFailWithError error: Error) {
        print("location error: \(error.localizedDescription)")
    }
}
```


In the above code:

* We import the CoreLocation library.
* We extend the ViewController with `CLLocationManagerDelegate` protocol.&#x20;
* On lines 13 through 19 we initialize the location manager.&#x20;
  * **(We need to define the `locationManager` constant in ViewController.swift file):**
    * `let locationManager = CLLocationManager()`.
  * On line 15, we delegate the location manager to the current controller (ViewController).
  * On line 16, we set up the accuracy of GPS location for this location manager. We select the best accuracy for this app. **Remember that the best accuracy setting is not great for your device's battery.** There are many other accuracy settings like kCLLocationAccuracyHundredMeters, kCLLocationAccuracyNearestTenMeters, kCLLocationAccuracyBestForNavigation, etc. For details: [https://www.flybuy.com/understanding-location-settings-for-your-ios-and-android-apps](https://www.flybuy.com/understanding-location-settings-for-your-ios-and-android-apps).
  * On line 17, we request permission from the user to access the current location. Here I am asking for the 'while using the app' permission.
  * On line 18, we ask the location manager to seek for current location periodically. If you do not need continuous periodic location updates, you can request location only once by calling `locationManager.requestLocation()`.&#x20;
* On lines 21 through 27, we write the code for the adopted protocol method `locationManagerDidChangeAuthorization()`.&#x20;
  * First, we check if the user has given permission to access the location. If yes, then we request the location once.
* On lines 29 through 34, we implement the adopted method when `didUpdateLocations` gets triggered. When the location manager gets updated location coordinates, this method is called.
  * Basically, the location manager returns a list of locations together, since the user can be moving. We take the first one from the array here.
  * On line 31, we hide the loading button or remove the progress indicator.
  * On lines 35 through 37, we handle the error accessing the location.

### Action when the Current Location button is tapped

We need to implement the logic when the `buttonCurrentLocation` is tapped by the user. So we write `mapView.mapView.centerToLocation(location: locationManager.location!)` inside the `@objc func onButtonCurrentLocationTapped()` method in ViewController.swift file.&#x20;

The code so far in ViewController.swift file is:


```swift
//
//  ViewController.swift
//  App14
//
//  Created by Sakib Miazi on 6/14/23.
//

import UIKit
import MapKit

class ViewController: UIViewController {
    let mapView = MapView()
    
    let locationManager = CLLocationManager()
    
    override func loadView() {
        view = mapView
    }

    override func viewDidLoad() {
        super.viewDidLoad()
        
        mapView.buttonCurrentLocation.addTarget(self, action: #selector(onButtonCurrentLocationTapped), for: .touchUpInside)
        
        setupLocationManager()
    }
    
    @objc func onButtonCurrentLocationTapped(){
        if let uwLocation = locationManager.location{
            mapView.mapView.centerToLocation(location: uwLocation)
        }
    }

}
```


On lines 29 through 31, we center the map view to the current location with a radius of 1000 meters.&#x20;

* Now, it should yell at you saying could not find method `centerToLocation()`. Because MKMapView does not have `centerToLocation()` method by default. We need to extend MKMapView to center the view.

### Extending MKMapView to center the view to the current location

Let's open ViewController.swift file and add the following extension to enable centering to the current location:


```swift
//
//  ViewController.swift
//  App14
//
//  Created by Sakib Miazi on 6/14/23.
//

import UIKit
import MapKit

class ViewController: UIViewController {
    let mapView = MapView()
    let locationManager = CLLocationManager()
    //codes omitted...
}

extension MKMapView{
    func centerToLocation(location: CLLocation, radius: CLLocationDistance = 1000){
        let coordinateRegion = MKCoordinateRegion(
            center: location.coordinate,
            latitudinalMeters: radius,
            longitudinalMeters: radius
        )
        setRegion(coordinateRegion, animated: true)
    }
}

```


In the above code,

* On lines 19 through 23, we define a map region, where we define the center point of the map view to the current location. And then, we set the latitudinal and longitudinal span around the center.&#x20;

When the app loads, it still loads the entire North America. So, we need to zoom to the current location. So in ViewController.swift, after `setupLocationManager()` method we will call the `onButtonCurrentLocationTapped` method once to center the view:

```swift
    override func viewDidLoad() {
        super.viewDidLoad()
        
        mapView.buttonCurrentLocation.addTarget(self, action: #selector(onButtonCurrentLocationTapped), for: .touchUpInside)
        
        setupLocationManager()
        
        //MARK: center the map view to current location when the app loads...
        onButtonCurrentLocationTapped()
    }
    
    @objc func onButtonCurrentLocationTapped(){
        mapView.mapView.centerToLocation(location: locationManager.location!)
    }
```

### Setting up Info.plist to allow the location access

<figure><img src="/gitbook-assets/14.one.gif" alt="Educational illustration for iOS concept"><figcaption></figcaption></figure>

* Let's open Info.plist of the project.&#x20;
* Add a new row
  * The key should be: "NSLocationWhenInUseUsageDescription"
  * The value should be your explanation of why you would need this access. My explanation was: "This app requires location access to provide all the utilities.**"**

The emulator location is often set up as 'none' by default. In that case, it will not take you to a particular location. You can emulate the location of the emulator.&#x20;

### Setting the Simulator/Emulator location

* When the simulator is running, click on the Simulator Menu -> Features - > Location. You will see this:

<figure><img src="/gitbook-assets/Screenshot 2023-06-14 at 6.02.27 PM.png" alt="Educational illustration for iOS concept"><figcaption></figcaption></figure>

* You can select 'Custom Location...' option to put your preferred coordinate to simulate the current location.

Let's run the app now.

<figure><img src="/gitbook-assets/14.six.gif" alt="Educational illustration for iOS concept"><figcaption></figcaption></figure>



### Code so far

[Download Project Archive](/gitbook-assets/App14_phase1.zip)



### Phase 2: Annotations and Accessories for a certain place

In this module, we will learn how to annotate a place in a particular coordinate on the map view. For example, we can annotate Northeastern University on the map view like the following:

<figure><img src="/gitbook-assets/14.sixty.gif" alt="Educational illustration for iOS concept"><figcaption></figcaption></figure>

### Defining a Place class with MKAnnotation

We will define a class named Place, adopting the MKAnnotation protocol to annotate places on the map view. So let's create a new file named 'Place.swift' and put the following code there:


```swift
//
//  Place.swift
//  App14
//
//  Created by Sakib Miazi on 6/14/23.
//

import MapKit
import UIKit

class Place: NSObject, MKAnnotation {
    var title: String?
    var coordinate: CLLocationCoordinate2D
    var info: String

    init(title: String, coordinate: CLLocationCoordinate2D, info: String) {
        self.title = title
        self.coordinate = coordinate
        self.info = info
    }
    
    var mapItem: MKMapItem?{
        guard let location = title else{
            return nil
        }
        
        let placemark = MKPlacemark(
            coordinate: coordinate,
            addressDictionary:  [:]
        )
        let mapItem = MKMapItem(placemark: placemark)
        mapItem.name = title
        
        return mapItem
    }
}
```


In the above code:

* The class Place extends another Swift class NSObject, and adopts MKAnnotation protocol. MKAnnotation is a protocol that allows a Swift object to adopt MapKit's annotation-specific data and use the object directly as a place on the map.&#x20;
* On lines 12 through 14, we keep three variables to use in the annotation for a place.
  * title - the name of the place.
  * coordinate - the lat and long coordinates of the place.
  * info - additional details you may want to store.
  * You can use as many variables as you want to store more data regarding a place.
* Our initializer for the class Place is defined on lines through 16 through 20.
* Then we also initialize a variable `mapItem` of the type MKMapItem, to interact with the place on the map. MKMapItem class contains the details of a map location, like a placemark, coordinate, name, etc.
  * The placemark in a map item is the details of the place the map item represents, like the coordinate, physical address, phone number, images, etc. For now, we keep an empty dictionary for the addressDictionary of the placemark.
* Between lines 23 and 25, we used **guard-let** instead of if-let.

### What is guard-let?

**guard-let** is very similar to if-let to unwrap an optional value. `guard-let` is often used when you do not need to deal with the unwrapped value immediately and would use it later. So, we get the unwrapped value and store it in a constant for later use. For more, visit: [https://www.hackingwithswift.com/quick-start/understanding-swift/when-to-use-guard-let-rather-than-if-let](https://www.hackingwithswift.com/quick-start/understanding-swift/when-to-use-guard-let-rather-than-if-let)

### Display an Annotated Place on Map

Let's open the ViewController.swift file, and put the following code there:


```swift
//
//  ViewController.swift
//  App14
//
//  Created by Sakib Miazi on 6/14/23.
//

import UIKit
import MapKit

class ViewController: UIViewController {
    //codes omitted...
    override func viewDidLoad() {
        super.viewDidLoad()
        
        //codes omitted...
        
        //MARK: Annotating Northeastern University...
        let northeastern = Place(
            title: "Northeastern University",
            coordinate: CLLocationCoordinate2D(latitude: 42.339918, longitude: -71.089797),
            info: "LVX VERITAS VIRTVS"
        )
        
        mapView.mapView.addAnnotation(northeastern)
        
    }
    
    //codes omitted...
}
//codes omitted...
```


In the above code:

* On lines 19 through 23, we create a Place object, `northeastern` with the details of Northeastern University (title, coordinate, and info).&#x20;
* Then we add the Place `northeastern` as an annotation on the map on line 25.

Let's run the app.&#x20;

<figure><img src="/gitbook-assets/14.sixty1.gif" alt="Educational illustration for iOS concept"><figcaption></figcaption></figure>

You can see there is a red bubble on the place `northeastern`. That is the placemark we talked about thus far.

### Interacting with the Annotations

Now to be able to interact with the bubble, we need to adopt a protocol `MKMapViewDelegate`. We  need to implement two adopted `mapView()` methods with parameters `viewFor` and `calloutAccessoryControlTapped`.&#x20;

Let's create a new file MapAnnotationDelegate.swift and put the following code there:


```swift
//
//  MapAnnotationDelegate.swift
//  App14
//  Repurposed from: https://www.hackingwithswift.com/read/16/3/annotations-and-accessory-views-mkpinannotationview
//  Created by Sakib Miazi on 6/14/23.
//

import Foundation
import MapKit

extension ViewController: MKMapViewDelegate{
    func mapView(_ mapView: MKMapView, viewFor annotation: MKAnnotation) 
        -> MKAnnotationView? {
        
    }
    
    func mapView(_ mapView: MKMapView, annotationView view: MKAnnotationView, 
        calloutAccessoryControlTapped control: UIControl) {
       
    }
}

```


In the above code:

* Between lines 12 through 15, we need to create an annotation view to display the placemark details. We can
* Between lines 17 through 20, we need to write the logic to handle in case the user taps on the accessory button of the annotation.

### Creating Annotation View

Let's put the following code in the `mapView()` method for `viewFor` (first method in the above code):


```swift
func mapView(_ mapView: MKMapView, viewFor annotation: MKAnnotation)
    -> MKAnnotationView? {
    guard let annotation = annotation as? Place else { return nil }
    
    var view:MKMarkerAnnotationView
    
    if let annotationView = mapView.dequeueReusableAnnotationView(
        withIdentifier: Configs.placeIdentifier) as? MKMarkerAnnotationView{
        
        annotationView.annotation = annotation
        view = annotationView
    
    }else{
        view = MKMarkerAnnotationView(annotation: annotation, reuseIdentifier: Configs.placeIdentifier)
        view.canShowCallout = true
        view.calloutOffset = CGPoint(x: -5, y: 5)
        view.rightCalloutAccessoryView = UIButton(type: .detailDisclosure)
    }
    return view
}
```


In the above code:

* On line 3, we define a new annotation from the `annotation` parameter as a Place object.
* Between line 7 and 18 we check if there is a reusable annotation already populated on screen,&#x20;
  * If yes, then we reuse the current annotation view.
  * Else, we create a new annotation&#x20;
    * We set the annotation view's `canShowCallout` parameter as true. It means it can display a callout interactive annotation view on this place.
    * Then we add a right accessory button on the callout annotation view.

### Delegating the User Interaction on the Callout

Let's put the following code in the `mapView()` method for `calloutAccessoryControlTapped` (second method):


```swift
func mapView(_ mapView: MKMapView, 
    annotationView view: MKAnnotationView, 
    calloutAccessoryControlTapped control: UIControl) {
        
    guard let annotation = view.annotation as? Place else { return }
    
    let ac = UIAlertController(
        title: annotation.title,
        message: "Navigate to \(annotation.title!) now?",
        preferredStyle: .alert
    )
    
    ac.addAction(UIAlertAction(title: "Navigate", style: .default, handler: {_ in
        let launchOptions = [
            MKLaunchOptionsDirectionsModeKey: MKLaunchOptionsDirectionsModeDriving
        ]
        annotation.mapItem?.openInMaps(launchOptions: launchOptions)
    }))
    
    ac.addAction(UIAlertAction(title: "Cancel", style: .cancel))
    present(ac, animated: true)
}
```


In the above code:

* The method gets triggered when the user taps the accessory callout right button.&#x20;
* It displays an alert controller with two actions (lines 7 through 21):
  * &#x20;On lines 13 through 18, we add the navigation action to the alert controller with a button named 'Navigation.'&#x20;
    * On lines 14 through 16, we define the launchOptions for opening navigation in Apple Maps. We set the navigation direction type as driving directions on line 15.
    * And on line 17, we open Apple Maps to navigate to the place annotated.
  * On line 20, we add a Cancel action for the alert controller.
  * Then finally, on line 21, we present the alert controller.&#x20;

We have a final task to do. We need to patch the delegate of the mapView to ViewController. Let's open ViewController.swift file and add the following line in `viewDidLoad()` method: `mapView.mapView.delegate = self`.&#x20;

Let's run the app.&#x20;

<figure><img src="/gitbook-assets/14.sixty4.gif" alt="Educational illustration for iOS concept"><figcaption></figcaption></figure>

We first load the screen and display the annotation for Northeastern. Then we change the current simulator location to Apple's headquarters location.  Then we try the navigation with annotation. It opens the Apple Map, and we can drive!

### Code so far

[Download Project Archive](/gitbook-assets/App14 Phase2.zip)



### Phase 3: Place Search and Navigate

At this point, we will add a Bottom Search Sheet to find the places around and navigate there.

### Setting up the Bottom Search Sheet

First, let's add a search button at the bottom of the Map Screen. Open MapView.swift file, and put the following code to add the search button and its constraints:


```swift
//
//  MapView.swift
//  App14
//
//  Created by Sakib Miazi on 6/14/23.
//

import UIKit
import MapKit

class MapView: UIView {
    //codes omitted...
    var buttonSearch:UIButton!
    
    override init(frame: CGRect) {
        //codes omitted...
        setupButtonSearch()
        initConstraints()
    }
   //codes omitted...
    
    func setupButtonSearch(){
        buttonSearch = UIButton(type: .system)
        buttonSearch.setTitle(" Search places...  ", for: .normal)
        buttonSearch.titleLabel?.font = UIFont.boldSystemFont(ofSize: 24)
        buttonSearch.setImage(UIImage(systemName: "magnifyingglass.circle.fill"), for: .normal)
        buttonSearch.layer.backgroundColor = UIColor.darkGray.cgColor
        buttonSearch.tintColor = .white
        buttonSearch.layer.cornerRadius = 10
        
        buttonSearch.layer.shadowOffset = .zero
        buttonSearch.layer.shadowRadius = 4
        buttonSearch.layer.shadowOpacity = 0.7
        
        buttonSearch.translatesAutoresizingMaskIntoConstraints = false
        buttonSearch.isHidden = true
        self.addSubview(buttonSearch)
    }
    
    func initConstraints(){
        NSLayoutConstraint.activate([
            //codes omitted...
            buttonSearch.bottomAnchor.constraint(equalTo: buttonCurrentLocation.bottomAnchor),
            buttonSearch.centerXAnchor.constraint(equalTo: self.safeAreaLayoutGuide.centerXAnchor),
            buttonSearch.heightAnchor.constraint(equalTo: buttonCurrentLocation.heightAnchor)
        ])
    }
    //codes omitted...
}

```


Now, let's create the files related to the Bottom Search Sheet in the project: SearchViewController.swift, SearchBottomSheet.swift, SearchTableViewCell.swift, and SearchTableViewManager.swift.&#x20;

![Educational illustration for iOS concept](</gitbook-assets/Screenshot 2023-06-15 at 1.31.59 PM.png>)

Then we set up the Bottom Search Sheet following the example in [Broken link](broken-reference "mention").&#x20;

### Bottom Search Sheet

### SearchViewController.swift

Let's add the following code to the file:


```swift
//
//  SearchViewController.swift
//  App14
//
//  Created by Sakib Miazi on 6/15/23.
//

import UIKit
import MapKit

class SearchViewController: UIViewController {

    let searchBottomSheet = SearchBottomSheet()

    override func loadView() {
        view = searchBottomSheet
    }
    
    override func viewDidLoad() {
        super.viewDidLoad()
        searchBottomSheet.tableViewSearchResults.delegate = self
        searchBottomSheet.tableViewSearchResults.dataSource = self
        searchBottomSheet.searchBar.delegate = self
        
        searchBottomSheet.tableViewSearchResults.separatorStyle = .none
        
    }
    
}

extension SearchViewController: UISearchBarDelegate{
    func searchBar(_ searchBar: UISearchBar, textDidChange searchText: String) {
        
    }
    
    func searchBarCancelButtonClicked(_ searchBar: UISearchBar) {
        self.dismiss(animated: true)
    }
}
```


### SearchBottomSheet.swift

Let's add the following code to the file:


```swift
//
//  SearchBottomSheet.swift
//  App14
//
//  Created by Sakib Miazi on 6/15/23.
//

import UIKit

class SearchBottomSheet: UIView {
    var searchBar: UISearchBar!
    var tableViewSearchResults: UITableView!
    override init(frame: CGRect) {
        super.init(frame: frame)
        backgroundColor = .white
        setupSearchBar()
        setupTableViewSearchResults()
        initConstraints()
    }
    
    func setupSearchBar(){
        searchBar = UISearchBar()
        searchBar.placeholder = "Search places..."
        searchBar.showsCancelButton = true
        searchBar.autocapitalizationType = .none
        searchBar.translatesAutoresizingMaskIntoConstraints = false
        self.addSubview(searchBar)
    }
    func setupTableViewSearchResults(){
        tableViewSearchResults = UITableView()
        tableViewSearchResults.register(SearchTableViewCell.self, forCellReuseIdentifier: Configs.searchTableViewID)
        tableViewSearchResults.translatesAutoresizingMaskIntoConstraints = false
        self.addSubview(tableViewSearchResults)
    }
    
    func initConstraints(){
        NSLayoutConstraint.activate([
            searchBar.topAnchor.constraint(equalTo: self.safeAreaLayoutGuide.topAnchor),
            searchBar.leadingAnchor.constraint(equalTo: self.safeAreaLayoutGuide.leadingAnchor, constant: 16),
            searchBar.trailingAnchor.constraint(equalTo: self.safeAreaLayoutGuide.trailingAnchor, constant: -16),
            
            tableViewSearchResults.topAnchor.constraint(equalTo: searchBar.bottomAnchor, constant: 8),
            tableViewSearchResults.bottomAnchor.constraint(equalTo: self.safeAreaLayoutGuide.bottomAnchor),
            tableViewSearchResults.widthAnchor.constraint(equalTo: self.safeAreaLayoutGuide.widthAnchor),
            tableViewSearchResults.widthAnchor.constraint(equalTo: self.safeAreaLayoutGuide.widthAnchor),
        ])
    }
    
    required init?(coder: NSCoder) {
        fatalError("init(coder:) has not been implemented")
    }
}
```


### SearchTableViewCell.swift

Let's add the following code to the file:


```swift
//
//  SearchTableViewCell.swift
//  App14
//
//  Created by Sakib Miazi on 6/15/23.
//

import UIKit

class SearchTableViewCell: UITableViewCell {

    var wrapperCellView: UIView!
    var labelTitle: UILabel!
    
    override init(style: UITableViewCell.CellStyle, reuseIdentifier: String?) {
        super.init(style: style, reuseIdentifier: reuseIdentifier)
        setupWrapperCellVIew()
        setupLabelTitle()
        initConstraints()
    }
    
    func setupWrapperCellVIew(){
        wrapperCellView = UITableViewCell()
        wrapperCellView.backgroundColor = .white
        wrapperCellView.translatesAutoresizingMaskIntoConstraints = false
        self.addSubview(wrapperCellView)
    }
    func setupLabelTitle(){
        labelTitle = UILabel()
        labelTitle.font = UIFont.boldSystemFont(ofSize: 20)
        labelTitle.translatesAutoresizingMaskIntoConstraints = false
        wrapperCellView.addSubview(labelTitle)
    }
    func initConstraints(){
        NSLayoutConstraint.activate([
            wrapperCellView.topAnchor.constraint(equalTo: self.topAnchor,constant: 10),
            wrapperCellView.leadingAnchor.constraint(equalTo: self.leadingAnchor, constant: 10),
            wrapperCellView.bottomAnchor.constraint(equalTo: self.bottomAnchor, constant: -10),
            wrapperCellView.trailingAnchor.constraint(equalTo: self.trailingAnchor, constant: -10),
            
            labelTitle.topAnchor.constraint(equalTo: wrapperCellView.topAnchor, constant: 8),
            labelTitle.leadingAnchor.constraint(equalTo: wrapperCellView.leadingAnchor, constant: 16),
            labelTitle.heightAnchor.constraint(equalToConstant: 20),
            labelTitle.widthAnchor.constraint(lessThanOrEqualTo: wrapperCellView.widthAnchor),
            
            wrapperCellView.heightAnchor.constraint(equalToConstant: 40)
        ])
        
    }
    
    required init?(coder: NSCoder) {
        fatalError("init(coder:) has not been implemented")
    }

}
```


### SearchTableViewManager.swift

Let's add the following code to the file:


```swift
//
//  SearchTableViewManager.swift
//  App14
//
//  Created by Sakib Miazi on 6/15/23.
//

import Foundation
import UIKit

extension SearchViewController: UITableViewDelegate, UITableViewDataSource{
    func tableView(_ tableView: UITableView, numberOfRowsInSection section: Int) -> Int {
        return mapItems.count
    }
    
    func tableView(_ tableView: UITableView, cellForRowAt indexPath: IndexPath) -> UITableViewCell {
        let cell = tableView.dequeueReusableCell(withIdentifier: Configs.searchTableViewID, for: indexPath) as! SearchTableViewCell
        
        return cell
    }
    
    func tableView(_ tableView: UITableView, didSelectRowAt indexPath: IndexPath) {
        
    }
}
```


### Displaying the Bottom Search Sheet

We need to add an action to the search button in ViewController. And then display the bottom search sheet.

Let's add the following code in ViewController.swift file:


```swift
//
//  ViewController.swift
//  App14
//
//  Created by Sakib Miazi on 6/14/23.
//

import UIKit
import MapKit

class ViewController: UIViewController {
    //codes omitted...
    override func viewDidLoad() {
        super.viewDidLoad()
        
        title = "Search in Map"
        navigationController?.navigationBar.prefersLargeTitles = true
        //codes omitted...
        
        //MARK: add action for bottom search button tap...
        mapView.buttonSearch.addTarget(self, action: #selector(onButtonSearchTapped), for: .touchUpInside)
        //codes omitted...
    }
    //codes omitted...
    @objc func onButtonSearchTapped(){
        
        //MARK: Setting up bottom search sheet...
        let searchViewController  = SearchViewController()
        let navForSearch = UINavigationController(rootViewController: searchViewController)
        navForSearch.modalPresentationStyle = .pageSheet
        
        if let searchBottomSheet = navForSearch.sheetPresentationController{
            searchBottomSheet.detents = [.medium(), .large()]
            searchBottomSheet.prefersGrabberVisible = true
        }
        
        present(navForSearch, animated: true)
    }

}
```


In the above code:

* On lines 25 through 38, we handle the action when the user taps on the search button.&#x20;
  * We create the bottom search sheet and embed it in a navigation controller.
  * Then we define the presentation style, detents, and grabber for the bottom search sheet.
  * Finally, present the sheet.

If we run the app now:

<figure><img src="/gitbook-assets/14.seventy.gif" alt="Educational illustration for iOS concept"><figcaption></figcaption></figure>

So, our bottom search sheet is working!

### Searching Nearby Places

Here we have to type something on the search bar, and depending on what we type, it should display the list of related places in the search results table view. So, let's open SearchViewController.swift and put in the following code to add a delegate to mapview:


```swift
//
//  SearchViewController.swift
//  App14
//
//  Created by Sakib Miazi on 6/15/23.
//

import UIKit
import MapKit

class SearchViewController: UIViewController {
    
    var delegateToMapView: ViewController!
    
    var mapItems = [MKMapItem]()
    //codes omitted...
        
}

extension SearchViewController: UISearchBarDelegate{
    func searchBar(_ searchBar: UISearchBar, textDidChange searchText: String) {
    }
    
    func searchBarCancelButtonClicked(_ searchBar: UISearchBar) {
        self.dismiss(animated: true)
    }
}
```


In the above code, on line 13, we declare a delegate variable to the ViewController where the map view is.

Now, let's create a new file named LoadPlaces.swift in the group "Map Screen." ![Educational illustration for iOS concept](</gitbook-assets/Screenshot 2023-06-15 at 7.40.50 PM.png>)

Let's write the following code in the file:


```swift
//
//  LoadPlaces.swift
//  App14
//
//  Created by Sakib Miazi on 6/15/23.
//

import Foundation
import CoreLocation
import MapKit

extension ViewController{
    func loadPlacesAround(query: String){
        var mapItems = [MKMapItem]()
        
        let searchRequest = MKLocalSearch.Request()
        searchRequest.naturalLanguageQuery = query


        // Set the region to an associated map view's region.
        searchRequest.region = mapView.mapView.region


        let search = MKLocalSearch(request: searchRequest)
        search.start { (response, error) in
            guard let response = response else {
                // Handle the error.
                return
            }
            mapItems = response.mapItems
            
            for item in response.mapItems {
                if let name = item.name,
                    let location = item.placemark.location {
                    print("\(name), \(location)")
                }
            }
        }
    }
}
```


In the above code:

* We import CoreLocation and MapKit libraries to search places.
* We extend the ViewController class and define the method `loadPlacesAround()` where we take a String parameter named `query`.&#x20;
* We use `MKLocalSearch` service from Apple Maps to search for places.
* On line 16, we create a search request instance.
* On line 17, we set the `naturalLanguageQuery` of the local search service to the parameter `query`.
* Now, the search request needs a region, right? We won't be searching the whole world. So on line 21, we set the search region to the current map view region. It means I will be looking for places close to the region we see on the map inside the screen.
* On lines 24 through 38, we run the search for the places related to the query.

Now, let's open SearchViewController.swift file again and call `loadPlacesAround()` method when the user type something:


```swift
//
//  SearchViewController.swift
//  App14
//
//  Created by Sakib Miazi on 6/15/23.
//

class SearchViewController: UIViewController {
    
    var delegateToMapView: ViewController!
    
    //codes omitted...
    
}

extension SearchViewController: UISearchBarDelegate{
    func searchBar(_ searchBar: UISearchBar, textDidChange searchText: String) {
        delegateToMapView.loadPlacesAround(query: searchText)
    }
    
    func searchBarCancelButtonClicked(_ searchBar: UISearchBar) {
        self.dismiss(animated: true)
    }
}

```


In the above code, on line 18, we call the `loadPlacesAround(query: searchText)` method of map screen using the delegate. We send the text the user writes on the search bar.

We need to update ViewController.swift file to initialize the delegateToMapView variable. So, let's initialize it as the following code:


```swift
//
//  ViewController.swift
//  App14
//
//  Created by Sakib Miazi on 6/14/23.
//
class ViewController: UIViewController {
    //codes omitted...
    
    @objc func onButtonSearchTapped(){
        
        //MARK: Setting up bottom search sheet...
        let searchViewController  = SearchViewController()
        searchViewController.delegateToMapView = self
        
        let navForSearch = UINavigationController(rootViewController: searchViewController)
        navForSearch.modalPresentationStyle = .pageSheet
        
        if let searchBottomSheet = navForSearch.sheetPresentationController{
            searchBottomSheet.detents = [.medium(), .large()]
            searchBottomSheet.prefersGrabberVisible = true
        }
        
        present(navForSearch, animated: true)
    }
}
//codes omitted...
```


In the above code, on line 14, we initialize `delegateToMapView` variable of the search view controller to `self`.

Let's run the app.

<figure><img src="/gitbook-assets/14.seventy1.gif" alt="Educational illustration for iOS concept"><figcaption></figcaption></figure>

The results are getting printed in the output area in the above demo. The results are related to the search query "coffee." It fetches all the coffee shops around.

### Displaying the search results in the search table view

Now we have the search results in the map screen, so we need to send them back to the search result table view. We will use Notification Center for that. We need to observe the data from the search bottom sheet. We post the notification from the map screen.

### Setting an observer from the bottom search sheet

Open SearchViewController.swift file, and put the following code there:


```swift
//
//  SearchViewController.swift
//  App14
//
//  Created by Sakib Miazi on 6/15/23.
//

import UIKit
import MapKit

class SearchViewController: UIViewController {
    
    var delegateToMapView: ViewController!
    
    //codes omitted...
    
    override func viewDidLoad() {
        super.viewDidLoad()
        //codes omitted... 
        notificationCenter.addObserver(
            self,
            selector: #selector(notificationForPlaces(notification:)),
            name: .placesFromMap,
            object: nil
        )
        
    }
    
    @objc func notificationForPlaces(notification: Notification){
        mapItems = notification.object as! [MKMapItem]
        self.searchBottomSheet.tableViewSearchResults.reloadData()
    }
    
}

extension SearchViewController: UISearchBarDelegate{
    func searchBar(_ searchBar: UISearchBar, textDidChange searchText: String) {
        delegateToMapView.loadPlacesAround(query: searchText)
    }
    
    func searchBarCancelButtonClicked(_ searchBar: UISearchBar) {
        self.dismiss(animated: true)
    }
}
```


In the above code:&#x20;

* We observe the notification center on lines 20 through 25.&#x20;
* On lines 29 through 32, we define the method for handling the notification received event.
  * We basically receive an array of map items. Then we have to display them in the table view.&#x20;

Let's open SearchTableViewManager.swift file and add the following code to display the map items on the cells:


```swift
//
//  SearchTableViewManager.swift
//  App14
//
//  Created by Sakib Miazi on 6/15/23.
//

import Foundation
import UIKit

extension SearchViewController: UITableViewDelegate, UITableViewDataSource{
    //codes omitted...
    func tableView(_ tableView: UITableView, cellForRowAt indexPath: IndexPath) -> UITableViewCell {
        let cell = tableView.dequeueReusableCell(withIdentifier: Configs.searchTableViewID, for: indexPath) as! SearchTableViewCell
        if let name = mapItems[indexPath.row].name{
                cell.labelTitle.text = name
        }
        return cell
    }
    //codes omitted...
}
```


In the above code:

* On lines 15 through 17, we set the text of the cell's `labelTitle` to the name of the current map item.

### Posting notification from Map Screen

Let's open LoadPlaces.swift file, and put the following code there:


```swift
//
//  LoadPlaces.swift
//  App14
//
//  Created by Sakib Miazi on 6/15/23.
//

import Foundation
import CoreLocation
import MapKit

extension ViewController{
    func loadPlacesAround(query: String){
        //MARK: initializing the notification center...
        let notificationCenter = NotificationCenter.default
        
        var mapItems = [MKMapItem]()
        
        let searchRequest = MKLocalSearch.Request()
        searchRequest.naturalLanguageQuery = query


        // Set the region to an associated map view's region.
        searchRequest.region = mapView.mapView.region


        let search = MKLocalSearch(request: searchRequest)
        search.start { (response, error) in
            guard let response = response else {
                // Handle the error.
                return
            }
            mapItems = response.mapItems
            
            for item in response.mapItems {
                if let name = item.name,
                    let location = item.placemark.location {
                    print("\(name), \(location)")
                }
            }
            
            //MARK: posting the search results...
            notificationCenter.post(name: .placesFromMap, object: mapItems)
        }
    }
}
```


In the above code:

* On line 15, we initialize the notification center.
* On line 43, we post the map items we fetched to the notification center.

Let's run the app again:

<figure><img src="/gitbook-assets/14.seventy3.gif" alt="Educational illustration for iOS concept"><figcaption></figcaption></figure>

**Great! We can see the search results!!! Now can we show the place on the map when we select it on the table view?**

### Code so far

[Download Project Archive](/gitbook-assets/App14_phase3.zip)



### Phase 4: Display Searched Places on Map

The last part of our app is to show a place selected from the search results on the map and navigate to it.

The task seems complicated, but we already have the code to display the annotations for a place, right? The rest of it is pretty straightforward.

Let's open ViewController.swift file and add a method `showSelectedPlace(placeItem: MKMapItem)` there:


```swift
//
//  ViewController.swift
//  App14
//
//  Created by Sakib Miazi on 6/14/23.
//

import UIKit
import MapKit

class ViewController: UIViewController {
    //codes omitted...
    
    //MARK: show selected place on map...
    func showSelectedPlace(placeItem: MKMapItem){
        let coordinate = placeItem.placemark.coordinate
        mapView.mapView.centerToLocation(
            location: CLLocation(
                latitude: coordinate.latitude,
                longitude: coordinate.longitude
            )
        )
        let place = Place(
            title: placeItem.name!,
            coordinate: coordinate,
            info: placeItem.description
        )
        mapView.mapView.addAnnotation(place)
    }

}
//codes omitted...
```


In the above code:

* On line 16, we fetch the coordinate from the map item.
* On lines 17 through 22, we center the map view around the coordinate.
* On lines 23 through 27, we create a Place object from the map item.
* On line 28, we add the annotation view to the place.

Now we need to call `showSelectedPlace()` method when a search result cell is tapped from the bottom search sheet. So, let's open SearchTableViewManager.swift file and update the tableView() method with parameter `didSelectRowAt.`


```swift
extension SearchViewController: UITableViewDelegate, UITableViewDataSource{
    //codes omitted...
    
    func tableView(_ tableView: UITableView, didSelectRowAt indexPath: IndexPath) {
        delegateToMapView.showSelectedPlace(placeItem: mapItems[indexPath.row])
        self.dismiss(animated: true)
    }
}
```


In the above code, on line 5, we call the `showSelectedPlace()` method with the selected place.

Nice! Let's try our app now.

<figure><img src="/gitbook-assets/14.seventy6.gif" alt="Educational illustration for iOS concept"><figcaption></figcaption></figure>

Awesome!!! Now we built a pretty useful basic place search application!



### Reference Code

[Download Project Archive](/gitbook-assets/App14.zip)

---

## Guided Practice Challenges

Before moving on to the next topic, try these low-stakes practice challenges in Xcode. They will build the exact muscle memory you need:

### Challenge 1: Experimentation
**The Scenario:** You've just learned about MapKit & Location.
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


### Implementing Register and Sign In

**Estimated effort:** 1-2 hours this topic
**Format:** Asynchronous online
**Prerequisites:** Previous iOS topics


**🎯 Topic Mission:** 
In this module, we will explore **12.5. Implementing Register and Sign In** and learn how to integrate it into our iOS applications. Your mission is to understand the mechanics behind this concept and write robust Swift code.


---

## Learning Objectives

By the end of this session, you will be able to:
1. Understand the core concepts of 12.5. Implementing Register and Sign In.
2. Implement 12.5. Implementing Register and Sign In in an Xcode project.
3. Apply best practices to ensure clean and maintainable code.

---

## The Story So Far...

We have been progressively building our knowledge of iOS and Swift. In this module, we will expand our toolkit by diving into 12.5. Implementing Register and Sign In. 
Open your current Xcode project or start a new Playground to follow along with the hands-on material.

---

## Walkthrough: Exploring 12.5. Implementing Register and Sign In

> 📁 **Target Project** — Follow along by building the mini-app presented in the steps below, or integrate these concepts into your own ongoing projects.

### Implementing Register and Sign In

Our next goal is to build the functionalities so that a user can register a new account and sign in to the account like the following:

<figure><img src="/gitbook-assets/12.two.gif" alt="Educational illustration for iOS concept"><figcaption></figcaption></figure>

* We need to add a right bar button to enable sign-in.
* If the user clicks on the bar button, the app should show an alert to give the user an option to put their email and password. It should also give them the option to register a new account.
* If the user clicks the 'Sign in' button, it should sign the user in using Firebase authentication.
* If the user clicks on the 'Register' button, it should open the registration screen to allow the user to create a new account.




### Building the Right Bar Button(s) for Sign In and Logout

We add two buttons on the right navigation bar, triggering the same action. We do it to display an image and text to explain to the user what to do. (This is not standard practice, you can design your own buttons.)

We will separate the logic of creating and handling the right bar button actions from the ViewController. So, let's create a new file `Main Screen -> RightBarButtonManager.swift` and write the following code there:

![Educational illustration for iOS concept](</gitbook-assets/Screenshot 2023-06-02 at 4.37.14 PM (1).png>)


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


### setupRightBarButton(isLoggedin: Bool)

In the above code:

* Depending on whether there is a signed-in user or not, we change the appearance and behavior of the right bar button. If the user is signed in, we display the logout button; else, we display the sign-in button.
* In both cases, we add two buttons to do the same tasks. If you look at lines 28 and 45, we add the pair of buttons together.
* For the logout buttons, the action would be `onLogOutBarButtonTapped()` method, and for the sign-in buttons, the action would be `onSignInBarButtonTapped()` method.

### onSignInBarButtonTapped()

When the sign-in bar button is tapped, we need to display an alert with the text fields to let the user sign in. It should have two buttons: 'SIgn In' and 'Logout.

So we will write the following logic inside the `onSignInBarButtonTapped()` method.


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


In the above code:

* On lines 2 through 5, we set up the title and message of the alert controller. Then on lines 7 through 19, we add two TextFields for email and password. The text fields are added to an array of text fields inside the alert controller.
* Then we define two actions for the alert controllers: "Sign In" (lines 22-28) and "Register" (lines 31-34). We need to write the logic for signing in and registering in these closures. We will write the logic momentarily.
* Then we will add the actions to the alert controller (lines 37-38).
* Then we present the alert controller (lines 40-46). In the completion closure, we write logic to handle if the user taps outside the alert. We need to dismiss the alert if the user taps outside. So, we add a Gesture Recognizer on the `superview` (the screen which popped this alert) of the alert controller. If the user taps on the super view, the alert gets dismissed.

**We will keep the sign-in and register logic empty and return to that momentarily.**

### onLogOutBarButtonTapped()

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

### Patching ViewController to display the Right Bar Buttons

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

<figure><img src="/gitbook-assets/12.three (1).gif" alt="Educational illustration for iOS concept"><figcaption></figcaption></figure>



### Progress Activity Indicator

If you noticed, when we clicked on the Register button, the UI was stuck for a few seconds as we were waiting for the create user operation to complete. In these cases, the user may get confused if we do not give the users a cue that the backend is working on their request. So we want to implement a loading screen with a progress indicator so that the user can understand the app is working in the backend to complete their request. Like this:

<figure><img src="/gitbook-assets/123.four (1).gif" alt="Educational illustration for iOS concept"><figcaption></figcaption></figure>

### Defining a Progress Activity Indicator

We will use a UI element in iOS called `UIActivityIndicatorView` to display the loading screen. Since we may reuse the same `UIActivityIndicatorView` for multiple backend tasks, we will write separate code to create the instance of it.

Let's create a new group called 'Progress Indicator' in the files navigator of Xcode. Then add two files in the group: ProgressSpinnerViewController.swift and ProgressSpinnerDelegate.swift.

![Educational illustration for iOS concept](</gitbook-assets/Screenshot 2023-06-02 at 9.23.32 PM (1).png>)

### ProgressSpinnerViewController.swift

Let's open ProgressSpinnerViewController.swift file and put the following code there:


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

### Displaying the Progress Indicator View while Registering a User

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

![Educational illustration for iOS concept](</gitbook-assets/Screenshot 2023-06-02 at 9.58.51 PM (1).png>)

Add the following code there:


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


In the above code:

* On line 15, before we start creating the request for creating a user, we show the progress indicator.
* Online 42, after the profile update is done, we hide the progress indicator.

If you run the application now, you will see that the progress indicator is working!

<figure><img src="/gitbook-assets/12.five (1).gif" alt="Educational illustration for iOS concept"><figcaption></figcaption></figure>



### Register Screen: Create a user in Firebase

Let's design the Register Screen to let the user create an account. It will look like the following:

<figure><img src="/gitbook-assets/12.three.2 (1).gif" alt="Educational illustration for iOS concept"><figcaption></figcaption></figure>

The Register Screen design is very simple; we have three text fields to put the name, email, and password so that the user can create an account with them.

### RegisterView.swift

Let's create a new Group named "Register Screen." Create another group "Views" inside the "Register Screen" group. Add a file named "RegisterView.swift" in it.

![Educational illustration for iOS concept](</gitbook-assets/Screenshot 2023-06-02 at 5.55.46 PM (2).png>)

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

### RegisterViewController.swift

Then let's create RegisterViewController.swift file to write code for controlling the Register screen.


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


In the above code:

* We have added the `onRegisterTapped()` method to handle if the Register button is tapped. We need to patch the Firebase code on line 30.

### RegisterFirebaseManager.swift

We will separate the code for Firebase from the controller. Let's create a new file `Register Screen -> RegisterFirebaseManager.swift`.

![Educational illustration for iOS concept](</gitbook-assets/Screenshot 2023-06-02 at 7.09.24 PM (1).png>)

In this file, we will handle the Firebase Authentication procedures.

### Firebase Authentication

Please visit the following documentation for using the Firebase Authentication service in iOS: [https://firebase.google.com/docs/auth/ios/start](https://firebase.google.com/docs/auth/ios/start). First look at their official documentation. If you are confused, ask us.

We have to do the following tasks:

* We need to register the user using email and password.
* Then we will update the profile's display name.

So, let's write the following code in RegisterFirebaseManager.swift file:


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


In the above code:

### (Creating a new User in Firebase)

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

### (Updating a User Profile in Firebase)

* The `setNameOfTheUserInFirebaseAuth(name: String)` method updates the profile of the created user. (See [https://firebase.google.com/docs/auth/ios/manage-users#update\_a\_users\_profile](https://firebase.google.com/docs/auth/ios/manage-users#update\_a\_users\_profile)).
  * On line 33, we create a change request for the current FirebaseAuth user.
  * On line 34, we set the intended name of the user in the change request.
  * Then on line 35, we commit the changes with a request.
    * The `completion` closure handles what happens after the profile update.
    * If there is no error, the response returns a nil error. So, here we can certainly say that the profile has been updated.
    * Since all the tasks are done, we can close the register screen and return to the main screen (line 38).

> **Very important:** Firebase calls are asynchronous, requiring network communications and server processing. **So the sequence of events is very important. You must wait until one operation is done, then conduct the next operation.** We cannot create a Firebase user and update profile operations together. We have to wait for the user to be created first. If the response is successful and the user is created, we update the profile. You must think carefully before writing codes and maintain the chain of Firebase calls correctly to avoid errors.

### RegisterViewController.swift

Now we need to handle when the user taps on the Register button. We need to call `registerNewAccount()` method from `onRegisterTapped()` method in RegisterViewMethod.swift file.\\

Open RegisterViewController.swift file, and update the `onRegisterTapped` method.

```swift
@objc func onRegisterTapped(){
    //MARK: creating a new user on Firebase...
    registerNewAccount()
}
```

### Patching the Main Screen to Show Register Screen

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

<figure><img src="/gitbook-assets/12.three.3 (1).gif" alt="Educational illustration for iOS concept"><figcaption></figcaption></figure>

If you now look into the Firebase Authentication portal,

<figure><img src="/gitbook-assets/Screenshot 2023-06-02 at 9.06.25 PM (1).png" alt="Educational illustration for iOS concept"><figcaption></figcaption></figure>



### Implementing Sign In

Now it's time to sign in with an already created user.

We just need to add a few lines of code inside `RightBarButtonManager.swift` file inside the `signInAction` alert action:


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


Here:

* We add line 24 to call a method to sign in to an existing account.
* On lines 30 through 41, we define the `signInToFirebase` method. If there is no error, then great! We will load the homepage with the signed-in user. Else, display an alert to notify the user that the email or password was wrong.

If we run the app now, you will see:

<figure><img src="/gitbook-assets/12.six (1).gif" alt="Educational illustration for iOS concept"><figcaption></figcaption></figure>

_**Can you display a progress indicator while the login operation is happening?**_

### App12 code so far:

[Download Project Archive](/gitbook-assets/App12_auth.zip)

---

## Guided Practice Challenges

Before moving on to the next topic, try these low-stakes practice challenges in Xcode. They will build the exact muscle memory you need:

### Challenge 1: Experimentation
**The Scenario:** You've just learned about 12.5. Implementing Register and Sign In.
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
