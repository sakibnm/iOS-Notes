---
coverY: 0
---

**Estimated effort:** 1-2 hours this topic
**Format:** Asynchronous online
**Prerequisites:** Previous iOS topics

{< hint info >}
**🎯 Topic Mission:** 
In this module, we will explore **this topic** and learn how to integrate it into our iOS applications. Your mission is to understand the mechanics behind this concept and write robust Swift code.
{< /hint >}

---

## Learning Objectives

By the end of this session, you will be able to:
1. Understand the core concepts of this topic.
2. Implement this topic in an Xcode project.
3. Apply best practices to ensure clean and maintainable code.

---

## The Story So Far...

We have been progressively building our knowledge of iOS and Swift. In this module, we will expand our toolkit by diving into this topic. 
Open your current Xcode project or start a new Playground to follow along with the hands-on material.

---

## Walkthrough: Exploring this topic

> 📁 **Target Project** — Follow along by building the mini-app presented in the steps below, or integrate these concepts into your own ongoing projects.

# 7. Bottom Sheet View: Modal Presentation

You probably have seen apps where you tap a button, and a page sheet pops up from the bottom. You can then interact with that page sheet and work with the app. We can use Swift's SheetPresentationController for building the bottom sheet views.&#x20;

In this short module, we will build the following app:

<figure><img src="/gitbook-assets/7.sixty (1).gif" alt=""><figcaption></figcaption></figure>

Basically, we build this app on top of the app in the [6.-search-bar](../6.-search-bar/ "mention") module. We will implement SearchBar on a bottom sheet view.

We have a Find button on our main screen and a label to display the selected name. If the user taps on the Find button, the app should present the bottom search sheet. The user searches for a name on the bottom search sheet and selects a name. Then, we need to dismiss the bottom sheet and set the text of the label to the selected name.




<!-- Merged from 1.-creating-the-screen-for-a-bottom-sheet-view.md -->

# 7.1. Creating the Screen for a Bottom Sheet View

**When building a bottom sheet (presentation) view, we must remember that the page we will present as a bottom sheet is a full and independent screen. It should have its own:**

* **View Controller**
* **Navigation Controller**

&#x20;So, let's design a separate screen for our search bottom sheet. Let's create the following three Swift files:

* SearchBottomSheetController.swift
* SearchBottomSheetView.swift
* SearchTableCell.swift

![](</gitbook-assets/Screenshot 2023-06-13 at 1.12.04 PM.png>)

Let's design the view first.

## Search Bottom Sheet View

Let's open the SearchBottomSheetView.swift file. **The design of this view should be exactly the same as** [6.1.-setting-up-the-views.md](../6.-search-bar/6.1.-setting-up-the-views.md "mention")**.** So let's put the following code in the file:

```swift
//
//  SearchBottomSheetView.swift
//  BottomSheetViewDemo
//
//  Created by Sakib Miazi on 6/13/23.
//

import UIKit

class SearchBottomSheetView: UIView {
    var searchBar: UISearchBar!
    var tableViewSearchResults: UITableView!
    
    override init(frame: CGRect) {
        super.init(frame: frame)
        
        self.backgroundColor = .white
        
        //MARK: Search Bar...
        searchBar = UISearchBar()
        searchBar.placeholder = "Search names.."
        searchBar.translatesAutoresizingMaskIntoConstraints = false
        self.addSubview(searchBar)
        
        //MARK: Table view...
        tableViewSearchResults = UITableView()
        tableViewSearchResults.register(SearchTableCell.self, forCellReuseIdentifier: Configs.searchTableViewID)
        tableViewSearchResults.translatesAutoresizingMaskIntoConstraints = false
        self.addSubview(tableViewSearchResults)
        
        //MARK: constraints...
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

## Search Table Cell

We will use the same table cell here as [6.-search-bar](../6.-search-bar/ "mention"). Let's open SearchTableCell.swift file and put the following code there:

```swift
//
//  SearchTableCell.swift
//  BottomSheetViewDemo
//
//  Created by Sakib Miazi on 6/13/23.
//

import UIKit

class SearchTableCell: UITableViewCell {
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
            labelTitle.trailingAnchor.constraint(equalTo: wrapperCellView.trailingAnchor, constant:  -16),
            labelTitle.heightAnchor.constraint(equalToConstant: 20),
            
            wrapperCellView.heightAnchor.constraint(equalToConstant: 36)
        ])
        
    }
    
    required init?(coder: NSCoder) {
        fatalError("init(coder:) has not been implemented")
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



<!-- Merged from 2.-setting-up-the-controller-for-the-search-bottom-sheet.md -->

# 7.2. Setting up the Controller for the Search Bottom Sheet

Let's open SearchBottomSheetController.swift file. We will mostly use the same code here as [6.-search-bar](../6.-search-bar/ "mention"). We would add a few more logic to handle a tap on a row and send data back to the main screen.&#x20;

Let's write the code for setting up the table view and the search bar. Let's open SearchBottomSheetController.swift file, and put the following code there:

{% code lineNumbers="true" %}
```swift
//
//  SearchBottomSheetController.swift
//  BottomSheetViewDemo
//
//  Created by Sakib Miazi on 6/13/23.
//

import UIKit

class SearchBottomSheetController: UIViewController {

    let searchSheet = SearchBottomSheetView()
    
    //MARK: the list of names...
    var namesDatabase = ["Marvin Cook","Samira Jimenez","Coral Hancock","Xander Wade","Terence Mcneil","Dewey Buckley","Ophelia Higgins","Asiya Anthony","Francesco Knight","Claude Gonzalez","Demi Decker","Casey Park","Jon Hendrix","Hope Harvey","Richie Alexander","Carmen Proctor","Mercedes Callahan","Yahya Gibbs","Julian Pittman","Shauna Ray"]
    
    //MARK: the array to display the table view...
    var namesForTableView = [String]()
    
    override func loadView() {
        view = searchSheet
    }
    override func viewDidLoad() {
        super.viewDidLoad()
        
        //MARK: sorting the names list...
        namesDatabase.sort()
        
        //MARK: setting up Table View data source and delegate...
        searchSheet.tableViewSearchResults.delegate = self
        searchSheet.tableViewSearchResults.dataSource = self
        
        //MARK: setting up Search Bar delegate...
        searchSheet.searchBar.delegate = self
        
        //MARK: initializing the array for the table view with all the names...
        namesForTableView = namesDatabase
    }
}

//MARK: adopting Table View protocols...
extension SearchBottomSheetController: UITableViewDelegate, UITableViewDataSource{
    func tableView(_ tableView: UITableView, numberOfRowsInSection section: Int) -> Int {
        return namesForTableView.count
    }
    
    func tableView(_ tableView: UITableView, cellForRowAt indexPath: IndexPath) -> UITableViewCell {
        let cell = tableView.dequeueReusableCell(
            withIdentifier: Configs.searchTableViewID, for: indexPath) as! SearchTableCell
        
        cell.labelTitle.text = namesForTableView[indexPath.row]
        return cell
    }
}

//MARK: adopting the search bar protocol...
extension SearchBottomSheetController: UISearchBarDelegate{
    func searchBar(_ searchBar: UISearchBar, textDidChange searchText: String) {
        if searchText == ""{
            namesForTableView = namesDatabase
        }else{
            self.namesForTableView.removeAll()

            for name in namesDatabase{
                if name.contains(searchText){
                    self.namesForTableView.append(name)
                }
            }
        }
        self.searchSheet.tableViewSearchResults.reloadData()
    }
}
```
{% endcode %}



<!-- Merged from 3.-main-screen.md -->

# 3. Main Screen

The main screen is very simple to design; we have:

* A label to display the selected name from the bottom search sheet.
* A Find button to pop the bottom search sheet.

## Main Screen View

Let's create a file named MainScreenView.swift:

![](</gitbook-assets/Screenshot 2023-06-13 at 1.35.29 PM.png>)

Let's put the following code there:

```swift
//
//  MainScreenView.swift
//  BottomSheetViewDemo
//
//  Created by Sakib Miazi on 6/13/23.
//

import UIKit

class MainScreenView: UIView {

    var labelName: UILabel!
    var buttonSelect: UIButton!
    
    override init(frame: CGRect) {
        super.init(frame: frame)
        
        self.backgroundColor = .white
        
        //MARK: initializing labelName...
        labelName = UILabel()
        labelName.text = "Tap Find to search a name..."
        labelName.translatesAutoresizingMaskIntoConstraints = false
        self.addSubview(labelName)
        
        //MARK: initializing buttonSelect...
        buttonSelect = UIButton(type: .system)
        buttonSelect.setTitle("Find", for: .normal)
        buttonSelect.setImage(UIImage(systemName: "magnifyingglass.circle.fill"), for: .normal)
        buttonSelect.translatesAutoresizingMaskIntoConstraints = false
        self.addSubview(buttonSelect)
        
        //MARK: initializing constraints...
        NSLayoutConstraint.activate([
            buttonSelect.topAnchor.constraint(equalTo: self.safeAreaLayoutGuide.topAnchor, constant: 32),
            buttonSelect.centerXAnchor.constraint(equalTo: self.safeAreaLayoutGuide.centerXAnchor),
            
            labelName.topAnchor.constraint(equalTo: buttonSelect.bottomAnchor, constant: 16),
            labelName.centerXAnchor.constraint(equalTo: self.safeAreaLayoutGuide.centerXAnchor),
            
        ])
    }
    
    required init?(coder: NSCoder) {
        fatalError("init(coder:) has not been implemented")
    }
}

```

## Main Screen Controller

Now it's time to patch the actions to pop the bottom search sheet from the view controller. Let's put the following code in ViewController.swift:

{% code lineNumbers="true" %}
```swift
//
//  ViewController.swift
//  BottomSheetViewDemo
//
//  Created by Sakib Miazi on 6/13/23.
//

import UIKit

class ViewController: UIViewController {
    let mainScreen = MainScreenView()
    
    let searchSheetController = SearchBottomSheetController()
    var searchSheetNavController: UINavigationController!
    
    override func loadView() {
        view = mainScreen
    }

    override func viewDidLoad() {
        super.viewDidLoad()
        title = "Bottom Sheet Demo"        
        mainScreen.buttonSelect.addTarget(self, action: #selector(onFindButtonTapped), for: .touchUpInside)
    }
    
    func setupSearchBottomSheet(){
        //MARK: setting up bottom search sheet...
        searchSheetNavController = UINavigationController(rootViewController: searchSheetController)
        
        // MARK: setting up modal style...
        searchSheetNavController.modalPresentationStyle = .pageSheet
        
        if let bottomSearchSheet = searchSheetNavController.sheetPresentationController{
            bottomSearchSheet.detents = [.medium(), .large()]
            bottomSearchSheet.prefersGrabberVisible = true
        }
    }    
    @objc func onFindButtonTapped(){
        setupSearchBottomSheet()
        present(searchSheetNavController, animated: true)
    }
}
```
{% endcode %}

In the above code:

* On line 13, we instantiate the bottom search sheet controller.
* On line 14, we declare the navigation controller to embed the bottom sheet controller into it.
* On lines 16 through 18, we patch the main screen's view with the controller.
* On line 23, we add a target action for the FInd button.
  * On lines 38 through 41, we define the action to handle the user tapping on the Find button.
  * We first call the `setupSearchBottomSheet()` method to instantiate the search bottom bar. ([More on this a little later](3.-main-screen.md#creating-the-bottom-search-sheet)).
  * Then we present the navigation controller `searchSheetNavController`.&#x20;

### Creating the Bottom Search Sheet

* On lines 26 through 37, we define and build the bottom search sheet.
* On line 28, we define the navigation controller `searchSheetNavController` embedding the   `searchSheetController` in it.
* On line 31, we define the presentation style of the bottom search sheet. There are other styles available. You can look here for the details: [https://developer.apple.com/documentation/uikit/uimodalpresentationstyle](https://developer.apple.com/documentation/uikit/uimodalpresentationstyle)
* **The next part is crucial for setting the behavior of the bottom search sheet.**&#x20;
  * On line 34, we define the detents of the bottom search sheet. _(detent means - a catch in a machine which prevents motion until released.)_&#x20;
  * **Detent** here means exactly the same thing. It means the detents can put a brake on its movement when the bottom sheet pops up. Swift currently allows two detents: medium() and large().
    * **medium()** detent brakes the pop up sheet in the middle of the screen.
    * **large()** detent does not brake the sheet until it reaches the top of the screens.&#x20;
    * We add both of the detents here so that it stops in the middle; then, if we want, we can fill up the screen with it.

<figure><img src="/gitbook-assets/7.sixtytwo.gif" alt=""><figcaption><p><strong>Detents</strong></p></figcaption></figure>

* On line 35, we display the grabber.

![](</gitbook-assets/Screenshot 2023-06-13 at 5.00.01 PM.png>)



Now, our app is almost ready. We just need to return the name to main screen when the user taps a name from the bottom search sheet's table view.



<!-- Merged from 4.-sending-data-back-to-main-screen.md -->

# 7.4. Sending data back to Main Screen

We will use Notification Center to do that.&#x20;

* **We will observe any notifications coming from the bottom search sheet if the user selects any of the names in the main screen's ViewController.**
* **We will post notifications from SearchBottomSheetController when the user selects a table view row.**&#x20;

Let's open ViewController.swift file, and update the file with the following code:

{% code lineNumbers="true" %}
```swift
//
//  ViewController.swift
//  BottomSheetViewDemo
//
//  Created by Sakib Miazi on 6/13/23.
//

import UIKit

class ViewController: UIViewController {
   //codes omitted...
    
    let notificationCenter = NotificationCenter.default
    
    override func loadView() {
        view = mainScreen
    }

    override func viewDidLoad() {
        //codes omitted
        
        observeNameSelected() 
    }
    
    //codes omitted...

    //MARK: Observe if the user selected a name from bottom sheet...
    func observeNameSelected(){
        notificationCenter.addObserver(
            self,
            selector: #selector(onNameSelected(notification:)),
            name: .nameSelected, object: nil)
    }
    @objc func onNameSelected(notification: Notification){
        if let selectedName = notification.object{
            mainScreen.labelName.text = selectedName as! String
        }
    }
  
}
```
{% endcode %}

In the above code:

* On line 13, we are initializing the Notification Center.
* On line 22, we set the observer for the notification.
* From lines 27 through 38 we are observing for a notification `.nameSelected`. We create a separate file to store the names of the Notifications just like [7.-notification-center](../../7.-notification-center/ "mention").&#x20;
* On line 34, the `onNameSelected()` method gets triggered when the notification is received.&#x20;
  * On line 36, we set the name with the data we receive through the notification.

## Table View in Bottom Search Sheet Controller: overriding didSelectRowAt

Let's open SearchBottomSheetController.swift file and add the following method inside the extension where we are adopting the table view protocols:

{% code lineNumbers="true" %}
```swift
//MARK: adopting Table View protocols...
extension SearchBottomSheetController: UITableViewDelegate, UITableViewDataSource{
    //codes omitted...
    
    func tableView(_ tableView: UITableView, didSelectRowAt indexPath: IndexPath) {
        //MARK: name selected....
        notificationCenter.post(name: .nameSelected, object: namesForTableView[indexPath.row])
        
        //MARK: dismiss the bottom search sheet...
        self.dismiss(animated: true)
    }
}
```
{% endcode %}

In the above code:

* We are waiting for the user to tap on a table view cell.&#x20;
* On line 7, we post the selected name to the notification center.
* On line 10, we remove the bottom search sheet by calling dismiss.

Let's run the app.

<figure><img src="/gitbook-assets/seven.5.gif" alt=""><figcaption></figcaption></figure>

**Nice! We built our first Bottom Sheet View!**



<!-- Merged from 5.-reference-code.md -->

# 7.5. Reference Code

{% file src="/gitbook-assets/BottomSheetView.zip" %}

---

## Guided Practice Challenges

Before moving on to the next topic, try these low-stakes practice challenges in Xcode. They will build the exact muscle memory you need:

### Challenge 1: Experimentation
**The Scenario:** You've just learned about this topic.
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

