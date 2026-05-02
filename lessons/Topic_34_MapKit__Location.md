# MapKit & Location


**Estimated effort:** 1-2 hours this topic
**Format:** Asynchronous online
**Prerequisites:** Previous iOS topics

{< hint info >}
**🎯 Topic Mission:** 
In this module, we will explore **MapKit & Location** and learn how to integrate it into our iOS applications. Your mission is to understand the mechanics behind this concept and write robust Swift code.
{< /hint >}

---

## Learning Objectives

By the end of this session, you will be able to:
1. Understand the core concepts of MapKit & Location.
2. Implement MapKit & Location in an Xcode project.
3. Apply best practices to ensure clean and maintainable code.

---

## The Story So Far...

We have been progressively building our knowledge of iOS and Swift. In this module, we will expand our toolkit by diving into MapKit & Location. 
Open your current Xcode project or start a new Playground to follow along with the hands-on material.

---

## Walkthrough: Exploring MapKit & Location

> 📁 **Target Project** — Follow along by building the mini-app presented in the steps below, or integrate these concepts into your own ongoing projects.

# 14. UIMapKit: Working with Location and Maps

In this module, we will learn how to use location services in iOS and build a few basic utilities of UIMapKit. Our end goal is to search places nearby on a Map View and navigate to the selected place using Apple Maps.

Let's create a new project on XCode and name it App14.




<!-- Merged from 14.1.-phase-1-displaying-map-view-and-current-location.md -->

# 14.1. Phase 1: Displaying Map View and Current Location

## Setting up the Map View

Our landing screen will be a Map screen. In the first step, we will have a button to show the current location on the map.&#x20;

Let's create a file named MapView.swift.&#x20;

![](</gitbook-assets/Screenshot 2023-06-14 at 11.20.25 AM (1).png>)

Let's put the following code in the file:

{% code lineNumbers="true" %}
```swift
//
//  MapView.swift
//  App14
//
//  Created by Sakib Miazi on 6/14/23.
//

import UIKit
import MapKit

class MapView: UIView {
    var mapView:MKMapView!
    var buttonLoading:UIButton!
    var buttonCurrentLocation:UIButton!
    
    override init(frame: CGRect) {
        super.init(frame: frame)
        backgroundColor = .white
        setupMapView()
        setupButtonLoading()
        setupButtonCurrentLocation()
        initConstraints()
    }
    
    func setupMapView(){
        mapView = MKMapView()
        mapView.translatesAutoresizingMaskIntoConstraints = false
        mapView.layer.cornerRadius = 10
        self.addSubview(mapView)
    }
    
    func setupButtonLoading(){
        buttonLoading = UIButton(type: .system)
        buttonLoading.setTitle(" Fetching Location...  ", for: .normal)
        buttonLoading.titleLabel?.font = UIFont.boldSystemFont(ofSize: 20)
        buttonLoading.setImage(UIImage(systemName: "circle.dotted"), for: .normal)
        buttonLoading.layer.backgroundColor = UIColor.black.cgColor
        buttonLoading.tintColor = .white
        buttonLoading.layer.cornerRadius = 10
        
        buttonLoading.layer.shadowOffset = .zero
        buttonLoading.layer.shadowRadius = 4
        buttonLoading.layer.shadowOpacity = 0.7
        
        buttonLoading.translatesAutoresizingMaskIntoConstraints = false
        
        buttonLoading.isEnabled = false
        self.addSubview(buttonLoading)
    }
    
    func setupButtonCurrentLocation(){
        buttonCurrentLocation = UIButton(type: .system)
        buttonCurrentLocation.setImage(UIImage(systemName: "location.circle"), for: .normal)
        buttonCurrentLocation.layer.backgroundColor = UIColor.lightGray.cgColor
        buttonCurrentLocation.tintColor = .blue
        buttonCurrentLocation.layer.cornerRadius = 10
        
        buttonCurrentLocation.layer.shadowOffset = .zero
        buttonCurrentLocation.layer.shadowRadius = 4
        buttonCurrentLocation.layer.shadowOpacity = 0.7
        
        buttonCurrentLocation.translatesAutoresizingMaskIntoConstraints = false
        
        self.addSubview(buttonCurrentLocation)
    }
    
    func initConstraints(){
        NSLayoutConstraint.activate([
            mapView.centerXAnchor.constraint(equalTo: self.safeAreaLayoutGuide.centerXAnchor),
            mapView.centerYAnchor.constraint(equalTo: self.safeAreaLayoutGuide.centerYAnchor),
            mapView.widthAnchor.constraint(equalTo: self.safeAreaLayoutGuide.widthAnchor, multiplier: 0.95),
            mapView.heightAnchor.constraint(equalTo: self.safeAreaLayoutGuide.heightAnchor, multiplier: 0.95),
            
            buttonLoading.centerXAnchor.constraint(equalTo: mapView.centerXAnchor),
            buttonLoading.centerYAnchor.constraint(equalTo: mapView.centerYAnchor),
            buttonLoading.widthAnchor.constraint(equalToConstant: 240),
            buttonLoading.heightAnchor.constraint(equalToConstant: 40),
            
            buttonCurrentLocation.trailingAnchor.constraint(equalTo: mapView.trailingAnchor, constant: -16),
            buttonCurrentLocation.bottomAnchor.constraint(equalTo: self.mapView.bottomAnchor, constant: -8),
            buttonCurrentLocation.heightAnchor.constraint(equalToConstant: 36),
            buttonCurrentLocation.widthAnchor.constraint(equalToConstant: 36)
        ])
    }
    
    required init?(coder: NSCoder) {
        fatalError("init(coder:) has not been implemented")
    }
}
```
{% endcode %}

In the above code:

* We import MapKit first.
* We have a MKMapView, and two UIButtons (`buttonLoading` and `buttonCurrentLocation`).
  * `buttonLoading` is just a dumb button to display the status when the location is getting fetched. You can use a Progress Activity Dialog instead of this.
* On lines 25 through 29, we initialize the map view.
  * On line 28, we set the corner radius of the map view.
* On lines 32 through 49, we define the `buttonLoading` button.
* On lines 51 through 65, we define the `buttonCurrentLocation` button.
* And finally, we initialize the constraints on lines 67 through 84.
  * Make sure you define the height and width of the map view using constraints.

## Patching the View with the Controller

Let's open the ViewController.swift file and put the following code there:

```swift
//
//  ViewController.swift
//  App14
//
//  Created by Sakib Miazi on 6/14/23.
//

import UIKit

class ViewController: UIViewController {
    let mapView = MapView()
    
    override func loadView() {
        view = mapView
    }

    override func viewDidLoad() {
        super.viewDidLoad()
        // Do any additional setup after loading the view.
    }

}

```

Let's run the app now.

<figure><img src="/gitbook-assets/Screenshot 2023-06-14 at 11.38.02 AM.png" alt="" width="188"><figcaption></figcaption></figure>

## Location Manager

Now we will work on fetching the current location and moving the camera (map frame) to that location. Let's create a new file named LocationManager.swift. ![](</gitbook-assets/Screenshot 2023-06-14 at 12.15.25 PM.png>)

Let's add the following code to the file:

{% code lineNumbers="true" %}
```swift
//
//  LocationManager.swift
//  App14
//
//  Created by Sakib Miazi on 6/14/23.
//

import Foundation
import CoreLocation

//MARK: setting up location manager delegate...
extension ViewController: CLLocationManagerDelegate{
    func setupLocationManager(){
        //MARK: setting up location manager to get the current location...
        locationManager.delegate = self
        locationManager.desiredAccuracy = kCLLocationAccuracyBest
        locationManager.requestWhenInUseAuthorization()
        locationManager.startUpdatingLocation()
    }
    
    func locationManagerDidChangeAuthorization(_ manager: CLLocationManager) {
        //MARK: if the user either allows location while using the app or always...
        if manager.authorizationStatus == .authorizedWhenInUse
            || manager.authorizationStatus == .authorizedAlways{
            manager.requestLocation()
        }
    }
    
    func locationManager(_ manager: CLLocationManager, didUpdateLocations locations: [CLLocation]) {
        if let location = locations.first{
            mapView.buttonLoading.isHidden = true
            
        }
    }
    func locationManager(_ manager: CLLocationManager, didFailWithError error: Error) {
        print("location error: \(error.localizedDescription)")
    }
}
```
{% endcode %}

In the above code:

* We import the CoreLocation library.
* We extend the ViewController with `CLLocationManagerDelegate` protocol.&#x20;
* On lines 13 through 19 we initialize the location manager.&#x20;
  * **(We need to define the `locationManager` constant in ViewController.swift file):**
    * `let locationManager = CLLocationManager()`.
  * On line 15, we delegate the location manager to the current controller (ViewController).
  * On line 16, we set up the accuracy of GPS location for this location manager. We select the best accuracy for this app. **Remember that the best accuracy setting is not great for your device's battery.** There are many other accuracy settings like kCLLocationAccuracyHundredMeters, kCLLocationAccuracyNearestTenMeters, kCLLocationAccuracyBestForNavigation, etc. For details: [https://www.flybuy.com/understanding-location-settings-for-your-ios-and-android-apps](https://www.flybuy.com/understanding-location-settings-for-your-ios-and-android-apps).
  * On line 17, we request permission from the user to access the current location. Here I am asking for the 'while using the app' permission.
  * On line 18, we ask the location manager to seek for current location periodically. If you do not need continuous periodic location updates, you can request location only once by calling `locationManager.requestLocation()`.&#x20;
* On lines 21 through 27, we write the code for the adopted protocol method `locationManagerDidChangeAuthorization()`.&#x20;
  * First, we check if the user has given permission to access the location. If yes, then we request the location once.
* On lines 29 through 34, we implement the adopted method when `didUpdateLocations` gets triggered. When the location manager gets updated location coordinates, this method is called.
  * Basically, the location manager returns a list of locations together, since the user can be moving. We take the first one from the array here.
  * On line 31, we hide the loading button or remove the progress indicator.
  * On lines 35 through 37, we handle the error accessing the location.

## Action when the Current Location button is tapped

We need to implement the logic when the `buttonCurrentLocation` is tapped by the user. So we write `mapView.mapView.centerToLocation(location: locationManager.location!)` inside the `@objc func onButtonCurrentLocationTapped()` method in ViewController.swift file.&#x20;

The code so far in ViewController.swift file is:

{% code lineNumbers="true" %}
```swift
//
//  ViewController.swift
//  App14
//
//  Created by Sakib Miazi on 6/14/23.
//

import UIKit
import MapKit

class ViewController: UIViewController {
    let mapView = MapView()
    
    let locationManager = CLLocationManager()
    
    override func loadView() {
        view = mapView
    }

    override func viewDidLoad() {
        super.viewDidLoad()
        
        mapView.buttonCurrentLocation.addTarget(self, action: #selector(onButtonCurrentLocationTapped), for: .touchUpInside)
        
        setupLocationManager()
    }
    
    @objc func onButtonCurrentLocationTapped(){
        if let uwLocation = locationManager.location{
            mapView.mapView.centerToLocation(location: uwLocation)
        }
    }

}
```
{% endcode %}

On lines 29 through 31, we center the map view to the current location with a radius of 1000 meters.&#x20;

* Now, it should yell at you saying could not find method `centerToLocation()`. Because MKMapView does not have `centerToLocation()` method by default. We need to extend MKMapView to center the view.

## Extending MKMapView to center the view to the current location

Let's open ViewController.swift file and add the following extension to enable centering to the current location:

{% code lineNumbers="true" %}
```swift
//
//  ViewController.swift
//  App14
//
//  Created by Sakib Miazi on 6/14/23.
//

import UIKit
import MapKit

class ViewController: UIViewController {
    let mapView = MapView()
    let locationManager = CLLocationManager()
    //codes omitted...
}

extension MKMapView{
    func centerToLocation(location: CLLocation, radius: CLLocationDistance = 1000){
        let coordinateRegion = MKCoordinateRegion(
            center: location.coordinate,
            latitudinalMeters: radius,
            longitudinalMeters: radius
        )
        setRegion(coordinateRegion, animated: true)
    }
}

```
{% endcode %}

In the above code,

* On lines 19 through 23, we define a map region, where we define the center point of the map view to the current location. And then, we set the latitudinal and longitudinal span around the center.&#x20;

When the app loads, it still loads the entire North America. So, we need to zoom to the current location. So in ViewController.swift, after `setupLocationManager()` method we will call the `onButtonCurrentLocationTapped` method once to center the view:

```swift
    override func viewDidLoad() {
        super.viewDidLoad()
        
        mapView.buttonCurrentLocation.addTarget(self, action: #selector(onButtonCurrentLocationTapped), for: .touchUpInside)
        
        setupLocationManager()
        
        //MARK: center the map view to current location when the app loads...
        onButtonCurrentLocationTapped()
    }
    
    @objc func onButtonCurrentLocationTapped(){
        mapView.mapView.centerToLocation(location: locationManager.location!)
    }
```

## Setting up Info.plist to allow the location access

<figure><img src="/gitbook-assets/14.one.gif" alt=""><figcaption></figcaption></figure>

* Let's open Info.plist of the project.&#x20;
* Add a new row
  * The key should be: "NSLocationWhenInUseUsageDescription"
  * The value should be your explanation of why you would need this access. My explanation was: "This app requires location access to provide all the utilities.**"**

The emulator location is often set up as 'none' by default. In that case, it will not take you to a particular location. You can emulate the location of the emulator.&#x20;

### Setting the Simulator/Emulator location

* When the simulator is running, click on the Simulator Menu -> Features - > Location. You will see this:

<figure><img src="/gitbook-assets/Screenshot 2023-06-14 at 6.02.27 PM.png" alt=""><figcaption></figcaption></figure>

* You can select 'Custom Location...' option to put your preferred coordinate to simulate the current location.

Let's run the app now.

<figure><img src="/gitbook-assets/14.six.gif" alt=""><figcaption></figcaption></figure>



## Code so far

{% file src="/gitbook-assets/App14_phase1.zip" %}



<!-- Merged from 14.2.-phase-2-annotations-and-accessories-for-a-certain-place.md -->

# 14.2. Phase 2: Annotations and Accessories for a certain place

In this module, we will learn how to annotate a place in a particular coordinate on the map view. For example, we can annotate Northeastern University on the map view like the following:

<figure><img src="/gitbook-assets/14.sixty.gif" alt=""><figcaption></figcaption></figure>

## Defining a Place class with MKAnnotation

We will define a class named Place, adopting the MKAnnotation protocol to annotate places on the map view. So let's create a new file named 'Place.swift' and put the following code there:

{% code lineNumbers="true" %}
```swift
//
//  Place.swift
//  App14
//
//  Created by Sakib Miazi on 6/14/23.
//

import MapKit
import UIKit

class Place: NSObject, MKAnnotation {
    var title: String?
    var coordinate: CLLocationCoordinate2D
    var info: String

    init(title: String, coordinate: CLLocationCoordinate2D, info: String) {
        self.title = title
        self.coordinate = coordinate
        self.info = info
    }
    
    var mapItem: MKMapItem?{
        guard let location = title else{
            return nil
        }
        
        let placemark = MKPlacemark(
            coordinate: coordinate,
            addressDictionary:  [:]
        )
        let mapItem = MKMapItem(placemark: placemark)
        mapItem.name = title
        
        return mapItem
    }
}
```
{% endcode %}

In the above code:

* The class Place extends another Swift class NSObject, and adopts MKAnnotation protocol. MKAnnotation is a protocol that allows a Swift object to adopt MapKit's annotation-specific data and use the object directly as a place on the map.&#x20;
* On lines 12 through 14, we keep three variables to use in the annotation for a place.
  * title - the name of the place.
  * coordinate - the lat and long coordinates of the place.
  * info - additional details you may want to store.
  * You can use as many variables as you want to store more data regarding a place.
* Our initializer for the class Place is defined on lines through 16 through 20.
* Then we also initialize a variable `mapItem` of the type MKMapItem, to interact with the place on the map. MKMapItem class contains the details of a map location, like a placemark, coordinate, name, etc.
  * The placemark in a map item is the details of the place the map item represents, like the coordinate, physical address, phone number, images, etc. For now, we keep an empty dictionary for the addressDictionary of the placemark.
* Between lines 23 and 25, we used **guard-let** instead of if-let.

### What is guard-let?

**guard-let** is very similar to if-let to unwrap an optional value. `guard-let` is often used when you do not need to deal with the unwrapped value immediately and would use it later. So, we get the unwrapped value and store it in a constant for later use. For more, visit: [https://www.hackingwithswift.com/quick-start/understanding-swift/when-to-use-guard-let-rather-than-if-let](https://www.hackingwithswift.com/quick-start/understanding-swift/when-to-use-guard-let-rather-than-if-let)

## Display an Annotated Place on Map

Let's open the ViewController.swift file, and put the following code there:

{% code lineNumbers="true" %}
```swift
//
//  ViewController.swift
//  App14
//
//  Created by Sakib Miazi on 6/14/23.
//

import UIKit
import MapKit

class ViewController: UIViewController {
    //codes omitted...
    override func viewDidLoad() {
        super.viewDidLoad()
        
        //codes omitted...
        
        //MARK: Annotating Northeastern University...
        let northeastern = Place(
            title: "Northeastern University",
            coordinate: CLLocationCoordinate2D(latitude: 42.339918, longitude: -71.089797),
            info: "LVX VERITAS VIRTVS"
        )
        
        mapView.mapView.addAnnotation(northeastern)
        
    }
    
    //codes omitted...
}
//codes omitted...
```
{% endcode %}

In the above code:

* On lines 19 through 23, we create a Place object, `northeastern` with the details of Northeastern University (title, coordinate, and info).&#x20;
* Then we add the Place `northeastern` as an annotation on the map on line 25.

Let's run the app.&#x20;

<figure><img src="/gitbook-assets/14.sixty1.gif" alt=""><figcaption></figcaption></figure>

You can see there is a red bubble on the place `northeastern`. That is the placemark we talked about thus far.

## Interacting with the Annotations

Now to be able to interact with the bubble, we need to adopt a protocol `MKMapViewDelegate`. We  need to implement two adopted `mapView()` methods with parameters `viewFor` and `calloutAccessoryControlTapped`.&#x20;

Let's create a new file MapAnnotationDelegate.swift and put the following code there:

{% code lineNumbers="true" %}
```swift
//
//  MapAnnotationDelegate.swift
//  App14
//  Repurposed from: https://www.hackingwithswift.com/read/16/3/annotations-and-accessory-views-mkpinannotationview
//  Created by Sakib Miazi on 6/14/23.
//

import Foundation
import MapKit

extension ViewController: MKMapViewDelegate{
    func mapView(_ mapView: MKMapView, viewFor annotation: MKAnnotation) 
        -> MKAnnotationView? {
        
    }
    
    func mapView(_ mapView: MKMapView, annotationView view: MKAnnotationView, 
        calloutAccessoryControlTapped control: UIControl) {
       
    }
}

```
{% endcode %}

In the above code:

* Between lines 12 through 15, we need to create an annotation view to display the placemark details. We can
* Between lines 17 through 20, we need to write the logic to handle in case the user taps on the accessory button of the annotation.

### Creating Annotation View

Let's put the following code in the `mapView()` method for `viewFor` (first method in the above code):

{% code lineNumbers="true" %}
```swift
func mapView(_ mapView: MKMapView, viewFor annotation: MKAnnotation)
    -> MKAnnotationView? {
    guard let annotation = annotation as? Place else { return nil }
    
    var view:MKMarkerAnnotationView
    
    if let annotationView = mapView.dequeueReusableAnnotationView(
        withIdentifier: Configs.placeIdentifier) as? MKMarkerAnnotationView{
        
        annotationView.annotation = annotation
        view = annotationView
    
    }else{
        view = MKMarkerAnnotationView(annotation: annotation, reuseIdentifier: Configs.placeIdentifier)
        view.canShowCallout = true
        view.calloutOffset = CGPoint(x: -5, y: 5)
        view.rightCalloutAccessoryView = UIButton(type: .detailDisclosure)
    }
    return view
}
```
{% endcode %}

In the above code:

* On line 3, we define a new annotation from the `annotation` parameter as a Place object.
* Between line 7 and 18 we check if there is a reusable annotation already populated on screen,&#x20;
  * If yes, then we reuse the current annotation view.
  * Else, we create a new annotation&#x20;
    * We set the annotation view's `canShowCallout` parameter as true. It means it can display a callout interactive annotation view on this place.
    * Then we add a right accessory button on the callout annotation view.

### Delegating the User Interaction on the Callout

Let's put the following code in the `mapView()` method for `calloutAccessoryControlTapped` (second method):

{% code lineNumbers="true" %}
```swift
func mapView(_ mapView: MKMapView, 
    annotationView view: MKAnnotationView, 
    calloutAccessoryControlTapped control: UIControl) {
        
    guard let annotation = view.annotation as? Place else { return }
    
    let ac = UIAlertController(
        title: annotation.title,
        message: "Navigate to \(annotation.title!) now?",
        preferredStyle: .alert
    )
    
    ac.addAction(UIAlertAction(title: "Navigate", style: .default, handler: {_ in
        let launchOptions = [
            MKLaunchOptionsDirectionsModeKey: MKLaunchOptionsDirectionsModeDriving
        ]
        annotation.mapItem?.openInMaps(launchOptions: launchOptions)
    }))
    
    ac.addAction(UIAlertAction(title: "Cancel", style: .cancel))
    present(ac, animated: true)
}
```
{% endcode %}

In the above code:

* The method gets triggered when the user taps the accessory callout right button.&#x20;
* It displays an alert controller with two actions (lines 7 through 21):
  * &#x20;On lines 13 through 18, we add the navigation action to the alert controller with a button named 'Navigation.'&#x20;
    * On lines 14 through 16, we define the launchOptions for opening navigation in Apple Maps. We set the navigation direction type as driving directions on line 15.
    * And on line 17, we open Apple Maps to navigate to the place annotated.
  * On line 20, we add a Cancel action for the alert controller.
  * Then finally, on line 21, we present the alert controller.&#x20;

We have a final task to do. We need to patch the delegate of the mapView to ViewController. Let's open ViewController.swift file and add the following line in `viewDidLoad()` method: `mapView.mapView.delegate = self`.&#x20;

Let's run the app.&#x20;

<figure><img src="/gitbook-assets/14.sixty4.gif" alt=""><figcaption></figcaption></figure>

We first load the screen and display the annotation for Northeastern. Then we change the current simulator location to Apple's headquarters location.  Then we try the navigation with annotation. It opens the Apple Map, and we can drive!

## Code so far

{% file src="/gitbook-assets/App14 Phase2.zip" %}



<!-- Merged from 14.3.-phase-3-place-search-and-navigate.md -->

# 14.3. Phase 3: Place Search and Navigate

At this point, we will add a Bottom Search Sheet to find the places around and navigate there.

## Setting up the Bottom Search Sheet

First, let's add a search button at the bottom of the Map Screen. Open MapView.swift file, and put the following code to add the search button and its constraints:

{% code lineNumbers="true" %}
```swift
//
//  MapView.swift
//  App14
//
//  Created by Sakib Miazi on 6/14/23.
//

import UIKit
import MapKit

class MapView: UIView {
    //codes omitted...
    var buttonSearch:UIButton!
    
    override init(frame: CGRect) {
        //codes omitted...
        setupButtonSearch()
        initConstraints()
    }
   //codes omitted...
    
    func setupButtonSearch(){
        buttonSearch = UIButton(type: .system)
        buttonSearch.setTitle(" Search places...  ", for: .normal)
        buttonSearch.titleLabel?.font = UIFont.boldSystemFont(ofSize: 24)
        buttonSearch.setImage(UIImage(systemName: "magnifyingglass.circle.fill"), for: .normal)
        buttonSearch.layer.backgroundColor = UIColor.darkGray.cgColor
        buttonSearch.tintColor = .white
        buttonSearch.layer.cornerRadius = 10
        
        buttonSearch.layer.shadowOffset = .zero
        buttonSearch.layer.shadowRadius = 4
        buttonSearch.layer.shadowOpacity = 0.7
        
        buttonSearch.translatesAutoresizingMaskIntoConstraints = false
        buttonSearch.isHidden = true
        self.addSubview(buttonSearch)
    }
    
    func initConstraints(){
        NSLayoutConstraint.activate([
            //codes omitted...
            buttonSearch.bottomAnchor.constraint(equalTo: buttonCurrentLocation.bottomAnchor),
            buttonSearch.centerXAnchor.constraint(equalTo: self.safeAreaLayoutGuide.centerXAnchor),
            buttonSearch.heightAnchor.constraint(equalTo: buttonCurrentLocation.heightAnchor)
        ])
    }
    //codes omitted...
}

```
{% endcode %}

Now, let's create the files related to the Bottom Search Sheet in the project: SearchViewController.swift, SearchBottomSheet.swift, SearchTableViewCell.swift, and SearchTableViewManager.swift.&#x20;

![](</gitbook-assets/Screenshot 2023-06-15 at 1.31.59 PM.png>)

Then we set up the Bottom Search Sheet following the example in [Broken link](broken-reference "mention").&#x20;

## Bottom Search Sheet

### SearchViewController.swift

Let's add the following code to the file:

{% code lineNumbers="true" %}
```swift
//
//  SearchViewController.swift
//  App14
//
//  Created by Sakib Miazi on 6/15/23.
//

import UIKit
import MapKit

class SearchViewController: UIViewController {

    let searchBottomSheet = SearchBottomSheet()

    override func loadView() {
        view = searchBottomSheet
    }
    
    override func viewDidLoad() {
        super.viewDidLoad()
        searchBottomSheet.tableViewSearchResults.delegate = self
        searchBottomSheet.tableViewSearchResults.dataSource = self
        searchBottomSheet.searchBar.delegate = self
        
        searchBottomSheet.tableViewSearchResults.separatorStyle = .none
        
    }
    
}

extension SearchViewController: UISearchBarDelegate{
    func searchBar(_ searchBar: UISearchBar, textDidChange searchText: String) {
        
    }
    
    func searchBarCancelButtonClicked(_ searchBar: UISearchBar) {
        self.dismiss(animated: true)
    }
}
```
{% endcode %}

### SearchBottomSheet.swift

Let's add the following code to the file:

{% code lineNumbers="true" %}
```swift
//
//  SearchBottomSheet.swift
//  App14
//
//  Created by Sakib Miazi on 6/15/23.
//

import UIKit

class SearchBottomSheet: UIView {
    var searchBar: UISearchBar!
    var tableViewSearchResults: UITableView!
    override init(frame: CGRect) {
        super.init(frame: frame)
        backgroundColor = .white
        setupSearchBar()
        setupTableViewSearchResults()
        initConstraints()
    }
    
    func setupSearchBar(){
        searchBar = UISearchBar()
        searchBar.placeholder = "Search places..."
        searchBar.showsCancelButton = true
        searchBar.autocapitalizationType = .none
        searchBar.translatesAutoresizingMaskIntoConstraints = false
        self.addSubview(searchBar)
    }
    func setupTableViewSearchResults(){
        tableViewSearchResults = UITableView()
        tableViewSearchResults.register(SearchTableViewCell.self, forCellReuseIdentifier: Configs.searchTableViewID)
        tableViewSearchResults.translatesAutoresizingMaskIntoConstraints = false
        self.addSubview(tableViewSearchResults)
    }
    
    func initConstraints(){
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

### SearchTableViewCell.swift

Let's add the following code to the file:

{% code lineNumbers="true" %}
```swift
//
//  SearchTableViewCell.swift
//  App14
//
//  Created by Sakib Miazi on 6/15/23.
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
            labelTitle.heightAnchor.constraint(equalToConstant: 20),
            labelTitle.widthAnchor.constraint(lessThanOrEqualTo: wrapperCellView.widthAnchor),
            
            wrapperCellView.heightAnchor.constraint(equalToConstant: 40)
        ])
        
    }
    
    required init?(coder: NSCoder) {
        fatalError("init(coder:) has not been implemented")
    }

}
```
{% endcode %}

### SearchTableViewManager.swift

Let's add the following code to the file:

{% code lineNumbers="true" %}
```swift
//
//  SearchTableViewManager.swift
//  App14
//
//  Created by Sakib Miazi on 6/15/23.
//

import Foundation
import UIKit

extension SearchViewController: UITableViewDelegate, UITableViewDataSource{
    func tableView(_ tableView: UITableView, numberOfRowsInSection section: Int) -> Int {
        return mapItems.count
    }
    
    func tableView(_ tableView: UITableView, cellForRowAt indexPath: IndexPath) -> UITableViewCell {
        let cell = tableView.dequeueReusableCell(withIdentifier: Configs.searchTableViewID, for: indexPath) as! SearchTableViewCell
        
        return cell
    }
    
    func tableView(_ tableView: UITableView, didSelectRowAt indexPath: IndexPath) {
        
    }
}
```
{% endcode %}

## Displaying the Bottom Search Sheet

We need to add an action to the search button in ViewController. And then display the bottom search sheet.

Let's add the following code in ViewController.swift file:

{% code lineNumbers="true" %}
```swift
//
//  ViewController.swift
//  App14
//
//  Created by Sakib Miazi on 6/14/23.
//

import UIKit
import MapKit

class ViewController: UIViewController {
    //codes omitted...
    override func viewDidLoad() {
        super.viewDidLoad()
        
        title = "Search in Map"
        navigationController?.navigationBar.prefersLargeTitles = true
        //codes omitted...
        
        //MARK: add action for bottom search button tap...
        mapView.buttonSearch.addTarget(self, action: #selector(onButtonSearchTapped), for: .touchUpInside)
        //codes omitted...
    }
    //codes omitted...
    @objc func onButtonSearchTapped(){
        
        //MARK: Setting up bottom search sheet...
        let searchViewController  = SearchViewController()
        let navForSearch = UINavigationController(rootViewController: searchViewController)
        navForSearch.modalPresentationStyle = .pageSheet
        
        if let searchBottomSheet = navForSearch.sheetPresentationController{
            searchBottomSheet.detents = [.medium(), .large()]
            searchBottomSheet.prefersGrabberVisible = true
        }
        
        present(navForSearch, animated: true)
    }

}
```
{% endcode %}

In the above code:

* On lines 25 through 38, we handle the action when the user taps on the search button.&#x20;
  * We create the bottom search sheet and embed it in a navigation controller.
  * Then we define the presentation style, detents, and grabber for the bottom search sheet.
  * Finally, present the sheet.

If we run the app now:

<figure><img src="/gitbook-assets/14.seventy.gif" alt=""><figcaption></figcaption></figure>

So, our bottom search sheet is working!

## Searching Nearby Places

Here we have to type something on the search bar, and depending on what we type, it should display the list of related places in the search results table view. So, let's open SearchViewController.swift and put in the following code to add a delegate to mapview:

{% code lineNumbers="true" %}
```swift
//
//  SearchViewController.swift
//  App14
//
//  Created by Sakib Miazi on 6/15/23.
//

import UIKit
import MapKit

class SearchViewController: UIViewController {
    
    var delegateToMapView: ViewController!
    
    var mapItems = [MKMapItem]()
    //codes omitted...
        
}

extension SearchViewController: UISearchBarDelegate{
    func searchBar(_ searchBar: UISearchBar, textDidChange searchText: String) {
    }
    
    func searchBarCancelButtonClicked(_ searchBar: UISearchBar) {
        self.dismiss(animated: true)
    }
}
```
{% endcode %}

In the above code, on line 13, we declare a delegate variable to the ViewController where the map view is.

Now, let's create a new file named LoadPlaces.swift in the group "Map Screen." ![](</gitbook-assets/Screenshot 2023-06-15 at 7.40.50 PM.png>)

Let's write the following code in the file:

{% code lineNumbers="true" %}
```swift
//
//  LoadPlaces.swift
//  App14
//
//  Created by Sakib Miazi on 6/15/23.
//

import Foundation
import CoreLocation
import MapKit

extension ViewController{
    func loadPlacesAround(query: String){
        var mapItems = [MKMapItem]()
        
        let searchRequest = MKLocalSearch.Request()
        searchRequest.naturalLanguageQuery = query


        // Set the region to an associated map view's region.
        searchRequest.region = mapView.mapView.region


        let search = MKLocalSearch(request: searchRequest)
        search.start { (response, error) in
            guard let response = response else {
                // Handle the error.
                return
            }
            mapItems = response.mapItems
            
            for item in response.mapItems {
                if let name = item.name,
                    let location = item.placemark.location {
                    print("\(name), \(location)")
                }
            }
        }
    }
}
```
{% endcode %}

In the above code:

* We import CoreLocation and MapKit libraries to search places.
* We extend the ViewController class and define the method `loadPlacesAround()` where we take a String parameter named `query`.&#x20;
* We use `MKLocalSearch` service from Apple Maps to search for places.
* On line 16, we create a search request instance.
* On line 17, we set the `naturalLanguageQuery` of the local search service to the parameter `query`.
* Now, the search request needs a region, right? We won't be searching the whole world. So on line 21, we set the search region to the current map view region. It means I will be looking for places close to the region we see on the map inside the screen.
* On lines 24 through 38, we run the search for the places related to the query.

Now, let's open SearchViewController.swift file again and call `loadPlacesAround()` method when the user type something:

{% code lineNumbers="true" %}
```swift
//
//  SearchViewController.swift
//  App14
//
//  Created by Sakib Miazi on 6/15/23.
//

class SearchViewController: UIViewController {
    
    var delegateToMapView: ViewController!
    
    //codes omitted...
    
}

extension SearchViewController: UISearchBarDelegate{
    func searchBar(_ searchBar: UISearchBar, textDidChange searchText: String) {
        delegateToMapView.loadPlacesAround(query: searchText)
    }
    
    func searchBarCancelButtonClicked(_ searchBar: UISearchBar) {
        self.dismiss(animated: true)
    }
}

```
{% endcode %}

In the above code, on line 18, we call the `loadPlacesAround(query: searchText)` method of map screen using the delegate. We send the text the user writes on the search bar.

We need to update ViewController.swift file to initialize the delegateToMapView variable. So, let's initialize it as the following code:

{% code lineNumbers="true" %}
```swift
//
//  ViewController.swift
//  App14
//
//  Created by Sakib Miazi on 6/14/23.
//
class ViewController: UIViewController {
    //codes omitted...
    
    @objc func onButtonSearchTapped(){
        
        //MARK: Setting up bottom search sheet...
        let searchViewController  = SearchViewController()
        searchViewController.delegateToMapView = self
        
        let navForSearch = UINavigationController(rootViewController: searchViewController)
        navForSearch.modalPresentationStyle = .pageSheet
        
        if let searchBottomSheet = navForSearch.sheetPresentationController{
            searchBottomSheet.detents = [.medium(), .large()]
            searchBottomSheet.prefersGrabberVisible = true
        }
        
        present(navForSearch, animated: true)
    }
}
//codes omitted...
```
{% endcode %}

In the above code, on line 14, we initialize `delegateToMapView` variable of the search view controller to `self`.

Let's run the app.

<figure><img src="/gitbook-assets/14.seventy1.gif" alt=""><figcaption></figcaption></figure>

The results are getting printed in the output area in the above demo. The results are related to the search query "coffee." It fetches all the coffee shops around.

## Displaying the search results in the search table view

Now we have the search results in the map screen, so we need to send them back to the search result table view. We will use Notification Center for that. We need to observe the data from the search bottom sheet. We post the notification from the map screen.

### Setting an observer from the bottom search sheet

Open SearchViewController.swift file, and put the following code there:

{% code lineNumbers="true" %}
```swift
//
//  SearchViewController.swift
//  App14
//
//  Created by Sakib Miazi on 6/15/23.
//

import UIKit
import MapKit

class SearchViewController: UIViewController {
    
    var delegateToMapView: ViewController!
    
    //codes omitted...
    
    override func viewDidLoad() {
        super.viewDidLoad()
        //codes omitted... 
        notificationCenter.addObserver(
            self,
            selector: #selector(notificationForPlaces(notification:)),
            name: .placesFromMap,
            object: nil
        )
        
    }
    
    @objc func notificationForPlaces(notification: Notification){
        mapItems = notification.object as! [MKMapItem]
        self.searchBottomSheet.tableViewSearchResults.reloadData()
    }
    
}

extension SearchViewController: UISearchBarDelegate{
    func searchBar(_ searchBar: UISearchBar, textDidChange searchText: String) {
        delegateToMapView.loadPlacesAround(query: searchText)
    }
    
    func searchBarCancelButtonClicked(_ searchBar: UISearchBar) {
        self.dismiss(animated: true)
    }
}
```
{% endcode %}

In the above code:&#x20;

* We observe the notification center on lines 20 through 25.&#x20;
* On lines 29 through 32, we define the method for handling the notification received event.
  * We basically receive an array of map items. Then we have to display them in the table view.&#x20;

Let's open SearchTableViewManager.swift file and add the following code to display the map items on the cells:

{% code lineNumbers="true" %}
```swift
//
//  SearchTableViewManager.swift
//  App14
//
//  Created by Sakib Miazi on 6/15/23.
//

import Foundation
import UIKit

extension SearchViewController: UITableViewDelegate, UITableViewDataSource{
    //codes omitted...
    func tableView(_ tableView: UITableView, cellForRowAt indexPath: IndexPath) -> UITableViewCell {
        let cell = tableView.dequeueReusableCell(withIdentifier: Configs.searchTableViewID, for: indexPath) as! SearchTableViewCell
        if let name = mapItems[indexPath.row].name{
                cell.labelTitle.text = name
        }
        return cell
    }
    //codes omitted...
}
```
{% endcode %}

In the above code:

* On lines 15 through 17, we set the text of the cell's `labelTitle` to the name of the current map item.

### Posting notification from Map Screen

Let's open LoadPlaces.swift file, and put the following code there:

{% code lineNumbers="true" %}
```swift
//
//  LoadPlaces.swift
//  App14
//
//  Created by Sakib Miazi on 6/15/23.
//

import Foundation
import CoreLocation
import MapKit

extension ViewController{
    func loadPlacesAround(query: String){
        //MARK: initializing the notification center...
        let notificationCenter = NotificationCenter.default
        
        var mapItems = [MKMapItem]()
        
        let searchRequest = MKLocalSearch.Request()
        searchRequest.naturalLanguageQuery = query


        // Set the region to an associated map view's region.
        searchRequest.region = mapView.mapView.region


        let search = MKLocalSearch(request: searchRequest)
        search.start { (response, error) in
            guard let response = response else {
                // Handle the error.
                return
            }
            mapItems = response.mapItems
            
            for item in response.mapItems {
                if let name = item.name,
                    let location = item.placemark.location {
                    print("\(name), \(location)")
                }
            }
            
            //MARK: posting the search results...
            notificationCenter.post(name: .placesFromMap, object: mapItems)
        }
    }
}
```
{% endcode %}

In the above code:

* On line 15, we initialize the notification center.
* On line 43, we post the map items we fetched to the notification center.

Let's run the app again:

<figure><img src="/gitbook-assets/14.seventy3.gif" alt=""><figcaption></figcaption></figure>

**Great! We can see the search results!!! Now can we show the place on the map when we select it on the table view?**

## Code so far

{% file src="/gitbook-assets/App14_phase3.zip" %}



<!-- Merged from 14.4.-phase-4-display-searched-places-on-map.md -->

# 14.4. Phase 4: Display Searched Places on Map

The last part of our app is to show a place selected from the search results on the map and navigate to it.

The task seems complicated, but we already have the code to display the annotations for a place, right? The rest of it is pretty straightforward.

Let's open ViewController.swift file and add a method `showSelectedPlace(placeItem: MKMapItem)` there:

{% code lineNumbers="true" %}
```swift
//
//  ViewController.swift
//  App14
//
//  Created by Sakib Miazi on 6/14/23.
//

import UIKit
import MapKit

class ViewController: UIViewController {
    //codes omitted...
    
    //MARK: show selected place on map...
    func showSelectedPlace(placeItem: MKMapItem){
        let coordinate = placeItem.placemark.coordinate
        mapView.mapView.centerToLocation(
            location: CLLocation(
                latitude: coordinate.latitude,
                longitude: coordinate.longitude
            )
        )
        let place = Place(
            title: placeItem.name!,
            coordinate: coordinate,
            info: placeItem.description
        )
        mapView.mapView.addAnnotation(place)
    }

}
//codes omitted...
```
{% endcode %}

In the above code:

* On line 16, we fetch the coordinate from the map item.
* On lines 17 through 22, we center the map view around the coordinate.
* On lines 23 through 27, we create a Place object from the map item.
* On line 28, we add the annotation view to the place.

Now we need to call `showSelectedPlace()` method when a search result cell is tapped from the bottom search sheet. So, let's open SearchTableViewManager.swift file and update the tableView() method with parameter `didSelectRowAt.`

{% code lineNumbers="true" %}
```swift
extension SearchViewController: UITableViewDelegate, UITableViewDataSource{
    //codes omitted...
    
    func tableView(_ tableView: UITableView, didSelectRowAt indexPath: IndexPath) {
        delegateToMapView.showSelectedPlace(placeItem: mapItems[indexPath.row])
        self.dismiss(animated: true)
    }
}
```
{% endcode %}

In the above code, on line 5, we call the `showSelectedPlace()` method with the selected place.

Nice! Let's try our app now.

<figure><img src="/gitbook-assets/14.seventy6.gif" alt=""><figcaption></figcaption></figure>

Awesome!!! Now we built a pretty useful basic place search application!



<!-- Merged from 14.5.-reference-code.md -->

# 14.5. Reference Code

{% file src="/gitbook-assets/App14.zip" %}

---

## Guided Practice Challenges

Before moving on to the next topic, try these low-stakes practice challenges in Xcode. They will build the exact muscle memory you need:

### Challenge 1: Experimentation
**The Scenario:** You've just learned about MapKit & Location.
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

