import os
import re

def update_module_03():
    filepath = 'lessons/Module_03_Introduction_To_Uikit.md'
    if not os.path.exists(filepath): return
    with open(filepath, 'r') as f:
        content = f.read()

    # Update UIButton setup
    content = content.replace(
        'buttonClickMe = UIButton(type: .system)',
        'buttonClickMe = UIButton(type: .system)\n        var config = UIButton.Configuration.filled()\n        buttonClickMe.configuration = config'
    )
    content = content.replace(
        'buttonSend = UIButton(type: .system)',
        'buttonSend = UIButton(type: .system)\n        var config = UIButton.Configuration.filled()\n        buttonSend.configuration = config'
    )
    content = content.replace(
        'buttonSubmit = UIButton(type: .system)',
        'buttonSubmit = UIButton(type: .system)\n        var config = UIButton.Configuration.filled()\n        buttonSubmit.configuration = config'
    )
    content = content.replace(
        'buttonSendMood = UIButton(type: .system)',
        'buttonSendMood = UIButton(type: .system)\n        var config = UIButton.Configuration.filled()\n        buttonSendMood.configuration = config'
    )

    with open(filepath, 'w') as f:
        f.write(content)
    print("Updated Module 03")

def update_module_05():
    filepath = 'lessons/Module_05_Networking_And_Apis.md'
    if not os.path.exists(filepath): return
    with open(filepath, 'r') as f:
        content = f.read()

    # Remove Alamofire imports
    content = re.sub(r'import Alamofire\n', '', content)
    
    # Update instructional text
    content = content.replace('Fetching Data with AlamoFire', 'Fetching Data with URLSession & Async/Await')
    content = content.replace('Using Alamofire for text responses', 'Using URLSession for text responses')
    content = content.replace('First of all, you need to **import the Alamofire library**.', 'We will use native `URLSession` along with `async/await`.')
    content = content.replace('The \'getall\' endpoint with Alamofire', 'The \'getall\' endpoint with Async/Await')
    
    # We will need more targeted replacements here but let's do the simple ones first
    
    with open(filepath, 'w') as f:
        f.write(content)
    print("Updated Module 05 simple text")

if __name__ == '__main__':
    update_module_03()
    update_module_05()
