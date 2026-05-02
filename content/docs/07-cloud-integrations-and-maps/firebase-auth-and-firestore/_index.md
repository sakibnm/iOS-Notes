---
title: "Firebase Auth & Firestore"
weight: 20
---

# 12. Firebase Authentication and Firestore

Firebase is a Google service portal through which Google provides users with many useful Cloud services. Firebase services are very fast, reliable, and easy to use. They have comprehensive guides for developers to integrate and build systems using their services on a plethora of platforms, like, iOS, Android, NodeJS, Flutter, Unity, etc.

**The landing portal of Firebase services is:** [https://firebase.google.com/](https://firebase.google.com/)

## Getting started with Firebase

{% embed url="https://youtu.be/1I9KMcQ_XCg" %}

## Enabling Authentication, Firestore, and Storage

{% embed url="https://youtu.be/gdQDxqoTT5U" %}

## Adding Firebase to our App

{% embed url="https://youtu.be/W0RGrDo4Bv4" %}

## Firestore Data Structure

{% embed url="https://youtu.be/eqW7KNChx5A" %}

## Firebase Official Documentation

* [**Firebase Authentication for iOS**](https://firebase.google.com/docs/auth/ios/start)
* [**Firebase Firestore for iOS**](https://firebase.google.com/docs/firestore/quickstart#ios+)
* [**Firebase Storage for iOS**](https://firebase.google.com/docs/storage/ios/start)




<!-- Merged from 12.1.-app-12-with-firebase.md -->

# 12.1. App 12 with Firebase

In this module, we will build App 12, which will be a contacts list app using,

* Firebase Authentication
* Firebase Firestore

## App12: My Contacts app

The overall goal is to build an app like the following:

<figure><img src="/gitbook-assets/12.one (1).gif" alt=""><figcaption></figcaption></figure>

The app has the following features:

* The user can create an account.
* The user can sign in.
* The user can store their contacts in a database.
* They can log out.
* Each authenticated user will have a separate contacts list.

## Setting up your Firebase project in Firebase's Console

* Please set up your own Firebase project.
* Create your own App12 in Xcode.
* Add your app to Firebase project.
* Download and add the GoogleService-Info.plist to your Xcode project.
* Configure Firebase in AppDelegate.
* Patch up Firebase libraries, Auth, Firestore, FirestoreSwift, and Storage using Swift Package manager.
* Then use the code provided.
* **Otherwise, you cannot see what is happening in Firebase.**



<!-- Merged from 12.2.-setting-up-the-main-screen-view.md -->

# 12.2. Setting up the Main Screen View

In this Project, we will keep the codes as modular as possible. So, let's create a new Group called 'Main Screen.' Put ViewController.swift file inside 'Main Screen.'

Then we create a new Group called 'Views' inside 'Main Screen.' Add a new file named MainScreenView.swift inside 'Views.' The structure looks like this:

![](</gitbook-assets/Screenshot 2023-06-02 at 2.39.45 PM.png>)

### MainScreenView.swift

Then open MainScreenView.swift, and the following code there:

{% code lineNumbers="true" %}
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
{% endcode %}

In the above code, you should have already worked with all the elements in your previous assignments. The only new concept here is to build a floating add button at the bottom right corner of the screen. If you look at lines 77 through 80, we are setting up the constraints for that button.

* It is a regular button; we make it appear floating on the screen.
* We first fix the height and width of the floating button. (Lines 77 and 78).
* Then we fix the bottom and right anchors of the floating button to the bottom and right anchors of the safe area.
* Later, in the controller code, we will force this button to appear over all the UI elements to make it float.
* In lines 43 through 56, we add some shadow effects to make this button look like it is over the other elements.

### ContactsTableViewCell.swift

We are displaying a table view for the contacts the user saves, so we need to design a cell layout for the table view. Let's create a new file inside `Main Screen -> Views ->` named 'ContactsTableViewCell.swift.' Then add the following code there:

{% code lineNumbers="true" %}
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
{% endcode %}

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

![](</gitbook-assets/Screenshot 2023-06-02 at 2.59.59 PM (1).png>)

Great! Now that our view is set up, we can start patching the ViewController.



<!-- Merged from 12.3.-setting-up-the-viewcontroller-with-tableview.md -->

# 12.3. Setting up the ViewController with TableView

Now we will patch up the view to the controller. Let's open up `MainScreen -> ViewController.swift` file, and add the following code there:

{% code lineNumbers="true" %}
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
{% endcode %}

In the above code,

* On line 21, we set the title to "My Contacts."
* On line 24, we tell the navigation controller that we prefer large titles, not the default smaller ones.
* On line 27, we bring the floating button on top of all the views.

If you run the app now, it'd look like this:

![](</gitbook-assets/Screenshot 2023-06-02 at 3.09.07 PM (1).png>)

## Patching the Table View

We need to create a data model for the contacts to display them. Let's create a data model (a struct) Contact in `Data Models -> Contact.swift` file.

Create a new Group named 'Data Models' and add Contact.swift file inside.

![](</gitbook-assets/Screenshot 2023-06-02 at 3.17.58 PM (2).png>)

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

![](</gitbook-assets/Screenshot 2023-06-02 at 3.24.55 PM (1).png>)

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



<!-- Merged from 12.4.-authentication-state-handler.md -->

# 12.4. Authentication State Handler

Now, it's time to set up the authentication for the app. We will use the right navigation bar buttons to manage the sign-in, register, and logout operations. Before we set up those buttons, let's write the logic to handle the authentication states in the app. Let's open ViewCOntroller.swift file and write the following code there:

{% code lineNumbers="true" %}
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
{% endcode %}

In the above code:

* On line 15, we create an authentication state change listener called `handleAuth`. We will use this listener to track whether any user is signed in.
* On line 16, we create a variable to keep an instance of the current signed-in Firebase user.
* Now, you can see that we are overriding two methods that we did not use before.
  * `viewWillAppear`: is a lifecycle method where you can handle the logic before the screen is loaded.
  * `viewWillDisappear`: is another lifecycle method where you can handle the logic right before the screen disappears.
* In `viewWillAppear` method, we define `handleAuth` handler with a closure to handle the authentication state changes. This closure will be automatically called every time a user signs in or logs out. In the closure, you see that we have two parameters: `auth`, and `user`. If the user is nil, there is no authenticated user; else, there is a signed-in user in the app.
* In `viewWillDisappear` method, we remove the listener from the app so that we do not run the listener infinitely.

## if user == nil

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

## else (the user is logged in)

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



<!-- Merged from 12.6.-firestore-structure-for-storing-contacts.md -->

# 12.6. Firestore Structure for Storing Contacts

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



<!-- Merged from 12.7.-adding-a-new-contact.md -->

# 12.7. Adding a New Contact

Let's focus on building the functionalities to add a new contact for a signed-in user in the app.

Let's add a new group in the file navigator, 'Add Contact Screen.' Create a file named 'AddContactViewController.swift' inside it.

Create a sub-group of 'Add Contact Screen' named 'Views' and create 'AddContactView.swift' file inside it.

![](</gitbook-assets/Screenshot 2023-06-02 at 11.30.10 PM (1).png>)

## AddContactView.swift

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

## AddContactViewController.swift

Open the 'AddContactViewController.swift' file. Now let's put the following code there:

{% code lineNumbers="true" %}
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
{% endcode %}

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

## Updating Contact.swift

Open `DataModels -> Contact.swift` and update it like the following:

{% code lineNumbers="true" %}
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
{% endcode %}

In the above code:

* We import FirebaseFirestoreSwift to encode and decode Swift objects to and from Firestore document objects. Each Swift Contact object will represent a contact document in Firestore.
* We adopt the Codable protocol to enable encoding and decoding.
* On line 12, you see that we added `@DocumentID var id: String?`. Do you remember that Firebase has two options for setting a document ID? You can either give an ID manually or auto-generate an ID. We need to put that declaration line to enable both to conform properly to the Firestore document structure. We are saying that the document ID of the Firestore document will be an optional string. For more clarification visit: [https://firebase.google.com/docs/firestore/solutions/swift-codable-data-mapping](https://firebase.google.com/docs/firestore/solutions/swift-codable-data-mapping).

## Uploading the Contact to Firestore

Now, let's put the following code to AddContactViewController.swift file:

{% code lineNumbers="true" %}
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
{% endcode %}

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

## Adding Progress Activity Indicator

We can easily add the progress indicator view when storing the contact in Firestore. Let's add the following code to AddContactViewController.swift:

{% code lineNumbers="true" %}
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
{% endcode %}

In the above code:

* On lines 46 through 58, we are adopting the `ProgressSpinnerDelegate` protocol to display the progress indicator.
* On line 25, we show the indicator before we start storing the contact in Firestore.
* On line 31, we hide the indicator after we complete storing the contact.

## Patching with the Main Screen

Once the floating add contact button is tapped, we need to display the add contact screen. So, let's add the following lines of code to ViewController.swift file:

{% code lineNumbers="true" %}
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
{% endcode %}

In the above code:

* In `viewDidLoad()` method, we add an action to `floatingButtonAddContact` button. The action is defined in `addContactButtonTapped()` method.
* On lines 26 through 30, we populate the Add Contact screen.

Now, if we run the app, we will see:

<figure><img src="/gitbook-assets/12.seven (1).gif" alt=""><figcaption></figcaption></figure>

If we look at the Firestore console, we will see the following:

<figure><img src="/gitbook-assets/Screenshot 2023-06-03 at 1.06.35 AM (1).png" alt=""><figcaption></figcaption></figure>

<figure><img src="/gitbook-assets/Screenshot 2023-06-03 at 1.06.45 AM (1).png" alt=""><figcaption></figcaption></figure>

You can see that:

* The "users" collection contains a document called "alice@email.com". Because the current user's email is "alice@email.com."
* The "alice@email.com" document contains a collection named "contacts."
* Inside the "contacts" collection, we have contact documents (with auto-generated IDs).
* Inside each contact document, we have details of that contact as fields.



<!-- Merged from 12.8.-observing-firestore-updates-updating-the-tableview.md -->

# 12.8. Observing Firestore Updates: Updating the TableView

We need to update our local array of contacts if anything changes in Firestore, right? If the user adds or removes a contact, we need to update the TableView.

So we need to add an observer for Firestore contacts list updates when there is a logged-in user. The observer for Firestore data change is called a `SnapshotListener`. ([https://firebase.google.com/docs/firestore/query-data/listen?hl=en\&authuser=0#swift](https://firebase.google.com/docs/firestore/query-data/listen?hl=en\&authuser=0#swift)).

We need to update `handleAuth` (the handler to handle authentication state changes) in ViewController.swift to add an observer. Open ViewController.swift and add the following code:

{% code lineNumbers="true" %}
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
{% endcode %}

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

<figure><img src="/gitbook-assets/12.ten (1).gif" alt=""><figcaption></figcaption></figure>

### <mark style="color:purple;">**YAY!!! We built our first app using Firebase!!!**</mark>



<!-- Merged from 12.9.-reference-code.md -->

# 12.9. Reference Code

{% file src="/gitbook-assets/App12 (1).zip" %}



## Table of Contents

{{< section >}}
