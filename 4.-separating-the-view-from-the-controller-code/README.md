# 4. Separating the View from the Controller code

One of the better ways of coding is to separate the Views (front-end codes) from the Controllers (back-end codes). That way, we can make ViewControllers less cluttered.

We have been keeping all the codes for a screen on a single file (ViewController.swift). We can easily separate the View codes from the ViewController. After we separate the Views, we willwillwillwillwillwillwillwill only have Control and Data access codes in ViewController.&#x20;

To be able to do that, we will create our App4. We will build something like the following:

<figure><img src="../.gitbook/assets/Screenshot 2023-05-16 at 11.05.16 AM.png" alt=""><figcaption></figcaption></figure>

On our first screen, we will have a Label to display "App4." Then we will have a TextField to get a text from the user. Next, we will have another Label to say, "How are you feeling today?" And then, we will show a PickerView to select a mood from "Happy," "Meh," and "Sad." Finally, we will have a Button, Submit. If the user taps the Submit Button, it should take them to the second screen. The second screen displays the message and the mood of the user.&#x20;
