# 9. Cocoa Pods

UIKit has thousands of modules, and we cannot learn all of them (you don't even need to). You only need to learn the most important, common, and useful ones. Then you can learn the others if you need them to solve a problem you are facing in real life.

Also, many developers build third-party modules that give generalized solutions to tricky problems, like making HTTP connections to talk to remote APIs over the Internet, building reactive screens that can deal with different sensors, etc. So, these community-built modules are also shared with others through Cocoa Pods, so you do not have to reinvent the wheels. ([https://cocoapods.org/](https://cocoapods.org/)).

<mark style="color:orange;">**Caution: You must be cautious since CocoaPods are not developed and released by Apple.**</mark>

* <mark style="color:orange;">The cocoa pods are usually general-purpose modules, meaning they are the Jacks of all trades, masters of none. So, for a large application, they might create slight performance issues. For example, you might have just needed to read the byte stream from a remote API. If you use a fancy general-purpose cocoa pod library that can do many more tasks and would implement a lot of abstractions before it gives you the stream, it might be overkill for you. And if your app is time and performance sensitive, you better build your own module.</mark>
* <mark style="color:orange;">Not all of the modules can be trusted since community members openly share these, and not many of us test all of them.</mark> <mark style="color:orange;">**Only use the most common and reputed ones. (Google might help you find them).**</mark>
* <mark style="color:orange;">**Only use the ones that get updated often.**</mark> <mark style="color:orange;">Many of the modules in Cocoa Pods seem useful, yet weren't been updated in the last couple of years.</mark> <mark style="color:orange;">**Do not use them.**</mark> <mark style="color:orange;">First, Swift gets updates very</mark> _<mark style="color:orange;">**swiftly**</mark>_<mark style="color:orange;">, so even if the module works today, the underlying libraries are probably deprecated. So, if they stop working tomorrow, you need to build your own module anyway.</mark> \ <mark style="color:orange;">Secondly, older modules risk being vulnerable regarding security, privacy, and overall code safety.</mark>

(Enough of being cautious) However, Cocoa Pods have some of the very best modules; those are even used in the industry. For example, AlamoFire is a beginner-friendly module that can be used to connect your app to the Internet and talk to the API servers. It is a general-purpose module that is used by millions of developers and very often gets updates and support from many contributors worldwide.

Here we will see how to integrate Cocoa Pod modules into our app.
