# 3.3. Send data back from Screen 2 to Screen 1

So, here is the goal for the extension of our current app:

* We will add a PickerView (selects one from a list of options) to the second screen (ShowViewController).
* The PickerView will show the user a list of moods: Happy, Meh, and Sad.
* The user selects a mood and sends the mood back to the first screen (ViewController).
* The first screen receives the mood and displays a corresponding image in an ImageView.

### Updating the screens with new UI elements.

**On ViewController,** we will add a new Label and an ImageView, as follows:

{% code lineNumbers="true" %}
```swift
//
//  ViewController.swift
//
import UIKit

class ViewController: UIViewController {
    
    var textFieldMessage: UITextField!
    var buttonSend: UIButton!
    var labelMood: UILabel!
    var imageMood: UIImageView!
    
    override func viewDidLoad() {
        super.viewDidLoad()
        // Do any additional setup after loading the view.
        
        //MARK: initializing the UI elements...
        
        // code in between is omitted...
        setupLabelMood()
        setupImageMood()
        
        //MARK: initializing the constraints...
        initConstraints()
        
        //MARK: on buttonSend tap...
        buttonSend.addTarget(self, action: #selector(onButtonSendTapped),
                             for: .touchUpInside)
    }
    
    // code in between is omitted...
    
    //labelMood...
    func setupLabelMood(){
        labelMood = UILabel()
        labelMood.translatesAutoresizingMaskIntoConstraints = false
        view.addSubview(labelMood)
    }
    
    //imageMood...
    func setupImageMood(){
        imageMood = UIImageView()
        imageMood.translatesAutoresizingMaskIntoConstraints = false
        view.addSubview(imageMood)
    }
    
    //updating constraints..
    func initConstraints(){
        NSLayoutConstraint.activate([
            // textFieldMessage constraints...
            textFieldMessage.centerXAnchor.constraint(equalTo: view.safeAreaLayoutGuide.centerXAnchor),
            textFieldMessage.topAnchor.constraint(equalTo: view.safeAreaLayoutGuide.topAnchor, constant: 32),
            
            // buttonSend constraints...
            buttonSend.centerXAnchor.constraint(equalTo: view.safeAreaLayoutGuide.centerXAnchor),
            buttonSend.topAnchor.constraint(equalTo: textFieldMessage.bottomAnchor, constant: 16),
            
            // labelMood constraints...
            labelMood.centerXAnchor.constraint(equalTo: view.safeAreaLayoutGuide.centerXAnchor),
            labelMood.topAnchor.constraint(equalTo: buttonSend.bottomAnchor, constant: 16),// labelMood constraints...
            
            // imageMood constraints...
            imageMood.centerXAnchor.constraint(equalTo: view.safeAreaLayoutGuide.centerXAnchor),
            imageMood.topAnchor.constraint(equalTo: labelMood.bottomAnchor, constant: 16),
        ])       
    }
}
```
{% endcode %}

The `labelMood` will show the mood the user selected on ShowViewController, and the ImageView `imageMood` will show an image corresponding to the mood.

**Now on ShowViewController,** we will add a new Label, a PickerView, and a Button, as follows:

{% code lineNumbers="true" %}
```swift
//
//  ShowViewController.swift
//
import UIKit

class ShowViewController: UIViewController {
    var labelMessage: UILabel!
    var labelMoodInstructions: UILabel!
    var moodPicker: UIPickerView!
    var buttonSendMood: UIButton!
    
    override func viewDidLoad() {
        super.viewDidLoad()
        
        //omitting the code in between...
        
        setupLabelMoodInstructions()
        setupMoodPicker()
        setupButtonSendMood()
        
        // MARK: setting up constraints...
        initConstraints()
    }
    
    //omitting the code in between...
    
    // setting up labelMoodInstructions...
    func setupLabelMoodInstructions(){
        labelMoodInstructions = UILabel()
        labelMoodInstructions.text = "How are you feeling today?"
        labelMoodInstructions.translatesAutoresizingMaskIntoConstraints = false
        view.addSubview(labelMoodInstructions)
    }
    
    // setting up mood picker...
    func setupMoodPicker(){
        moodPicker = UIPickerView()
        moodPicker.isUserInteractionEnabled = true
        moodPicker.translatesAutoresizingMaskIntoConstraints = false
        view.addSubview(moodPicker)
    }
    
    // setting up buttonSendMood...
    func setupButtonSendMood(){
        buttonSendMood = UIButton(type: .system)
        buttonSendMood.setTitle("Send Mood back!", for: .normal)
        buttonSendMood.translatesAutoresizingMaskIntoConstraints = false
        view.addSubview(buttonSendMood)
    }
    
    //omitting the code in between...
    
    // MARK: setting up constraints...
    func initConstraints(){
        NSLayoutConstraint.activate([
            //labelMessage constraints...
            labelMessage.centerXAnchor.constraint(equalTo: view.safeAreaLayoutGuide.centerXAnchor),
            labelMessage.topAnchor.constraint(equalTo: view.safeAreaLayoutGuide.topAnchor, constant: 32),
            
            //labelMoodInstructions constraints...
            labelMoodInstructions.centerXAnchor.constraint(equalTo: view.safeAreaLayoutGuide.centerXAnchor),
            labelMoodInstructions.topAnchor.constraint(equalTo: labelMessage.bottomAnchor, constant: 16),
            
            //mood picker constraints...
            moodPicker.centerXAnchor.constraint(equalTo: view.safeAreaLayoutGuide.centerXAnchor),
            moodPicker.topAnchor.constraint(equalTo: labelMoodInstructions.bottomAnchor, constant: 16),
            
            //buttonSendMood constraints...
            buttonSendMood.centerXAnchor.constraint(equalTo: view.safeAreaLayoutGuide.centerXAnchor),
            buttonSendMood.topAnchor.constraint(equalTo: moodPicker.bottomAnchor, constant: 16),
            
        ])
    }
}    
```
{% endcode %}

Here, `labelMoodInstructions` shows the message: "How are you feeling today?"

Then we place the `moodPicker` and finally put `buttonSendMood` at the bottom.

If we run the app now, we will see:

<figure><img src="../../.gitbook/assets/nine (1).gif" alt=""><figcaption></figcaption></figure>

Here, we do not see the two elements we added to ViewController, because `labelMood` and `imageMood` doesn't have anything to display.

On ShowViewController, we see there is an empty `moodPicker` and the newly added `buttonSendMood`.
