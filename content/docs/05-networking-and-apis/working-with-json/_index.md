---
title: "Working with JSON"
weight: 20
---

**Estimated effort:** 1-2 hours this topic
**Format:** Asynchronous online
**Prerequisites:** Previous iOS topics

{< hint info >}
**🎯 Topic Mission:** 
In this module, we will explore **Working with JSON** and learn how to integrate it into our iOS applications. Your mission is to understand the mechanics behind this concept and write robust Swift code.
{< /hint >}

---

## Learning Objectives

By the end of this session, you will be able to:
1. Understand the core concepts of Working with JSON.
2. Implement Working with JSON in an Xcode project.
3. Apply best practices to ensure clean and maintainable code.

---

## The Story So Far...

We have been progressively building our knowledge of iOS and Swift. In this module, we will expand our toolkit by diving into Working with JSON. 
Open your current Xcode project or start a new Playground to follow along with the hands-on material.

---

## Walkthrough: Exploring Working with JSON

> 📁 **Target Project** — Follow along by building the mini-app presented in the steps below, or integrate these concepts into your own ongoing projects.

# 11. Working with APIs and JSON

JSON stands for JavaScript Object Notation. It is a standard text-based format for representing structured data. It follows the JavaScript object syntax. It is the most popular standard of text data for web APIs nowadays. That means almost all the APIs you will work with or build will be structured in JSON. So it is paramount to learn how to parse JSON data and use them in iOS.

### JSON Structure

Since JSON is a string that resembles JavaScript object syntax, we can put all basic data types inside a JSON string - strings, numbers, arrays, booleans, etc.

### JSON Object

For example, a simple JSON string for a contact would be:

```json
{
    "name": "Alex F",
    "email": "alex@email.com",
    "phone": 1234567890
}
```

This JSON string is exactly like a JavaScript object having three attributes: `name`, `email`, and `phone`. Each attribute has its values (like key-value pairs). Notice that this object contains string type values for name and email and an integer type value for phone.

Another JSON object representing an address could be:

```json
{
    "line1": "100 Winter Street",
    "line2": "Apt 202",
    "city": "Boston",
    "state": "MA",
    "zip": 02115
}
```

Now, a contact that includes an address could be written as:

```json
{
    "name": "Alex F",
    "email": "alex@email.com",
    "phone": 1234567890,
    "address": {
        "line1": "100 Winter Street",
        "line2": "Apt 202",
        "city": "Boston",
        "state": "MA",
        "zip": 02115
    }
}
```

So we can create a hierarchy of objects in JSON. A JSON object can hold other JSON objects.

### JSON Array

JSON can hold arrays of JSON objects as well. As usual, we use `[]` to define an array of JSON objects. For example, we can define an array of contact JSON objects written above:

```json
{
    "contacts": [
        {
            "name": "Alex F",
            "email": "alex@email.com",
            "phone": 1234567890,
            "address": {
                "line1": "100 Winter Street",
                "line2": "Apt 202",
                "city": "Boston",
                "state": "MA",
                "zip": 02115
            }
        },

        {
            "name": "Bob P",
            "email": "bob@email.com",
            "phone": 9864567890,
            "address": {
                "line1": "100 Summer Street",
                "line2": "Apt 562",
                "city": "Boston",
                "state": "MA",
                "zip": 02115
            }
        },

        {
            "name": "Max V",
            "email": "max@email.com",
            "phone": 9123456790,
            "address": {
                "line1": "300 Summer Street",
                "line2": "Apt 582",
                "city": "Boston",
                "state": "MA",
                "zip": 02115
            }
        }
    ]
}
```

In this module, we will build a new app, App11, to demonstrate JSON data parsing.

App11 will look the same as App10, but we will use a JSON-based API.




<!-- Merged from 11.1.-the-json-api-for-the-contact-app.md -->

# 11.1. The JSON API for the Contact App

## The API details:

The setup of the JSON API is exactly the same as the text API we used in App9. Just change the base URL. It'll work just fine.

### The base URL:

https://apis.sakibnm.work:8888/contacts/json/

**The endpoints:**

* Get all contacts: `getall`
  * Method: `GET`
  * Query Params: none
* Get the details of a particular contact: `details`
  * Method: `GET`
  * Query Params: `name`
* Add a contact: `add`
  * Method: `POST`
  * Body Params: `name`, `email`, `phone`.
* Delete a particular contact: `delete`
  * Method: `GET`
  * Query Params: `name`

The only difference is that the response we will get from the API server is not plain String. They are JSON-formatted Strings.

For example,

### **getall:**

https://apis.sakibnm.work:8888/contacts/json/getall

* The response you should get is similar to the following:

```json
    {
        "contacts": [
            {
                "name": "Alice Smith"
            },
            {
                "name": "Bob Smith"
            },
            {
                "name": "David B"
            },
            {
                "name": "Alex C"
            },
            {
                "name": "Mark W"
            },
            {
                "name": "Bob P"
            },
            {
                "name": "Adam F"
            }
        ]
    }
```

### **details:**

https://apis.sakibnm.work:8888/contacts/json/details?name=Alice Smith

* The response should be:

```json
    {
        "email": "asmith@gmail.com",
        "name": "Alice Smith",
        "phone": 9801234567
    }
```

* If the contact is not found, the response should be:

```json
    {
        "error": "Error: Contact Alice Smith not found!"
    }
```

### **delete:**

https://apis.sakibnm.work:8888/contacts/json/delete?name=Alice Smith

* The response should be:

```json
    {
        "info": "Contact Alice Smith is deleted!"
    }
```

* If the contact is not found, the response should be:

```json
    {
        "error": "Error: Contact not found!"
    }
```

### **add:**

https://apis.sakibnm.work:8888/contacts/json/add \[with POST body form]

* If successful, you should receive something like the following:

```json
    {
        "info": "Contact created: Alice Smith, david@email.comt, 6781234567"
    }
```

* If the contact is already there:

```json
    {
        "error": "Error: Contact Alice Smith already exists!"
    }
```

#### PLEASE test the API using Postman.



<!-- Merged from 11.2.-app11-getting-all-the-contact-names-getall-endpoint.md -->

# 11.2. App11: Getting All the Contact Names (getall endpoint)

### Representing JSON in Swift (getall)

From the API details ([11.1.-the-json-api-for-the-contact-app.md](11.1.-the-json-api-for-the-contact-app.md "mention")), we know that `getall` API returns a JSON string like:

```json
{
    "contacts": [
        {
            "name": "David Tu"
        },
        {
            "name": "Alice Smith"
        }
    ]
}
```

**Now, think about the structure of the JSON above.** First of all, the whole thing is a JSON object.

* This JSON object contains a JSON array named "contacts."
  * The "contacts" array contains a list of two JSON objects.
    * Each JSON object contains a key-value pair, where the key is "name."

**Now, think about a similar struct/class in Swift. Can we represent the above JSON structure with a Swift struct?**

Yes, we do. What about the following struct?

```swift
struct ContactName{
    let name:String
}

struct ContactNames{
    let contacts: [ContactName]
}
```

**The first struct `ContactName` represents the objects in the "contacts" array, and the second struct `ContactNames` represents the "contacts" array.**

### Parsing JSON

Let's write the code to parse the JSON response we receive after calling `getall`. Let's create a new Xcode project, App11, and integrate Alamofire into the project using CocoaPods.

**Set up the same Views, Data Models and APIConfigs (MainScreenView.swift, ContactsTableViewCell.swift, APIConfigs.swift, and Contact.swift) as App10.**

Do not forget to change the URL in APIConfigs.swift file to json:

```swift
//
//  APIConfigs.swift
//  App11
//
//  Created by Sakib Miazi on 5/26/23.
//
import Foundation

class APIConfigs{
    //MARK: API base URL...
    static let baseURL = "https://apis.sakibnm.work:8888/contacts/json/"
}
```

The project file structure would look like this:

![](</gitbook-assets/Screenshot 2023-05-26 at 4.05.44 PM (1).png>)

Let's open the View Controller and write the initial controller code similar to App10.

{% code lineNumbers="true" %}
```swift
//
//  ViewController.swift
//  App11
//
//  Created by Sakib Miazi on 5/26/23.
//

import UIKit
import Alamofire

class ViewController: UIViewController {
    let mainScreen = MainScreenView()
    
    //MARK: list to display the contact names in the TableView...
    var contactNames = [String]()
    
    override func loadView() {
        view = mainScreen
    }
    
    override func viewDidLoad() {
        super.viewDidLoad()
        
        title = "Contacts JSON API"
        
        //MARK: setting the delegate and data source...
        mainScreen.tableViewContacts.dataSource = self
        mainScreen.tableViewContacts.delegate = self
        //MARK: removing the separator line...
        mainScreen.tableViewContacts.separatorStyle = .none
        
        //get all contact names when the main screen loads...
        getAllContacts()
        
        //MARK: add action to Add Contact button...
        mainScreen.buttonAdd.addTarget(self, action: #selector(onButtonAddTapped), for: .touchUpInside)
    }
    
    @objc func onButtonAddTapped(){
        
    }
    
    func clearAddViewFields(){
        mainScreen.textFieldAddName.text = ""
        mainScreen.textFieldAddEmail.text = ""
        mainScreen.textFieldAddPhone.text = ""
    }
    
    func showDetailsInAlert(data: String){
        let parts = data.components(separatedBy: ",")
        print(parts)
        
        //MARK: trim the whitespaces from the strings, and show alert...
        let name = parts[0].trimmingCharacters(in: .whitespacesAndNewlines)
        let email = parts[1].trimmingCharacters(in: .whitespacesAndNewlines)
        if let phone = Int(parts[2].trimmingCharacters(in: .whitespacesAndNewlines)){
            //MARK: show alert...
            let message = """
                name: \(name)
                email: \(email)
                phone: \(phone)
                """
            let alert = UIAlertController(title: "Selected Contact", message: message, preferredStyle: .alert)
            alert.addAction(UIAlertAction(title: "OK", style: .default))
            self.present(alert, animated: true)
        }
        
    }
    
    //MARK: add a new contact call: add endpoint...
    func addANewContact(){
        
    }
    
    //MARK: get all contacts call: getall endpoint...
    func getAllContacts(){
        
    }
    
    //MARK: get details of a contact...
    func getContactDetails(name: String){
        
    }
}

extension ViewController: UITableViewDelegate, UITableViewDataSource{
    func tableView(_ tableView: UITableView, numberOfRowsInSection section: Int) -> Int {
        return contactNames.count
    }
    
    func tableView(_ tableView: UITableView, cellForRowAt indexPath: IndexPath) -> UITableViewCell {
        let cell = tableView.dequeueReusableCell(withIdentifier: "names", for: indexPath) as! ContactsTableViewCell
        cell.labelName.text = contactNames[indexPath.row]
        return cell
    }
    
    func tableView(_ tableView: UITableView, didSelectRowAt indexPath: IndexPath) {
        getContactDetails(name: self.contactNames[indexPath.row])
    }
}
```
{% endcode %}

#### Representing the 'getall' JSON with Swift (ContactNames.swift)

Now, let's create the ContactNames.swift file to represent the JSON structure:

```swift
//
//  ContactNames.swift
//  App11
//
//  Created by Sakib Miazi on 5/26/23.
//

import Foundation

struct ContactName{
    let name:String
}

struct ContactNames{
    let contacts: [ContactName]
}
```

### Creating the 'getall' request using Alamofire

Open ViewController.swift file, and let's write the following code in `getAllContacts()`:

{% code lineNumbers="true" %}
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
{% endcode %}

In the above code, we are

* Setting the method to GET (line 4).
* **Now, we are not receiving a regular String like before; we are receiving a JSON response. So, we will use `responseData` instead of `responseString` (line 4).**
* Like before, if there is no network error and the status code is a 200-level code (line 15), we will decode the data using `JSONDecoder()`.
* In lines 20-22, we decode the received `data` using the decoder with the data model we wrote, `ContactNames`. Notice that we are using a try-catch block. Since the decoder might have a runtime exception, we have to handle it gracefully in the catch block.
* The `receivedData` is an object of the `ContactNames` struct, which corresponds to the JSON object we received. In the object, we have a `contacts` array. (Review ContactNames.swift).
  * So, `receivedData.contacts` (line 24), should contain the data from JSON's contacts array.
* In line 24, we are running through each `ContactName` object and appending the name from the object to `contactNames` array for the table view (the table view data source).
* Then we reload the data for the table view.

**Now, this code will not work yet. You will get an error like this:**

<figure><img src="/gitbook-assets/Screenshot 2023-05-26 at 4.35.09 PM (1) (1).png" alt=""><figcaption></figcaption></figure>

### Adopting Codable protocol

It means the data type (`ContactNames`) we are using as the blueprint to decode the JSON data, cannot be used until it is a decodable data type. So, we need to adopt a protocol named [**Codable**](https://developer.apple.com/documentation/swift/codable) from the structs `ContactName` and `ContactNames`. Let's open ContactNames.swift file and update them by adopting the `Codable` protocol.

```swift
//
//  ContactNames.swift
//  App11
//
//  Created by Sakib Miazi on 5/26/23.
//

import Foundation

struct ContactName: Codable{
    let name:String
}

struct ContactNames: Codable{
    let contacts: [ContactName]
}

```

Now, the error will go away.

(Make sure you enable unencrypted HTTP) Let's run the app. It will show us the current contacts.

![](</gitbook-assets/Screenshot 2023-05-26 at 5.26.46 PM (1).png>)

Great! We are done with **getall.**



<!-- Merged from 11.3.-app11-getting-the-details-of-a-selected-contact-details-endpoint.md -->

# 11.3. App11: Getting the Details of a Selected Contact (details endpoint)

The **details** endpoint sends us a response like this:

```swift
{
    "email": "alice@email.comt",
    "name": "Alice Smith",
    "phone": 6781234567
}
```

We already have a data type `Contact` to match this structure. We need to make it adopt the `Codable` protocol:

```swift
//
//  Contact.swift
//  App11
//
//  Created by Sakib Miazi on 5/26/23.
//

import Foundation

//MARK: struct for a contact...
struct Contact: Codable{
    var name:String
    var email:String
    var phone:Int
    
    init(name: String, email: String, phone: Int) {
        self.name = name
        self.email = email
        self.phone = phone
    }
}

```

Now, let's update the `getContactDetails(name: String)` method:

{% code lineNumbers="true" %}
```swift
//MARK: get details of a contact...
func getContactDetails(name: String){
    print(name)
    if let url = URL(string: APIConfigs.baseURL+"details"){
        AF.request(url, method: .get, parameters: ["name":name])
            .responseData(completionHandler: { response in
            //MARK: retrieving the status code...
            let status = response.response?.statusCode
            
            switch response.result{
            case .success(let data):
                print(data)
                //MARK: there was no network error...
                
                //MARK: status code is Optional, so unwrapping it...
                if let uwStatusCode = status{
                    switch uwStatusCode{
                        case 200...299:
                        //MARK: the request was valid 200-level...
                            let decoder = JSONDecoder()
                            do{
                                let receivedData = try decoder
                                    .decode(Contact.self, from: data)
                                print(receivedData)
                                self.showDetailsInAlert(data: receivedData)
                            }catch{

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

//MARK: codes omitted...

//MARK: show details in alert...
func showDetailsInAlert(data: Contact){
        //MARK: show alert...
        let message = """
            name: \(data.name)
            email: \(data.email)
            phone: \(data.phone)
            """
        let alert = UIAlertController(title: "Selected Contact", message: message, preferredStyle: .alert)
        alert.addAction(UIAlertAction(title: "OK", style: .default))
        self.present(alert, animated: true)
        
}
```
{% endcode %}

In the above code:

* In line 4, we are setting the URL for the details endpoint.
* In line 5, we set the parameters to `["name": name]`.
* Between lines 21 to 28, we decode the data with JSONDecoder() using the struct `Contact`. And then, we create an alert to display the details of the received contact.
* (You get to call this method from the adopted method, `didSelectRowAt` related to table view).
* Between lines 56 through 68, we display an alert to show the details.

Now, if we run the app, we will see:

<figure><img src="/gitbook-assets/11.three (1).gif" alt=""><figcaption></figcaption></figure>



<!-- Merged from 11.4.-must-dos-while-decoding-json-adopting-codable.md -->

# 11.4. 'Must Do's While Decoding JSON adopting Codable

Let's look into the example JSON response for the `details` endpoint again:

```json
{
    "email": "alice@email.comt",
    "name": "Alice Smith",
    "phone": 6781234567
}
```

And the data model for the above JSON that adopts the Codable protocol is:

```swift
struct Contact: Codable{
    var name:String
    var email:String
    var phone:Int
}
```

So let's compare the two and think about what are the things we need to handle to parse data carefully from JSON response by adopting Codable:

* The names of the keys (e.g., "email") must match the names of the variables in the Codable struct (e.g., name).
* The types of the values in the response JSON must match the types of the variables in the Codable struct. For example, `"phone": 6781234567` means the value for the key "phone" has a value of integer data type. So we must set the type of the variable `phone` in struct `Contact` to `Int`.
* You do not have to define variables for all the keys in JSON. You can selectively write variables to parse the needed data from a big JSON object.

<mark style="color:red;">**So, the name and the data type of the variables in a Codable must match the name of the keys and the type of the values in JSON. Otherwise, JSON decoding will not work.**</mark>



<!-- Merged from 11.5.-app11-add-a-new-contact.md -->

# 11.5. App11: Add a new Contact

The code is unchanged here since we just upload the data and do not necessarily need to parse JSON responses (for now).

So let's put the code from App10 to `addANewContact(contact: Contact)` and `onButtonAddTapped()` methods:

```swift
//MARK: add a new contact call: add endpoint...
func addANewContact(contact: Contact){
    if let url = URL(string: APIConfigs.baseURL+"add"){
        
        AF.request(url, method:.post, parameters:
                    [
                        //MARK: we can unwrap them here since we made sure they are not null above...
                        "name": contact.name,
                        "email": contact.email,
                        "phone": contact.phone
                    ])
            .responseString(completionHandler: { response in
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
                            self.getAllContacts()
                            self.clearAddViewFields()
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
    }else{
        //alert that the URL is invalid...
    }
}
```

```swift
@objc func onButtonAddTapped(){
    //do the validations...
    if let name = mainScreen.textFieldAddName.text,
       let email = mainScreen.textFieldAddEmail.text,
       let phoneText = mainScreen.textFieldAddPhone.text{
        
        if let phone = Int(phoneText){
            //The String 'phoneText' is successfully converted to an Int...
            let contact = Contact(name: name, email: email, phone: phone)
            print(contact)
            //MARK: call add a new contact API endpoint...
            addANewContact(contact: contact)
        }else{
            //alert...
        }
    }
    else{
        //alert....
    }
}
```

Now, let's run the app.

<figure><img src="/gitbook-assets/11.eight (1).gif" alt=""><figcaption></figcaption></figure>



<!-- Merged from 11.6.-adding-accessory-button-to-table-view-edit-delete-a-contact.md -->

# 11.6. Adding Accessory Button to Table View (Edit/Delete a Contact)

### **Adding a Button to the TableView Cell as an Accessory**

UITableView allows us to add views as accessories. Adding an accessory view is the easiest way to enable user interactions with a cell in a table view. So, in our app, we want to do the following:

<figure><img src="/gitbook-assets/11.ten (1).gif" alt=""><figcaption></figcaption></figure>

* We will have a settings button. If the user taps on the button, there will be a menu to give the user two options: Edit and Delete.
* The user can select one of the options to either edit or delete the contact.

Let's open ViewController.swift file.\
Go to where we adopt the protocols related to the table view.\
Then go to the adopted method for `cellForRowAt`, where we initialize the cell.

Add the following code to add an accessory button:

{% code lineNumbers="true" %}
```swift
func tableView(_ tableView: UITableView, cellForRowAt indexPath: IndexPath) -> UITableViewCell {
    let cell = tableView.dequeueReusableCell(withIdentifier: "names", for: indexPath) as! ContactsTableViewCell
    cell.labelName.text = contactNames[indexPath.row]
    
    //MARK: crating an accessory button...
    let buttonOptions = UIButton(type: .system)
    buttonOptions.sizeToFit()
    buttonOptions.showsMenuAsPrimaryAction = true
    //MARK: setting an icon from sf symbols...
    buttonOptions.setImage(UIImage(systemName: "slider.horizontal.3"), for: .normal)
    
    //MARK: setting up menu for button options click...
    buttonOptions.menu = UIMenu(title: "Edit/Delete?",
                                children: [
                                    UIAction(title: "Edit",handler: {(_) in
                                        self.editSelectedFor(contact: indexPath.row)
                                    }),
                                    UIAction(title: "Delete",handler: {(_) in
                                        self.deleteSelectedFor(contact: indexPath.row)
                                    })
                                ])
    //MARK: setting the button as an accessory of the cell...
    cell.accessoryView = buttonOptions
    return cell
}
```
{% endcode %}

In the above code:

* We create a system button called `buttonOptions`. We set the `buttonOptions` to `sizeToFit()`. It means we ask the button to size to fit the cell's width.
* Then we set the settings to show the menu as the primary action on tapping the button.
* Then we set the image for the button from an appropriate icon from SF Symbols.
* Then from line 13 through 21, we setup the menu.
* **Finally, in line 23,** we set the cell's accessory view to the button.

_<mark style="color:purple;">**If you noticed, the accessory view is a UIView. So technically, you can design your custom view with multiple UI elements. You can add multiple buttons if you want to. For the buttons, you must work with proper constraints, height, width, etc. (And it is a little complicated).**</mark>_

### Writing methods when the user selects an option

We need to write the methods for enabling the actions when the user selects an option from the menu (edit/delete). We write them in the ViewController class.

```swift
func editSelectedFor(contact: Int){
    print("Will edit \(contactNames[contact])")
}

func deleteSelectedFor(contact: Int){
    print("Will delete \(contactNames[contact])")
}
```

Now, let's run the app:

<figure><img src="/gitbook-assets/11.eleven (1).gif" alt=""><figcaption></figcaption></figure>

See? They are printing the appropriate logs as outputs. You can now do anything to edit or delete the contact.



<!-- Merged from 11.7.-reference-code.md -->

# 11.7. Reference Code

{% file src="/gitbook-assets/App11 (1).zip" %}



<!-- Merged from useful-extra-11.8.-decluttering-codes-from-view-controller.md -->

# 11.8. Decluttering codes from View Controller (Recommended Read)

If you noticed, we have 281 lines of code in ViewController.swift. It appears to be a jumble of code. And in many ways, it's hard to read when you'll return to it after a week.

We can utilize protocols and extensions to break the code into multiple files, making it more modular.

## Separating the API calls from the Controller

Let's first separate the code we used to call the Contacts API. The methods we have related to the Contacts API are:

* getAllContacts()
* addANewContact(contact: Contact)
* getContactDetails(name: String)

### Defining a Protocol for the API Calls

So, let's write a protocol where we will declare the methods we will use to call the Contacts API. Let's create a new Swift file ContactsProtocol.swift, inside the 'Contact API Configs' folder.

```swift
//
//  ContactsProtocol.swift
//  App11
//
//  Created by Sakib Miazi on 5/29/23.
//

import Foundation

protocol ContactsProtocol{
    func getAllContacts()
    func addANewContact(contact: Contact)
    func getContactDetails(name: String)
}
```

### Adopting the Protocol

Awesome, now that we have a protocol, let's create another Swift file, ContactsAPICalls.swift, in the MainScreen folder. Import UIKit and Alamofire in this file. Let's write the following code in the file:

```swift
//
//  ContactsAPICalls.swift
//  App11
//
//  Created by Sakib Miazi on 5/29/23.
//

import Foundation
import UIKit
import Alamofire

extension ViewController: ContactsProtocol{
    
}
```

In the above code, we use the extension magic to adopt the ContactsProtocol from ViewController. Now, it's time to move the methods from ViewController.swift to ContactsAPICalls.swift.

{% code lineNumbers="true" %}
```swift
//
//  ContactsAPICalls.swift
//  App11
//
//  Created by Sakib Miazi on 5/29/23.
//

import Foundation
import UIKit
import Alamofire

extension ViewController:ContactsProtocol{
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
    
    //MARK: get details of a contact...
    func getContactDetails(name: String){
        print(name)
        if let url = URL(string: APIConfigs.baseURL+"details"){
            AF.request(url, method: .get, parameters: ["name":name])
                .responseData(completionHandler: { response in
                //MARK: retrieving the status code...
                let status = response.response?.statusCode
                
                switch response.result{
                case .success(let data):
                    print(data)
                    //MARK: there was no network error...
                    
                    //MARK: status code is Optional, so unwrapping it...
                    if let uwStatusCode = status{
                        switch uwStatusCode{
                            case 200...299:
                            //MARK: the request was valid 200-level...
                                let decoder = JSONDecoder()
                                do{
                                    let receivedData = try decoder.decode(Contact.self, from: data)
                                    print(receivedData)
                                    self.showDetailsInAlert(data: receivedData)
                                }catch{

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
    
    //MARK: add a new contact call: add endpoint...
    func addANewContact(contact: Contact){
        if let url = URL(string: APIConfigs.baseURL+"add"){
            
            AF.request(url, method:.post, parameters:
                        [
                            //MARK: we can unwrap them here since we made sure they are not null above...
                            "name": contact.name,
                            "email": contact.email,
                            "phone": contact.phone
                        ])
                .responseString(completionHandler: { response in
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
                                self.getAllContacts()
                                self.clearAddViewFields()
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
        }else{
            //alert that the URL is invalid...
        }
    }
}

```
{% endcode %}

### The file structure of the project now looks like this:

<figure><img src="/gitbook-assets/Screenshot 2023-05-29 at 2.32.25 PM (1).png" alt=""><figcaption></figcaption></figure>

Now, the code is more modular and more manageable.

**Note: You can make it even more modular by putting the table view protocol codes into a separate file from the ViewController.**

{% file src="/gitbook-assets/App11_modular (2).zip" %}

---

## Guided Practice Challenges

Before moving on to the next topic, try these low-stakes practice challenges in Xcode. They will build the exact muscle memory you need:

### Challenge 1: Experimentation
**The Scenario:** You've just learned about Working with JSON.
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

