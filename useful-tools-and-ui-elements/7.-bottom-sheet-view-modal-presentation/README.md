# 7. Bottom Sheet View: Modal Presentation

You probably have seen apps where you tap a button, and a page sheet pops up from the bottom. You can then interact with that page sheet and work with the app. We can use Swift's SheetPresentationController for building the bottom sheet views.&#x20;

In this short module, we will build the following app:

<figure><img src="../../.gitbook/assets/7.sixty (1).gif" alt=""><figcaption></figcaption></figure>

Basically, we build this app on top of the app in the [6.-search-bar](../6.-search-bar/ "mention") module. We will implement SearchBar on a bottom sheet view.

We have a Find button on our main screen and a label to display the selected name. If the user taps on the Find button, the app should present the bottom search sheet. The user searches for a name on the bottom search sheet and selects a name. Then, we need to dismiss the bottom sheet and set the text of the label to the selected name.
