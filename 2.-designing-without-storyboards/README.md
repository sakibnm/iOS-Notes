---
coverY: 0
---

# 2. Designing without Storyboards

In our first app, we dragged and dropped the UI elements on Storyboard and set up the constraints using the Interface Builder's tools. Now, I said we would ditch this approach and start designing the UI with codes.

### Why don't we use storyboards?

There are several reasons for it, as this blog post discusses: [https://kissdigital.com/blog/why-we-stopped-using-storyboards](https://kissdigital.com/blog/why-we-stopped-using-storyboards). However, long story short, Storyboards automatically create the XML tags for the UI elements. Since they are machine generated, the resource IDs of the UI elements change very frequently. So, if you run your friend's code on your computer, the IDs will change. Think about you are collaborating with a friend using GitHub. It will probably be fine if you do not work concurrently in different branches. However, it will be a massive pain if you work on the same project concurrently and want to merge the updates. Using codes to generate the UIs programmatically doesn't have this issue.

**Constraints and Attributes**

Before we start, let's have a quick look at the UI we had from 'App1':

![](<../.gitbook/assets/Screenshot 2023-05-09 at 10.25.49 PM.png>)

Let's look into the constraints of the UI:

![](<../.gitbook/assets/Screenshot 2023-05-09 at 10.50.48 PM (1) (1).png>)

So the Label ("Hello World!") has two constraints:

* Centered to the x-axis (horizontal axis).
* There is a gap of 32 points between the screen's top edge and the Label's top edge.

The TextField ("Put some text") has two constraints:

* Centered to the x-axis (horizontal axis).
* There is a gap of 16 points between the Label's bottom edge and the TextField's top edge.

Similarly, the Button ("Click me!") has two constraints:

* Centered to the x-axis (horizontal axis).
* There is a gap of 16 points between TextField's bottom edge and Button's top edge.

### Understanding the constraint notations

Let's look at the following grid:

<figure><img src="../.gitbook/assets/grid (2).png" alt=""><figcaption><p>The grid on a screen</p></figcaption></figure>

The above grid is similar to a mobile screen. **The origin of the grid `(0, 0)` above is the top-left point,** unlike to the regular grid we use in our regular visualizations. So, when we want to anchor the object on the screen, there are four constraints we may need to set:

* Leading constraint - how far the object is from the reference point at its left.
* Trailing constraint - how far the object is from the reference point at its right.
* Top constraint - how far the object is from the reference point above it.
* Bottom constraint - how far the object is from the reference point below it.

Please note you do not need to add all four constraints to anchor an object on the screen. For example, the UI elements of 'App1' do not have all four anchors. They all have top, leading, and trailing anchors. _Centering an element takes care of two constraints: leading and trailing together._
