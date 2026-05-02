---
coverY: 0
---

# 5. Tab Bar Controller

We often see apps with bottom navigation bars, where you can tap on an icon from the bottom bar, and the app loads different screens for different buttons pressed like the following:

<figure><img src="../../.gitbook/assets/5.one (1).gif" alt=""><figcaption></figcaption></figure>

iOS gives us an easy-to-use and customizable tool called UITabBarController to build such screens. In this module, we will create an app that uses a Tab Bar.

## The TabControllerDemo app

Let's create an app called TabControllerDemo in XCode. The app will have:

* A bottom Tab Bar having three Tab Bar buttons: red, green, and blue.
* Tapping the "red" button opens the Red Screen.
* Tapping the "blue" button opens the Blue Screen.
* Tapping the "green" button opens the Green Screen.
* Each screen has
  * A color box displaying the corresponding color.
  * A button to send data to other screens.
  * A label to display the received data from other screens.
