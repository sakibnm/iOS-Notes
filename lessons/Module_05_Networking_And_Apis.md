# Module 05: Networking And APIs

## Table of Contents




### HTTP & Networking

**Estimated effort:** 1-2 hours this topic
**Format:** Asynchronous online
**Prerequisites:** Previous iOS topics


**🎯 Topic Mission:** 
In this module, we will explore **HTTP & Networking** and understand its fundamental mechanics. Your mission is to understand the mechanics behind this concept and write robust Swift code.


---

## Learning Objectives

By the end of this session, you will be able to:
1. Understand the core concepts of HTTP & Networking.
2. Implement HTTP & Networking in an Xcode project.
3. Apply best practices to ensure clean and maintainable code.

---

## The Story So Far...

We have been progressively building our knowledge of iOS and Swift. In this module, we will expand our toolkit by diving into HTTP & Networking. 
Open your current Xcode project or start a new Playground to follow along with the hands-on material.

---

## Walkthrough: Exploring HTTP & Networking

> 📁 **Target Project** — Follow along by building the mini-app presented in the steps below, or integrate these concepts into your own ongoing projects.

### Making the app communicate over the Internet

In this module, we will learn how an iOS app can talk to a server over the Internet. We will learn how to use remote APIs, fetch data from a server, and send data to a server using those APIs.





### HTTP connections

Intro to HTTP

[View Resource](https://northeastern.hosted.panopto.com/Panopto/Pages/Viewer.aspx?id=d52f70dc-ac38-4530-9e9a-ae9e01243cec)

HTTP stands for HyperText Transfer Protocol. It is used by two parties to transmit data between themselves over the Internet. For example, When you browse the web, your browser uses HTTP. The two parties are called:

* **Client**: who requests data. For example, an app is requesting information about the user.
* **Server**: who responds with the requested data. For example, the database server who responds to the app by sending the user information.

<figure><img src="/gitbook-assets/Screenshot 2023-05-25 at 1.09.07 PM (2).png" alt="Educational illustration for iOS concept"><figcaption></figcaption></figure>

**The request from a client:** When a client sends a request to the server, it includes the following:

* **URL (Host/path): Uniform Resource Locator (URL)** is the server's web address/IP address so that the client can locate it over the Internet.
* **Method:** There are [a few kinds of requests](https://developer.mozilla.org/en-US/docs/Web/HTTP/Methods) a client can make to the server:
  * **GET:** this method is used if a client wants to get some data from the server. This method is the most used one in real life.
  * **POST:** This method is used if a client wants to send some data to the server.
  * **PUT:** Similar to POST, the system admins often use PUT to update the database servers.
  * We will use **GET and POST** methods more than 99% of the time in real life.
  * There are other methods, like PUT and DELETE, which we will not discuss here.
* **Headers:** the metadata a client can send to the server, where a client gives additional details for the request they are sending. For example, a header can hold the client's authentication token to prove the client's authenticity to the server.
* **Query String:** If you noticed in real life, many websites have `?` in their URLs when you browse. For example: `http://example.com?q=test&state=MA`.
  * Here the URL is `http://example.com`
  * After `?` we have `q=test` and `state=MA` separated by `&`.
  * These are key-value pairs. In `q=test`, q is the key, and test is the value.
  * A client can send information to the server using these key-value pairs. The whole thing after `?` is the query string.
* **Body:** the body is the rest of the request. There is no limit to the body. A client can send additional information to the server using the request's body—for example, form data, JSON data, etc.

**The server's response:** A typical response from the server includes:

* **Status code:** it indicates whether a specific HTTP request has been successfully completed.
  * Informational (100-199)
  * **Successful (200-299)**
  * Redirects (300-399)
  * **Client errors (400-499)**
  * **Server errors (500-599)**
  * You have probably seen the error 404 at some point in your cyber life. The 400-level codes usually mean the request the client sent was invalid.
  * 500-level codes are also pretty common. It means the request was correct, yet the server failed to execute properly to process the request.
  * 200-level codes are the most common, and usually, we don't see them in our browsers because they indicate a successful response.
* **Body:** the response from the server comes as a part of the body.
* **Headers:** SImilar to the request headers, server may use headers to send additional meta data.



### Postman: a Useful Tool to Test Web Services

### Installing Postman

<div style="position: relative; padding-bottom: 56.25%; height: 0; overflow: hidden; margin-bottom: 1.5rem; border-radius: 8px; border: 1px solid var(--rule);">
  <iframe src="https://www.youtube.com/embed/v62mZZ6HG8Y" style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;" frameborder="0" allowfullscreen></iframe>
</div>

* Visit [this link](https://www.postman.com/downloads/?utm\_source=postman-home) to download Postman. Install it on your Mac by copying the extracted file into the Applications folder. Open it, create an account, and log in.
* Then create a new collection by clicking on `+` icon on the top left corner. Then add requests to start testing.



### Testing our Simple Custom API with Postman

Please watch the video to learn how to use Postman with an API.

<div style="position: relative; padding-bottom: 56.25%; height: 0; overflow: hidden; margin-bottom: 1.5rem; border-radius: 8px; border: 1px solid var(--rule);">
  <iframe src="https://www.youtube.com/embed/0kQbmIaIvVk" style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;" frameborder="0" allowfullscreen></iframe>
</div>

### Contacts API details

**The base URL:** [https://apis.sakibnm.work:8888/contacts/text/](https://apis.sakibnm.work:8888/contacts/text/)

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



### App that Uses Our Contact API

Our app should look like the following at the end.:

<figure><img src="/gitbook-assets/10.one (1).gif" alt="Educational illustration for iOS concept"><figcaption></figcaption></figure>

Let's create a new project in Xcode, "App10." And add Alamofire to the project using Cocoapods. ( See [9.-cocoa-pods](../9.-cocoa-pods/ "mention")).

Open the workspace (not the xcodeproject).

###



### Setting up the View of App10

### Setting up the View

* In the app, we will add a bottom view to add a new contact.
  * The bottom add view contains three text fields for name, email, and phone.
* At the top, we will have a table view displaying current contacts.

Let's add the following files:

* MainScreenView.swift
* ContactsTableView.swift

### **MainScreenView.swift**

Let's add the following code to the MainScreenView.swift file:


```swift
//
//  MainScreenView.swift
//  App10
//
//  Created by Sakib Miazi on 5/25/23.
//

import UIKit

class MainScreenView: UIView {
    //MARK: tableView for contacts...
    var tableViewContacts: UITableView!
    
    //MARK: bottom view for adding a Contact...
    var bottomAddView:UIView!
    var textFieldAddName:UITextField!
    var textFieldAddEmail:UITextField!
    var textFieldAddPhone:UITextField!
    var buttonAdd:UIButton!
    
    override init(frame: CGRect) {
        super.init(frame: frame)
        self.backgroundColor = .white
        
        setupTableViewContacts()
        
        setupBottomAddView()
        setupTextFieldAddName()
        setupTextFieldAddEmail()
        setupTextFieldAddPhone()
        setupButtonAdd()
        
        initConstraints()
    }
    
    //MARK: the table view to show the list of contacts...
    func setupTableViewContacts(){
        tableViewContacts = UITableView()
        tableViewContacts.register(ContactsTableViewCell.self, forCellReuseIdentifier: "names")
        tableViewContacts.translatesAutoresizingMaskIntoConstraints = false
        self.addSubview(tableViewContacts)
    }
    
    //MARK: the bottom add contact view....
    func setupBottomAddView(){
        bottomAddView = UIView()
        bottomAddView.backgroundColor = .white
        bottomAddView.layer.cornerRadius = 6
        bottomAddView.layer.shadowColor = UIColor.lightGray.cgColor
        bottomAddView.layer.shadowOffset = .zero
        bottomAddView.layer.shadowRadius = 4.0
        bottomAddView.layer.shadowOpacity = 0.7
        bottomAddView.translatesAutoresizingMaskIntoConstraints = false
        self.addSubview(bottomAddView)
    }
    
    func setupTextFieldAddName(){
        textFieldAddName = UITextField()
        textFieldAddName.placeholder = "Name"
        textFieldAddName.borderStyle = .roundedRect
        textFieldAddName.translatesAutoresizingMaskIntoConstraints = false
        bottomAddView.addSubview(textFieldAddName)
    }
    
    func setupTextFieldAddEmail(){
        textFieldAddEmail = UITextField()
        textFieldAddEmail.placeholder = "Email"
        textFieldAddEmail.borderStyle = .roundedRect
        textFieldAddEmail.translatesAutoresizingMaskIntoConstraints = false
        bottomAddView.addSubview(textFieldAddEmail)
    }
    
    func setupTextFieldAddPhone(){
        textFieldAddPhone = UITextField()
        textFieldAddPhone.placeholder = "Phone"
        textFieldAddPhone.borderStyle = .roundedRect
        textFieldAddPhone.translatesAutoresizingMaskIntoConstraints = false
        bottomAddView.addSubview(textFieldAddPhone)
    }
    
    func setupButtonAdd(){
        buttonAdd = UIButton(type: .system)
        buttonAdd.titleLabel?.font = .boldSystemFont(ofSize: 16)
        buttonAdd.setTitle("Add Contact", for: .normal)
        buttonAdd.translatesAutoresizingMaskIntoConstraints = false
        bottomAddView.addSubview(buttonAdd)
    }
    
    func initConstraints(){
        NSLayoutConstraint.activate([
            //bottom add view...
            bottomAddView.bottomAnchor.constraint(equalTo: self.safeAreaLayoutGuide.bottomAnchor,constant: -8),
            bottomAddView.leadingAnchor.constraint(equalTo: self.safeAreaLayoutGuide.leadingAnchor, constant: 8),
            bottomAddView.trailingAnchor.constraint(equalTo: self.safeAreaLayoutGuide.trailingAnchor, constant: -8),
            
            buttonAdd.bottomAnchor.constraint(equalTo: bottomAddView.bottomAnchor, constant: -8),
            buttonAdd.leadingAnchor.constraint(equalTo: bottomAddView.leadingAnchor, constant: 4),
            buttonAdd.trailingAnchor.constraint(equalTo: bottomAddView.trailingAnchor, constant: -4),
            
            textFieldAddPhone.bottomAnchor.constraint(equalTo: buttonAdd.topAnchor, constant: -8),
            textFieldAddPhone.leadingAnchor.constraint(equalTo: buttonAdd.leadingAnchor, constant: 4),
            textFieldAddPhone.trailingAnchor.constraint(equalTo: buttonAdd.trailingAnchor, constant: -4),
            
            textFieldAddEmail.bottomAnchor.constraint(equalTo: textFieldAddPhone.topAnchor, constant: -8),
            textFieldAddEmail.leadingAnchor.constraint(equalTo: textFieldAddPhone.leadingAnchor),
            textFieldAddEmail.trailingAnchor.constraint(equalTo: textFieldAddPhone.trailingAnchor),
            
            textFieldAddName.bottomAnchor.constraint(equalTo: textFieldAddEmail.topAnchor, constant: -8),
            textFieldAddName.leadingAnchor.constraint(equalTo: textFieldAddEmail.leadingAnchor),
            textFieldAddName.trailingAnchor.constraint(equalTo: textFieldAddEmail.trailingAnchor),
            
            bottomAddView.topAnchor.constraint(equalTo: textFieldAddName.topAnchor, constant: -8),
            //...
            
            tableViewContacts.topAnchor.constraint(equalTo: self.safeAreaLayoutGuide.topAnchor, constant: 32),
            tableViewContacts.leadingAnchor.constraint(equalTo: self.safeAreaLayoutGuide.leadingAnchor, constant: 8),
            tableViewContacts.trailingAnchor.constraint(equalTo: self.safeAreaLayoutGuide.trailingAnchor, constant: -8),
            tableViewContacts.bottomAnchor.constraint(equalTo: bottomAddView.topAnchor, constant: -8),
            
            
        ])
    }
    
    
    //MARK: initializing constraints...
    required init?(coder: NSCoder) {
        fatalError("init(coder:) has not been implemented")
    }
}

```


In the above code, we add three text fields as the sub-views of the bottom add view. Then we anchor the bottom add view to the bottom of the safe area. Then we anchor the table view to the top, leading and trailing anchors of the safe area. Finally, we anchor the bottom of the table view to the top of the bottom add view.

Look at `setupBottomAddView()`. Play with the attributes (color, margins, border, etc.) to design it as you want to.

### **ContactsTableViewCell.swift**

In the ContactsTableViewCell.swift file, we define the view for each cell in the table view. Let's add the following code:


```swift
//
//  ContactsTableViewCell.swift
//  App10
//
//  Created by Sakib Miazi on 5/25/23.
//

import UIKit

class ContactsTableViewCell: UITableViewCell {
    
    var wrapperCellView: UIView!
    var labelName: UILabel!
    
    override init(style: UITableViewCell.CellStyle, reuseIdentifier: String?) {
        super.init(style: style, reuseIdentifier: reuseIdentifier)
        
        setupWrapperCellView()
        setupLabelName()
        
        initConstraints()
    }

    func setupWrapperCellView(){
        wrapperCellView = UITableViewCell()
        
        //working with the shadows and colors...
        wrapperCellView.backgroundColor = .white
        wrapperCellView.layer.cornerRadius = 4.0
        wrapperCellView.layer.shadowColor = UIColor.gray.cgColor
        wrapperCellView.layer.shadowOffset = .zero
        wrapperCellView.layer.shadowRadius = 2.0
        wrapperCellView.layer.shadowOpacity = 0.7
        wrapperCellView.translatesAutoresizingMaskIntoConstraints = false
        self.addSubview(wrapperCellView)
    }
    
    func setupLabelName(){
        labelName = UILabel()
        labelName.font = UIFont.boldSystemFont(ofSize: 16)
        labelName.translatesAutoresizingMaskIntoConstraints = false
        wrapperCellView.addSubview(labelName)
    }
    
    func initConstraints(){
        NSLayoutConstraint.activate([
            wrapperCellView.topAnchor.constraint(equalTo: self.topAnchor,constant: 4),
            wrapperCellView.leadingAnchor.constraint(equalTo: self.leadingAnchor, constant: 10),
            wrapperCellView.trailingAnchor.constraint(equalTo: self.trailingAnchor, constant: -10),
            wrapperCellView.bottomAnchor.constraint(equalTo: self.bottomAnchor, constant: -4),
            
            labelName.topAnchor.constraint(equalTo: wrapperCellView.topAnchor, constant: 8),
            labelName.leadingAnchor.constraint(equalTo: wrapperCellView.leadingAnchor, constant: 10),
            labelName.heightAnchor.constraint(equalToConstant: 20),
            labelName.widthAnchor.constraint(equalTo: wrapperCellView.widthAnchor),
            
            wrapperCellView.heightAnchor.constraint(equalToConstant: 36)
            
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
    
    required init?(coder: NSCoder) {
        fatalError("init(coder:) has not been implemented")
    }

}
```


Look at `setupWrapperCellView()`. Play with the attributes (color, margins, border, etc.) to design it as you want to.

### **ViewController.swift**

Let's add load the view in the controller. Let's add the following code to ViewController.swift:


```swift
//
//  ViewController.swift
//  App10
//
//  Created by Sakib Miazi on 5/25/23.
//

import UIKit
import Alamofire

class ViewController: UIViewController {
    
    let mainScreen = MainScreenView()
    
    override func loadView() {
        view = mainScreen
    }
    
    override func viewDidLoad() {
        super.viewDidLoad()
        
        title = "Contacts API Testing"
    }
}

```


If we run the app now, it will look like:

![Educational illustration for iOS concept](</gitbook-assets/Screenshot 2023-05-25 at 7.42.51 PM (1).png>)



### Fetching Data with AlamoFire: GET

It's time to fetch the contacts' names and display them in our table view. We will call the API with `getall` endpoint when the app starts, and display the response on the table view ([10.3.-testing-our-simple-custom-api-with-postman.md](10.3.-testing-our-simple-custom-api-with-postman.md "mention")).

### Using Alamofire for text responses

If you noticed, in our API, we are getting back text responses from the server. We will use Alamofire to process the responses. Before we do, let's define an array of Strings in our ViewController for populating the table view. That array will hold the names of the contacts returned by the API endpoint `getall`.


```swift
//
//  ViewController.swift
//  App10
//
//  Created by Sakib Miazi on 5/25/23.
//

import UIKit
import Alamofire

class ViewController: UIViewController {
    
    let mainScreen = MainScreenView()
    
    //MARK: list to display the contact names in the TableView...
    var contactNames = [String]()
    
    //codes omitted...
}

```


First, we need the API base URL to be set up. You can directly use the URL string in the call; however, it is always a better practice if you save these API details in a separate file as a static String, so that you can reuse that from any screen if you need to.

Let's create a file named `APIConfigs.swift` under `App10` folder. It is a Swift class file, **not a CocoaTouch Class.**

![Educational illustration for iOS concept](</gitbook-assets/Screenshot 2023-05-25 at 8.45.51 PM (1).png>)

In APIConfig.swift, let's add the static constant for the base URL:


```swift
//
//  Configs.swift
//  App10
//
//  Created by Sakib Miazi on 5/25/23.
//

import Foundation

class APIConfigs{
    //MARK: API base URL...
    static let baseURL = "https://apis.sakibnm.work:8888/contacts/text/"
}
```


You can access the base URL by writing `APIConfigs.baseURL` from anywhere in the project.

### The 'getall' endpoint with Alamofire

Now, let's write a function to call the `getall` API endpoint and load the names in `contactNames` array.

<pre class="language-swift" data-line-numbers><code class="lang-swift">//
//  ViewController.swift
//  App10
//
//  Created by Sakib Miazi on 5/25/23.
//
import UIKit
import Alamofire

<strong>class ViewController: UIViewController {
</strong>    
    let mainScreen = MainScreenView()
    
    //MARK: list to display the contact names in the TableView...
    var contactNames = [String]()
    
    override func loadView() {
        view = mainScreen
    }
    
    override func viewDidLoad() {
        super.viewDidLoad()
        
        title = "Contacts API Testing"
        
        //get all contact names when the main screen loads...
        getAllContacts()
    }
    
    //MARK: get all contacts...
    func getAllContacts(){
        if let url = URL(string: APIConfigs.baseURL + "getall"){
            AF.request(url, method: .get)
                .responseString(completionHandler: { response in
                        print(response.result)
                    }
                )
        }
    }
}

</code></pre>

First of all, you need to **import the Alamofire library**.

Let's look at the function `getAllContacs()` method definition:

* First, we build the URL with the `baseURL` and the `getall` endpoint using URL() initializer. URL() returns a URL wrapped with optional (in case it cannot create a valid URL, it returns an Optional(nil)). We have to unwrap it. So we unwrap it and put it in the constant `url`.
* Then we use `url` to make a request with Alamofire. We use `AF` to use Alamofire functions. So, here we are creating an Alamofire request with the `url` we built.
* If you noticed, we set the method of the request to `.get`. Remember, `getall` endpoint of the API server expects a GET request.
* Then we call the `responseString()` method for the request. We are handling text responses, right? So, we need to catch String-type data from the response we get from the server.
* Then we write a closure `completionHandler` to deal with the data after we receive the response.\
  \
  &#xNAN;_**Please note any communication over the Internet is Asynchronous. That means we are dealing with data that are hosted probably hundreds if not thousands of miles away. So, it will take time to receive the response from the server after you send the request. It might feel like it's real-time, but logically, it's not. So, when we build apps that communicate over the Internet, we must be very careful dealing with it. We should not expect that we will receive the response right away.**_&#x20;
* In the closure, we print `response.result` to see what kind of data we received as the response. If you run the app now, It prints something like this:\
  &#xNAN;**`success("Alice Smith\nBob Smith\nDavid B\nAlex C\nMark W\n")`**
  * `success()` in the response means the request was successfully transmitted, and there was no network error.
  * See, we have  in between two consecutive names. The character  means a new line. So, we have to fetch the whole String and then use it.
* **Also, the status code the response has is very important. We need to check if it is a 200-level or a 400-level code.**
  * **200-level codes mean the request was valid, and we received a desirable response.**
  * **400-level codes mean the request was incorrect, so we must handle the response appropriately to manage the UI elements properly.**

Let's write the following code in the `completionHandler` closure taking care of the status codes and network errors:


```swift
//MARK: get all contacts...
func getAllContacts(){
    if let url = URL(string: APIConfigs.baseURL + "getall"){
        AF.request(url, method: .get).responseString(completionHandler: { response in
            //MARK: retrieving the status code...
            let status = response.response?.statusCode
            
            switch response.result{
            case .success(let data):
                //MARK: there was no network error...
                
                //status code is Optional, so unwrapping it...
                if let uwStatusCode = status{
                    switch uwStatusCode{
                        case 200...299:
                        //MARK: the request was valid 200-level...
                            var names = data.components(separatedBy: "\n")
                            self.contactNames = names
                            print(self.contactNames)
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


In the above code:

* First, we retrieve the status code from the response (at line 6). It is an optional value. So, we need to unwrap it when we use it.
* Then we check for network errors from `response.result`. (At line 8).
  * If there is no network error, we now check if the status code is a 200-level- or 400-level.
  * If the code is a 200-level code:
    * Then we separate each line by splitting the data using the delimiter . (At line 17).
    * Then we set the Strings from data to `contactNames` array.
    * And then, we print the array.
  * If the code is 400- or 500-level, we print the debug log for now. You might want to handle these conditions depending on the app's needs.
* We might need to check our internet connection if there is a network failure. (at line 36).

**Now, if we run the app, it will run, but you won't see any items printed.** If you check the outputs, you might see something like the following:


```
sessionTaskFailed(error: Error Domain=NSURLErrorDomain Code=-1022 "The resource could not be loaded because the App Transport Security policy requires the use of a secure connection." 
```


**By default, iOS does not allow HTTP connections without encryption. We should always use the connections through HTTPS.**

**However,** since my API is a dumb API, and I am using the API for demonstration purposes, I didn't go through the HTTPS configuration process. So, we need to enable unencrypted HTTP connections in our app.

If you face this, you can solve this by doing the following:

### Enabling unencrypted HTTP in our app

* We need to open `Info.plist` file from the File Navigator of the project.
* Right-click (control + click) on the empty space of `Info.plist`.
* Select `Add Row`.
* Search and Select "App Transport Security Settings."
  * Inside "App Transport Security Settings," add an attribute by clicking plus icon(`+`).
  * Set "Allow Arbitrary Loads" attribute's value to YES.

<figure><img src="/gitbook-assets/10.12 (1).gif" alt="Educational illustration for iOS concept"><figcaption></figcaption></figure>

It should now allow unencrypted HTTP.

If we run the app now, it should print the following:

**`["Alice Smith", "Bob Smith", "David B", "Alex C", "Mark W", ""]`****.**

**Interestingly, there is an empty String at the end.** This happens because the server adds a  character at the end of the last user's name. So we need to remove it from the `contactNames`.

Let's add `self.contactNames.removeLast()` after line 18.

Now, we have the perfect `contactNames` array to be displayed in the table view.

### Displaying data on the table view

Now, let's adopt the protocols for the table view:


```swift
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
        
    }
}
```


Then, set the delegate and data source in `viewDidLoad()` method.

<pre class="language-swift" data-line-numbers><code class="lang-swift">override func viewDidLoad() {
     super.viewDidLoad()
     
     title = "Contacts API Testing"
     
     //MARK: setting the delegate and data source...
     mainScreen.tableViewContacts.dataSource = self
     mainScreen.tableViewContacts.delegate = self
<strong>     
</strong><strong>     //MARK: removing the separator line...
</strong>     mainScreen.tableViewContacts.separatorStyle = .none
     
     //get all contact names when the main screen loads...
     getAllContacts()
}
</code></pre>

In the above code, at line 11, we remove the separator line of the table view. If you want to remove the line, you get to do this after the table view is populated. If you add this instruction when setting up the table view, it will not work. So, we write this code in the controller.

If you run the app now, the table view remains empty. As I discussed before, the internet calls are asynchronous. So, we need to wait until the response is received. Once we receive the response, we should reload the data for the table view. Hence, we add the following line into `getAllContacts()` method after we remove the last element from `contactNames`: `self.mainScreen.tableViewContacts.reloadData()`.

The final `getAllContacts()` method looks as follows:


```swift
//MARK: get all contacts...
func getAllContacts(){
    if let url = URL(string: APIConfigs.baseURL + "getall"){
        AF.request(url, method: .get).responseString(completionHandler: { response in
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
                            var names = data.components(separatedBy: "\n")
                            self.contactNames = names
                            self.contactNames.removeLast()
                            self.mainScreen.tableViewContacts.reloadData()
                            print(self.contactNames)
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


Let's run the app again. It should look like this:

![Educational illustration for iOS concept](</gitbook-assets/Screenshot 2023-05-25 at 10.35.15 PM (1).png>)



### Posting Data with AlamoFire: POST

Now it's time to add a new contact. We need to read the name, email, and phone number the user puts into the bottom add view. Then when the user taps the Add Contact button, we need to use Alamofire to post the data to the API server.

### Fetching the user inputs and creating a new Contact object

Let's open ViewController.swift file. Then add an action to `mainScreen.buttonAdd` (Add Contact button):


```swift
//
//  ViewController.swift
//  App10
//
//  Created by Sakib Miazi on 5/25/23.
//

import UIKit
import Alamofire

class ViewController: UIViewController {
    
    //codes omitted...
    
    override func viewDidLoad() {
        super.viewDidLoad()
        
        //codes omitted...
        
        //MARK: add action to Add Contact button...
        mainScreen.buttonAdd.addTarget(self, action: #selector(onButtonAddTapped), for: .touchUpInside)
    }
    
    //MARK: on Add Contact button tapped...
    @objc func onButtonAddTapped(){
        
    }
    
    //MARK: add a new contact call: add endpoint...
    func addANewContact(contact: Contact){
        
    }
}
```


Now let's define a struct `Contact` in a separate file. We will use this struct to create Swift contact objects for the API contacts.

![Educational illustration for iOS concept](</gitbook-assets/Screenshot 2023-05-25 at 11.08.19 PM (1).png>)


```swift
//
//  Contact.swift
//  App10
//
//  Created by Sakib Miazi on 5/25/23.
//

import Foundation
//MARK: struct for a contact...
struct Contact{
    var name:String
    var email:String
    var phone: Int
    
    init(name: String, email: String, phone: Int) {
        self.name = name
        self.email = email
        self.phone = phone
    }
}
```


Now, `onButtonAddTapped()` method, we will fetch the values from the text fields of the bottom add view. Let's write following code in `onButtonAddTapped()`:


```swift
@objc func onButtonAddTapped(){
    //do the validations...
    if let name = mainScreen.textFieldAddName.text,
       let email = mainScreen.textFieldAddEmail.text,
       let phoneText = mainScreen.textFieldAddPhone.text{
        
        if let phone = Int(phoneText){
            //The String 'phoneText' is successfully converted to an Int...
            let contact = Contact(name: name, email: email, phone: phone)
            
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


We unwrapped the optional values from the text fields and fetched the strings. Then we convert the phone number's text to an integer.

### Making the API call for the endpoint 'add.'

We need to use Alamofire to POST the new contact we created above to the server. We now write the following code in `addANewContact(contact: Contact)` method:


```swift
//MARK: add a new contact call: add endpoint...
func addANewContact(contact: Contact){
    if let url = URL(string: APIConfigs.baseURL+"add"){
        
        AF.request(url, method:.post, parameters:
                    [
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


In the above code:

* We use Alamofire to create a POST request (at line 5) and add the body parameters. In the Postman testing, we used body form parameters to send data to post to the API server, right? We create a dictionary to create key-value pairs here in Alamofire and post them with the request.
* The handler closure is pretty straightforward. We first check if there is any network error or not. If the network is OK, then we check the status code. If the code is 200-level, we know that our request was valid and the response is desirable.
  * If it is a 200-level code, we will get the updated contacts by calling `getAllContacts()` again.
  * Also, we clear the text fields to empty after we complete adding the new user by calling `clearAddViewFields()` method.

```swift
func clearAddViewFields(){
    mainScreen.textFieldAddName.text = ""
    mainScreen.textFieldAddEmail.text = ""
    mainScreen.textFieldAddPhone.text = ""
}
```

If you are still with me, we are done with adding a new contact. Let's run the app again.

<figure><img src="/gitbook-assets/10.seven (1).gif" alt="Educational illustration for iOS concept"><figcaption></figcaption></figure>

Yay! we are done adding a new contact!



### Fetching Data with AlamoFire: 'details' endpoint

Let's get the details of a selected user when the user taps on a cell on the table view.

We already know that when the user taps on a cell of the table view, we can handle the interaction in the adopted method regarding `didSelectRowAt`.

So let's write this line of code `getContactDetails(name: self.contactNames[indexPath.row])` inside `didSelectRowAt`.

```swift
extension ViewController: UITableViewDelegate, UITableViewDataSource{
    //codes omitted...
    
    func tableView(_ tableView: UITableView, didSelectRowAt indexPath: IndexPath) {
        getContactDetails(name: self.contactNames[indexPath.row])
    }
}
```

Here we are saying if the user selects a row, we will call the `getContactDetails(name:)` with the contact name getting displayed on that cell.

Let's define the `getContactDetails()` method:


```swift
//MARK: get details of a contact...
    func getContactDetails(name: String){
        let parameters = ["name":name]
        if let url = URL(string: APIConfigs.baseURL+"details"){
            AF.request(url, method:.get,
                       parameters: ["name":name],
                       encoding: URLEncoding.queryString)
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
                                //MARK: show alert with details...
                                self.showDetailsInAlert(data: data)
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


Here in the above code:

* We set the method of the request to **GET.**
* If you remember from the Postman test, we added the name parameter with the API call for the details API endpoint. Here, we are doing it using the `parameters` attribute to the Alamofire request (at line 6).
* The response closure for this case is pretty straightforward too. If there is no network error and the status code is a 200-level code, we call the method `showDetailsInAlert(data: data)` to show an alert with the received data (line 23).

Now let's write the code to display the alert in method `showDetailsInAlert():`


```swift
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
```


In the above code, we split the data string into multiple parts to separate the name, email, and phone. Then we remove the whitespaces from each part's beginning and end, and display the alert using them.

Let's run the app now.

<figure><img src="/gitbook-assets/10.eight (1).gif" alt="Educational illustration for iOS concept"><figcaption></figcaption></figure>

So, we are done writing codes for three API calls. **Can you do the 'delete'?**



### Reference Code

[Download Project Archive](/gitbook-assets/App10 (2).zip)

---

## Guided Practice Challenges

Before moving on to the next topic, try these low-stakes practice challenges in Xcode. They will build the exact muscle memory you need:

### Challenge 1: Experimentation
**The Scenario:** You've just learned about HTTP & Networking.
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


### Working with JSON

**Estimated effort:** 1-2 hours this topic
**Format:** Asynchronous online
**Prerequisites:** Previous iOS topics


**🎯 Topic Mission:** 
In this module, we will explore **Working with JSON** and understand its fundamental mechanics. Your mission is to understand the mechanics behind this concept and write robust Swift code.


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

### Working with APIs and JSON

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




### The JSON API for the Contact App

### The API details:

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



### App11: Getting All the Contact Names (getall endpoint)

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

![Educational illustration for iOS concept](</gitbook-assets/Screenshot 2023-05-26 at 4.05.44 PM (1).png>)

Let's open the View Controller and write the initial controller code similar to App10.


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

<figure><img src="/gitbook-assets/Screenshot 2023-05-26 at 4.35.09 PM (1) (1).png" alt="Educational illustration for iOS concept"><figcaption></figcaption></figure>

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

![Educational illustration for iOS concept](</gitbook-assets/Screenshot 2023-05-26 at 5.26.46 PM (1).png>)

Great! We are done with **getall.**



### App11: Getting the Details of a Selected Contact (details endpoint)

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


In the above code:

* In line 4, we are setting the URL for the details endpoint.
* In line 5, we set the parameters to `["name": name]`.
* Between lines 21 to 28, we decode the data with JSONDecoder() using the struct `Contact`. And then, we create an alert to display the details of the received contact.
* (You get to call this method from the adopted method, `didSelectRowAt` related to table view).
* Between lines 56 through 68, we display an alert to show the details.

Now, if we run the app, we will see:

<figure><img src="/gitbook-assets/11.three (1).gif" alt="Educational illustration for iOS concept"><figcaption></figcaption></figure>



### 'Must Do's While Decoding JSON adopting Codable

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

**So, the name and the data type of the variables in a Codable must match the name of the keys and the type of the values in JSON. Otherwise, JSON decoding will not work.**



### App11: Add a new Contact

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

<figure><img src="/gitbook-assets/11.eight (1).gif" alt="Educational illustration for iOS concept"><figcaption></figcaption></figure>



### Adding Accessory Button to Table View (Edit/Delete a Contact)

### **Adding a Button to the TableView Cell as an Accessory**

UITableView allows us to add views as accessories. Adding an accessory view is the easiest way to enable user interactions with a cell in a table view. So, in our app, we want to do the following:

<figure><img src="/gitbook-assets/11.ten (1).gif" alt="Educational illustration for iOS concept"><figcaption></figcaption></figure>

* We will have a settings button. If the user taps on the button, there will be a menu to give the user two options: Edit and Delete.
* The user can select one of the options to either edit or delete the contact.

Let's open ViewController.swift file.\
Go to where we adopt the protocols related to the table view.\
Then go to the adopted method for `cellForRowAt`, where we initialize the cell.

Add the following code to add an accessory button:


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


In the above code:

* We create a system button called `buttonOptions`. We set the `buttonOptions` to `sizeToFit()`. It means we ask the button to size to fit the cell's width.
* Then we set the settings to show the menu as the primary action on tapping the button.
* Then we set the image for the button from an appropriate icon from SF Symbols.
* Then from line 13 through 21, we setup the menu.
* **Finally, in line 23,** we set the cell's accessory view to the button.

_**If you noticed, the accessory view is a UIView. So technically, you can design your custom view with multiple UI elements. You can add multiple buttons if you want to. For the buttons, you must work with proper constraints, height, width, etc. (And it is a little complicated).**_

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

<figure><img src="/gitbook-assets/11.eleven (1).gif" alt="Educational illustration for iOS concept"><figcaption></figcaption></figure>

See? They are printing the appropriate logs as outputs. You can now do anything to edit or delete the contact.



### Reference Code

[Download Project Archive](/gitbook-assets/App11 (1).zip)



### Decluttering codes from View Controller (Recommended Read)

If you noticed, we have 281 lines of code in ViewController.swift. It appears to be a jumble of code. And in many ways, it's hard to read when you'll return to it after a week.

We can utilize protocols and extensions to break the code into multiple files, making it more modular.

### Separating the API calls from the Controller

Let's first separate the code we used to call the Contacts API. The methods we have related to the Contacts API are:

* getAllContacts()
* addANewContact(contact: Contact)
* getContactDetails(name: String)

### Defining a Protocol for the API Calls

Let's write a protocol where we will declare the methods we will use to call the Contacts API. Let's create a new Swift file ContactsProtocol.swift, inside the 'Contact API Configs' folder.

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


### The file structure of the project now looks like this:

<figure><img src="/gitbook-assets/Screenshot 2023-05-29 at 2.32.25 PM (1).png" alt="Educational illustration for iOS concept"><figcaption></figcaption></figure>

Now, the code is more modular and more manageable.

**Note: You can make it even more modular by putting the table view protocol codes into a separate file from the ViewController.**

[Download Project Archive](/gitbook-assets/App11_modular (2).zip)

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
