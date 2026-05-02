---
title: "UIMenu & Image Pickers"
weight: 30
---

# 6. UIMenu, Picking Images from Gallery and Camera, and UIImageView

## App6: Adding more features on App5

Let's create a new project, "App6." Add all the codes from the current "App5." For your convenience, download the project from here:

{% file src="/gitbook-assets/App6_initial (1).zip" %}

Our goal here is to:

* Learn to use UIMenu instead of PickerView.
* Add an ImageView to the TableView Cell to display the expense receipt.
* Add options to take a photo of the receipt using the camera or gallery.

App6 would look something like this:

<figure><img src="/gitbook-assets/6.1.one.gif" alt=""><figcaption></figcaption></figure>




<!-- Merged from 6.1.-updating-the-tableview-cell-to-accommodate-an-imageview.md -->

# 6.1. Updating the TableView Cell to accommodate an ImageView

Let's open TableViewExpenseCell.swift file to add an ImageView. Let's add a new variable named, `imageViewReceipt` of type `UIImageView` in the file, set it up, and initialize its constraints. Add the following code to TableViewExpenseCell.swift file:

{% code lineNumbers="true" %}
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
{% endcode %}

In the above code, we have a few very important key points to discuss:

**Defining the ImageView `imageReceipt`:**

* Let's look into the method where we define the new `imageReceipt` ImageView (`setupimageReceipt()`). We wrote: `imageReceipt.image = UIImage(systemName: "photo")`. We are trying to set a default image for the ImageView. For the default image, we select an iOS system image named "photo" (<img src="/gitbook-assets/photo@2x (1).png" alt="" data-size="line">). Xcode ships with these system images. But we need to know the names of those images. Fortunately, we can easily find the names of the system images. You need to install an Apple developer app called "SF Symbols" on your Mac. [Download, install, and learn how to use the app.](6.1.-updating-the-tableview-cell-to-accommodate-an-imageview.md#installing-and-using-sf-symbols-app)
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

## Appendix

### Installing and using SF Symbols app

* Download the SF Symbols app from here: [https://developer.apple.com/sf-symbols/](https://developer.apple.com/sf-symbols/)

<figure><img src="/gitbook-assets/6.1.two (1).gif" alt=""><figcaption></figcaption></figure>

* Open the .DMG file
* Then Install the .pkg file by double-clicking on it:

<figure><img src="/gitbook-assets/6.1.four.gif" alt=""><figcaption></figcaption></figure>

*   Let's open the app. Press `Command` + `Space` to open the spotlight search. Then look for SF Symbols and press `return` to open it. \\

    <figure><img src="/gitbook-assets/5.6.1.five (1).gif" alt=""><figcaption></figcaption></figure>
*   Now we can use the app to find the appropriate iOS system icon/symbol for us and fetch the name of it. Here I am finding the name for the icon I will use:\\

    <figure><img src="/gitbook-assets/5.6.1.six (1).gif" alt=""><figcaption></figcaption></figure>



<!-- Merged from 6.2.-add-expense-screen.md -->

# 6.2. Add Expense Screen

The screen would be something like this:

![](</gitbook-assets/Screenshot 2023-05-19 at 12.47.14 AM.png>)

We have:

* Two TextFields
* One Button to choose the type of expense
* One Button (use the Camera icon as the background) to pick the image for receipt.
* FInally, the Add Expense Button.

## AddExpenseView

Let's open the AddExpenseView.swift file and update the code. Remove the PickerView and add two buttons (to select expense type and pick receipt image).

Let's see the updated code in the following:

{% code lineNumbers="true" %}
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
{% endcode %}

### Setting up the Buttons

#### buttonSelectType:

Let's look into the setup method for `buttonSelectType`:

{% code lineNumbers="true" %}
```swift
func setupbuttonSelectType(){
    buttonSelectType = UIButton(type: .system)
    buttonSelectType.setTitle("Select the type of expense:", for: .normal)
    buttonSelectType.translatesAutoresizingMaskIntoConstraints = false
    self.addSubview(buttonSelectType)
}
```
{% endcode %}

It looks pretty straight forward now. At some point, we need to tweak the setup a little.

#### buttonTakePhoto:

Let's look into the setup method:

{% code lineNumbers="true" %}
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
{% endcode %}

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



<!-- Merged from 6.3.-addexpenseviewcontroller-uimenu-for-buttonselecttype.md -->

# 6.3. AddExpenseViewController: UIMenu for buttonSelectType

Now, it's time to remove the PickerView codes. After we remove the PickerView, the code looks like this:

{% code lineNumbers="true" %}
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
{% endcode %}

Now if you run the app, it will look like the following:

<figure><img src="/gitbook-assets/6.2.one (1).gif" alt=""><figcaption></figcaption></figure>

So now, let's add the actions for the newly added buttons, `buttonSelectType` and `buttonTakePhoto`.

### UIMenu for buttonSelectType

When the user taps on `buttonSelectType`, it should display a pop-up menu with four options. Let's add the code for it. In AddExpenseViewController.swift add:

{% code lineNumbers="true" %}
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
{% endcode %}

We write `addExpenseScreen.buttonSelectType.menu` to set the menu. We write a method `getMenuTypes() -> UIMenu` to generate the menu. Let's look into the method.

We create an array of UIMenu items (four in our case). Each UIMenu item is a UIAction with the title of the menu item and the [closure](https://github.com/sakibnm/iOS/blob/main/7.-closures) for defining the tasks we should do if we select that item from the menu. For example, in each iteration of the loop:

{% code lineNumbers="true" %}
```swift
for type in Utilities.types{
    let menuItem = UIAction(title: type,handler: {(_) in
                self.selectedType = type
                self.addExpenseScreen.buttonSelectType.setTitle(self.selectedType, for: .normal)
            })
    menuItems.append(menuItem)
}
```
{% endcode %}

Here, we are creating a menu item using the `Utilities.types` array. The `handler` closure defines the on-select actions for that item. We are saying that if the user selects this particular menu item, set the value of `selectedType` to the corresponding type of expense. And set the title of the button to the selected item.

So, let's run the app now.

<figure><img src="/gitbook-assets/6.2.two (1).gif" alt=""><figcaption></figcaption></figure>

See, if we long tap on `buttonSelectType` then a menu pops up, and we can select a type of expense. But we want this menu to pop up when we do regular tap. By default, the menu pop-up is not set as the primary action of a Button. We have to set it as an attribute of the Button when we initialize it. So let's go to AddExpenseView.swift and edit the `setupbuttonSelectType()` method:

{% code lineNumbers="true" %}
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
{% endcode %}

Now let's run the app again:

<figure><img src="/gitbook-assets/6.2.three (1) (1).gif" alt=""><figcaption></figcaption></figure>

Now, our menu is working as intended.



<!-- Merged from 6.4.-addexpenseviewcontroller-uimenu-for-buttontakephoto.md -->

# 6.4. AddExpenseViewController: UIMenu for buttonTakePhoto

<figure><img src="/gitbook-assets/6.2.three (2).gif" alt=""><figcaption><p><strong>The app so far</strong></p></figcaption></figure>

Now let's handle the actions for `buttonTakePhoto` (with the camera icon). If the user taps the button, it should display two options: "Camera" and "Gallery." If the user selects the "Camera" option, it will open the camera and take a photo; else, if the user selects "Gallery," it will open the image gallery to pick a photo. Finally, the chosen photo will be set as the image inside `buttonTakePhoto`.

Let's open AddExpenseViewController.swift file. and add the following code in it:

{% code lineNumbers="true" %}
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
{% endcode %}

Here we are writing `getMenuImagePicker() -> UIMenu` method to create a pop-up menu for displaying the options. In the closures, we call two methods, `pickUsingCamera()` and `pickPhotoFromGallery()` to handle the option clicks.

### Modify the buttonTakePhoto in AddExpenseView

Now we need to set the menu as the primary action for `buttonTakePhoto`. Open AddExpenseView.swift and add the following line to the method `setupbuttonTakePhoto()`:

```swift
buttonTakePhoto.showsMenuAsPrimaryAction = true
```

Let's run the app now.

<figure><img src="/gitbook-assets/6.3.one (1).gif" alt=""><figcaption></figcaption></figure>

Our next task is to implement the Gallery and Camera functions.



<!-- Merged from 6.5.-using-gallery-phpicker.md -->

# 6.5. Using Gallery: PHPicker

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

<figure><img src="/gitbook-assets/6.5.one (1).gif" alt=""><figcaption></figcaption></figure>

[^1]: importing required library.



<!-- Merged from 6.6.-using-camera-uiimagepickercontroller.md -->

# 6.6. Using Camera: UIImagePickerController

Now it's time to build the final part of the app: integrating the camera to take a photo.

<mark style="color:red;">**Please note: the camera doesn't work in the emulator; you need a physical iOS device to test it. Do not worry; picking images using the camera is not mandatory in this course. This is an example for your future reference.**</mark>

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

<figure><img src="/gitbook-assets/6.6.two (1).gif" alt=""><figcaption></figcaption></figure>

Now let's run the app. I ran the app on my iPad to demonstrate it is working.

{% embed url="https://www.youtube.com/watch?v=FnCsBWWiv0Y" %}



<!-- Merged from 6.7.-getting-the-expense-back-to-viewcontroller.md -->

# 6.7. Getting the expense back to ViewController

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

<figure><img src="/gitbook-assets/6.7.one (1).gif" alt=""><figcaption></figcaption></figure>



<!-- Merged from 6.8.-wrapping-up-a-bit-of-polishing.md -->

# 6.8. Wrapping Up: a bit of polishing

We will polish the TableView a little bit to make our TableView look like this:

![](</gitbook-assets/Screenshot 2023-05-20 at 5.18.17 PM (2).png>)

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

<figure><img src="/gitbook-assets/6.8.one (1).gif" alt=""><figcaption></figcaption></figure>

There we have a 3D effect!



<!-- Merged from 6.9.-reference-code.md -->

# 6.9. Reference Code

{% file src="/gitbook-assets/App6 (2).zip" %}

