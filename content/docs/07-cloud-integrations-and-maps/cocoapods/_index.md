---
title: "CocoaPods"
weight: 10
---

# 9. Cocoa Pods

UIKit has thousands of modules, and we cannot learn all of them (you don't even need to). You only need to learn the most important, common, and useful ones. Then you can learn the others if you need them to solve a problem you are facing in real life.

Also, many developers build third-party modules that give generalized solutions to tricky problems, like making HTTP connections to talk to remote APIs over the Internet, building reactive screens that can deal with different sensors, etc. So, these community-built modules are also shared with others through Cocoa Pods, so you do not have to reinvent the wheels. ([https://cocoapods.org/](https://cocoapods.org/)).

<mark style="color:orange;">**Caution: You must be cautious since CocoaPods are not developed and released by Apple.**</mark>

* <mark style="color:orange;">The cocoa pods are usually general-purpose modules, meaning they are the Jacks of all trades, masters of none. So, for a large application, they might create slight performance issues. For example, you might have just needed to read the byte stream from a remote API. If you use a fancy general-purpose cocoa pod library that can do many more tasks and would implement a lot of abstractions before it gives you the stream, it might be overkill for you. And if your app is time and performance sensitive, you better build your own module.</mark>
* <mark style="color:orange;">Not all of the modules can be trusted since community members openly share these, and not many of us test all of them.</mark> <mark style="color:orange;">**Only use the most common and reputed ones. (Google might help you find them).**</mark>
* <mark style="color:orange;">**Only use the ones that get updated often.**</mark> <mark style="color:orange;">Many of the modules in Cocoa Pods seem useful, yet weren't been updated in the last couple of years.</mark> <mark style="color:orange;">**Do not use them.**</mark> <mark style="color:orange;">First, Swift gets updates very</mark> _<mark style="color:orange;">**swiftly**</mark>_<mark style="color:orange;">, so even if the module works today, the underlying libraries are probably deprecated. So, if they stop working tomorrow, you need to build your own module anyway.</mark> \ <mark style="color:orange;">Secondly, older modules risk being vulnerable regarding security, privacy, and overall code safety.</mark>

(Enough of being cautious) However, Cocoa Pods have some of the very best modules; those are even used in the industry. For example, AlamoFire is a beginner-friendly module that can be used to connect your app to the Internet and talk to the API servers. It is a general-purpose module that is used by millions of developers and very often gets updates and support from many contributors worldwide.

Here we will see how to integrate Cocoa Pod modules into our app.




<!-- Merged from 9.1.-installing-cocoa-pods.md -->

# 9.1. Installing Cocoa Pods

Let's visit the web page [https://cocoapods.org/](https://cocoapods.org/).

{% embed url="https://cocoapods.org/" %}

It should open a page like this:

<figure><img src="/gitbook-assets/Screenshot 2023-05-24 at 12.27.12 PM (1).png" alt=""><figcaption></figcaption></figure>

Now let's open the Terminal app on your Mac.

* Press `command` ⌘ `+` `Space` and it'll open the Spotlight search.
* Type "Terminal," and it should find the Terminal app for you.
* Press the return key to open it.

<figure><img src="/gitbook-assets/9.1 (1).gif" alt=""><figcaption></figcaption></figure>

### **There are two ways of installing CocoaPods on your Mac:**

#### 1. Using the command in cocoapods.org:

* Copy the command (`sudo gem install cocoapods`) from the CocoaPods webpage and paste it into the Terminal. Put in your password and press return. It should install CocoaPods. After installation is done, put the command `pod --version` into your terminal. It should show something like: `1.12.1`. If you see that, you are done installing CocoaPods on your Mac.

#### **2. If the above method doesn't work and your Terminal is not responding, try the following (more stable) method:**

* **Install Homebrew on your Mac:** **Homebrew** is an alternative (Linux-like) package manager for Mac. It is very widely used and quite useful to install open-sourced software packages.
  * Visit: [https://github.com/Homebrew/install](https://github.com/Homebrew/install)
  * Copy the terminal command posted there: `/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"`.
  * Paste it into your Terminal.
  * Press the return key.
  * Put in your Mac password.
  * It should install **homebrew** on your Mac.
* **Install CocoaPods using Homebrew:**
  * Open your Terminal and put the following command there:
    * `brew install cocoapods`
  * Press the return key.
  * It should be installing **CocoaPods** on your Mac.
  * After it's done, put the following command `pod --version` into your terminal. It should show something like the following: `1.12.1`. If you see that, you are done installing CocoaPods on your Mac.

<figure><img src="/gitbook-assets/9.two (2).gif" alt=""><figcaption></figcaption></figure>



<!-- Merged from 9.2.-integrating-cocoapods-into-a-project.md -->

# 9.2. Integrating CocoaPods into a Project

Let's create a new project App9 in Xcode. We will not write any code here; we will just use it to see how we can integrate cocoa pods into the project.

**The setup part might look a little bit tricky, but it's really easy.**

* **After you create the project, remember the directory you store the project into.**
* Open the directory using FInder (file browser on Mac). Browse to the directory (folder) where you saved the project. Do not get into the directory yet. So, you should be in the parent directory of the project directory now.
* Open Terminal.
* Type `cd` and put a space. **Do not press return yet.**
* Drag and drop the project directory onto the Terminal. You will see the path to the directory is pasted on the Terminal after `cd`.
* Press return. Now you should be in the project directory through Terminal.
* Type `ls` and press return. You will see the project files in the Terminal.

<figure><img src="/gitbook-assets/9.one (1).gif" alt=""><figcaption></figcaption></figure>

* Now, type in `pod init` command on Terminal.
* Open Finder again. You will see that there is a file called **Podfile** has been created.

<figure><img src="/gitbook-assets/9.4 (1).gif" alt=""><figcaption></figcaption></figure>

* Now open the Podfile with your favorite text editor.
* You will see a line `# Pods for App9`. You can add modules after the line.

<figure><img src="/gitbook-assets/9.5 (1).gif" alt=""><figcaption></figcaption></figure>

### Adding a CocoaPod module, Alamofire, to our project

As I said before, Alamofire is a widely used module for beginners to manage Internet data transmission. We will integrate Alamofire to App9.

* Visit [https://cocoapods.org](https://cocoapods.org).
* Search for Alamofire. On top of the search results, you will see something like '**Alamofire 5.6.4.'**
* Click on the button to the right, 'Site.'
* It will load the main project site in Github.

<figure><img src="/gitbook-assets/9.6 (2).gif" alt=""><figcaption></figcaption></figure>

* If you scroll down to **Installation,** you will see the instructions of how to install Alamofire using CocoaPods. Copy the line that says: `pod 'Alamofire'`.
* Open the Podfile we have seen before.
* Paste the line after `# Pods for App9`.

<figure><img src="/gitbook-assets/9.7.gif" alt=""><figcaption></figcaption></figure>

* Now go back to the Terminal again. Go to the project directory if you are not there (see above if you forgot how to).
* Put the following command onto the Terminal: `pod install`.
* You will see, depending on the modules you added to the Podfile, it will install them. When it's done installing the pods, in this case, it is Alamofire, your project can use this CocoaPod module.

<mark style="color:red;">**Now, the final step is to be able to use the module. The following part is very important. We often forget to do that and the modules do not work in code.**</mark>

* Now, what you have to do is, **close the Xcode project.**
* Open the project directory again.
* <mark style="color:red;">**Do not open the .xcodeproj file.**</mark> <mark style="color:green;">**Open the .xcworkspace file for this project.**</mark>
* **Once you install a third-party module using CocoaPods, you must always use the workspace file (.**<mark style="color:green;">**xcworkspace**</mark>**) to open the project. Otherwise, you can't use the third-party modules.**

<figure><img src="/gitbook-assets/9.9 (1).gif" alt=""><figcaption></figcaption></figure>

**Now, we have completed adding the 'Alamofire' module to our project using CocoaPods.**

### Reference Code

{% file src="/gitbook-assets/App9_cocoapods (1).zip" %}

