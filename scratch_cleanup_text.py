import os

filepath = 'lessons/Module_05_Networking_And_Apis.md'
if os.path.exists(filepath):
    with open(filepath, 'r') as f:
        content = f.read()

    replacements = {
        'And add Alamofire to the project using Cocoapods. ( See [9.-cocoa-pods](../9.-cocoa-pods/ "mention")).': '',
        'We will use Alamofire to process the responses.': 'We will use `URLSession` to process the responses.',
        '* Then we use `url` to make a request with Alamofire. We use `AF` to use Alamofire functions. So, here we are creating an Alamofire request with the `url` we built.': '* Then we use `url` to make a request with `URLSession`. We use `URLSession.shared.data(from: url)` to fetch the data asynchronously.',
        'we need to use Alamofire to post the data to the API server.': 'we need to use `URLSession` to post the data to the API server.',
        'We need to use Alamofire to POST the new contact we created above to the server.': 'We need to use `URLSession` to POST the new contact we created above to the server.',
        'Let\'s create a new Xcode project, App11, and integrate Alamofire into the project using CocoaPods.': 'Let\'s create a new Xcode project, App11.',
        '### Creating the \'getall\' request using Alamofire': '### Creating the \'getall\' request using URLSession',
        'Import UIKit and Alamofire in this file.': 'Import UIKit in this file.'
    }

    for old, new in replacements.items():
        content = content.replace(old, new)

    with open(filepath, 'w') as f:
        f.write(content)
    print("Cleaned up remaining text references.")
