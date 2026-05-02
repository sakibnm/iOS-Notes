---
title: "1. Writing Clean Code For Asynchronous Operations"
---

**Estimated effort:** 1-2 hours this topic
**Format:** Asynchronous online
**Prerequisites:** Previous iOS topics

{< hint info >}
**🎯 Topic Mission:** 
In this module, we will explore **1. Writing Clean Code For Asynchronous Operations** and learn how to integrate it into our iOS applications. Your mission is to understand the mechanics behind this concept and write robust Swift code.
{< /hint >}

---

## Learning Objectives

By the end of this session, you will be able to:
1. Understand the core concepts of 1. Writing Clean Code For Asynchronous Operations.
2. Implement 1. Writing Clean Code For Asynchronous Operations in an Xcode project.
3. Apply best practices to ensure clean and maintainable code.

---

## The Story So Far...

We have been progressively building our knowledge of iOS and Swift. In this module, we will expand our toolkit by diving into 1. Writing Clean Code For Asynchronous Operations. 
Open your current Xcode project or start a new Playground to follow along with the hands-on material.

---

## Walkthrough: Exploring 1. Writing Clean Code For Asynchronous Operations

> 📁 **Target Project** — Follow along by building the mini-app presented in the steps below, or integrate these concepts into your own ongoing projects.

<!-- Merged from 1.1.-decluttering-our-app11-contacts-app-with-json.md -->

# 1.1. Decluttering our App11 (Contacts App with JSON)

So far in [useful-extra-11.8.-decluttering-codes-from-view-controller.md](../../11.-working-with-json/useful-extra-11.8.-decluttering-codes-from-view-controller.md "mention") section, we learned how to write protocols and use extensions to modularize your code. Let's start there.&#x20;

So far, we have the following structure of the project:

* App 11
  * Data Models (Directory)
    * Contact.swift
    * ContactNames.swift
  * Contact API Coinfigs (Directory)
    * APIConfigs.swift
    * ContactsProtocol.swift
  * Edit Screen (Directory) _—_ _<mark style="color:$info;">Added later for completeness</mark>_
    * Views (Directory)&#x20;
      * EditScreenView.swift
    * EditViewController.swift
  * Main Screen (Directory)
    * Views (Directory)
      * ContactsTableViewCell.swift
      * MainScreenView.swift
    * ContactListTableViewManager.swift _— <mark style="color:$info;">Added later with extension magic!</mark>_
    * ContactsAPICalls.swift
    * ContactsViewController.swift — _<mark style="color:$info;">Changed from ViewController using SceneDelegate</mark>_
  * _<mark style="color:$info;">AppDelegate.swift</mark>_
  * _<mark style="color:$info;">SceneDelegate.swift</mark>_

## 1.1.1. Updating Contact API Protocol code

To be able to accommodate the async-await calls to remove the spaghetti code, we need a few changes in our Contact API protocol in ContactsProtocol.swift file:

```swift
import Foundation

protocol ContactsProtocol{
    func getAllContacts() async -> Bool
    func addANewContact(contact: Contact) async -> Bool
    func getContactDetails(name: String) async -> Contact?
    func deleteContact(name: String) async -> Bool
}

```

The basic differences here from before are:

1. We made all the API call functions asynchronous by adding the _**async**_ notation.&#x20;
2. We are also making the functions return something (Bool, Contact, etc.) so that it becomes easier when we sequence them from the controller.

## 1.1.2. Making API calls async

So we will now rewrite (a little) the current code for the API calls (getall, add, delete, getdetails) to be able to call them asynchronously.

#### getAllContacts()

For example, the previous code for the getall API call in ContactAPICalls.swift file was:

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

Here, our callback was on line 4, **completionHandler**. This closure gets returned when the network call is complete.&#x20;

Now, we need to get rid of the completionHandler since we will be managing the asynchronous operations ourselves.&#x20;

So, the updated code becomes something like:

{% code lineNumbers="true" %}
```swift
//MARK: get all contacts...
func getAllContacts() async -> Bool{
    if let url = URL(string: APIConfigs.baseURL + "getall") {
        
        let response = await AF.request(url, method: .get)
            .serializingData()
            .response
        
        let statusCode = response.response?.statusCode
        
        switch response.result {
        case .success(let data):
            if let uwStatusCode = statusCode {
                switch uwStatusCode {
                case 200...299:
                    //MARK: the request was valid 200-level...
                    self.contactNames.removeAll()
                    let decoder = JSONDecoder()
                    do {
                        let receivedData = try decoder.decode(ContactNames.self, from: data)
                        for item in receivedData.contacts {
                            self.contactNames.append(item.name)
                        }
                        return true
                    } catch {
                        print("JSON couldn't be decoded.")
                        return false
                    }
                    
                case 400...499:
                    //MARK: the request was not valid 400-level...
                    print(data)
                    return false
                    
                default:
                    //MARK: probably a 500-level error...
                    print(data)
                    return false
                }
            }
            
        case .failure(let error):
            //MARK: there was a network error...
            print(error)
            return false
        }
    } else {
        return false
    }
    return false
}
```
{% endcode %}

Let's compare the two codes and check what happened here.

1. Instead of using the completionHandler, we are separating the AlamoFire call on line 5 with the await notation and retrieving the response asynchronously.
   1. Since we are sequencing the call, **await** will suspend execution until it receives the response.
2. Then, we retrieve the status code from the response on line 9, and subsequently write a switch-case block to filter cases with different status codes.
   1. We only return **true** if it is in the 200-level block. Every other case returns **false.**

It already looks less cluttered!&#x20;

### 1.1.3. Control Code

Now, let's see how we can call getAllContacts using the Task{} block from the ViewController. Let's check the corresponding code in ContactsViewController.swift file:

{% code lineNumbers="true" %}
```swift
import UIKit
import Alamofire

class ContactsViewController: UIViewController {
    
    //MARK: list to display the contact names in the TableView...
    var contactNames = [String]()
    
    let notificationCenter = NotificationCenter.default
    
    let mainScreen = MainScreenView()
    
    override func loadView() {
        view = mainScreen
    }
    
    override func viewDidLoad() {
        super.viewDidLoad()
        
        title = "Contacts JSON API"
        
        //Code reducted...
        
        //MARK: get all contact names when the main screen loads...
        callGetAllContacts()
        
        //Code reducted...
    }
    
    func callGetAllContacts(){
        Task{
            let getallSuccess = try await getAllContacts()
            if getallSuccess{
                mainScreen.tableViewContacts.reloadData()
            }
        }
    }
    
}
```
{% endcode %}

In the above code:

1. When the app loads, we want to load the list of current contacts, so we call callGetAllContacts() function on line 25. Lines 30 through 37 show the implementation of the function.
   1. You can see we have a Task{} block. Inside the block, everything will sequentially wait.
   2. On line 32, we call the API and wait for it to return the result. If the response was of 200-level, we reload the data in our table view.



<!-- Merged from 1.2.-decluttering-continues....md -->

# 1.2. Decluttering continues...

Now we will look at an example where we will edit a contact. We would need to make two API calls sequentially: delete the contact, and then add a new contact with updated data.

For the sake of simplicity in this tutorial, I will skip most of the code; however, I will discuss the most important parts.

Let's look at the updated delete and add contact API calls:

#### addANewContact(contact: Contact)

{% code lineNumbers="true" %}
```swift
//MARK: add a new contact call: add endpoint...
func addANewContact(contact: Contact) async -> Bool{
    if let url = URL(string: APIConfigs.baseURL + "add") {
        
        let response = await AF.request(
            url,
            method: .post,
            parameters: [
                "name": contact.name,
                "email": contact.email,
                "phone": contact.phone
            ]
        )
        .serializingData()
        .response
        
        let statusCode = response.response?.statusCode
        
        switch response.result {
        case .success(let data):
            if let uwStatusCode = statusCode {
                switch uwStatusCode {
                case 200...299:
                    return true
                    
                case 400...499:
                    return false
                    
                default:
                    return false
                }
            }
            return false
            
        case .failure(_):
            return false
        }
    } else {
        return false
    }
}
```
{% endcode %}

#### deleteContact(name: String)

{% code lineNumbers="true" %}
```swift
//MARK: delete the selected contact...
func deleteContact(name: String) async -> Bool{
    
    if let url = URL(string: APIConfigs.baseURL + "delete") {
        
        let response = await AF.request(
            url,
            method: .get,
            parameters: ["name": name]
        )
        .serializingData()
        .response
        
        let statusCode = response.response?.statusCode
        
        switch response.result {
        case .success(let data):
            if let uwStatusCode = statusCode {
                switch uwStatusCode {
                case 200...299:
                    return true
                    
                case 400...499:
                    return false
                    
                default:
                    return false
                }
            }
            return false
            
        case .failure(_):
            return false
        }
    } else {
        return false
    }
}
```
{% endcode %}

Both calls were defined as asynchronous calls. Now, let's look into the code snippet where the user taps on the save button from the edit screen:

{% code lineNumbers="true" %}
```swift
@objc func editContactSaveButtonPressed(notification: Notification){
    let tuple: (Contact, String) = notification.object as! (Contact, String)
    Task{
        let deleteSuccess = try await deleteContact(name: tuple.1)
        if deleteSuccess{
            let addSuccess = try await addANewContact(contact: tuple.0)
            if addSuccess{
                self.navigationController?.popViewController(animated: true)
                self.callGetAllContacts()
            }
        }
    }
}
```
{% endcode %}

In the above code:

1. I am sending a notification from the Edit Screen to the Main Screen to indicate that the user has tapped the Save button. The object in the notification contained a tuple that holds two values: the updated contact and the name from the old contact.
2. On lines 3 through 12, I am writing a Task{} block which enables sequential async operations.&#x20;
   1. First, on line 4, I am calling the delete API and waiting for it to complete.
   2. If the deletion is successful, I then call the add API.
   3. When deletion becomes successful, then I call the getall API and refresh the list.

The code looks certainly more readable now!

Please download the whole project and study that to understand the concepts.



<!-- Merged from 1.3.-reference-code.md -->

# 1.3. Reference Code

{% file src="/gitbook-assets/App 11 modular async.zip" %}

---

## Guided Practice Challenges

Before moving on to the next topic, try these low-stakes practice challenges in Xcode. They will build the exact muscle memory you need:

### Challenge 1: Experimentation
**The Scenario:** You've just learned about 1. Writing Clean Code For Asynchronous Operations.
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

