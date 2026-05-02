---
title: "Firebase Storage"
weight: 30
---

**Estimated effort:** 1-2 hours this topic
**Format:** Asynchronous online
**Prerequisites:** Previous iOS topics

{< hint info >}
**🎯 Topic Mission:** 
In this module, we will explore **Firebase Storage** and learn how to integrate it into our iOS applications. Your mission is to understand the mechanics behind this concept and write robust Swift code.
{< /hint >}

---

## Learning Objectives

By the end of this session, you will be able to:
1. Understand the core concepts of Firebase Storage.
2. Implement Firebase Storage in an Xcode project.
3. Apply best practices to ensure clean and maintainable code.

---

## The Story So Far...

We have been progressively building our knowledge of iOS and Swift. In this module, we will expand our toolkit by diving into Firebase Storage. 
Open your current Xcode project or start a new Playground to follow along with the hands-on material.

---

## Walkthrough: Exploring Firebase Storage

> 📁 **Target Project** — Follow along by building the mini-app presented in the steps below, or integrate these concepts into your own ongoing projects.

# 13. Firebase Storage

In this module, we will extend App12 to store images in FIrebase storage. Please review [https://github.com/sakibnm/iOS/blob/main/12.-firebase-authentication-and-firestore](https://github.com/sakibnm/iOS/blob/main/12.-firebase-authentication-and-firestore "mention") section to set up your Firebase Storage service in your Firebase services.

## App 12 extended for storage

We will extend App 12 to store images in Firestore Storage. We will do the following:

* In the Register Screen, we will have the option to pick a profile photo.
* Once we create the profile, we have to store the profile photo in Firebase Storage.
* Then, when we are on the main screen, we should see the profile photo loaded on the Screen. Like the following:

<figure><img src="/gitbook-assets/13.one (1).gif" alt=""><figcaption></figcaption></figure>




<!-- Merged from 13.1.-integrating-photo-pickers.md -->

# 13.1. Integrating Photo Pickers

## Updating RegisterView.swift

Let's open App 12

We need to update the Register Screen's view to accommodate the profile photo. Let's open the `Register Screen -> RegisterView.swift` file. Let's add a couple of UI elements to the view:

* labelPhoto
* buttonTakePhoto

And then update the constraints to accommodate the new elements on the screen.

{% code lineNumbers="true" %}
```swift
//
//  RegisterView.swift
//  App12
//
//  Created by Sakib Miazi on 6/2/23.
//

import UIKit

class RegisterView: UIView {
    //codes omitted...
    var labelPhoto:UILabel!
    var buttonTakePhoto: UIButton!
    
    //codes omitted...
    
    override init(frame: CGRect){
        super.init(frame: frame)
        self.backgroundColor = .white
        //codes omitted...
        
        setuplabelPhoto()
        setupbuttonTakePhoto()
        
        //codes omitted...
        
        initConstraints()
    }
    
    //codes omitted...
    
    func setuplabelPhoto(){
        labelPhoto = UILabel()
        labelPhoto.text = "Add Profile Photo"
        labelPhoto.font = UIFont.boldSystemFont(ofSize: 14)
        labelPhoto.translatesAutoresizingMaskIntoConstraints = false
        self.addSubview(labelPhoto)
    }
    
    func setupbuttonTakePhoto(){
        buttonTakePhoto = UIButton(type: .system)
        buttonTakePhoto.setTitle("", for: .normal)
        buttonTakePhoto.setImage(UIImage(systemName: "camera.fill")?.withRenderingMode(.alwaysOriginal), for: .normal)
        //buttonTakePhoto.setImage(UIImage(systemName: "camera.fill")?.withRenderingMode(.alwaysOriginal), for: .normal)
        buttonTakePhoto.contentHorizontalAlignment = .fill
        buttonTakePhoto.contentVerticalAlignment = .fill
        buttonTakePhoto.imageView?.contentMode = .scaleAspectFit
        buttonTakePhoto.showsMenuAsPrimaryAction = true
        buttonTakePhoto.translatesAutoresizingMaskIntoConstraints = false
        self.addSubview(buttonTakePhoto)
    }
    
    //codes omitted...
    
    func initConstraints(){
        NSLayoutConstraint.activate([
            textFieldName.topAnchor.constraint(equalTo: self.safeAreaLayoutGuide.topAnchor, constant: 32),
            textFieldName.centerXAnchor.constraint(equalTo: self.safeAreaLayoutGuide.centerXAnchor),
            textFieldName.widthAnchor.constraint(equalTo: self.safeAreaLayoutGuide.widthAnchor, multiplier: 0.9),
            
            textFieldEmail.topAnchor.constraint(equalTo: textFieldName.bottomAnchor, constant: 16),
            textFieldEmail.centerXAnchor.constraint(equalTo: self.safeAreaLayoutGuide.centerXAnchor),
            textFieldEmail.widthAnchor.constraint(equalTo: self.safeAreaLayoutGuide.widthAnchor, multiplier: 0.9),
            
            textFieldPassword.topAnchor.constraint(equalTo: textFieldEmail.bottomAnchor, constant: 16),
            textFieldPassword.centerXAnchor.constraint(equalTo: self.safeAreaLayoutGuide.centerXAnchor),
            textFieldPassword.widthAnchor.constraint(equalTo: self.safeAreaLayoutGuide.widthAnchor, multiplier: 0.9),
            
            buttonTakePhoto.topAnchor.constraint(equalTo: textFieldPassword.bottomAnchor, constant: 16),
            buttonTakePhoto.centerXAnchor.constraint(equalTo: self.safeAreaLayoutGuide.centerXAnchor),
            //MARK: setting buttonTakePhoto's height and width..
            buttonTakePhoto.widthAnchor.constraint(equalToConstant: 100),
            buttonTakePhoto.heightAnchor.constraint(equalToConstant: 100),
            
            labelPhoto.topAnchor.constraint(equalTo: buttonTakePhoto.bottomAnchor),
            labelPhoto.centerXAnchor.constraint(equalTo: self.safeAreaLayoutGuide.centerXAnchor),
            
            buttonRegister.topAnchor.constraint(equalTo: labelPhoto.bottomAnchor, constant: 32),
            buttonRegister.centerXAnchor.constraint(equalTo: self.safeAreaLayoutGuide.centerXAnchor)
        ])
    }
    
    //codes omitted...
}

```
{% endcode %}

## Patching RegisterViewController to Pick Photo

Now we update the RegisterViewController.swift:

{% code lineNumbers="true" %}
```swift
//
//  RegisterViewController.swift
//  App12
//
//  Created by Sakib Miazi on 6/2/23.
//

import UIKit
import PhotosUI

class RegisterViewController: UIViewController {
    
    //codes omitted...
    
    //MARK: variable to store the picked Image...
    var pickedImage:UIImage?
    //codes omitted...
    
    override func viewDidLoad() {
        super.viewDidLoad()
        //codes omitted...
        registerView.buttonTakePhoto.menu = getMenuImagePicker()
        //codes omitted...
    }
    
    //MARK: menu for buttonTakePhoto setup...
    func getMenuImagePicker() -> UIMenu{
        let menuItems = [
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
        let cameraController = UIImagePickerController()
        cameraController.sourceType = .camera
        cameraController.allowsEditing = true
        cameraController.delegate = self
        present(cameraController, animated: true)
    }
    
    //MARK: pick Photo using Gallery...
    func pickPhotoFromGallery(){
        //MARK: Photo from Gallery...
        var configuration = PHPickerConfiguration()
        configuration.filter = PHPickerFilter.any(of: [.images])
        configuration.selectionLimit = 1
        
        let photoPicker = PHPickerViewController(configuration: configuration)
        
        photoPicker.delegate = self
        present(photoPicker, animated: true, completion: nil)
    }
    //codes omitted...
}

```
{% endcode %}

In the above code:

* We import PhotosUI library to implement photo pickers.
* We declare a UIImage variable `pickedImage` on line 16 to keep the picked photo.
* We set up the menu items for two options: Camera and Gallery (line 22 and lines 26 through 38).
* Then as we did in [https://github.com/sakibnm/iOS/blob/main/6.-uimenu-picking-images-from-gallery-and-camera-and-uiimageview](https://github.com/sakibnm/iOS/blob/main/6.-uimenu-picking-images-from-gallery-and-camera-and-uiimageview "mention"), we define `pickUsingCamera()` and `pickPhotoFromGallery()` methods.

We still need to adopt the protocols related to PHPickerView, and UIImagePicker. We will separate the adoption of protocols from RegisterViewController.swift file.

## PhotoManager.swift

Let's create a new file PhotoManager.swift in `Register Screen` group and put the following code in it:

{% code lineNumbers="true" %}
```swift
//
//  PhotoManager.swift
//  App12
//
//  Created by Sakib Miazi on 6/5/23.
//

import UIKit
import PhotosUI

//MARK: adopting required protocols for PHPicker...
extension RegisterViewController:PHPickerViewControllerDelegate{
    func picker(_ picker: PHPickerViewController, didFinishPicking results: [PHPickerResult]) {
        dismiss(animated: true)
        
        print(results)
        
        let itemprovider = results.map(\.itemProvider)
        
        for item in itemprovider{
            if item.canLoadObject(ofClass: UIImage.self){
                item.loadObject(
                    ofClass: UIImage.self,
                    completionHandler: { (image, error) in
                        DispatchQueue.main.async{
                            if let uwImage = image as? UIImage{
                                self.registerView.buttonTakePhoto.setImage(
                                    uwImage.withRenderingMode(.alwaysOriginal),
                                    for: .normal
                                )
                                self.pickedImage = uwImage
                            }
                        }
                    }
                )
            }
        }
    }
}

//MARK: adopting required protocols for UIImagePicker...
extension RegisterViewController: UINavigationControllerDelegate, UIImagePickerControllerDelegate{
    func imagePickerController(_ picker: UIImagePickerController, didFinishPickingMediaWithInfo info: [UIImagePickerController.InfoKey : Any]) {
        picker.dismiss(animated: true)
        
        if let image = info[.editedImage] as? UIImage{
            self.registerView.buttonTakePhoto.setImage(
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
{% endcode %}

In the above code, we save the selected image in `pickedImage` variable (on lines 31 and 51).

Now that the Photo Pickers are integrated let's run the app. We should see the following:

<figure><img src="/gitbook-assets/13.two (1).gif" alt=""><figcaption></figcaption></figure>

**Note: we are making 'pick a profile photo' for the new user optional. So, a user can be created without even picking a photo.**



<!-- Merged from 13.2.-uploading-the-picked-photo-to-firebase-storage.md -->

# 13.2. Uploading the Picked Photo to Firebase Storage

We need to update the RegisterFirebaseManager.swift file to upload the picked photo to Firebase Storage.

**Firebase operations are asynchronous network calls. So we have to be very careful about the sequence of operations. We need to maintain the following sequence:**

1. Upload the picked image to Firebase Storage. We have to wait until the upload is successful and fetch the download URL of that photo.
2. Once the image upload is successful, we create the account with the email and password. We have to wait until the account is successfully created.
3. Once the account is created, we update the profile with the user's name and photo URL.

So we will overhaul the whole RegisterFirebaseManager.swift file. But before we do, we need to import the `FirebaseStorage` library and create a Firebase Storage instance in RegisterViewController.swift file, like the following:

```swift
//
//  RegisterViewController.swift
//  App12
//
//  Created by Sakib Miazi on 6/2/23.
//

import FirebaseStorage

class RegisterViewController: UIViewController {
    //codes omitted...
    let storage = Storage.storage()
    //codes omitted...
}
```

## Uploading a File to Storage: RegisterFirebaseManager.swift

Let's open the RegisterFirebaseManager.swift file and write the following code:

{% code lineNumbers="true" %}
```swift
//
//  RegisterFirebaseManager.swift
//  App12
//
//  Created by Sakib Miazi on 6/2/23.
//

import Foundation
import FirebaseAuth
import FirebaseStorage

extension RegisterViewController{    
    func uploadProfilePhotoToStorage(){
        var profilePhotoURL:URL?
        
        //MARK: Upload the profile photo if there is any...
        if let image = pickedImage{
            if let jpegData = image.jpegData(compressionQuality: 80){
                let storageRef = storage.reference()
                let imagesRepo = storageRef.child("imagesUsers")
                let imageRef = imagesRepo.child("\(NSUUID().uuidString).jpg")
                
                let uploadTask = imageRef.putData(jpegData, completion: {(metadata, error) in
                    if error == nil{
                        imageRef.downloadURL(completion: {(url, error) in
                            if error == nil{
                                profilePhotoURL = url
                                self.registerUser(photoURL: profilePhotoURL)
                            }
                        })
                    }
                })
            }
        }else{
            registerUser(photoURL: profilePhotoURL)
        }
    }
    
    func registerUser(photoURL: URL?){
        if let name = registerView.textFieldName.text,
           let email = registerView.textFieldEmail.text,
           let password = registerView.textFieldPassword.text{
            Auth.auth().createUser(withEmail: email, password: password, completion: {result, error in
                if error == nil{
                    self.setNameAndPhotoOfTheUserInFirebaseAuth(name: name, email: email, photoURL: photoURL)
                }
            })
        }
    }
    
    func setNameAndPhotoOfTheUserInFirebaseAuth(name: String, email: String, photoURL: URL?){
        let changeRequest = Auth.auth().currentUser?.createProfileChangeRequest()
        changeRequest?.displayName = name
        changeRequest?.photoURL = photoURL
        
        print("\(photoURL)")
        changeRequest?.commitChanges(completion: {(error) in
            if error != nil{
                print("Error occured: \(String(describing: error))")
            }else{
                self.hideActivityIndicator()
                self.navigationController?.popViewController(animated: true)
            }
        })
    }
}

```
{% endcode %}

In the above code:

* We are following the sequence we talked about before.
* We extend RegisterViewController class.
* On line 10, we import the FirebaseStorage library.
* **On lines 13 through 37**, we upload the `pickedImage`.
  * Since picking a profile photo is optional for the user, we might not have a selected image. So if there is no image selected (lines 34 through 36), we directly jump to `registerUser(photoURL: profilePhotoURL)` method.
  * If the user picked an image (lines 18 through 33):
    * **Line 18:** We first get a jpeg image from the picked image. (I set the compression quality to 80%, but you can set it anywhere between 70-95%. The higher the number is, the more space it takes in the storage).
    * **Line 19:** We initiate the Firebase Storage.
    * **Line 20**: We create a folder named `imagesUsers` in the storage bucket.
    * **Line 21:** We want to add a new file in the `imageUsers` folder, right? The file new file is the image we picked. We must provide the file's name when we upload it to Firebase Storage. Here we create a unique name for the file using `NSUUID().uuidString`. `NSUUID()` is the iOS's default Universal Unique Identifier (UUID) generator. It generates 128-bit long unique IDs. We get the string value of that random UUID and name the jpeg file with it.
    * **Lines 23 through 32:** we upload the image to the Storage.
      * We are uploading the file using `putData()` method on line 23. The completion closure deals with the response from Firebase Storage.
      * On line 24, we check if the response is successful or not.
        * Now on line 25, we make a separate network call to fetch the download URL of the uploaded image.
        * On line 26, we check whether the `downloadURL()` call returns an error or not.
          * If the download URL is returned successfully, then we save the URL locally in variable `profilePhotoURL`.
          * And then, to maintain the sequence of operations correctly, we call the `registerUser()` method to register the new user with the uploaded photo.
* **Lines 39 through 49:** we create the user as before. Then on success, we call the `setNameAndPhotoOfTheUserInFirebaseAuth(name: name, email: email, photoURL: photoURL)` method to update the user profile.
* **Lines 51 through 65:** Then we create a `changeRequest` as before to update the current user profile. We set the value of `photoURL` parameter of the user profile to the download URL we fetched.
  * Lines 60 through 63: If the profile update is successful, we pop the current screen from the navigation controller.
  * (We also hide the progress activity indicator).

Now uploading files to Firebase Storage code is ready!

We must patch the RegisterViewController.swift file to call these sequence operations correctly.

### RegisterViewController.swift

Let's open the RegisterViewController.swift file again, and scroll down to `@objc func onRegisterTapped()` method. Let's put the following code in the method:

```swift
@objc func onRegisterTapped(){
    //MARK: creating a new user on Firebase with photo...
    showActivityIndicator()
    uploadProfilePhotoToStorage()
}
```

Here we are just displaying the progress activity indicator, and then calling the first method of the sequence of operations.

Now! If you run the app again, you'll see:

<figure><img src="/gitbook-assets/13.four (1).gif" alt=""><figcaption></figcaption></figure>

Let's look into the FirebaseStorage console:

<figure><img src="/gitbook-assets/13.five (2).gif" alt=""><figcaption></figcaption></figure>

So the files are getting uploaded. Now we need to display the images, and then it's done.



<!-- Merged from 13.3.-displaying-images-hosted-in-cloud.md -->

# 13.3. Displaying Images Hosted in Cloud

Now, we know the download URL of the profile photo of the logged-in user. We will now display it in an ImageView.

We first add a custom utility for the UIImageView class using `extension` keyword. Let's create a file named 'ImageViewUtils.swift'.

<figure><img src="/gitbook-assets/Screenshot 2023-06-05 at 6.52.34 PM (1).png" alt="" width="345"><figcaption></figcaption></figure>

Put the following code there:

{% code lineNumbers="true" %}
```swift
//
//  ImageViewUtils.swift
//  App12
//
//  Created by Sakib Miazi on 6/5/23.
//

import Foundation
import UIKit

extension UIImageView {
    //MARK: Borrowed from: https://www.hackingwithswift.com/example-code/uikit/how-to-load-a-remote-image-url-into-uiimageview
    
    func loadRemoteImage(from url: URL) {
        DispatchQueue.global().async { [weak self] in
            if let data = try? Data(contentsOf: url) {
                if let image = UIImage(data: data) {
                    DispatchQueue.main.async {
                        self?.image = image
                    }
                }
            }
        }
    }
}
```
{% endcode %}

In the above code:

* We are extending the default UIImageView class and adding `loadRemoteImage(from url: URL)` method.
* On line 15: We are creating a background task to load the cloud image. It has to be through an asynchronous background thread because it is a network call. We cannot guarantee the image getting downloaded instantly.
* If the data from the remote URL is a valid image, then we load the data as image into the UIImageView.

Now, we need to open ViewController.swift file and scroll down to `handleAuth`.

Let's add the following couple of lines of code in the file:

{% code lineNumbers="true" %}
```swift
//
//  ViewController.swift
//  App12
//
//  Created by Sakib Miazi on 6/1/23.
//

//codes omitted...

class ViewController: UIViewController {

   //codes omitted...
    
    override func viewWillAppear(_ animated: Bool) {
        super.viewWillAppear(animated)
        
        //MARK: handling if the Authentication state is changed (sign in, sign out, register)...
        handleAuth = Auth.auth().addStateDidChangeListener{ auth, user in
            if user == nil{
               //codes omitted...
                
            }else{
                //codes omitted...
                
                //MARK: setting the profile photo...
                if let url = self.currentUser?.photoURL{
                    self.mainScreen.profilePic.loadRemoteImage(from: url)
                }
                
                //codes omitted...
                
            }
        }
    }
    
    //codes omitted...
}


```
{% endcode %}

In the above code:

* If the user is logged in on lines 26 through 28, we are checking whether the user's profile photo is nil. If it's not nil, we set the `profilePic`'s image using our custom utility.

Let's run the app now.

<figure><img src="/gitbook-assets/13.seven (1).gif" alt=""><figcaption></figcaption></figure>

### Great!!! We now know how to store and retrieve an image using Firebase Storage.

### What data can you store in a FirebaseAuth user object?

* Firebase users have a fixed set of basic properties—a unique ID, a primary email address, a name and a photo URL—stored in the project's user database, that can be updated by the user (iOS, Android, web). **You cannot add other properties to the user object directly; instead, you can store the additional properties in any other storage services, like Google Cloud Firestore.**



<!-- Merged from 13.4.-reference-code.md -->

# 13.4. Reference Code

{% file src="/gitbook-assets/App13(App 12 extension with Storage) (1).zip" %}

---

## Guided Practice Challenges

Before moving on to the next topic, try these low-stakes practice challenges in Xcode. They will build the exact muscle memory you need:

### Challenge 1: Experimentation
**The Scenario:** You've just learned about Firebase Storage.
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

