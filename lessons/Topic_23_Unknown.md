# Unknown


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

# 6. Search Bar

The Search Bar in iOS is a very common UI element, and it is very useful to filter or search data from a list of data. In this module, we will build a demo app with a search bar. The app would look like the following:

<figure><img src="/gitbook-assets/6.one (1).gif" alt=""><figcaption></figcaption></figure>

The app will have the following:

* A list of names.
* A table view to display the names.
* A search bar to filter the names.
  * For example, if the user types something on the search bar and any name contains that text, it will filter out those names containing the text.

So let's create a new app named "SearchBarDemo."




<!-- Merged from 6.1.-setting-up-the-views.md -->

# 6.1. Setting up the Views

The view of this app is very simple; we have two UI elements on the screen:

* A Search Bar
* A Table View

## MainScreenView.swift

Let's create a file named MainScreenView.swift and put the following code there:

{% code lineNumbers="true" %}
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
{% endcode %}

In the above code, on lines 19 through 23, we define the search bar. On line 21, we give a placeholder that describes what this Search Bar is about. The rest of the code is trivial, where we define the table view and the constraints.

## SearchTableViewCell.swift

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



<!-- Merged from 6.2.-setting-up-the-view-controller-handling-the-search-bar.md -->

# 6.2. Setting up the View Controller: Handling the Search Bar

Let's open ViewController.swift file and put the following code there:

{% code lineNumbers="true" %}
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
{% endcode %}

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

{% code lineNumbers="true" %}
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
{% endcode %}

In the above code:

* ,On line 4, we are checking if the user removed the search text. If the searchText is empty, then we load all the names.
* Else, on lines 6 through 14,
  * The user typed something on the search bar.
  * So first, we remove all the names from the array on line 7.
  * Then we search all the names to find if the searchText matches any part of any name we have (lines 9 through 13). We append the matched names in the array for the table view.
  * Then on line 15, we reload the table view data to display the search result.

Let's run the app again:

<figure><img src="/gitbook-assets/6.six (1).gif" alt=""><figcaption></figcaption></figure>

Yay! Our simple search bar is working!



<!-- Merged from 6.3.-reference-code.md -->

# 6.3. Reference Code

{% file src="/gitbook-assets/SearchBarDemo (1).zip" %}

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

