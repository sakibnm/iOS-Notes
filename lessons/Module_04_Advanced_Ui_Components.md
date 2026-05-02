# Module 04: Advanced Ui Components

## Table of Contents




### UITableView

**Estimated effort:** 1-2 hours this topic
**Format:** Asynchronous online
**Prerequisites:** Previous iOS topics


**🎯 Topic Mission:** 
In this module, we will explore **UITableView** and learn how to integrate it into our iOS applications. Your mission is to understand the mechanics behind this concept and write robust Swift code.


---

## Learning Objectives

By the end of this session, you will be able to:
1. Understand the core concepts of UITableView.
2. Implement UITableView in an Xcode project.
3. Apply best practices to ensure clean and maintainable code.

---

## The Story So Far...

We have been progressively building our knowledge of iOS and Swift. In this module, we will expand our toolkit by diving into UITableView. 
Open your current Xcode project or start a new Playground to follow along with the hands-on material.

---

## Walkthrough: Exploring UITableView

> 📁 **Target Project** — Follow along by building the mini-app presented in the steps below, or integrate these concepts into your own ongoing projects.

### UITableView, and more

So far, we have worked with multiple screens and NavigationController. Now, we will learn how to display a list of data and work with some other UI elements.

More specifically, we will learn about the following:

* UITableView to display a list of data.
* A few more key concepts like static variables and handling Double inputs.




### Expense App

So, let's create an app called 'App5'. Our preliminary target is to build something like the following app:

![Educational illustration for iOS concept](</gitbook-assets/Screenshot 2023-05-18 at 10.45.04 AM (1).png>) ![Educational illustration for iOS concept](</gitbook-assets/Screenshot 2023-05-18 at 10.45.19 AM (1).png>)

The first screen contains a list of expenses. The user can add a new expense by tapping on the plus icon (`+`) on the navigation bar. If a user taps on `+` icon, it takes them to the next screen where they can put the details of the expense.

![Educational illustration for iOS concept](</gitbook-assets/Screenshot 2023-05-18 at 10.56.57 AM (1).png>) ![Educational illustration for iOS concept](</gitbook-assets/Screenshot 2023-05-18 at 10.45.48 AM (1).png>)

Once the user puts in the details and taps the Add Expense button, it should return to the first screen and show the newly added expense.

Now let's build the app.



### First screen, part 1: Adding a Bar Button

Let's create a new project, 'App5' in Xcode.

<figure><img src="/gitbook-assets/Screenshot 2023-05-18 at 10.45.04 AM (1).png" alt="Educational illustration for iOS concept" width="343"><figcaption><p>App 5: First screen</p></figcaption></figure>

In App3 ([3.-our-first-multi-screen-app](../3.-our-first-multi-screen-app/ "mention")), we discussed the basics of the Navigation Controller. Navigation Controller automatically adds a top bar (Navigation Bar) on the screen, where you have seen the Back buttons. You can add more buttons there, either on the left side or right side. Usually, we add our custom buttons on the right side of the Bar since the left side is usually reserved for going back. We will add our plus button (`+`) on the right side of the Bar.

First, open the Main storyboard and embed the storyboard in the Navigation Controller.

Open ViewController.swift file, and add the following codes there:

```swift
//
//  ViewController.swift
//  App5_draft
//
//  Created by Sakib Miazi on 5/17/23.
//

import UIKit

class ViewController: UIViewController {
    override func viewDidLoad() {
        super.viewDidLoad()
        title = "Expense App"
        
        //MARK: setting the add button to the navigation controller...
        navigationItem.rightBarButtonItem = UIBarButtonItem(
            barButtonSystemItem: .add, target: self,
            action: #selector(onAddBarButtonTapped)
        )
    }
    @objc func onAddBarButtonTapped(){
        //Will implement later...
    }
}
    
```

In the above code, we are creating a new UIBarButtonItem and setting it to the right Bar Button of the Navigation Bar. We are also adding an action listener `onAddBarButtonTapped()` to handle the user tap. If you run it now, you will see the plus button on the Bar's right side.

<figure><img src="/gitbook-assets/one (1) (1).gif" alt="Educational illustration for iOS concept"><figcaption></figcaption></figure>

Now we will set up the TableView and then return to this button.



### First screen, part 2: Setting up the View of the First Screen with TableView.

We have to build our first TableView here in this app. Before we build one, we need to understand what it is.

### What is a TableView?

According to [Apple developer documentation](https://developer.apple.com/documentation/uikit/uitableview): _Table views in iOS display rows of vertically scrolling content in a single column. Each row in the table contains one piece of your app’s content. For example, the Contacts app displays the name of each contact in a separate row, and the main page of the Settings app displays the available groups of settings. You can configure a table to display a single long list of rows, or you can group related rows into sections to make navigating the content easier._

A good example of a TableView is the Settings app on our iPhones or iPads.

<figure><img src="/gitbook-assets/two (2) (1).gif" alt="Educational illustration for iOS concept"><figcaption><p>Settings app</p></figcaption></figure>

You can see that the Settings app has multiple groups of items in the list. For example, the first group has 'Sign in' and 'VPN' rows. The second group has the 'Screen Time' row. And the third group has 'General,' 'Accessibility,' and 'Privacy and Security' rows. **These groups are called sections.** Each group can have one or more rows.

### Creating the View file of the first screen, FirstScreenView

Let's create a new file called 'FirstScreenView', just like what we did in the previous [module](https://github.com/sakibnm/iOS/blob/main/4.-separating-the-view-and-the-controller-codes). We will build the View of the First Screen in this file. Let's put the code in the file:

```swift
//
//  FirstScreenView.swift
//  App5_draft
//
//  Created by Sakib Miazi on 5/17/23.
//

import UIKit

class FirstScreenView: UIView {
    
    var tableViewExpense: UITableView!
    

    override init(frame: CGRect) {
        super.init(frame: frame)
        backgroundColor = .white
        
        //MARK: initializing a TableView...
        setupTableViewExpense()
        initConstraints()
    }
    
    func setupTableViewExpense(){
        tableViewExpense = UITableView()
        tableViewExpense.translatesAutoresizingMaskIntoConstraints = false
        self.addSubview(tableViewExpense)
    }
    
    //MARK: setting the constraints...
    func initConstraints(){
        NSLayoutConstraint.activate([
            tableViewExpense.topAnchor.constraint(equalTo: self.safeAreaLayoutGuide.topAnchor, constant: 8),
            tableViewExpense.bottomAnchor.constraint(equalTo: self.safeAreaLayoutGuide.bottomAnchor, constant: -8),
            tableViewExpense.leadingAnchor.constraint(equalTo: self.safeAreaLayoutGuide.leadingAnchor, constant: 8),
            tableViewExpense.trailingAnchor.constraint(equalTo: self.safeAreaLayoutGuide.trailingAnchor, constant: -8),
        ])
    }
    
    required init?(coder: NSCoder) {
        fatalError("init(coder:) has not been implemented")
    }
    
}
```

The FirstScreenView's background is set to white. The view only contains a TableView. We add 8 points of margin around the TableView using the constraints.

### Patching FirstScreenView with ViewController

Then we will patch it up with the controller, ViewController. Open up View Controller.swift, and add the following code:

```swift
//
//  ViewController.swift
//  App5
//
//  Created by Sakib Miazi on 5/18/23.
//

import UIKit

class ViewController: UIViewController {
    
    let firstScreen = FirstScreenView()
    
    override func loadView() {
        view = firstScreen
    }

    //codes omitted...
}
```

### Designing each Cell/Row of the TableView:

Each row in our TableView (`tableViewExpense`) should look like this:

![Educational illustration for iOS concept](</gitbook-assets/Screenshot 2023-05-18 at 12.12.41 PM (1).png>)

So we can see that there are three Labels there, displaying:

* The title of the expense.
* The amount the user spent.
* And the type of expense.

So, we need to design our TableView row. **The view of the row is called a cell**. We need to create a new Swift file to design the cell.

**File -> New -> File... -> Cocoa Touch Class -> Next ->**

Give the file's name as "TableViewExpenseCell" and set the file as the 'Subclass of' UITableViewCell. Then click **Next. And then click Create.**

<figure><img src="/gitbook-assets/three (1) (1).gif" alt="Educational illustration for iOS concept"><figcaption><p>Creating a Cell's View</p></figcaption></figure>

Now, let's open the TableViewExpenseCell.swift file. You will see that there are two methods already given there (`awakeFromNib()` and `setSelected()`). We won't use them. Let's add the following code to the file:

```swift
//
//  TableViewExpenseCell.swift
//  App5
//
//  Created by Sakib Miazi on 5/18/23.
//

import UIKit

class TableViewExpenseCell: UITableViewCell {
    var wrapperCellView: UIView!
    var labelTitle: UILabel!
    var labelAmount: UILabel!
    var labelType: UILabel!
    
    override init(style: UITableViewCell.CellStyle, reuseIdentifier: String?) {
        super.init(style: style, reuseIdentifier: reuseIdentifier)

    }
    
    //MARK: unused methods...
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

In the above code, you can see that we are adding four variables, three of which are Labels we know we have to put in the cell. We also added a UIView named `wrapperCellView` to hold all the UI elements inside. In other words, this wrapperCellView will act as a container for all the required UI elements of the cell. We use a UIView as a wrapper because UIViews have many configuration and styling options to create stable and nicer-looking cells.

#### Setting up the UI elements and initializing the constraints

Let's add the following codes in TableViewExpenseCell.swift file:

```swift
//
//  TableViewExpenseCell.swift
//  App5
//
//  Created by Sakib Miazi on 5/18/23.
//

import UIKit

class TableViewExpenseCell: UITableViewCell {
    //codes omitted...
    
    override init(style: UITableViewCell.CellStyle, reuseIdentifier: String?) {
        super.init(style: style, reuseIdentifier: reuseIdentifier)
        setupWrapperCellView()
        setupLabelTitle()
        setupLabelAmount()
        setupLabelType()
        initConstraints()
    }
    
    func setupWrapperCellView(){
        wrapperCellView = UITableViewCell()
        wrapperCellView.translatesAutoresizingMaskIntoConstraints = false
        self.addSubview(wrapperCellView)
    }
    
    func setupLabelTitle(){
        labelTitle = UILabel()
        labelTitle.translatesAutoresizingMaskIntoConstraints = false
        wrapperCellView.addSubview(labelTitle)
    }
    func setupLabelAmount(){
        labelAmount = UILabel()
        labelAmount.translatesAutoresizingMaskIntoConstraints = false
        wrapperCellView.addSubview(labelAmount)
    }
    func setupLabelType(){
        labelType = UILabel()
        labelType.translatesAutoresizingMaskIntoConstraints = false
        wrapperCellView.addSubview(labelType)
    }
    
    func initConstraints(){
        NSLayoutConstraint.activate([
            wrapperCellView.topAnchor.constraint(equalTo: self.topAnchor),
            wrapperCellView.leadingAnchor.constraint(equalTo: self.leadingAnchor),
            wrapperCellView.bottomAnchor.constraint(equalTo: self.bottomAnchor),
            wrapperCellView.trailingAnchor.constraint(equalTo: self.trailingAnchor),
            
            labelTitle.topAnchor.constraint(equalTo: wrapperCellView.topAnchor, constant: 4),
            labelTitle.leadingAnchor.constraint(equalTo: wrapperCellView.leadingAnchor, constant: 4),
            labelTitle.heightAnchor.constraint(equalToConstant: 20),
            
            labelAmount.topAnchor.constraint(equalTo: labelTitle.bottomAnchor, constant: 4),
            labelAmount.leadingAnchor.constraint(equalTo: labelTitle.leadingAnchor),
            labelAmount.heightAnchor.constraint(equalToConstant: 20),
            
            labelType.topAnchor.constraint(equalTo: labelAmount.bottomAnchor, constant: 4),
            labelType.leadingAnchor.constraint(equalTo: labelTitle.leadingAnchor),
            labelType.heightAnchor.constraint(equalToConstant: 20),
            
            wrapperCellView.heightAnchor.constraint(equalToConstant: 76)
        ])
    }
    //Codes omitted....
}
```

In the above code, you can see that `wrapperCellView` is a sub-view of this cell. All the other elements are the subviews of `wrapperCellView`. If you look into the constraints, the `wrapperCellView` covers the entirety of the cell.

`labelTitle` constraints:

* We anchored the `labelTitle'`s top and leading anchors to the top and leading anchors of `wrapperCellView` with a margin of 4 points.
* We are also setting the height of the Label with the third constraint to 20 points: `labelTitle.heightAnchor.constraint(equalToConstant: 20)`. (Yes, you can set the size of the UI elements using constraints; in many cases, **it is better to use constraints** to set the heights and widths of a UI element).

The constraints for `labelAmount` and `labelType` are very similar to the constraints of `labelTitle`.

In the last constraint of the constraints array, we finally set the height of the `wrapperCellView`. The `wrapperCellView` is the container of other UI elements, so we need to set up the height of the container after we set the heights of other elements. We count the height of the container by adding the heights of the UI elements and the margins. (4+20+4+20+4+20+4 = 76).

Alright, we are done with designing our cell.

### **Patching the Cell with the TableView**

Now let's open the FirstScreenView.swift file and add `tableViewExpense.register(TableViewExpenseCell.self, forCellReuseIdentifier: "expenses")` to the method `setupTableViewExpense()`:

```swift
func setupTableViewExpense(){
    tableViewExpense = UITableView()
    tableViewExpense.register(TableViewExpenseCell.self, forCellReuseIdentifier: "expenses")
    tableViewExpense.translatesAutoresizingMaskIntoConstraints = false
    self.addSubview(tableViewExpense)
}
```

Here, we are registering the `tableViewExpense` with the cell we just designed. The most important part is `forCellReuseIdentifier: "expenses" .` It means when we access this table view from the controller, we need to use the cells the table view holds. We set an identifier, "expenses," for the cells. If you design multiple cells to display multiple kinds of information, you can later identify them with the identifier you set here.

That's it. We set up the view of the first screen and added a TableView with a designed Cell.



### First screen, part 3: Setting up the View Controller and populating TableView

Now we must patch the views with our controller (ViewController.swift). Before we do, let's create a data model for the data we will display in the TableView `tableViewExpense`. We have three data points for displaying a row in the table view: expense title, amount, and type.

### Creating a data model for expenses

So, let's create a new swift file called "Expense."

* **File -> New -> File...**
* Select **iOS**
* **Select Swift file (not Cocoa Touch Class).**
* **Next**
* Name it as **"Expense."**
* Click **Create.**

<figure><img src="/gitbook-assets/four (1) (1).gif" alt="Educational illustration for iOS concept"><figcaption></figcaption></figure>

Let's add the following code to Expense.swift file:

```swift
//
//  Expense.swift
//  App5
//
//  Created by Sakib Miazi on 5/18/23.
//

import Foundation

struct Expense{
    var title: String?
    var amount: Double?
    var type: String?
    
    init(title: String? = nil, amount: Double? = nil, type: String? = nil) {
        self.title = title
        self.amount = amount
        self.type = type
    }
    
}
```

We created a struct `Expense` with three properties: `title`, `amount`, and `type`. We also define the `init()` method to initialize the properties.

### Setting up the Controller

Let's add some dummy data to test out TableView. Add the following code in your ViewController.swift:

```swift
//
//  ViewController.swift
//  App5
//
//  Created by Sakib Miazi on 5/18/23.
//

import UIKit

class ViewController: UIViewController {
    
    //codes omitted...
    
    //MARK: expenses array to populate TableView...
    var expenses = [Expense]()
    
    //MARK: predefined types of expenses...
    let types = ["Groceries", "Rent", "Subscriptions", "Gadgets and Electronics"]
    
    //codes omitted...
    
    override func viewDidLoad() {
        super.viewDidLoad()
        //codes omitted...
                
        //MARK: adding dummy data for testing table view...
        expenses.append(Expense(title: "Pixel 7 pro", amount: 750.0, type: types[3]))
        expenses.append(Expense(title: "iPhone SE", amount: 349.0, type: types[3]))
        expenses.append(Expense(title: "Target", amount: 150.0, type: types[0]))
        expenses.append(Expense(title: "Netflix", amount: 19.0, type: types[2]))
                
        //codes omitted...
    }
    
    //codes omitted...
}
```

Here we create an array of `Expense` types (struct we created) to hold data to display in the table view. Then we predefine four types of expenses ("Groceries", "Rent", "Subscriptions", "Gadgets and Electronics") in the `types` array. Then we add four dummy expenses to test the table view.

### Patching TableView delegate and data source with the controller

Remember `extension` keyword? Now, we will adopt `UITableViewDelegate`, and `UITableViewDataSource` protocols in ViewController using `extension` keyword.

```swift
//
//  ViewController.swift
//  App5
//
//  Created by Sakib Miazi on 5/18/23.
//

import UIKit

class ViewController: UIViewController {
    //codes omitted...
    
    //MARK: expenses array to populate TableView...
    var expenses = [Expense]()
    
    //MARK: predefined types of expenses...
    let types = ["Groceries", "Rent", "Subscriptions", "Gadgets and Electronics"]
    
    //codes omitted...

    override func viewDidLoad() {
        //codes omitted...
        
        //MARK: adding dummy data for testing table view...
        expenses.append(Expense(title: "Pixel 7 pro", amount: 750.0, type: types[3]))
        expenses.append(Expense(title: "iPhone SE", amount: 349.0, type: types[3]))
        expenses.append(Expense(title: "Target", amount: 150.0, type: types[0]))
        expenses.append(Expense(title: "Netflix", amount: 19.0, type: types[2]))
                
        //codes omitted...
    }
    //codes omitted...

}

extension ViewController: UITableViewDelegate, UITableViewDataSource{
    func tableView(_ tableView: UITableView, numberOfRowsInSection section: Int) -> Int {
        return expenses.count
    }
    
    func tableView(_ tableView: UITableView, cellForRowAt indexPath: IndexPath) -> UITableViewCell {
        let cell = tableView.dequeueReusableCell(withIdentifier: "expenses", for: indexPath) as! TableViewExpenseCell
        cell.labelTitle.text = expenses[indexPath.row].title
        if let uwAmount = expenses[indexPath.row].amount{
            cell.labelAmount.text = "Cost: $\(uwAmount)"
        }
        if let uwType = expenses[indexPath.row].type{
            cell.labelType.text = "Type: \(uwType)"
        }
        return cell
    }
    
    
}


```

Let's try to understand the table view methods. Once you adopt the protocols, Xcode asks you to implement the required methods with `numberOfRowsInSection` and `cellForRowAt`.

* `numberOfRowsInSection`: First, think about the number of sections/groups we are working with in this table view. We are building only one section, just the expenses list with the same kind of cells. We just fetch the data from `expenses` array and display them. So, the number of rows would be equal to the number of items in `expenses` array. That's why we return `expenses.count`.
* `cellForRowAt`: This method returns the Cell for displaying a particular expense in the current row. Now, we need to think about how to display the data from the data source (`expenses` array) to the Cell. We display the data in the Cell we designed before (`TableViewExpenseCell`). Do you remember the identifier we set for the cell? It was "expenses."\
  \
  So in the first line, we write: `let cell = tableView.dequeueReusableCell(withIdentifier: "expenses", for: indexPath) as! TableViewExpenseCell`. Here we basically fetch an empty cell (of identifier "expenses") from the current table view and reuse it.\
  \
  &#xNAN;_**What is a reusable cell?**_\
  &#xNAN;_&#x49;f you open up the settings app on your iPhone, you will see a long table view with many rows. Do you see all the rows at once? Or a few of the rows on the screen at once? The screen can accommodate only a limited number of them. So a table view doesn't load the whole data table at once in the memory; rather, it just loads a few of the cells it can accommodate within the screen. So, when we scroll down, it removes the cells it cannot show anymore on the screen. Those cells are still loaded in the memory but unused. So iOS recycles them. When we call dequeueReusableCell(), it checks if it already has a reusable empty cell with the identifier provided. If yes, it will reuse that; else, it will create a new cell of that identifier. For more:_ [_https://medium.com/doyeona/things-that-you-must-know-about-uitableview-in-swift-fa2f6330a337_](https://medium.com/doyeona/things-that-you-must-know-about-uitableview-in-swift-fa2f6330a337)\
  \
  Then we set the variables of that particular cell with the data we have. `indexPath.row` corresponds to the element in the data source (expenses) for that row. Then we return the cell.

Now, we need to add the following couple of lines in the `viewDidLoad()` method:

```swift
override func viewDidLoad() {
        super.viewDidLoad()
        // Do any additional setup after loading the view.
        title = "Expense App"
        
        //code omitted...
        
        //MARK: patching the table view delegate and datasource to controller...
        firstScreen.tableViewExpense.delegate = self
        firstScreen.tableViewExpense.dataSource = self
        
        //codes omitted...
    }
```

We are patching the table view's delegate and data source to the controller. By saying that, we are asking the table view to use data from this controller and assigning the controller to manage the table view.

Now, let's run it.

<figure><img src="/gitbook-assets/six (2).gif" alt="Educational illustration for iOS concept"><figcaption></figcaption></figure>

Our Table View is up and running now, displaying our dummy data!

### File structures

Since we are almost done with our first screen, let's create groups of files and put them in separate folders to structure them better.

<figure><img src="/gitbook-assets/seven (2).gif" alt="Educational illustration for iOS concept"><figcaption></figcaption></figure>

The file structure looks like this:

![Educational illustration for iOS concept](</gitbook-assets/Screenshot 2023-05-18 at 3.01.03 PM (1).png>)



### Second screen, part 1: Setting up the View of the Add Expense Screen

When the user clicks the plus Bar button (`+`), we should populate a screen to add a new expense. So, let's create two new files: AddExpenseView.swift (subclass of UIView) and AddExpenseViewController.swift (subclass of UIViewController). And add them to a new group, "Add Expense Screen." (**Use the Cocoa Touch Class template, not a Swift file template).**

<figure><img src="/gitbook-assets/5.ten (1).gif" alt="Educational illustration for iOS concept"><figcaption></figcaption></figure>

### Setting up the View

![Educational illustration for iOS concept](</gitbook-assets/Screenshot 2023-05-18 at 10.45.19 AM (1).png>)

We can see that we need the following UI elements:

* Two TextFields to put the title and amount of the expense.
* One Label to display "Select the type of expense:"
* One PickerView to select the types of expenses.
* One button to finally Add an expense.

Let's open AddExpenseView.swift file and put the following codes to build the front end:

```swift
//
//  AddExpenseView.swift
//  App5
//
//  Created by Sakib Miazi on 5/18/23.
//

import UIKit

class AddExpenseView: UIView {

    var textFieldTitle: UITextField!
    var textFieldAmount: UITextField!
    var labelType: UILabel!
    var pickerType: UIPickerView!
    var buttonAdd: UIButton!

    override init(frame: CGRect) {
        super.init(frame: frame)
        backgroundColor = .white
        
        setuptextFieldTitle()
        setuptextFieldAmount()
        setuplabelType()
        setuppickerType()
        setupbuttonAdd()
        
        initConstraints()
    }
    
//    MARK: methods to initialize the UI elements...
    func setuptextFieldTitle(){
        textFieldTitle = UITextField()
        textFieldTitle.placeholder = "Put title"
        textFieldTitle.translatesAutoresizingMaskIntoConstraints = false
        self.addSubview(textFieldTitle)
    }
    func setuptextFieldAmount(){
        textFieldAmount = UITextField()
        textFieldAmount.placeholder = "Put amount"
        textFieldAmount.translatesAutoresizingMaskIntoConstraints = false
        self.addSubview(textFieldAmount)
    }
    func setuplabelType(){
        labelType = UILabel()
        labelType.textColor = .systemGray
        labelType.text = "Select the type of expense:"
        labelType.textAlignment = .center
        labelType.translatesAutoresizingMaskIntoConstraints = false
        self.addSubview(labelType)
    }
    func setuppickerType(){
        pickerType = UIPickerView()
        pickerType.translatesAutoresizingMaskIntoConstraints = false
        self.addSubview(pickerType)
    }
    func setupbuttonAdd(){
        buttonAdd = UIButton(type: .system)
        buttonAdd.setTitle("Add Expense", for: .normal)
        buttonAdd.translatesAutoresizingMaskIntoConstraints = false
        self.addSubview(buttonAdd)
    }
    
    //MARK: initialize the constraints...
    func initConstraints(){
        NSLayoutConstraint.activate([
            textFieldTitle.topAnchor.constraint(equalTo: self.safeAreaLayoutGuide.topAnchor, constant: 32),
            textFieldTitle.centerXAnchor.constraint(equalTo: self.safeAreaLayoutGuide.centerXAnchor),
            
            textFieldAmount.topAnchor.constraint(equalTo: textFieldTitle.bottomAnchor, constant: 16),
            textFieldAmount.centerXAnchor.constraint(equalTo: self.safeAreaLayoutGuide.centerXAnchor),
            
            labelType.topAnchor.constraint(equalTo: textFieldAmount.bottomAnchor, constant: 16),
            labelType.centerXAnchor.constraint(equalTo: self.safeAreaLayoutGuide.centerXAnchor),
            
            pickerType.topAnchor.constraint(equalTo: labelType.bottomAnchor, constant: 8),
            pickerType.centerXAnchor.constraint(equalTo: self.safeAreaLayoutGuide.centerXAnchor),
            
            buttonAdd.topAnchor.constraint(equalTo: pickerType.bottomAnchor, constant: 16),
            buttonAdd.centerXAnchor.constraint(equalTo: self.safeAreaLayoutGuide.centerXAnchor),
        ])
    }
    
   
    
    //MARK: unused methods...
    required init?(coder: NSCoder) {
        fatalError("init(coder:) has not been implemented")
    }
}

```

This file should be very straightforward to understand. Now that we have added our front end, we will now get to the controller code (AddExpenseViewController).



### Second screen, part 2: Setting up Add Expense View Controller

Now, let's open the AddExpenseViewController.swift file. We need to patch this view controller with the front-end view (AddExpenseView) we created. So, we write the following code to load the view:

```swift
//
//  AddExpenseViewController.swift
//  App5
//
//  Created by Sakib Miazi on 5/18/23.
//

import UIKit

class AddExpenseViewController: UIViewController {

    //MARK: initializing the ADDExpenseView...
    let addExpenseScreen = AddExpenseView()
    
    //MARK: set the current view to addExpenseScreen...
    override func loadView() {
        view = addExpenseScreen
    }
    
    override func viewDidLoad() {
        super.viewDidLoad()

        // Do any additional setup after loading the view.
    }

}

```

### **Patching the PickerView to pick the type of expense**

Now, let's patch the PickerView (`addExpenseScreen.pickerType`) to the controller.

We will pick the type of expense using this PickerView. We know that we added an array of four expense types in ViewController.swift. Since we need to use the same array instead of writing the array again, we can define a static array to be shared with all the classes in the project. The keyword `static` makes it persistent in the memory while the app is running. **Do not make all the data static; you can keep it static if it is small shared data.**

### Defining static array 'types'

Let's create a new Swift file named "Utilities.swift" in the project.

<figure><img src="/gitbook-assets/5.6.1.one (1).gif" alt="Educational illustration for iOS concept"><figcaption></figcaption></figure>

Let's add the following code to the new file:

```swift
//
//  Utilities.swift
//  App5
//
//  Created by Sakib Miazi on 5/18/23.
//

import Foundation

class Utilities{
    static let types = ["Groceries", "Rent", "Subscriptions", "Gadgets and Electronics"]
}
```

Here, the Utilities class holds these usable shared data like the types array. We kept the `types` array as static.

Now let's get back to implementing the PickerView in AddExpenseViewController.swift file.

### Adopting the Picker View's protocols

So, we again use the `extension` keyword to adopt `UIPickerViewDelegate` and `UIPickerViewDataSource` protocols. Let's write the code below to AddExpenseViewController.swift file:

```swift
//
//  AddExpenseViewController.swift
//  App5
//
//  Created by Sakib Miazi on 5/18/23.
//

import UIKit

class AddExpenseViewController: UIViewController {
    //MARK: by default Groceries is selected...
    var selectedType = "Groceries"
    
    //codes omitted...
}

//MARK: adopting the required protocols...
extension AddExpenseViewController: UIPickerViewDelegate, UIPickerViewDataSource{
    func numberOfComponents(in pickerView: UIPickerView) -> Int {
        //MARK: we are using only one section...
        return 1
    }
    
    func pickerView(_ pickerView: UIPickerView, numberOfRowsInComponent component: Int) -> Int {
        //MARK: we are displaying the options from Utilities.types...
        return Utilities.types.count
    }
    
    func pickerView(_ pickerView: UIPickerView, titleForRow row: Int, forComponent component: Int) -> String? {
        
        //MARK: updating the selected type when the user picks this row...
        selectedType = Utilities.types[row]
        return Utilities.types[row]
    }
}
```

We have only one component to select in this PickerVIew, so the `numberOfComponents` should return just 1. We are displaying the `Utilities.types` array, so `numberOfRowsInComponent` should return `Utilities.types.count`. We keep a variable `selectedType` to keep the current selection of the user. So, we set the currently selected row to `selectedType` variable in `titleForRow` and return `Utilities.types[row]`.

Now, we need to patch the delegate and data sources of the PickerView with AddExpenseViewController. Add the following couple of lines in `viewDidLoad()` method:

```swift
//
//  AddExpenseViewController.swift
//  App5
//
//  Created by Sakib Miazi on 5/18/23.
//

import UIKit

class AddExpenseViewController: UIViewController {
    //codes omitted...
        
    override func viewDidLoad() {
        super.viewDidLoad()
        //MARK: patching delegate and datasource of the type PickerView...
        addExpenseScreen.pickerType.dataSource = self
        addExpenseScreen.pickerType.delegate = self
    }

}
//codes omitted...

```

Now, we need to update ViewController.swift file to be able to navigate to AddExpenseViewController.swift and get back with the new expense. So, let's add an instance variable of ViewController named "delegate" to AddExpenseViewController.

```swift
//
//  AddExpenseViewController.swift
//  App5
//
//  Created by Sakib Miazi on 5/18/23.
//

import UIKit

class AddExpenseViewController: UIViewController {
    //MARK: delegate to ViewController when getting back...
    var delegate:ViewController!
    //codes omitted...
}
//codes omitted...

```

### Housekeeping: Updating Navigation controller and patching Utilities.types in View Controller

Open the ViewController.swift file. Now, let's complete the plus (`+`) button actions. When we tap on the `+` button on the Navigation Bar, we need to switch from the First Screen to Add Expense Screen. So let's write the following code in the method `@objc func onAddBarButtonTapped()`:

```swift
//
//  ViewController.swift
//  App5
//
//  Created by Sakib Miazi on 5/18/23.
//

import UIKit

class ViewController: UIViewController {
    
//codes omitted...

    override func viewDidLoad() {
        //codes omitted...
        
        //MARK: setting the add button to the navigation controller...
        navigationItem.rightBarButtonItem = UIBarButtonItem(
            barButtonSystemItem: .add, target: self,
            action: #selector(onAddBarButtonTapped)
        )
    }
    
    @objc func onAddBarButtonTapped(){
        let addExpenseController = AddExpenseViewController()
        addExpenseController.delegate = self
        navigationController?.pushViewController(addExpenseController, animated: true)
    }


}

//codes omitted...


```

The code above creates a new Add Expense Screen, sets the delegate, and pushes it on the Navigation Stack. Now let's run the app:

<figure><img src="/gitbook-assets/5.6.1.two (1).gif" alt="Educational illustration for iOS concept"><figcaption></figcaption></figure>

### Updating ViewController to use Utilities.types instead of the local array.

Now let's **remove** the array `types` from ViewController.swift:

```swift
//remove the line:
let types = ["Groceries", "Rent", "Subscriptions", "Gadgets and Electronics"]
```

Also, we can now remove the dummy data from the codes. So remove the following lines from ViewController's `viewDidLoad()` method:

```swift
//remove the lines:
expenses.append(Expense(title: "Pixel 7 pro", amount: 750.0, type: types[3]))
expenses.append(Expense(title: "iPhone SE", amount: 349.0, type: types[3]))
expenses.append(Expense(title: "Target", amount: 150.0, type: types[0]))
expenses.append(Expense(title: "Netflix", amount: 19.0, type: types[2]))
```

### **So far, the updated controller codes are as follows:**

#### ViewController.swift

```swift
//
//  ViewController.swift
//  App5
//
//  Created by Sakib Miazi on 5/18/23.
//

import UIKit

class ViewController: UIViewController {
    
    let firstScreen = FirstScreenView()
    
    //MARK: expenses array to populate TableView...
    var expenses = [Expense]()
    
    //MARK: predefined types of expenses...
    let types = ["Groceries", "Rent", "Subscriptions", "Gadgets and Electronics"]
    
    override func loadView() {
        view = firstScreen
    }

    override func viewDidLoad() {
        super.viewDidLoad()
        title = "Expense App"
        
        //MARK: patching the table view delegate and datasource to controller...
        firstScreen.tableViewExpense.delegate = self
        firstScreen.tableViewExpense.dataSource = self
                
        //MARK: setting the add button to the navigation controller...
        navigationItem.rightBarButtonItem = UIBarButtonItem(
            barButtonSystemItem: .add, target: self,
            action: #selector(onAddBarButtonTapped)
        )
    }
    
    @objc func onAddBarButtonTapped(){
        let addExpenseController = AddExpenseViewController()
        addExpenseController.delegate = self
        navigationController?.pushViewController(addExpenseController, animated: true)
    }


}

extension ViewController: UITableViewDelegate, UITableViewDataSource{
    func tableView(_ tableView: UITableView, numberOfRowsInSection section: Int) -> Int {
        return expenses.count
    }
    
    func tableView(_ tableView: UITableView, cellForRowAt indexPath: IndexPath) -> UITableViewCell {
        let cell = tableView.dequeueReusableCell(withIdentifier: "expenses", for: indexPath) as! TableViewExpenseCell
        cell.labelTitle.text = expenses[indexPath.row].title
        if let uwAmount = expenses[indexPath.row].amount{
            cell.labelAmount.text = "Cost: $\(uwAmount)"
        }
        if let uwType = expenses[indexPath.row].type{
            cell.labelType.text = "Type: \(uwType)"
        }
        return cell
    }
    
    
}
```

#### AddExpenseViewController.swift

```swift
//
//  AddExpenseViewController.swift
//  App5
//
//  Created by Sakib Miazi on 5/18/23.
//

import UIKit

class AddExpenseViewController: UIViewController {
    
    //MARK: delegate to ViewController when getting back...
    var delegate:ViewController!
    
    //MARK: by default Groceries is selected...
    var selectedType = "Groceries"

    //MARK: initializing the ADDExpenseView...
    let addExpenseScreen = AddExpenseView()
    
    //MARK: set the current view to addExpenseScreen...
    override func loadView() {
        view = addExpenseScreen
    }
    
    override func viewDidLoad() {
        super.viewDidLoad()

        //MARK: patching delegate and datasource of the type PickerView...
        addExpenseScreen.pickerType.dataSource = self
        addExpenseScreen.pickerType.delegate = self
    }

}

//MARK: adopting the required protocols...
extension AddExpenseViewController: UIPickerViewDelegate, UIPickerViewDataSource{
    func numberOfComponents(in pickerView: UIPickerView) -> Int {
        //MARK: we are using only one section...
        return 1
    }
    
    func pickerView(_ pickerView: UIPickerView, numberOfRowsInComponent component: Int) -> Int {
        //MARK: we are displaying the options from Utilities.types...
        return Utilities.types.count
    }
    
    func pickerView(_ pickerView: UIPickerView, titleForRow row: Int, forComponent component: Int) -> String? {
        
        //MARK: updating the selected type when the user picks this row...
        selectedType = Utilities.types[row]
        return Utilities.types[row]
    }
}

```



### Second screen, part 3: Send new expense back to ViewController and update the TableView

Let's open AddExpenseViewController.swift file. Now, we will add an action for tapping on`addExpenseScreen.buttonAdd`. Once this button is tapped, we need to create an Expense object from the data the user put in and delegate the next tasks to ViewController.

So, let's add the action target for `addExpenseScreen.buttonAdd` by writing the following code in `viewDidLoad()`:

```swift
//
//  AddExpenseViewController.swift
//  App5
//
//  Created by Sakib Miazi on 5/18/23.
//

import UIKit

class AddExpenseViewController: UIViewController {
    
    //codes omitted...
    override func viewDidLoad() {
        
        //codes omitted...
        
        //MARK: adding the action for tapping on buttonAdd...
        addExpenseScreen.buttonAdd.addTarget(self, action: #selector(onAddButtonTapped), for: .touchUpInside)
    }
    
    //MARK: action for tapping buttonAdd..
    @objc func onAddButtonTapped(){
        var title:String?
        if let titleText = addExpenseScreen.textFieldTitle.text{
            if !titleText.isEmpty{
                title = titleText
            }else{
                //do your thing to alert user...
                return
            }
        }
        
        var amount = 0.0
        if let amountText = addExpenseScreen.textFieldAmount.text{
            if !amountText.isEmpty{
                if let optionalAmount = Double(amountText){
                    amount = optionalAmount
                }else{
                    //alert the user that it's not a valid input...
                    return
                }
            
                
            }else{
                //do your thing to alert the user...
                return
            }
            
        }
        
        let newExpense = Expense(title: title, amount: amount, type: selectedType)
        delegate.delegateOnAddExpense(expense: newExpense)
        navigationController?.popViewController(animated: true)
    }

}
//codes omitted...
```

Here we are fetching the inputs from the user. I am not writing the AlertController codes here again. If the user puts an empty string, you should alert the user.

### (Handling Double inputs)

Here, we are first reading the TextField text. Then, we unwrap the text and convert it to Double. The issue is the converted value is also Optional. So, we attempt to unwrap it; if we can unwrap it with `if-let`, then we set the unwrapped value to `amount`. Else, we alert the user that it is not a valid input.

Now, we will create an object of `Expense` with the fetched data and delegate the next tasks to ViewController by calling `delegateOnAddExpense(expense: newExpense)`.

### Delegating the task to ViewController

**The problem is, ViewController doesn't have `delegateOnAddExpense()` method yet.** So let's open the ViewController.swift file and add the method there:

```swift
//
//  ViewController.swift
//  App5
//
//  Created by Sakib Miazi on 5/18/23.
//

import UIKit

class ViewController: UIViewController {
    //codes omitted...
    
    //MARK: got the new expense back and delegated to ViewController...
    func delegateOnAddExpense(expense: Expense){
        expenses.append(expense)
        firstScreen.tableViewExpense.reloadData()
    }


}
//codes omitted...
```

Here, we receive an object of Expense, `expense` through the delegated method and append the new expense to the array. Then we reload the data for the TableView by calling: `firstScreen.tableViewExpense.reloadData()`.

Let's run the app.

<figure><img src="/gitbook-assets/5.6.1.three (1).gif" alt="Educational illustration for iOS concept"><figcaption></figcaption></figure>

One last thing to discuss before we finish this module. We can also deal with when a user clicks on a cell in the TableView.



### Tapping a cell in TableView and Practice exercise

Let's open ViewController.swift file and add the following code to the protocols adoption block:

```swift
//
//  ViewController.swift
//  App5
//
//  Created by Sakib Miazi on 5/18/23.
//

//codes omitted...

extension ViewController: UITableViewDelegate, UITableViewDataSource{
    //codes omitted...
    
    //MARK: deal with user interaction with a cell...
    func tableView(_ tableView: UITableView, didSelectRowAt indexPath: IndexPath) {
        print(self.expenses[indexPath.row])
    }
    
}
```

We added the `tableView()` method for `didSelectRowAt`. It is the call-back method if a user taps on a cell (selected a cell) in TableView. After you add this method, let's run the app. It should print the corresponding data.

<figure><img src="/gitbook-assets/5.6.1.four (1).gif" alt="Educational illustration for iOS concept"><figcaption></figcaption></figure>

Now, you can see that you can handle it if a user taps on a cell. It's time for exercise.

### Exercise

**Now your task is to build a third screen, "DisplayExpense," to show the details of an expense if a user taps on it. It could be just three Labels to display the title, amount, and type of the selected expense.**



### Reference Code

[Download Project Archive](/gitbook-assets/App5 (1).zip)

---

## Guided Practice Challenges

Before moving on to the next topic, try these low-stakes practice challenges in Xcode. They will build the exact muscle memory you need:

### Challenge 1: Experimentation
**The Scenario:** You've just learned about UITableView.
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


### UIScrollView

**Estimated effort:** 1-2 hours this topic
**Format:** Asynchronous online
**Prerequisites:** Previous iOS topics


**🎯 Topic Mission:** 
In this module, we will explore **UIScrollView** and learn how to integrate it into our iOS applications. Your mission is to understand the mechanics behind this concept and write robust Swift code.


---

## Learning Objectives

By the end of this session, you will be able to:
1. Understand the core concepts of UIScrollView.
2. Implement UIScrollView in an Xcode project.
3. Apply best practices to ensure clean and maintainable code.

---

## The Story So Far...

We have been progressively building our knowledge of iOS and Swift. In this module, we will expand our toolkit by diving into UIScrollView. 
Open your current Xcode project or start a new Playground to follow along with the hands-on material.

---

## Walkthrough: Exploring UIScrollView

> 📁 **Target Project** — Follow along by building the mini-app presented in the steps below, or integrate these concepts into your own ongoing projects.

### UIScrollView

So far, we have worked with screens that do not scroll. I think all of you faced a similar issue: if you rotate the screen, the UI elements get outside the bottom edge. The reason behind it is that the screen is not scrollable. So here, we will implement a scrollable view.

Let's build a small app App8 to implement a ScrollView. The app should look like this:

<figure><img src="/gitbook-assets/8.11 (1).gif" alt="Educational illustration for iOS concept"><figcaption></figcaption></figure>

**So there will be the following UI elements:**

* One text field at the top (`textField1`).
* Next, we will have a large image covering almost the whole screen.
* Then two more text fields at the bottom (`textField1` and `textField2`).




### Creating the View of the Screen

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

![Educational illustration for iOS concept](</gitbook-assets/image@3x (1).jpg>)

So, let's import the image into the project:

<figure><img src="/gitbook-assets/Screenshot 2023-05-24 at 10.59.28 AM (1).png" alt="Educational illustration for iOS concept"><figcaption></figcaption></figure>

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



### Creating the Controller

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

<figure><img src="/gitbook-assets/8.11 (1).gif" alt="Educational illustration for iOS concept"><figcaption></figcaption></figure>

_Now that you know how to use scrollable views. Use it carefully when you use it._



### Reference Code

[Download Project Archive](/gitbook-assets/App8 (1).zip)

---

## Guided Practice Challenges

Before moving on to the next topic, try these low-stakes practice challenges in Xcode. They will build the exact muscle memory you need:

### Challenge 1: Experimentation
**The Scenario:** You've just learned about UIScrollView.
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


### UIMenu & Image Pickers

**Estimated effort:** 1-2 hours this topic
**Format:** Asynchronous online
**Prerequisites:** Previous iOS topics


**🎯 Topic Mission:** 
In this module, we will explore **UIMenu & Image Pickers** and learn how to integrate it into our iOS applications. Your mission is to understand the mechanics behind this concept and write robust Swift code.


---

## Learning Objectives

By the end of this session, you will be able to:
1. Understand the core concepts of UIMenu & Image Pickers.
2. Implement UIMenu & Image Pickers in an Xcode project.
3. Apply best practices to ensure clean and maintainable code.

---

## The Story So Far...

We have been progressively building our knowledge of iOS and Swift. In this module, we will expand our toolkit by diving into UIMenu & Image Pickers. 
Open your current Xcode project or start a new Playground to follow along with the hands-on material.

---

## Walkthrough: Exploring UIMenu & Image Pickers

> 📁 **Target Project** — Follow along by building the mini-app presented in the steps below, or integrate these concepts into your own ongoing projects.

### UIMenu, Picking Images from Gallery and Camera, and UIImageView

### App6: Adding more features on App5

Let's create a new project, "App6." Add all the codes from the current "App5." For your convenience, download the project from here:

[Download Project Archive](/gitbook-assets/App6_initial (1).zip)

Our goal here is to:

* Learn to use UIMenu instead of PickerView.
* Add an ImageView to the TableView Cell to display the expense receipt.
* Add options to take a photo of the receipt using the camera or gallery.

App6 would look something like this:

<figure><img src="/gitbook-assets/6.1.one.gif" alt="Educational illustration for iOS concept"><figcaption></figcaption></figure>




### Updating the TableView Cell to accommodate an ImageView

Let's open TableViewExpenseCell.swift file to add an ImageView. Let's add a new variable named, `imageViewReceipt` of type `UIImageView` in the file, set it up, and initialize its constraints. Add the following code to TableViewExpenseCell.swift file:


```swift
//
//  TableViewExpenseCell.swift
//  App6
//
//  Created by Sakib Miazi on 5/18/23.
//

import UIKit

class TableViewExpenseCell: UITableViewCell {
    //codes omitted...
    
    //MARK: declaring the ImageView for receipt image...
    var imageReceipt: UIImageView!
    
    override init(style: UITableViewCell.CellStyle, reuseIdentifier: String?) {
        //Codes omitted...
        
        //MARK: defining the ImageView for receipt image...
        setupimageReceipt()
        
        initConstraints()
    }
    
    //Codes omitted...
    
    //Adding the ImageView for receipt...
    func setupimageReceipt(){
        imageReceipt = UIImageView()
        imageReceipt.image = UIImage(systemName: "photo")
        imageReceipt.contentMode = .scaleToFill
        imageReceipt.clipsToBounds = true
        imageReceipt.layer.cornerRadius = 10
        imageReceipt.translatesAutoresizingMaskIntoConstraints = false
        wrapperCellView.addSubview(imageReceipt)
    }
    
    //MARK: initializing the constraints...
    func initConstraints(){
        NSLayoutConstraint.activate([
            wrapperCellView.topAnchor.constraint(equalTo: self.topAnchor,constant: 10),
            wrapperCellView.leadingAnchor.constraint(equalTo: self.leadingAnchor, constant: 10),
            wrapperCellView.bottomAnchor.constraint(equalTo: self.bottomAnchor, constant: -10),
            wrapperCellView.trailingAnchor.constraint(equalTo: self.trailingAnchor, constant: -10),
            
            labelTitle.topAnchor.constraint(equalTo: wrapperCellView.topAnchor, constant: 2),
            labelTitle.leadingAnchor.constraint(equalTo: imageReceipt.trailingAnchor, constant: 8),
            labelTitle.heightAnchor.constraint(equalToConstant: 32),
            labelTitle.widthAnchor.constraint(lessThanOrEqualTo: wrapperCellView.widthAnchor),
            
            labelAmount.topAnchor.constraint(equalTo: labelTitle.bottomAnchor, constant: 2),
            labelAmount.leadingAnchor.constraint(equalTo: labelTitle.leadingAnchor),
            labelAmount.heightAnchor.constraint(equalToConstant: 32),
            labelAmount.widthAnchor.constraint(lessThanOrEqualTo: labelTitle.widthAnchor),
            
            labelType.topAnchor.constraint(equalTo: labelAmount.bottomAnchor, constant: 2),
            labelType.leadingAnchor.constraint(equalTo: labelTitle.leadingAnchor),
            labelType.heightAnchor.constraint(equalToConstant: 32),
            labelType.widthAnchor.constraint(lessThanOrEqualTo: labelTitle.widthAnchor),
            
            imageReceipt.leadingAnchor.constraint(equalTo: wrapperCellView.leadingAnchor, constant: 8),
            imageReceipt.centerYAnchor.constraint(equalTo: wrapperCellView.centerYAnchor),
            //MARK: it is better to set the height and width of an ImageView with constraints...
            imageReceipt.heightAnchor.constraint(equalTo: wrapperCellView.heightAnchor, constant: -20),
            imageReceipt.widthAnchor.constraint(equalTo: wrapperCellView.heightAnchor, constant: -20),
            
            wrapperCellView.heightAnchor.constraint(equalToConstant: 104)
        ])
    }
    
    //codes omitted...

}

```


In the above code, we have a few very important key points to discuss:

**Defining the ImageView `imageReceipt`:**

* Let's look into the method where we define the new `imageReceipt` ImageView (`setupimageReceipt()`). We wrote: `imageReceipt.image = UIImage(systemName: "photo")`. We are trying to set a default image for the ImageView. For the default image, we select an iOS system image named "photo" (<img src="/gitbook-assets/photo@2x (1).png" alt="Educational illustration for iOS concept" data-size="line">). Xcode ships with these system images. But we need to know the names of those images. Fortunately, we can easily find the names of the system images. You need to install an Apple developer app called "SF Symbols" on your Mac. [Download, install, and learn how to use the app.](6.1.-updating-the-tableview-cell-to-accommodate-an-imageview.md#installing-and-using-sf-symbols-app)
* Next, we write `imageReceipt.contentMode = .scaleToFill` to say, fill the ImageView with the image by resizing it. For more details on `contentMode`, read: [https://www.delasign.com/blog/uiimageview-content-modes/](https://www.delasign.com/blog/uiimageview-content-modes/)
* We write `imageReceipt.clipsToBounds = true` to say, clip the image if it overflows the ImageView frame.
* We write `imageReceipt.layer.cornerRadius = 10` to make the corners of the ImageView rounded with a radius of 10.

**Constraints of the ImageView `imageReceipt`:**

* We place the ImageView to the left of the cell. So, for all the other UI elements, we set their `leadingAnchor` to `imageReceipt`'s `trailingAnchor` with a gap of 8 points. For example: `labelTitle.leadingAnchor.constraint(equalTo: imageReceipt.trailingAnchor, constant: 8)`.
* It's better to define the heights and widths of the UI elements while designing the cell. We set the heights of the Labels to 32 points. For example, `labelTitle.heightAnchor.constraint(equalToConstant: 32)`.\
  \
  Also, we define the constraints of the Labels so that they can take all the remaining space in the cell after we populate the ImageView. For example, `labelTitle.widthAnchor.constraint(lessThanOrEqualTo: wrapperCellView.widthAnchor)`. `lessThanOrEqualTo` means that it will try to occupy the whole width of the wrapper; if it can't, it will occupy the remaining space.
* We are using the width of the cell to create a square ImageView by writing: `imageReceipt.heightAnchor.constraint(equalTo: wrapperCellView.heightAnchor, constant: -20)`.\
  It means if the wrapper's width is 104, the frame size of the ImageView will be 84x84.
* Finally, we add all the constraint values (2+32+2+32+2+32+2) and define the wrapper's height to 104.

Now that we are done with the file, we move to the Add Expense Screen.

### Appendix

### Installing and using SF Symbols app

* Download the SF Symbols app from here: [https://developer.apple.com/sf-symbols/](https://developer.apple.com/sf-symbols/)

<figure><img src="/gitbook-assets/6.1.two (1).gif" alt="Educational illustration for iOS concept"><figcaption></figcaption></figure>

* Open the .DMG file
* Then Install the .pkg file by double-clicking on it:

<figure><img src="/gitbook-assets/6.1.four.gif" alt="Educational illustration for iOS concept"><figcaption></figcaption></figure>

*   Let's open the app. Press `Command` + `Space` to open the spotlight search. Then look for SF Symbols and press `return` to open it. \\

    <figure><img src="/gitbook-assets/5.6.1.five (1).gif" alt="Educational illustration for iOS concept"><figcaption></figcaption></figure>
*   Now we can use the app to find the appropriate iOS system icon/symbol for us and fetch the name of it. Here I am finding the name for the icon I will use:\\

    <figure><img src="/gitbook-assets/5.6.1.six (1).gif" alt="Educational illustration for iOS concept"><figcaption></figcaption></figure>



### Add Expense Screen

The screen would be something like this:

![Educational illustration for iOS concept](</gitbook-assets/Screenshot 2023-05-19 at 12.47.14 AM.png>)

We have:

* Two TextFields
* One Button to choose the type of expense
* One Button (use the Camera icon as the background) to pick the image for receipt.
* FInally, the Add Expense Button.

### AddExpenseView

Let's open the AddExpenseView.swift file and update the code. Remove the PickerView and add two buttons (to select expense type and pick receipt image).

Let's see the updated code in the following:


```swift
//
//  AddExpenseView.swift
//  App6
//
//  Created by Sakib Miazi on 5/18/23.
//

import UIKit

class AddExpenseView: UIView {
    var textFieldTitle: UITextField!
    var textFieldAmount: UITextField!
    var buttonSelectType: UIButton!
    var buttonTakePhoto: UIButton!
    var buttonAdd: UIButton!

    override init(frame: CGRect) {
        super.init(frame: frame)
        backgroundColor = .white
        
        setuptextFieldTitle()
        setuptextFieldAmount()
        setupbuttonSelectType()
        setupbuttonTakePhoto()
        setupbuttonAdd()
        
        initConstraints()
    }
    
    func setuptextFieldTitle(){
        textFieldTitle = UITextField()
        textFieldTitle.placeholder = "Put title"
        textFieldTitle.translatesAutoresizingMaskIntoConstraints = false
        self.addSubview(textFieldTitle)
    }
    func setuptextFieldAmount(){
        textFieldAmount = UITextField()
        textFieldAmount.placeholder = "Put amount"
        textFieldAmount.translatesAutoresizingMaskIntoConstraints = false
        self.addSubview(textFieldAmount)
    }
    func setupbuttonSelectType(){
        buttonSelectType = UIButton(type: .system)
        buttonSelectType.setTitle("Select the type of expense:", for: .normal)
        buttonSelectType.translatesAutoresizingMaskIntoConstraints = false
        self.addSubview(buttonSelectType)
    }
    func setupbuttonTakePhoto(){
        buttonTakePhoto = UIButton(type: .system)
        buttonTakePhoto.setTitle("", for: .normal)
        buttonTakePhoto.setImage(UIImage(systemName: "camera.fill"), for: .normal)
        buttonTakePhoto.contentHorizontalAlignment = .fill
        buttonTakePhoto.contentVerticalAlignment = .fill
        buttonTakePhoto.imageView?.contentMode = .scaleAspectFit
        buttonTakePhoto.translatesAutoresizingMaskIntoConstraints = false
        self.addSubview(buttonTakePhoto)
    }
    func setupbuttonAdd(){
        buttonAdd = UIButton(type: .system)
        buttonAdd.setTitle("Add Expense", for: .normal)
        buttonAdd.translatesAutoresizingMaskIntoConstraints = false
        self.addSubview(buttonAdd)
    }
    
    func initConstraints(){
        NSLayoutConstraint.activate([
            textFieldTitle.topAnchor.constraint(equalTo: self.safeAreaLayoutGuide.topAnchor, constant: 32),
            textFieldTitle.centerXAnchor.constraint(equalTo: self.safeAreaLayoutGuide.centerXAnchor),
            
            textFieldAmount.topAnchor.constraint(equalTo: textFieldTitle.bottomAnchor, constant: 16),
            textFieldAmount.centerXAnchor.constraint(equalTo: self.safeAreaLayoutGuide.centerXAnchor),
            
            buttonSelectType.topAnchor.constraint(equalTo: textFieldAmount.bottomAnchor, constant: 16),
            buttonSelectType.centerXAnchor.constraint(equalTo: self.safeAreaLayoutGuide.centerXAnchor),
            
            buttonTakePhoto.topAnchor.constraint(equalTo: buttonSelectType.bottomAnchor, constant: 16),
            buttonTakePhoto.centerXAnchor.constraint(equalTo: self.safeAreaLayoutGuide.centerXAnchor),
            buttonTakePhoto.widthAnchor.constraint(equalToConstant: 100),
            buttonTakePhoto.heightAnchor.constraint(equalToConstant: 100),
            
            buttonAdd.topAnchor.constraint(equalTo: buttonTakePhoto.bottomAnchor, constant: 16),
            buttonAdd.centerXAnchor.constraint(equalTo: self.safeAreaLayoutGuide.centerXAnchor),
        ])
    }
    
   
    
    //MARK: unused functions...
    required init?(coder: NSCoder) {
        fatalError("init(coder:) has not been implemented")
    }
}

```


### Setting up the Buttons

#### buttonSelectType:

Let's look into the setup method for `buttonSelectType`:


```swift
func setupbuttonSelectType(){
    buttonSelectType = UIButton(type: .system)
    buttonSelectType.setTitle("Select the type of expense:", for: .normal)
    buttonSelectType.translatesAutoresizingMaskIntoConstraints = false
    self.addSubview(buttonSelectType)
}
```


It looks pretty straight forward now. At some point, we need to tweak the setup a little.

#### buttonTakePhoto:

Let's look into the setup method:


```swift
func setupbuttonTakePhoto(){
    buttonTakePhoto = UIButton(type: .system)
    buttonTakePhoto.setTitle("", for: .normal)
    buttonTakePhoto.setImage(UIImage(systemName: "camera.fill"), for: .normal)
    buttonTakePhoto.contentHorizontalAlignment = .fill
    buttonTakePhoto.contentVerticalAlignment = .fill
    buttonTakePhoto.imageView?.contentMode = .scaleAspectFit
    buttonTakePhoto.translatesAutoresizingMaskIntoConstraints = false
    self.addSubview(buttonTakePhoto)
}
```


This button is a little different. We set a background to it, which shows a camera icon instead of text. So, we set an empty title to it. Then set an image of the system name, "camera.fill". (I found the name using the SF Symbols app). These couple of lines are very important.

For example, `buttonTakePhoto.contentHorizontalAlignment = .fill` means that the contents of this button can fill the whole width of the button. In our case, the content is the camera image inside the button. The same idea works with the next line: `buttonTakePhoto.contentVerticalAlignment = .fill` to allow the image of the button fill the height of the button.

Then, we set the frame of the image so that the image can be loaded with the content mode `scaleAspectFit`. (`buttonTakePhoto.imageView?.contentMode = .scaleAspectFit`).

### The Constraints

The constraints here are pretty straightforward, except for the `buttonTakePhoto`. Let's look into the constraints for the Button:

```swift
buttonTakePhoto.topAnchor.constraint(equalTo: buttonSelectType.bottomAnchor, constant: 16),
buttonTakePhoto.centerXAnchor.constraint(equalTo: self.safeAreaLayoutGuide.centerXAnchor),
//MARK: setting buttonTakePhoto's height and width...
buttonTakePhoto.widthAnchor.constraint(equalToConstant: 100),
buttonTakePhoto.heightAnchor.constraint(equalToConstant: 100),
```

We set the height and width of `buttonTakePhoto`. **When you are working with images, you should set a frame size. The best way to set the frame size is to do it using the constraints.** Use `widthAnchor` as the width and `heightAnchor` as the height of the frame.



### AddExpenseViewController: UIMenu for buttonSelectType

Now, it's time to remove the PickerView codes. After we remove the PickerView, the code looks like this:


```swift
//
//  AddExpenseViewController.swift
//  App6
//
//  Created by Sakib Miazi on 5/18/23.
//

import UIKit

class AddExpenseViewController: UIViewController {
    
    //MARK: delegate to ViewController when getting back...
    var delegate:ViewController!
    
    //MARK: by default Groceries is selected...
    var selectedType = "Groceries"

    //MARK: initializing the ADDExpenseView...
    let addExpenseScreen = AddExpenseView()
    
    //MARK: set the current view to addExpenseScreen...
    override func loadView() {
        view = addExpenseScreen
    }
    
    override func viewDidLoad() {
        super.viewDidLoad()
        
        //MARK: adding the action for tapping on buttonAdd...
        addExpenseScreen.buttonAdd.addTarget(self, action: #selector(onAddButtonTapped), for: .touchUpInside)
    }
    
    //MARK: action for tapping buttonAdd..
    @objc func onAddButtonTapped(){
        var title:String?
        if let titleText = addExpenseScreen.textFieldTitle.text{
            if !titleText.isEmpty{
                title = titleText
            }else{
                //do your thing to alert user...
            }
        }
        
        var amount = 0.0
        if let amountText = addExpenseScreen.textFieldAmount.text{
            if !amountText.isEmpty{
                if let uwAmount = Double(amountText){
                    amount = uwAmount
                }else{
                    //alert the user that it's not a valid input...
                }
            
                
            }else{
                //do your thing to alert the user...
            }
            
        }
        
        let newExpense = Expense(title: title, amount: amount, type: selectedType)
        delegate.delegateOnAddExpense(expense: newExpense)
        navigationController?.popViewController(animated: true)
    }

}
```


Now if you run the app, it will look like the following:

<figure><img src="/gitbook-assets/6.2.one (1).gif" alt="Educational illustration for iOS concept"><figcaption></figcaption></figure>

So now, let's add the actions for the newly added buttons, `buttonSelectType` and `buttonTakePhoto`.

### UIMenu for buttonSelectType

When the user taps on `buttonSelectType`, it should display a pop-up menu with four options. Let's add the code for it. In AddExpenseViewController.swift add:


```swift
//
//  AddExpenseViewController.swift
//  App6
//

class AddExpenseViewController: UIViewController {
    //codes omitted...
    
    override func viewDidLoad() {
        super.viewDidLoad()
        
        //MARK: adding menu to buttonSelectType...
        addExpenseScreen.buttonSelectType.menu = getMenuTypes()
        
        //codes omitted...
    }
    
    //MARK: menu for buttonSelectType setup...
    func getMenuTypes() -> UIMenu{
        var menuItems = [UIAction]()
        
        for type in Utilities.types{
            let menuItem = UIAction(title: type,handler: {(_) in
                                self.selectedType = type
                                self.addExpenseScreen.buttonSelectType.setTitle(self.selectedType, for: .normal)
                            })
            menuItems.append(menuItem)
        }
        
        return UIMenu(title: "Select type", children: menuItems)
    }
    //codes omitted...
}

```


We write `addExpenseScreen.buttonSelectType.menu` to set the menu. We write a method `getMenuTypes() -> UIMenu` to generate the menu. Let's look into the method.

We create an array of UIMenu items (four in our case). Each UIMenu item is a UIAction with the title of the menu item and the [closure](https://github.com/sakibnm/iOS/blob/main/7.-closures) for defining the tasks we should do if we select that item from the menu. For example, in each iteration of the loop:


```swift
for type in Utilities.types{
    let menuItem = UIAction(title: type,handler: {(_) in
                self.selectedType = type
                self.addExpenseScreen.buttonSelectType.setTitle(self.selectedType, for: .normal)
            })
    menuItems.append(menuItem)
}
```


Here, we are creating a menu item using the `Utilities.types` array. The `handler` closure defines the on-select actions for that item. We are saying that if the user selects this particular menu item, set the value of `selectedType` to the corresponding type of expense. And set the title of the button to the selected item.

So, let's run the app now.

<figure><img src="/gitbook-assets/6.2.two (1).gif" alt="Educational illustration for iOS concept"><figcaption></figcaption></figure>

See, if we long tap on `buttonSelectType` then a menu pops up, and we can select a type of expense. But we want this menu to pop up when we do regular tap. By default, the menu pop-up is not set as the primary action of a Button. We have to set it as an attribute of the Button when we initialize it. So let's go to AddExpenseView.swift and edit the `setupbuttonSelectType()` method:


```swift
func setupbuttonSelectType(){
    buttonSelectType = UIButton(type: .system)
    buttonSelectType.setTitle("Select the type of expense:", for: .normal)
    //MARK: the on-tap primary action will pop up the menu...
    buttonSelectType.showsMenuAsPrimaryAction = true
    buttonSelectType.translatesAutoresizingMaskIntoConstraints = false
    self.addSubview(buttonSelectType)
}
```


Now let's run the app again:

<figure><img src="/gitbook-assets/6.2.three (1) (1).gif" alt="Educational illustration for iOS concept"><figcaption></figcaption></figure>

Now, our menu is working as intended.



### AddExpenseViewController: UIMenu for buttonTakePhoto

<figure><img src="/gitbook-assets/6.2.three (2).gif" alt="Educational illustration for iOS concept"><figcaption><p><strong>The app so far</strong></p></figcaption></figure>

Now let's handle the actions for `buttonTakePhoto` (with the camera icon). If the user taps the button, it should display two options: "Camera" and "Gallery." If the user selects the "Camera" option, it will open the camera and take a photo; else, if the user selects "Gallery," it will open the image gallery to pick a photo. Finally, the chosen photo will be set as the image inside `buttonTakePhoto`.

Let's open AddExpenseViewController.swift file. and add the following code in it:


```swift
//
//  AddExpenseViewController.swift
//  App6
//
//  Created by Sakib Miazi on 5/18/23.
//

import UIKit

class AddExpenseViewController: UIViewController {
    
    //Codes omitted...
    
    override func viewDidLoad() {
        super.viewDidLoad()
        
       //codes omitted...
        
        //MARK: adding menu to buttonTakePhoto...
        addExpenseScreen.buttonTakePhoto.menu = getMenuImagePicker()
        
        //codes omitted...
    }
    
    //codes omitted...
    
    func getMenuImagePicker() -> UIMenu{
        var menuItems = [
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
        
    }
    
    //MARK: pick Photo using Gallery...
    func pickPhotoFromGallery(){
        
    }
    //codes omitted...

}

```


Here we are writing `getMenuImagePicker() -> UIMenu` method to create a pop-up menu for displaying the options. In the closures, we call two methods, `pickUsingCamera()` and `pickPhotoFromGallery()` to handle the option clicks.

### Modify the buttonTakePhoto in AddExpenseView

Now we need to set the menu as the primary action for `buttonTakePhoto`. Open AddExpenseView.swift and add the following line to the method `setupbuttonTakePhoto()`:

```swift
buttonTakePhoto.showsMenuAsPrimaryAction = true
```

Let's run the app now.

<figure><img src="/gitbook-assets/6.3.one (1).gif" alt="Educational illustration for iOS concept"><figcaption></figcaption></figure>

Our next task is to implement the Gallery and Camera functions.



### Using Gallery: PHPicker

[PHPicker](https://developer.apple.com/documentation/photokit/phpickerviewcontroller) _is a view controller that provides the user interface for choosing assets from the photo library._ We use this view controller to browse the local image assets, select the chosen image(s), and retrieve the image(s). It is a highly configurable and scalable tool and fairly easy to use. We need to import `PhotosUI` library to use the tool.

So, let's open AddExpenseViewController.swift file. We will write codes in `pickPhotoFromGallery()` method. We also need to adopt `PHPickerViewControllerDelegate` protocol using the `extension` keyword. Let's add the following code in AddExpenseViewController.swift file:

<pre class="language-swift" data-line-numbers><code class="lang-swift">//
//  AddExpenseViewController.swift
//  App6
//
//  Created by Sakib Miazi on 5/18/23.
//

import UIKit
<a data-footnote-ref href="#user-content-fn-1">import PhotosUI</a> //MARK: importing the library to use PHPicker...

class AddExpenseViewController: UIViewController {
    //codes omitted...
    
    //MARK: variable to store the picked Image...
    var pickedImage:UIImage?
    
    //Codes omitted...
    
    override func viewDidLoad() {
        super.viewDidLoad()
        
       //codes omitted...
        
        //MARK: adding menu to buttonTakePhoto...
        addExpenseScreen.buttonTakePhoto.menu = getMenuImagePicker()
        
        //codes omitted...
    }
    
    //codes omitted...
    
    func getMenuImagePicker() -> UIMenu{
        var menuItems = [
            UIAction(title: "Camera",handler: {(_) in
                self.pickUsingCamera()
            }),
            UIAction(title: "Gallery",handler: {(_) in
                self.pickPhotoFromGallery()
            })
        ]
        
        return UIMenu(title: "Select source", children: menuItems)
    }
    
    //codes omitted...
    
    //MARK: pick Photo using Gallery...
    func pickPhotoFromGallery(){
        var configuration = PHPickerConfiguration()
        configuration.filter = PHPickerFilter.any(of: [.images])
        configuration.selectionLimit = 1
        
        let photoPicker = PHPickerViewController(configuration: configuration)
        
        photoPicker.delegate = self
        present(photoPicker, animated: true, completion: nil)
    }
    //codes omitted...

}

//MARK: adopting required protocols for PHPicker...
extension AddExpenseViewController:PHPickerViewControllerDelegate{
    func picker(_ picker: PHPickerViewController, didFinishPicking results: [PHPickerResult]) {
        dismiss(animated: true)
        
        print(results)
        
        let itemprovider = results.map(\.itemProvider)
        
        for item in itemprovider{
            if item.canLoadObject(ofClass: UIImage.self){
                item.loadObject(ofClass: UIImage.self, completionHandler: { (image, error) in
                    DispatchQueue.main.async{
                        if let uwImage = image as? UIImage{
                            self.addExpenseScreen.buttonTakePhoto.setImage(
                                uwImage.withRenderingMode(.alwaysOriginal),
                                for: .normal
                            )
                            self.pickedImage = uwImage
                        }
                    }
                })
            }
        }
    }
}
</code></pre>

Here,

* We are importing the library `PhotosUI` using `import` keyword.
* Then, inside the class, we keep a variable `pickedImage` of type `UIImage` to store the picked image.
* **Inside the `pickPhotoFromGallery()` method:**
  * We create a configuration for the picker.
  * We are saying that we want to pick the images from the Gallery. You can modify it to pick Videos, GIFs, etc.
  * We write `configuration.selectionLimit = 1` to say that only one image can be selected from the Gallery. If you have used texting apps like WhatsApp or even Messages, you can see that you can select multiple images together and send them together in a message. PHPicker allows you to build similar functionalities. For our case, we need to select only one image.
  * Then we create the instance of `PHPickerViewController`, `photoPicker`with the configuration we created.
  * Then we set the `photoPicker`'s delegate to `self` to enable this screen to handle the PHPicker.
  * Then we present the `photoPicker` on the screen.
* **Adopting PHPickerViewControllerDelegate protocol:**
  * We must implement `didFinishPicking` method to handle the results. results contain the images we picked using the `photoPicker`.
  *   If you directly print the results, you should see something like the following:

      ```
      [PhotosUI.PHPickerResult(
          itemProvider: <PUPhotosFileProviderItemProvider: 0x600001091290> {
              types = (
                  "public.jpeg"
              )
          }, 
          assetIdentifier: nil, 
          __personIdentifier: nil)
      ]
      ```
  * Notice that it is a file structure. It creates a package of selected images in the 'itemProvider' directory. For example, I selected the "public.jpeg" image from the gallery, and the `photoPicker` sent the image with this package.
  * Now, between line 71 through 85, we iterate through all the images inside the package and **asynchronously (DispatchQueue)** fetch the images and deal with them. Since we have only one image, we set the image to `pickedImage`.
  * You might get confused by seeing:
  * ```swift
    self.addExpenseScreen.buttonTakePhoto.setImage(
        uwImage.withRenderingMode(.alwaysOriginal),
        for: .normal
    )
    ```
  * Here, we are setting the image rendering mode to `alwaysOriginal` for setting the image for `buttonTakePhoto`. We set a specific rendering mode because iOS sets a tint on top of the images inside a button. That would ruin the original image. To remove the tinting effect, we set the rendering mode to `alwaysOriginal`. _Try removing the rendering mode, and see the tinting effect._

Alright! We are done setting up the PHPicker, and now it's time to test the app.

<figure><img src="/gitbook-assets/6.5.one (1).gif" alt="Educational illustration for iOS concept"><figcaption></figcaption></figure>

[^1]: importing required library.



### Using Camera: UIImagePickerController

Now it's time to build the final part of the app: integrating the camera to take a photo.

**Please note: the camera doesn't work in the emulator; you need a physical iOS device to test it. Do not worry; picking images using the camera is not mandatory in this course. This is an example for your future reference.**

So, let's open AddExpenseViewController.swift file. We will write codes in `pickUsingCamera()` method. We also need to adopt `UINavigationControllerDelegate`, and `UIImagePickerControllerDelegate` protocols using the `extension` keyword. Let's add the following code in AddExpenseViewController.swift file:

```swift
//
//  AddExpenseViewController.swift
//  App6
//
//  Created by Sakib Miazi on 5/18/23.
//

//codes omitted...

class AddExpenseViewController: UIViewController {
    //codes omitted...
    
    //MARK: variable to store the picked Image...
    var pickedImage:UIImage?
    
    //Codes omitted...
    
    override func viewDidLoad() {
        super.viewDidLoad()
        
       //codes omitted...
        
        //MARK: adding menu to buttonTakePhoto...
        addExpenseScreen.buttonTakePhoto.menu = getMenuImagePicker()
        
        //codes omitted...
    }
    
    //codes omitted...
    
    func getMenuImagePicker() -> UIMenu{
        var menuItems = [
            UIAction(title: "Camera",handler: {(_) in
                self.pickUsingCamera()
            }),
            UIAction(title: "Gallery",handler: {(_) in
                self.pickPhotoFromGallery()
            })
        ]
        
        return UIMenu(title: "Select source", children: menuItems)
    }
    
    //codes omitted...
    
    //MARK: take Photo using Camera...
    func pickUsingCamera(){
        let cameraController = UIImagePickerController()
        cameraController.sourceType = .camera
        cameraController.allowsEditing = true
        cameraController.delegate = self
        present(cameraController, animated: true)
    }
    //codes omitted...

}

//codes omitted...

//MARK: adopting required protocols for UIImagePicker...
extension AddExpenseViewController: UINavigationControllerDelegate, UIImagePickerControllerDelegate{
    func imagePickerController(_ picker: UIImagePickerController, didFinishPickingMediaWithInfo info: [UIImagePickerController.InfoKey : Any]) {
        picker.dismiss(animated: true)
        
        if let image = info[.editedImage] as? UIImage{
            self.addExpenseScreen.buttonTakePhoto.setImage(
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

Here we can see using a camera is pretty straightforward.

#### Inside pickUsingCamera() method:

* We create an instance of `UIImagePickerController` named `cameraController`.
* Then we set the source type of the controller to the camera. (This controller was also used to pick gallery images; however, Apple deprecated sources other than the camera for this controller).
* Then we allow cropping and editing after the user takes the photo.
* We set the camera delegate to `self` to handle the images after they are picked.
* Then we present the camera.

**Adopting UINavigationControllerDelegate and UIImagePickerControllerDelegate protocol:**

* We must implement the `imagePickerController()` method corresponding to `didFinishPickingMediaWithInfo`.
* First, we must dismiss the picker; otherwise, iOS will not close the camera app.
* Then we unwrap the image we took and edited.
* Finally, we set it to `pickedImage`.

### Changing the privacy settings of the App to allow the app to access the Camera

You need to update the privacy description for Camera Usage in the app 'Info' configurations.

* Click on 'Info' from the left pane.
* Right-click on the empty space
* Select "Add Row."
* Find "Privacy - Camera Usage Description."
* Add "We need to use the camera to take the receipt of the expense." as your justification for the user to access the camera.

<figure><img src="/gitbook-assets/6.6.two (1).gif" alt="Educational illustration for iOS concept"><figcaption></figcaption></figure>

Now let's run the app. I ran the app on my iPad to demonstrate it is working.

[View Resource](https://www.youtube.com/watch?v=FnCsBWWiv0Y)



### Getting the expense back to ViewController

We now need to get the expense back when we press `buttonAdd`. We need to tweak the data model Expense to accommodate the image, right?

### Update Expense data model:

Let's open the Expense.swift file and update the file as the following:

```swift
//
//  Expense.swift
//  App6
//
//  Created by Sakib Miazi on 5/18/23.
//

import Foundation
import UIKit

struct Expense{
    var title: String?
    var amount: Double?
    var type: String?
    var image: UIImage?
    
    init(title: String, amount: Double, type: String, image: UIImage) {
        self.title = title
        self.amount = amount
        self.type = type
        self.image = image
    }
    
}
```

### Update AddExpenseViewController's onAddButtonTapped() method:

We write:

```swift
//MARK: action for tapping buttonAdd..
@objc func onAddButtonTapped(){
    var title:String = ""
    if let titleText = addExpenseScreen.textFieldTitle.text{
        if !titleText.isEmpty{
            title = titleText
        }else{
            //do your thing to alert user...
            return
        }
    }
    
    var amount = 0.0
    if let amountText = addExpenseScreen.textFieldAmount.text{
        if !amountText.isEmpty{
            if let uwAmount = Double(amountText){
                amount = uwAmount
            }else{
                //alert the user that it's not a valid input...
                return
            }
        
            
        }else{
            //do your thing to alert the user...
            return
        }
        
    }
    
    let newExpense = Expense(
                        title: title, 
                        amount: amount, 
                        type: selectedType, 
                        image: pickedImage ?? (UIImage(systemName: "photo"))!
                    )
    delegate.delegateOnAddExpense(expense: newExpense)
    navigationController?.popViewController(animated: true)
}
```

Here, we are creating a new expense with the title, amount, type, and image. The `pickedImage` might be nil since it is Optional. So if it becomes nil (at any point), we send a default system image named "photo" to be safe.

### Update the TableView to display the image in the cell

Open ViewController.swift. We need to update where we are adopting the TableView protocools.

```swift
//MARK: adopting the procols for TableView...
extension ViewController: UITableViewDelegate, UITableViewDataSource{
    //MARK: returns the number of rows in the current section...
    func tableView(_ tableView: UITableView, numberOfRowsInSection section: Int) -> Int {
        return expenses.count
    }
    
    //MARK: populate a cell for the currecnt row...
    func tableView(_ tableView: UITableView, cellForRowAt indexPath: IndexPath) -> UITableViewCell {
        let cell = tableView.dequeueReusableCell(withIdentifier: "expenses", for: indexPath) as! TableViewExpenseCell
        cell.labelTitle.text = expenses[indexPath.row].title
        if let uwAmount = expenses[indexPath.row].amount{
            cell.labelAmount.text = "Cost: $\(uwAmount)"
        }
        if let uwType = expenses[indexPath.row].type{
            cell.labelType.text = "Type: \(uwType)"
        }
        
        //MARK: setting the image of the receipt...
        if let uwImage = expenses[indexPath.row].image{
            cell.imageReceipt.image = uwImage
        }
        
        return cell
    }
    
    //MARK: deal with user interaction with a cell...
    func tableView(_ tableView: UITableView, didSelectRowAt indexPath: IndexPath) {
        print(self.expenses[indexPath.row])
    }


}
```

We unwrap the image, and then set it to `cell.imageReceipt.image`.

Finally, let's run the app!

<figure><img src="/gitbook-assets/6.7.one (1).gif" alt="Educational illustration for iOS concept"><figcaption></figcaption></figure>



### Wrapping Up: a bit of polishing

We will polish the TableView a little bit to make our TableView look like this:

![Educational illustration for iOS concept](</gitbook-assets/Screenshot 2023-05-20 at 5.18.17 PM (2).png>)

Let's make the following changes to the code:

**Removing the separator line:**

Open ViewController.swift file. Put the following line in `viewDidLoad()` method:

<pre class="language-swift"><code class="lang-swift">override func viewDidLoad() {
<strong>    super.viewDidLoad()
</strong>    title = "Expense App"
    
    //MARK: manipulating TableView separator line...
    firstScreen.tableViewExpense.separatorStyle = .none
    
    //Codes omitted...
}
</code></pre>

**Working with shadows:**

Open the TableViewExpenseCell.swift file. Update the code in the method where we initialize the `wrapperCellView` (`setupWrapperCellView()`) :

```swift
func setupWrapperCellView(){
    wrapperCellView = UITableViewCell()
    
    //working with the shadows and colors...
    wrapperCellView.backgroundColor = .white
    wrapperCellView.layer.cornerRadius = 10.0
    wrapperCellView.layer.shadowColor = UIColor.gray.cgColor
    wrapperCellView.layer.shadowOffset = .zero
    wrapperCellView.layer.shadowRadius = 6.0
    wrapperCellView.layer.shadowOpacity = 0.7
    
    
    wrapperCellView.translatesAutoresizingMaskIntoConstraints = false
    self.addSubview(wrapperCellView)
}
```

* By default, a view has a transparent background, hence, `wrapperCellView's` background is transparent too. So, we set it to white.
* Then we set the cell's corner radius to 10.0.
* We want to create a shadow effect. So first, we set the shadow color to gray. (The color has to be a [CGColor](https://stackoverflow.com/a/20140941/2959067)).
* Then we set the offset of the shadow. If you set the offset to `.zero`, it means that there will be no gap between the object (cell) and the shadow.
* Then we set how wide the shadow would be; we set it to 6 points.
* And then, we set the shadow opacity. We set it to .7. Meaning the opacity will be 70%.

**Changing the constraints to make room for the shadows:**

In TableViewExpenseCell.swift file, let's update the constraints for the `wrapperCellView`.

```swift
//MARK: initializing the constraints...
    func initConstraints(){
        NSLayoutConstraint.activate([
            wrapperCellView.topAnchor.constraint(equalTo: self.topAnchor,constant: 10),
            wrapperCellView.leadingAnchor.constraint(equalTo: self.leadingAnchor, constant: 10),
            wrapperCellView.bottomAnchor.constraint(equalTo: self.bottomAnchor, constant: -10),
            wrapperCellView.trailingAnchor.constraint(equalTo: self.trailingAnchor, constant: -10),
            //codes omitted...
            
            wrapperCellView.heightAnchor.constraint(equalToConstant: 104)ft            
        ])
    }
```

Here, we are adding 10 points margins around the Cell wrapper.

**Now, let's run the app again.**

<figure><img src="/gitbook-assets/6.8.one (1).gif" alt="Educational illustration for iOS concept"><figcaption></figcaption></figure>

There we have a 3D effect!



### Reference Code

[Download Project Archive](/gitbook-assets/App6 (2).zip)

---

## Guided Practice Challenges

Before moving on to the next topic, try these low-stakes practice challenges in Xcode. They will build the exact muscle memory you need:

### Challenge 1: Experimentation
**The Scenario:** You've just learned about UIMenu & Image Pickers.
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


### Useful UI Elements

**Estimated effort:** 1-2 hours this topic
**Format:** Asynchronous online
**Prerequisites:** Previous iOS topics


**🎯 Topic Mission:** 
In this module, we will explore **Useful UI Elements** and learn how to integrate it into our iOS applications. Your mission is to understand the mechanics behind this concept and write robust Swift code.


---

## Learning Objectives

By the end of this session, you will be able to:
1. Understand the core concepts of Useful UI Elements.
2. Implement Useful UI Elements in an Xcode project.
3. Apply best practices to ensure clean and maintainable code.

---

## The Story So Far...

We have been progressively building our knowledge of iOS and Swift. In this module, we will expand our toolkit by diving into Useful UI Elements. 
Open your current Xcode project or start a new Playground to follow along with the hands-on material.

---

## Walkthrough: Exploring Useful UI Elements

> 📁 **Target Project** — Follow along by building the mini-app presented in the steps below, or integrate these concepts into your own ongoing projects.

### Hiding Keyboard when tapped outside

When you are building iOS apps, you might have noticed that if you put some texts into TextFields, the emulator/phone keyboard doesn't disappear if you tap outside the keyboard automatically, like this:

<figure><img src="/gitbook-assets/KeyboardNotHiding (1).gif" alt="Educational illustration for iOS concept"><figcaption></figcaption></figure>

Now if we want to hide the keyboard, it is very simple. Inside the ViewController of a Screen, add the following code in `viewDidLoad()` method:

```swift
override func viewDidLoad() {
    super.viewDidLoad()
    
    //MARK: recognizing the taps on the app screen, not the keyboard...
    let tapRecognizer = UITapGestureRecognizer(target: self, action: #selector(hideKeyboardOnTap))
    tapRecognizer.cancelsTouchesInView = false
    view.addGestureRecognizer(tapRecognizer)

}


//MARK: Hide Keyboard...
@objc func hideKeyboardOnTap(){
    //MARK: removing the keyboard from screen...
    view.endEditing(true)
}
```

Here, we create a gesture recognizer that recognizes that the user taps on the app screen. Then we add the recognizer to the view. Then we add the action (`@objc func hideKeyboardOnTap()`) for reacting to that gesture that would hide the keyboard. The end result is:

<figure><img src="/gitbook-assets/KeyboardHiding (1).gif" alt="Educational illustration for iOS concept"><figcaption></figcaption></figure>



A great guide with other tricks can be found here: [https://kaushalelsewhere.medium.com/how-to-dismiss-keyboard-in-a-view-controller-of-ios-3b1bfe973ad1](https://kaushalelsewhere.medium.com/how-to-dismiss-keyboard-in-a-view-controller-of-ios-3b1bfe973ad1)&#x20;



### Slide Up the View to Accommodate the On-screen Keyboard

It is a little complicated, watch the video below to understand the aspects of it:

[View Resource](https://www.youtube.com/watch?v=O4tP7egAV1I)

Source code: [https://github.com/jrasmusson/ios-professional-course/blob/main/Password-Reset/7-Dealing-Keyboards/README.md](https://github.com/jrasmusson/ios-professional-course/blob/main/Password-Reset/7-Dealing-Keyboards/README.md)



### Saving small data when the App is not running (session or other state variables)

We can store any data type in the local storage as long as the App is installed. It means even if the app is not running, small values can be stored in the storage, and the app can access them whenever needed, like from a database. We use `UserDefaults` for that.

We can store key-value pairs using UserDefaults. For each key, the app can store a value. The value can be of many data types, like Bool, Float, Double, Int, String, URL, etc. You can also write more complex types such as arrays, dictionaries, and Date – and even Data values.

The syntax is very simple. You need to instantiate user defaults by writing something like:

```swift
let defaults = UserDefaults.standard
```

### Writing data

You can save data by writing something like:

```swift
let valueToBeSaved = "THIS_IS_THE_API_KEY"
defaults.set(valueToBeSaved, forKey: "apiKey")
```

In the above code, we are saving `valueToBeSaved` String to the local storage with the key "apiKey." The key is important to retrieve the data.

### Reading data

You can read data by accessing something like:

```swift
let apiKeySaved = defaults.object(forKey: "apiKey") as! String?
        
if let apiKey = apiKeySaved{
    //MARK: tasks if there is a key saved
    print("The Saved API Key: \(apiKey)")
}else{
    //MARK: tasks if there is no key saved
    print("No API Key saved at the moment!")
}
```

In the above code, we access the value saved using the key "apiKey."

**Please note,**

* **You should not be saving heavy data using UserDefaults. It is a slow transaction since the data is saved in the local storage, not in the RAM on your device.**
* **You should not use UserDefaults for inter-screen communications.**

**For more details, please read Paul Hudson's explanations here:** [**https://www.hackingwithswift.com/read/12/2/reading-and-writing-basics-userdefaults**](https://www.hackingwithswift.com/read/12/2/reading-and-writing-basics-userdefaults)



### Stack View

We often face a situation where we have more than two UI elements on a single row of the screen; then, it becomes really hard to align them proportionately with spacing using layout constraints. We can use UIStackView to deal with that situations.

For example, our goal is to have something like the following:

<figure><img src="/gitbook-assets/Screenshot 2023-06-08 at 1.05.38 PM (1).png" alt="Educational illustration for iOS concept"><figcaption></figcaption></figure>

There are three buttons, and we want to align them perfectly with each other without working with custom constraints.

### Designing View with UIStackView:

Let's create a new App and name it "StackViewDemo." Create a new file called StackView.swift, and put the following code there:


```swift
//
//  StackView.swift
//  StackViewDemo
//
//  Created by Sakib Miazi on 6/6/23.
//

import UIKit

class StackView: UIView {
    //MARK: UI elements...
    var button1: UIButton!
    var button2: UIButton!
    var button3: UIButton!
    var stack: UIStackView!
    
    override init(frame: CGRect) {
        super.init(frame: frame)
        
        backgroundColor = .white
        
        setupHorizontalStack()
        setupButton1()
        setupButton2()
        setupButton3()
        
        initConstraints()
    }
    
    func setupHorizontalStack(){
        stack = UIStackView()
        stack.axis = .horizontal //the stack grows horizontally...
        //stack.alignment = .center // Useful for vertical stacks. The stack will be centrally aligned
        stack.distribution = .fillProportionally //make spaces in between UI elements proportionately and automatically...
        stack.translatesAutoresizingMaskIntoConstraints = false
        self.addSubview(stack)
    }
    func setupButton1(){
        button1 = UIButton(type: .system)
        button1.setImage(.add, for: .normal)
        button1.setTitle("Button 1", for: .normal)
        //button1.translatesAutoresizingMaskIntoConstraints = false
        stack.addArrangedSubview(button1)
    }
    func setupButton2(){
        button2 = UIButton(type: .infoDark)
        button2.setImage(.checkmark, for: .normal)
        button2.setTitle("Button 1", for: .normal)
        //button2.translatesAutoresizingMaskIntoConstraints = false
        stack.addArrangedSubview(button2)
    }
    func setupButton3(){
        button3 = UIButton(type: .infoDark)
        button3.setImage(.remove, for: .normal)
        button3.setTitle("Button 1", for: .normal)
        //button3.translatesAutoresizingMaskIntoConstraints = false
        stack.addArrangedSubview(button3)
    }
    
    func initConstraints(){
        NSLayoutConstraint.activate([
            stack.topAnchor.constraint(equalTo: self.safeAreaLayoutGuide.topAnchor, constant: 16),
            stack.leadingAnchor.constraint(equalTo: self.safeAreaLayoutGuide.leadingAnchor, constant: 16),
            stack.trailingAnchor.constraint(equalTo: self.safeAreaLayoutGuide.trailingAnchor, constant: -16),
        ])
    }
    
    required init?(coder: NSCoder) {
        fatalError("init(coder:) has not been implemented")
    }
}
```


In the above code, we have three buttons and a stack to hold these three buttons.

* On lines 11 through 15, we declare the buttons and the stack.
* On lines 30 through 37, we define the stack.
  * On line 32, we define the axis of the stack. There are two possible axes: horizontal and vertical. **The horizontal stack grows horizontally from left to right. The vertical stack grows downward, from top to bottom.**
  * Line 33 is commented out but important. If the stack is vertical, you might want to align the UI elements since we will have empty spaces on both sides.
  * Line 34 talks about empty space distribution. I used `filledProportionally`. It means the row is filled with the UI elements while keeping proportional spaces between them. It dynamically adjusts the empty spaces. You do not have to write complex constraints for them.
* On lines 38 through 57, we define three buttons, just as always. **However, the most important thing here is we are not adding the buttons as the sub-view of `self` here. We are adding the buttons as the arranged sub-views of the stack.**
* On lines 60 through 66, we are defining the constraints for the screen. See how easy it is to set up the layout constraints for stacks. **We define the stack view's top, leading, and trailing anchors here.** The stack height is automatically dealt with by the UI elements we added to the stack.

### Patching ViewController

Now, let's load the view we created in the ViewController.swift file.

### Run the App

If we run the app now, we will see:

<figure><img src="/gitbook-assets/24.one (1).gif" alt="Educational illustration for iOS concept"><figcaption></figcaption></figure>

If we change the axis to vertical ( `stack.axis = .vertical` ), the screen will look like:

<figure><img src="/gitbook-assets/24.two (3).gif" alt="Educational illustration for iOS concept"><figcaption></figcaption></figure>



### Embed Navigation Controller from code (Not Storyboard)

So far you have noticed, we embed the Navigation Controller using the Storyboard (refer to [3.1.-navigation-controller.md](../3.-our-first-multi-screen-app/3.1.-navigation-controller.md "mention") ). What about we want to remove that process and want to add Navigation Controller by writing code? That way it'll be easy to change the name of the default "ViewController.swift" file to a more appropriate name.&#x20;

To start, we will create a new iOS project in Xcode named, "NavConFromCode."&#x20;

<figure><img src="/gitbook-assets/Screenshot 2025-10-09 at 1.22.15 PM.png" alt="Educational illustration for iOS concept"><figcaption></figcaption></figure>

We already know that it comes with a default view controller: **ViewController.swift**

So let's first change the name of it to a different name: **FirstScreenViewController.swift**

<figure><img src="/gitbook-assets/sdf.gif" alt="Educational illustration for iOS concept"><figcaption></figcaption></figure>

**Please note, we are also changing the name of the class.**&#x20;

Then just open SceneDelegate.swift file, and update the \
`func scene(_ scene: UIScene, willConnectTo session: UISceneSession, options connectionOptions: UIScene.ConnectionOptions)` function.


```swift
func scene(_ scene: UIScene, willConnectTo session: UISceneSession, options connectionOptions: UIScene.ConnectionOptions) {
            
    guard let windowScene = (scene as? UIWindowScene) else { return }
    
    // Create your root view controller
    let rootViewController = FirstScreenViewController()
    
    // Embed it in a navigation controller
    let navigationController = UINavigationController(
                    rootViewController: rootViewController
            )
    
    // Create and configure the window
    window = UIWindow(windowScene: windowScene)
    window?.rootViewController = navigationController
    window?.makeKeyAndVisible()
}
```


On line 3, we define windowScene as a variable since we want to manipulate the window on the app.

On line 6, we define our root view controller for the navigation stack. (Our first/main screen).

On line 9, we define the navigation controller to be added. And set the root view controller to the main screen.

Then on lines 14 through 16, we setup the window of the app.&#x20;

Now, if we run the app, it should run as the FirstScreenViewController being the main view controller.



### Deleting the Main.storyboard

1. Delete the storyboard file from file explorer.
2. Open project's Info.plist
   1. Select your project in the Project Navigator
   2. Select your app target
   3. Go to the "Info" tab
   4. Expand "Application Scene Manifest"
   5. Expand "Scene Configuration"
   6. Expand "Application Session Role"
   7. Expand "Item 0"
   8. Delete the row: "Storyboard Name" (value: "Main")
   9. Find "Main storyboard file base name" or "Main Interface". Delete the value (set it to empty)

### Resource Files

[Download Project Archive](/gitbook-assets/NavConFromCode.zip)



## Table of Contents

{{< section >}}

---

## Guided Practice Challenges

Before moving on to the next topic, try these low-stakes practice challenges in Xcode. They will build the exact muscle memory you need:

### Challenge 1: Experimentation
**The Scenario:** You've just learned about Useful UI Elements.
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


### 6.-search-bar

**Estimated effort:** 1-2 hours this topic
**Format:** Asynchronous online
**Prerequisites:** Previous iOS topics


**🎯 Topic Mission:** 
In this module, we will explore **this topic** and learn how to integrate it into our iOS applications. Your mission is to understand the mechanics behind this concept and write robust Swift code.


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

### Search Bar

The Search Bar in iOS is a very common UI element, and it is very useful to filter or search data from a list of data. In this module, we will build a demo app with a search bar. The app would look like the following:

<figure><img src="/gitbook-assets/6.one (1).gif" alt="Educational illustration for iOS concept"><figcaption></figcaption></figure>

The app will have the following:

* A list of names.
* A table view to display the names.
* A search bar to filter the names.
  * For example, if the user types something on the search bar and any name contains that text, it will filter out those names containing the text.

So let's create a new app named "SearchBarDemo."




### Setting up the Views

The view of this app is very simple; we have two UI elements on the screen:

* A Search Bar
* A Table View

### MainScreenView.swift

Let's create a file named MainScreenView.swift and put the following code there:


```swift
//
//  MainScreenView.swift
//  SearchBarDemo
//
//  Created by Sakib Miazi on 6/12/23.
//

import UIKit

class MainScreenView: UIView {
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
        tableViewSearchResults.register(SearchTableViewCell.self, forCellReuseIdentifier: Configs.searchTableViewID)
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


In the above code, on lines 19 through 23, we define the search bar. On line 21, we give a placeholder that describes what this Search Bar is about. The rest of the code is trivial, where we define the table view and the constraints.

### SearchTableViewCell.swift

Now we define the view for each cell of the table view. The view for each cell is also very simple. We have one label that displays a name. Let's create a file named SearchTableViewCell.swift and put the following code there:

```swift
//
//  SearchTableViewCell.swift
//  SearchBarDemo
//
//  Created by Sakib Miazi on 6/12/23.
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



### Setting up the View Controller: Handling the Search Bar

Let's open ViewController.swift file and put the following code there:


```swift
//
//  ViewController.swift
//  SearchBarDemo
//
//  Created by Sakib Miazi on 6/12/23.
//

import UIKit

class ViewController: UIViewController {
    
    let mainScreen = MainScreenView()
    
    //MARK: the list of names...
    var namesDatabase = [
        "Marvin Cook","Samira Jimenez","Coral Hancock","Xander Wade","Terence Mcneil",
        "Dewey Buckley","Ophelia Higgins","Asiya Anthony","Francesco Knight",
        "Claude Gonzalez","Demi Decker","Casey Park","Jon Hendrix","Hope Harvey",
        "Richie Alexander","Carmen Proctor","Mercedes Callahan","Yahya Gibbs",
        "Julian Pittman","Shauna Ray"
    ]
    
    //MARK: the array to display the table view...
    var namesForTableView = [String]()
    
    override func loadView() {
        view = mainScreen
    }

    override func viewDidLoad() {
        super.viewDidLoad()
        
        //MARK: sorting the names list...
        namesDatabase.sort()
        
        //MARK: setting up Table View data source and delegate...
        mainScreen.tableViewSearchResults.delegate = self
        mainScreen.tableViewSearchResults.dataSource = self
        
        //MARK: setting up Search Bar delegate...
        mainScreen.searchBar.delegate = self
        
        //MARK: initializing the array for the table view with all the names...
        namesForTableView = namesDatabase
    }
}

//MARK: adopting Table View protocols...
extension ViewController: UITableViewDelegate, UITableViewDataSource{
    func tableView(_ tableView: UITableView, numberOfRowsInSection section: Int) -> Int {
        return namesForTableView.count
    }
    
    func tableView(_ tableView: UITableView, cellForRowAt indexPath: IndexPath) -> UITableViewCell {
        let cell = tableView.dequeueReusableCell(
            withIdentifier: Configs.searchTableViewID, for: indexPath) as! SearchTableViewCell
        
        cell.labelTitle.text = namesForTableView[indexPath.row]
        return cell
    }
    
}

//MARK: adopting the search bar protocol...
extension ViewController: UISearchBarDelegate{
    func searchBar(_ searchBar: UISearchBar, textDidChange searchText: String) {
        
    }
}
```


In the above code:

* On lines 15 through 21, we create the list of names `namesDatabase`, which will be used as the data source for the names.
* On line 24, we define an array `namesForTableView` that we will use to display the TableView.
* On lines 30 through 46, we write the code for `viewDidLoad`.
  * On lines 37 through 38, we set the delegate and data source of the table view.
  * On line 41, we set the search bar's delegate to self.
  * On line 44, we initialize the array for table view with all the names.
* On lines 48 through 62, we adopt the protocols related to the table view delegate and data source as we have been doing so far.
* On lines 65 through 69, we adopt the protocol `UISearchBarDelegate` regarding the search bar's delegate.
  * We have to override the `searchBar()` method regarding `textDidChange` if we want to handle the search bar behaviors while the user is typing on the search bar.
  * **On line 66, the method regarding `textDidChange` gets called when the search bar senses that something is typed on it.**

### Handling when the User is Typing on the Search Bar

Let's put the following code into the method regarding `textDidChange` (in between lines 66 and 68 in the above code):


```swift
//MARK: adopting the search bar protocol...
extension ViewController: UISearchBarDelegate{
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
        self.mainScreen.tableViewSearchResults.reloadData()
    }
}
```


In the above code:

* ,On line 4, we are checking if the user removed the search text. If the searchText is empty, then we load all the names.
* Else, on lines 6 through 14,
  * The user typed something on the search bar.
  * So first, we remove all the names from the array on line 7.
  * Then we search all the names to find if the searchText matches any part of any name we have (lines 9 through 13). We append the matched names in the array for the table view.
  * Then on line 15, we reload the table view data to display the search result.

Let's run the app again:

<figure><img src="/gitbook-assets/6.six (1).gif" alt="Educational illustration for iOS concept"><figcaption></figcaption></figure>

Yay! Our simple search bar is working!



### Reference Code

[Download Project Archive](/gitbook-assets/SearchBarDemo (1).zip)

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


### 5.-tab-bar-controller

**Estimated effort:** 1-2 hours this topic
**Format:** Asynchronous online
**Prerequisites:** Previous iOS topics


**🎯 Topic Mission:** 
In this module, we will explore **this topic** and learn how to integrate it into our iOS applications. Your mission is to understand the mechanics behind this concept and write robust Swift code.


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

### Tab Bar Controller

We often see apps with bottom navigation bars, where you can tap on an icon from the bottom bar, and the app loads different screens for different buttons pressed like the following:

<figure><img src="/gitbook-assets/5.one (1).gif" alt="Educational illustration for iOS concept"><figcaption></figcaption></figure>

iOS gives us an easy-to-use and customizable tool called UITabBarController to build such screens. In this module, we will create an app that uses a Tab Bar.

### The TabControllerDemo app

Let's create an app called TabControllerDemo in XCode. The app will have:

* A bottom Tab Bar having three Tab Bar buttons: red, green, and blue.
* Tapping the "red" button opens the Red Screen.
* Tapping the "blue" button opens the Blue Screen.
* Tapping the "green" button opens the Green Screen.
* Each screen has
  * A color box displaying the corresponding color.
  * A button to send data to other screens.
  * A label to display the received data from other screens.




### Views of the Screens

### Views

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



### Controllers of the Screens

For each different screen (red, blue, and green), we need to have different Controllers. Let's create three controller files.

### RedViewController.swift

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

### BlueViewController.swift

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

### GreenViewController.swift

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



### Patching the Screens in the Tab Bar

We have three screens. Now we want to patch these three screens in a Tab Bar Controller. Now it's time to use our main ViewController.swift file.

Let's look into the logical structure of a Tab Bar:

<figure><img src="/gitbook-assets/Screenshot 2023-06-12 at 12.41.40 PM (1).png" alt="Educational illustration for iOS concept"><figcaption></figcaption></figure>

* The Tab Bar is the UI component that displays the bottom tabs.
* So it needs a controller to control the UI. In our case, we will use the main ViewController as the Tab Bar Controller.
* The Tab Bar contains the bar items. In our case, we will use three bar items: red, green, and blue.
  * Each bar item represents a screen; for example, the red item represents the Red Screen.
  * **Since each screen is independent of other tab bar screens, they should also have their own Navigation Controllers. (Do you remember that we have been embedding Navigation Controllers through the Storyboards? We can also do that by writing codes)**
  * For each screen, we define its Navigation Controller, then embed it in the corresponding view controller.
  * We have already patched the screen views to their view controllers.

### Setting up the Tab Bar: ViewController.swift

Let's open the ViewController.swift file and put the following code there:


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

<figure><img src="/gitbook-assets/5.two (1).gif" alt="Educational illustration for iOS concept"><figcaption></figcaption></figure>



### Sending data From one Tab to Another

We will use Notification Center to send data between the tabs. If the user taps on the "Send Hello" button from the Red Screen, it will send all the other tabs a message, "Hello From Red Screen." The other screens will display the message on the labels.

We now have to write code in the view controllers to enable this feature. Let's open RedViewController.swift file and write the following code:


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

<figure><img src="/gitbook-assets/5.four (1).gif" alt="Educational illustration for iOS concept"><figcaption></figcaption></figure>



### Reference Code

[Download Project Archive](/gitbook-assets/TabControllerDemo.zip)



### Notes for Tab Bar Controller

* **Tab Bar Controller is a powerful tool.**
* **Each tab has its own Navigation Controller. So, you can build a separate tree of screens for each tab with its navigation.**
* **So, each tab can potentially work like a separate multiscreen app module.**
* **You can play around with the UI style elements of the tab bar items to design them as you like.**

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


### bottom-sheet-view-modal-presentation

**Estimated effort:** 1-2 hours this topic
**Format:** Asynchronous online
**Prerequisites:** Previous iOS topics


**🎯 Topic Mission:** 
In this module, we will explore **this topic** and learn how to integrate it into our iOS applications. Your mission is to understand the mechanics behind this concept and write robust Swift code.


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

### Bottom Sheet View: Modal Presentation

You probably have seen apps where you tap a button, and a page sheet pops up from the bottom. You can then interact with that page sheet and work with the app. We can use Swift's SheetPresentationController for building the bottom sheet views.&#x20;

In this short module, we will build the following app:

<figure><img src="/gitbook-assets/7.sixty (1).gif" alt="Educational illustration for iOS concept"><figcaption></figcaption></figure>

Basically, we build this app on top of the app in the [6.-search-bar](../6.-search-bar/ "mention") module. We will implement SearchBar on a bottom sheet view.

We have a Find button on our main screen and a label to display the selected name. If the user taps on the Find button, the app should present the bottom search sheet. The user searches for a name on the bottom search sheet and selects a name. Then, we need to dismiss the bottom sheet and set the text of the label to the selected name.




### Creating the Screen for a Bottom Sheet View

**When building a bottom sheet (presentation) view, we must remember that the page we will present as a bottom sheet is a full and independent screen. It should have its own:**

* **View Controller**
* **Navigation Controller**

&#x20;So, let's design a separate screen for our search bottom sheet. Let's create the following three Swift files:

* SearchBottomSheetController.swift
* SearchBottomSheetView.swift
* SearchTableCell.swift

![Educational illustration for iOS concept](</gitbook-assets/Screenshot 2023-06-13 at 1.12.04 PM.png>)

Let's design the view first.

### Search Bottom Sheet View

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

### Search Table Cell

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



### Setting up the Controller for the Search Bottom Sheet

Let's open SearchBottomSheetController.swift file. We will mostly use the same code here as [6.-search-bar](../6.-search-bar/ "mention"). We would add a few more logic to handle a tap on a row and send data back to the main screen.&#x20;

Let's write the code for setting up the table view and the search bar. Let's open SearchBottomSheetController.swift file, and put the following code there:


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




### Main Screen

The main screen is very simple to design; we have:

* A label to display the selected name from the bottom search sheet.
* A Find button to pop the bottom search sheet.

### Main Screen View

Let's create a file named MainScreenView.swift:

![Educational illustration for iOS concept](</gitbook-assets/Screenshot 2023-06-13 at 1.35.29 PM.png>)

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

### Main Screen Controller

Now it's time to patch the actions to pop the bottom search sheet from the view controller. Let's put the following code in ViewController.swift:


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

<figure><img src="/gitbook-assets/7.sixtytwo.gif" alt="Educational illustration for iOS concept"><figcaption><p><strong>Detents</strong></p></figcaption></figure>

* On line 35, we display the grabber.

![Educational illustration for iOS concept](</gitbook-assets/Screenshot 2023-06-13 at 5.00.01 PM.png>)



Now, our app is almost ready. We just need to return the name to main screen when the user taps a name from the bottom search sheet's table view.



### Sending data back to Main Screen

We will use Notification Center to do that.&#x20;

* **We will observe any notifications coming from the bottom search sheet if the user selects any of the names in the main screen's ViewController.**
* **We will post notifications from SearchBottomSheetController when the user selects a table view row.**&#x20;

Let's open ViewController.swift file, and update the file with the following code:


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


In the above code:

* On line 13, we are initializing the Notification Center.
* On line 22, we set the observer for the notification.
* From lines 27 through 38 we are observing for a notification `.nameSelected`. We create a separate file to store the names of the Notifications just like [7.-notification-center](../../7.-notification-center/ "mention").&#x20;
* On line 34, the `onNameSelected()` method gets triggered when the notification is received.&#x20;
  * On line 36, we set the name with the data we receive through the notification.

### Table View in Bottom Search Sheet Controller: overriding didSelectRowAt

Let's open SearchBottomSheetController.swift file and add the following method inside the extension where we are adopting the table view protocols:


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


In the above code:

* We are waiting for the user to tap on a table view cell.&#x20;
* On line 7, we post the selected name to the notification center.
* On line 10, we remove the bottom search sheet by calling dismiss.

Let's run the app.

<figure><img src="/gitbook-assets/seven.5.gif" alt="Educational illustration for iOS concept"><figcaption></figcaption></figure>

**Nice! We built our first Bottom Sheet View!**



### Reference Code

[Download Project Archive](/gitbook-assets/BottomSheetView.zip)

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
