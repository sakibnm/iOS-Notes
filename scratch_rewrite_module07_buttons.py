import os
import re

filepath = 'lessons/Module_07_Cloud_Integrations_And_Maps.md'
if os.path.exists(filepath):
    with open(filepath, 'r') as f:
        content = f.read()

    # Update UIButton setup
    buttons = [
        'floatingButtonAddContact', 'buttonAdd', 'buttonTakePhoto', 
        'buttonLoading', 'buttonCurrentLocation', 'buttonSearch', 'buttonRegister'
    ]

    for btn in buttons:
        content = content.replace(
            f'{btn} = UIButton(type: .system)',
            f'{btn} = UIButton(type: .system)\n        var config = UIButton.Configuration.filled()\n        {btn}.configuration = config'
        )

    with open(filepath, 'w') as f:
        f.write(content)
    print("Updated UIButtons in Module 07")
