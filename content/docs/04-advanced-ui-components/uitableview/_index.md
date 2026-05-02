---
title: "UITableView"
weight: 10
---

# 5. UITableView, and more

So far, we have worked with multiple screens and NavigationController. Now, we will learn how to display a list of data and work with some other UI elements.

More specifically, we will learn about the following:

* UITableView to display a list of data.
* A few more key concepts like static variables and handling Double inputs.




<!-- Merged from 5.1.-expense-app.md -->

# 5.1. Expense App

So, let's create an app called 'App5'. Our preliminary target is to build something like the following app:

![](</gitbook-assets/Screenshot 2023-05-18 at 10.45.04 AM (1).png>) ![](</gitbook-assets/Screenshot 2023-05-18 at 10.45.19 AM (1).png>)

The first screen contains a list of expenses. The user can add a new expense by tapping on the plus icon (`+`) on the navigation bar. If a user taps on `+` icon, it takes them to the next screen where they can put the details of the expense.

![](</gitbook-assets/Screenshot 2023-05-18 at 10.56.57 AM (1).png>) ![](</gitbook-assets/Screenshot 2023-05-18 at 10.45.48 AM (1).png>)

Once the user puts in the details and taps the Add Expense button, it should return to the first screen and show the newly added expense.

Now let's build the app.



<!-- Merged from 5.2.-first-screen-part-1-adding-a-bar-button.md -->

# 5.2. First screen, part 1: Adding a Bar Button

Let's create a new project, 'App5' in Xcode.

<figure><img src="/gitbook-assets/Screenshot 2023-05-18 at 10.45.04 AM (1).png" alt="" width="343"><figcaption><p>App 5: First screen</p></figcaption></figure>

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

<figure><img src="/gitbook-assets/one (1) (1).gif" alt=""><figcaption></figcaption></figure>

Now we will set up the TableView and then return to this button.



<!-- Merged from 5.3.-first-screen-part-2-setting-up-the-view-of-the-first-screen-with-tableview..md -->

# 5.3. First screen, part 2: Setting up the View of the First Screen with TableView.

We have to build our first TableView here in this app. Before we build one, we need to understand what it is.

### What is a TableView?

According to [Apple developer documentation](https://developer.apple.com/documentation/uikit/uitableview): _Table views in iOS display rows of vertically scrolling content in a single column. Each row in the table contains one piece of your app’s content. For example, the Contacts app displays the name of each contact in a separate row, and the main page of the Settings app displays the available groups of settings. You can configure a table to display a single long list of rows, or you can group related rows into sections to make navigating the content easier._

A good example of a TableView is the Settings app on our iPhones or iPads.

<figure><img src="/gitbook-assets/two (2) (1).gif" alt=""><figcaption><p>Settings app</p></figcaption></figure>

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

![](</gitbook-assets/Screenshot 2023-05-18 at 12.12.41 PM (1).png>)

So we can see that there are three Labels there, displaying:

* The title of the expense.
* The amount the user spent.
* And the type of expense.

So, we need to design our TableView row. **The view of the row is called a cell**. We need to create a new Swift file to design the cell.

**File -> New -> File... -> Cocoa Touch Class -> Next ->**

Give the file's name as "TableViewExpenseCell" and set the file as the 'Subclass of' UITableViewCell. Then click **Next. And then click Create.**

<figure><img src="/gitbook-assets/three (1) (1).gif" alt=""><figcaption><p>Creating a Cell's View</p></figcaption></figure>

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



<!-- Merged from 5.4.-first-screen-part-3-setting-up-the-view-controller-and-populating-tableview.md -->

# 5.4. First screen, part 3: Setting up the View Controller and populating TableView

Now we must patch the views with our controller (ViewController.swift). Before we do, let's create a data model for the data we will display in the TableView `tableViewExpense`. We have three data points for displaying a row in the table view: expense title, amount, and type.

### Creating a data model for expenses

So, let's create a new swift file called "Expense."

* **File -> New -> File...**
* Select **iOS**
* **Select Swift file (not Cocoa Touch Class).**
* **Next**
* Name it as **"Expense."**
* Click **Create.**

<figure><img src="/gitbook-assets/four (1) (1).gif" alt=""><figcaption></figcaption></figure>

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

## Setting up the Controller

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

<figure><img src="/gitbook-assets/six (2).gif" alt=""><figcaption></figcaption></figure>

Our Table View is up and running now, displaying our dummy data!

### File structures

Since we are almost done with our first screen, let's create groups of files and put them in separate folders to structure them better.

<figure><img src="/gitbook-assets/seven (2).gif" alt=""><figcaption></figcaption></figure>

The file structure looks like this:

![](</gitbook-assets/Screenshot 2023-05-18 at 3.01.03 PM (1).png>)



<!-- Merged from 5.5.-second-screen-part-1-setting-up-the-view-of-the-add-expense-screen.md -->

# 5.5. Second screen, part 1: Setting up the View of the Add Expense Screen

When the user clicks the plus Bar button (`+`), we should populate a screen to add a new expense. So, let's create two new files: AddExpenseView.swift (subclass of UIView) and AddExpenseViewController.swift (subclass of UIViewController). And add them to a new group, "Add Expense Screen." (**Use the Cocoa Touch Class template, not a Swift file template).**

<figure><img src="/gitbook-assets/5.ten (1).gif" alt=""><figcaption></figcaption></figure>

### Setting up the View

![](</gitbook-assets/Screenshot 2023-05-18 at 10.45.19 AM (1).png>)

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



<!-- Merged from 5.6.-second-screen-part-2-setting-up-add-expense-view-controller.md -->

# 5.6. Second screen, part 2: Setting up Add Expense View Controller

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

## **Patching the PickerView to pick the type of expense**

Now, let's patch the PickerView (`addExpenseScreen.pickerType`) to the controller.

We will pick the type of expense using this PickerView. We know that we added an array of four expense types in ViewController.swift. Since we need to use the same array instead of writing the array again, we can define a static array to be shared with all the classes in the project. The keyword `static` makes it persistent in the memory while the app is running. **Do not make all the data static; you can keep it static if it is small shared data.**

### Defining static array 'types'

Let's create a new Swift file named "Utilities.swift" in the project.

<figure><img src="/gitbook-assets/5.6.1.one (1).gif" alt=""><figcaption></figcaption></figure>

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

## Housekeeping: Updating Navigation controller and patching Utilities.types in View Controller

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

<figure><img src="/gitbook-assets/5.6.1.two (1).gif" alt=""><figcaption></figcaption></figure>

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



<!-- Merged from 5.7.-second-screen-part-3-send-new-expense-back-to-viewcontroller-and-update-the-tableview.md -->

# 5.7. Second screen, part 3: Send new expense back to ViewController and update the TableView

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

<figure><img src="/gitbook-assets/5.6.1.three (1).gif" alt=""><figcaption></figcaption></figure>

One last thing to discuss before we finish this module. We can also deal with when a user clicks on a cell in the TableView.



<!-- Merged from 5.8.-tapping-a-cell-in-tableview-and-practice-exercise.md -->

# 5.8. Tapping a cell in TableView and Practice exercise

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

<figure><img src="/gitbook-assets/5.6.1.four (1).gif" alt=""><figcaption></figcaption></figure>

Now, you can see that you can handle it if a user taps on a cell. It's time for exercise.

### Exercise

**Now your task is to build a third screen, "DisplayExpense," to show the details of an expense if a user taps on it. It could be just three Labels to display the title, amount, and type of the selected expense.**



<!-- Merged from 5.9.-reference-code.md -->

# 5.9. Reference Code

{% file src="/gitbook-assets/App5 (1).zip" %}

