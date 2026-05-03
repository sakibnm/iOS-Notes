import os

filepath = 'lessons/Module_07_Cloud_Integrations_And_Maps.md'
if os.path.exists(filepath):
    with open(filepath, 'r') as f:
        content = f.read()

    replacements = {
        '### Adding a CocoaPod module, Alamofire, to our project': '### Adding a CocoaPod module, SDWebImage, to our project',
        'As I said before, Alamofire is a widely used module for beginners to manage Internet data transmission. We will integrate Alamofire to App9.': 'SDWebImage is a widely used module for downloading and caching images from the internet. We will integrate SDWebImage to App9 as an example.',
        '* Search for Alamofire. On top of the search results, you will see something like \'**Alamofire 5.6.4.\'**': '* Search for SDWebImage. On top of the search results, you will see something like \'**SDWebImage 5.x.x.\'**',
        '* If you scroll down to **Installation,** you will see the instructions of how to install Alamofire using CocoaPods. Copy the line that says: `pod \'Alamofire\'`.': '* If you scroll down to **Installation,** you will see the instructions of how to install SDWebImage using CocoaPods. Copy the line that says: `pod \'SDWebImage\'`.',
        '* You will see, depending on the modules you added to the Podfile, it will install them. When it\'s done installing the pods, in this case, it is Alamofire, your project can use this CocoaPod module.': '* You will see, depending on the modules you added to the Podfile, it will install them. When it\'s done installing the pods, in this case, it is SDWebImage, your project can use this CocoaPod module.',
        '**Now, we have completed adding the \'Alamofire\' module to our project using CocoaPods.**': '**Now, we have completed adding the \'SDWebImage\' module to our project using CocoaPods.**'
    }

    for old, new in replacements.items():
        content = content.replace(old, new)

    with open(filepath, 'w') as f:
        f.write(content)
    print("Updated Cocoapods example to SDWebImage")
