import os
import re

filepath = 'lessons/Module_04_Advanced_Ui_Components.md'
if os.path.exists(filepath):
    with open(filepath, 'r') as f:
        content = f.read()

    # Update UIButton setup
    buttons = [
        'buttonAdd', 'buttonSelectType', 'buttonTakePhoto', 
        'button1', 'button2', 'button3', 'buttonSend', 'buttonSelect'
    ]

    for btn in buttons:
        content = content.replace(
            f'{btn} = UIButton(type: .system)',
            f'{btn} = UIButton(type: .system)\n        var config = UIButton.Configuration.filled()\n        {btn}.configuration = config'
        )
        content = content.replace(
            f'{btn} = UIButton(type: .infoDark)',
            f'{btn} = UIButton(type: .system)\n        var config = UIButton.Configuration.tinted()\n        {btn}.configuration = config'
        )

    with open(filepath, 'w') as f:
        f.write(content)
    print("Updated UIButtons in Module 04")
