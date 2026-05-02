# HTTP & Networking


**Estimated effort:** 1-2 hours this topic
**Format:** Asynchronous online
**Prerequisites:** Previous iOS topics

{< hint info >}
**🎯 Topic Mission:** 
In this module, we will explore **HTTP & Networking** and learn how to integrate it into our iOS applications. Your mission is to understand the mechanics behind this concept and write robust Swift code.
{< /hint >}

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

# 10. Making the app communicate over the Internet

In this module, we will learn how an iOS app can talk to a server over the Internet. We will learn how to use remote APIs, fetch data from a server, and send data to a server using those APIs.





<!-- Merged from 10.1.-http-connections.md -->

# 10.1. HTTP connections

Intro to HTTP

{% embed url="https://northeastern.hosted.panopto.com/Panopto/Pages/Viewer.aspx?id=d52f70dc-ac38-4530-9e9a-ae9e01243cec" %}

HTTP stands for HyperText Transfer Protocol. It is used by two parties to transmit data between themselves over the Internet. For example, When you browse the web, your browser uses HTTP. The two parties are called:

* **Client**: who requests data. For example, an app is requesting information about the user.
* **Server**: who responds with the requested data. For example, the database server who responds to the app by sending the user information.

<figure><img src="/gitbook-assets/Screenshot 2023-05-25 at 1.09.07 PM (2).png" alt=""><figcaption></figcaption></figure>

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



<!-- Merged from 10.2.-postman-a-useful-tool-to-test-web-services.md -->

# 10.2. Postman: a Useful Tool to Test Web Services

### Installing Postman

{% embed url="https://www.youtube.com/watch?v=v62mZZ6HG8Y" %}

* Visit [this link](https://www.postman.com/downloads/?utm\_source=postman-home) to download Postman. Install it on your Mac by copying the extracted file into the Applications folder. Open it, create an account, and log in.
* Then create a new collection by clicking on `+` icon on the top left corner. Then add requests to start testing.



<!-- Merged from 10.3.-testing-our-simple-custom-api-with-postman.md -->

# 10.3. Testing our Simple Custom API with Postman

Please watch the video to learn how to use Postman with an API.

{% embed url="https://www.youtube.com/watch?v=0kQbmIaIvVk" %}

## Contacts API details

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



<!-- Merged from 10.4.-app-that-uses-our-contact-api.md -->

# 10.4. App that Uses Our Contact API

Our app should look like the following at the end.:

<figure><img src="/gitbook-assets/10.one (1).gif" alt=""><figcaption></figcaption></figure>

Let's create a new project in Xcode, "App10." And add Alamofire to the project using Cocoapods. ( See [9.-cocoa-pods](../9.-cocoa-pods/ "mention")).

Open the workspace (not the xcodeproject).

###



<!-- Merged from 10.5.-setting-up-the-view-of-app10.md -->

# 10.5. Setting up the View of App10

## Setting up the View

* In the app, we will add a bottom view to add a new contact.
  * The bottom add view contains three text fields for name, email, and phone.
* At the top, we will have a table view displaying current contacts.

So, let's add the following files:

* MainScreenView.swift
* ContactsTableView.swift

### **MainScreenView.swift**

Let's add the following code to the MainScreenView.swift file:

{% code lineNumbers="true" %}
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
{% endcode %}

In the above code, we add three text fields as the sub-views of the bottom add view. Then we anchor the bottom add view to the bottom of the safe area. Then we anchor the table view to the top, leading and trailing anchors of the safe area. Finally, we anchor the bottom of the table view to the top of the bottom add view.

Look at `setupBottomAddView()`. Play with the attributes (color, margins, border, etc.) to design it as you want to.

### **ContactsTableViewCell.swift**

In the ContactsTableViewCell.swift file, we define the view for each cell in the table view. Let's add the following code:

{% code lineNumbers="true" %}
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
{% endcode %}

Look at `setupWrapperCellView()`. Play with the attributes (color, margins, border, etc.) to design it as you want to.

### **ViewController.swift**

Let's add load the view in the controller. Let's add the following code to ViewController.swift:

{% code lineNumbers="true" %}
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
{% endcode %}

If we run the app now, it will look like:

![](</gitbook-assets/Screenshot 2023-05-25 at 7.42.51 PM (1).png>)



<!-- Merged from 10.6.-fetching-data-with-alamofire-get.md -->

# 10.6. Fetching Data with AlamoFire: GET

It's time to fetch the contacts' names and display them in our table view. We will call the API with `getall` endpoint when the app starts, and display the response on the table view ([10.3.-testing-our-simple-custom-api-with-postman.md](10.3.-testing-our-simple-custom-api-with-postman.md "mention")).

### Using Alamofire for text responses

If you noticed, in our API, we are getting back text responses from the server. We will use Alamofire to process the responses. Before we do, let's define an array of Strings in our ViewController for populating the table view. That array will hold the names of the contacts returned by the API endpoint `getall`.

{% code lineNumbers="true" %}
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
{% endcode %}

First, we need the API base URL to be set up. You can directly use the URL string in the call; however, it is always a better practice if you save these API details in a separate file as a static String, so that you can reuse that from any screen if you need to.

Let's create a file named `APIConfigs.swift` under `App10` folder. It is a Swift class file, **not a CocoaTouch Class.**

![](</gitbook-assets/Screenshot 2023-05-25 at 8.45.51 PM (1).png>)

In APIConfig.swift, let's add the static constant for the base URL:

{% code lineNumbers="true" %}
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
{% endcode %}

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
  &#xNAN;_<mark style="color:orange;">**Please note any communication over the Internet is Asynchronous. That means we are dealing with data that are hosted probably hundreds if not thousands of miles away. So, it will take time to receive the response from the server after you send the request. It might feel like it's real-time, but logically, it's not. So, when we build apps that communicate over the Internet, we must be very careful dealing with it. We should not expect that we will receive the response right away.**</mark>_&#x20;
* In the closure, we print `response.result` to see what kind of data we received as the response. If you run the app now, It prints something like this:\
  &#xNAN;**`success("Alice Smith\nBob Smith\nDavid B\nAlex C\nMark W\n")`**
  * `success()` in the response means the request was successfully transmitted, and there was no network error.
  * See, we have  in between two consecutive names. The character  means a new line. So, we have to fetch the whole String and then use it.
* **Also, the status code the response has is very important. We need to check if it is a 200-level or a 400-level code.**
  * <mark style="color:green;">**200-level codes mean the request was valid, and we received a desirable response.**</mark>
  * <mark style="color:red;">**400-level codes mean the request was incorrect, so we must handle the response appropriately to manage the UI elements properly.**</mark>

So, let's write the following code in the `completionHandler` closure taking care of the status codes and network errors:

{% code lineNumbers="true" %}
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
{% endcode %}

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

{% code overflow="wrap" %}
```
sessionTaskFailed(error: Error Domain=NSURLErrorDomain Code=-1022 "The resource could not be loaded because the App Transport Security policy requires the use of a secure connection." 
```
{% endcode %}

<mark style="color:red;">**By default, iOS does not allow HTTP connections without encryption. We should always use the connections through HTTPS.**</mark>

**However,** since my API is a dumb API, and I am using the API for demonstration purposes, I didn't go through the HTTPS configuration process. So, we need to enable unencrypted HTTP connections in our app.

If you face this, you can solve this by doing the following:

### <mark style="color:$info;">Enabling unencrypted HTTP in our app</mark>

* <mark style="color:$info;">We need to open</mark> <mark style="color:$info;"></mark><mark style="color:$info;">`Info.plist`</mark> <mark style="color:$info;"></mark><mark style="color:$info;">file from the File Navigator of the project.</mark>
* <mark style="color:$info;">Right-click (control + click) on the empty space of</mark> <mark style="color:$info;"></mark><mark style="color:$info;">`Info.plist`</mark><mark style="color:$info;">.</mark>
* <mark style="color:$info;">Select</mark> <mark style="color:$info;"></mark><mark style="color:$info;">`Add Row`</mark><mark style="color:$info;">.</mark>
* <mark style="color:$info;">Search and Select "App Transport Security Settings."</mark>
  * <mark style="color:$info;">Inside "App Transport Security Settings," add an attribute by clicking plus icon(</mark><mark style="color:$info;">`+`</mark><mark style="color:$info;">).</mark>
  * <mark style="color:$info;">Set "Allow Arbitrary Loads" attribute's value to YES.</mark>

<figure><img src="/gitbook-assets/10.12 (1).gif" alt=""><figcaption></figcaption></figure>

<mark style="color:$info;">It should now allow unencrypted HTTP.</mark>

<mark style="color:$info;">If we run the app now, it should print the following:</mark>

<mark style="color:$info;">**`["Alice Smith", "Bob Smith", "David B", "Alex C", "Mark W", ""]`**</mark><mark style="color:$info;">**.**</mark>

<mark style="color:$info;">**Interestingly, there is an empty String at the end.**</mark> <mark style="color:$info;"></mark><mark style="color:$info;">This happens because the server adds a  character at the end of the last user's name. So we need to remove it from the</mark> <mark style="color:$info;"></mark><mark style="color:$info;">`contactNames`</mark><mark style="color:$info;">.</mark>

<mark style="color:$info;">Let's add</mark> <mark style="color:$info;"></mark><mark style="color:$info;">`self.contactNames.removeLast()`</mark> <mark style="color:$info;"></mark><mark style="color:$info;">after line 18.</mark>

<mark style="color:$info;">Now, we have the perfect</mark> <mark style="color:$info;"></mark><mark style="color:$info;">`contactNames`</mark> <mark style="color:$info;"></mark><mark style="color:$info;">array to be displayed in the table view.</mark>

### Displaying data on the table view

Now, let's adopt the protocols for the table view:

{% code lineNumbers="true" %}
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
{% endcode %}

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

{% code lineNumbers="true" %}
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
{% endcode %}

Let's run the app again. It should look like this:

![](</gitbook-assets/Screenshot 2023-05-25 at 10.35.15 PM (1).png>)



<!-- Merged from 10.7.-posting-data-with-alamofire-post.md -->

# 10.7. Posting Data with AlamoFire: POST

Now it's time to add a new contact. We need to read the name, email, and phone number the user puts into the bottom add view. Then when the user taps the Add Contact button, we need to use Alamofire to post the data to the API server.

### Fetching the user inputs and creating a new Contact object

Let's open ViewController.swift file. Then add an action to `mainScreen.buttonAdd` (Add Contact button):

{% code lineNumbers="true" %}
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
{% endcode %}

Now let's define a struct `Contact` in a separate file. We will use this struct to create Swift contact objects for the API contacts.

![](</gitbook-assets/Screenshot 2023-05-25 at 11.08.19 PM (1).png>)

{% code lineNumbers="true" %}
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
{% endcode %}

Now, `onButtonAddTapped()` method, we will fetch the values from the text fields of the bottom add view. Let's write following code in `onButtonAddTapped()`:

{% code lineNumbers="true" %}
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
{% endcode %}

We unwrapped the optional values from the text fields and fetched the strings. Then we convert the phone number's text to an integer.

### Making the API call for the endpoint 'add.'

We need to use Alamofire to POST the new contact we created above to the server. We now write the following code in `addANewContact(contact: Contact)` method:

{% code lineNumbers="true" %}
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
{% endcode %}

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

<figure><img src="/gitbook-assets/10.seven (1).gif" alt=""><figcaption></figcaption></figure>

Yay! we are done adding a new contact!



<!-- Merged from 10.8.-fetching-data-with-alamofire-details-endpoint.md -->

# 10.8. Fetching Data with AlamoFire: 'details' endpoint

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

{% code lineNumbers="true" %}
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
{% endcode %}

Here in the above code:

* We set the method of the request to **GET.**
* If you remember from the Postman test, we added the name parameter with the API call for the details API endpoint. Here, we are doing it using the `parameters` attribute to the Alamofire request (at line 6).
* The response closure for this case is pretty straightforward too. If there is no network error and the status code is a 200-level code, we call the method `showDetailsInAlert(data: data)` to show an alert with the received data (line 23).

Now let's write the code to display the alert in method `showDetailsInAlert():`

{% code lineNumbers="true" %}
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
{% endcode %}

In the above code, we split the data string into multiple parts to separate the name, email, and phone. Then we remove the whitespaces from each part's beginning and end, and display the alert using them.

Let's run the app now.

<figure><img src="/gitbook-assets/10.eight (1).gif" alt=""><figcaption></figcaption></figure>

So, we are done writing codes for three API calls. **Can you do the 'delete'?**



<!-- Merged from 10.9.-reference-code.md -->

# 10.9. Reference Code

{% file src="/gitbook-assets/App10 (2).zip" %}

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

