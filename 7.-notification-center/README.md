# 7. Notification Center

<mark style="color:purple;">**(Do not confuse it with the push notifications)**</mark>

NotificationCenter is a very useful utility for iOS to handle data independent of the lifecycles of the screens.

According to Apple Developer: It is _a notification dispatch mechanism that enables the broadcast of information to registered observers._ Sounds confusing? Luckily, it is not that confusing, though.

Simply put, NotificationCenter is a central dispatcher of data to broadcast data from one part of the app to another. A 'part' of an app could be any Swift class.

For example, there are two screens in an app. Screen2 takes text input from the user, and it has to send the text to Screen1 and display the text in a Label. Here is how it can be handled using a NotificationCenter:

* NotificationCenter works as a separate mediator. A class can post data to or observe data from the NotificationCenter.
* Screen2 can post the text. And Screen1 can observe the text.
* When Screen2 posts a new text, the NotificationCenter detects an update of data been made and broadcasts the notifications to all the observers of that particular data.
* At this point, Screen1, as an observer of that particular text, receives the notification that the text has been updated.
* Finally, Screen1 reacts to the notification and updates it's local UI elements accordingly, such as updating it's Label with the updated text.

So, let's build a small App to test it out.
