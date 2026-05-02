import os
import shutil
import re

docs_dir = "/Users/nsm/iOS-Notes/content/docs"

modules = {
    "01-getting-started": {
        "title": "Module 1: Getting Started",
        "weight": 100,
        "folders": [
            ("getting-started", "getting-started", "Getting Started")
        ]
    },
    "02-swift-fundamentals": {
        "title": "Module 2: Swift Fundamentals",
        "weight": 200,
        "folders": [
            ("swift-the-programming-language", "swift-the-programming-language", "Variables & Data Types"),
            ("2.-collections", "collections", "Collections"),
            ("3.-operators", "operators", "Operators"),
            ("4.-conditionals", "conditionals", "Conditionals"),
            ("5.-loops", "loops", "Loops"),
            ("6.-functions", "functions", "Functions"),
            ("7.-closures", "closures", "Closures"),
            ("8.-optionals.md", "optionals", "Optionals"),
            ("9.-creating-your-own-data-types", "custom-data-types", "Custom Data Types"),
            ("10.-protocols", "protocols", "Protocols"),
            ("11.-sorting-arrays", "sorting-arrays", "Sorting Arrays")
        ]
    },
    "03-introduction-to-uikit": {
        "title": "Module 3: Introduction to UIKit",
        "weight": 300,
        "folders": [
            ("ios-development-with-uikit", "creating-our-first-app", "Creating Our First App"),
            ("2.-designing-without-storyboards", "designing-without-storyboards", "Designing Without Storyboards"),
            ("3.-our-first-multi-screen-app", "multi-screen-apps", "Multi-Screen Apps"),
            ("4.-separating-code-view-from-the-controller", "mvc-architecture", "MVC Architecture")
        ]
    },
    "04-advanced-ui-components": {
        "title": "Module 4: Advanced UI Components",
        "weight": 400,
        "folders": [
            ("5.-uitableview-and-more", "uitableview", "UITableView"),
            ("8.-uiscrollview", "uiscrollview", "UIScrollView"),
            ("6.-uimenu-picking-images-from-gallery-and-camera-and-uiimageview", "uimenu-and-image-pickers", "UIMenu & Image Pickers"),
            ("useful-tools-and-ui-elements", "useful-ui-elements", "Useful UI Elements")
        ]
    },
    "05-networking-and-apis": {
        "title": "Module 5: Networking & APIs",
        "weight": 500,
        "folders": [
            ("10.-making-the-app-communicate-over-the-internet", "http-and-networking", "HTTP & Networking"),
            ("11.-working-with-json", "working-with-json", "Working with JSON")
        ]
    },
    "06-data-persistence-and-architecture": {
        "title": "Module 6: Architecture & Data Flow",
        "weight": 600,
        "folders": [
            ("7.-notification-center", "notification-center", "Notification Center"),
            ("decluttering-code", "clean-code-and-async", "Clean Code & Async")
        ]
    },
    "07-cloud-integrations-and-maps": {
        "title": "Module 7: Cloud Integrations & Maps",
        "weight": 700,
        "folders": [
            ("9.-cocoa-pods", "cocoapods", "CocoaPods"),
            ("12.-firebase-authentication-and-firestore", "firebase-auth-and-firestore", "Firebase Auth & Firestore"),
            ("13.-firebase-storage", "firebase-storage", "Firebase Storage"),
            ("14.-uimapkit-working-with-location-and-maps", "mapkit-and-location", "MapKit & Location")
        ]
    }
}

def prepend_frontmatter(file_path, title, weight):
    with open(file_path, "r") as f:
        content = f.read()
    
    # Remove existing frontmatter if any
    content = re.sub(r'^---\n.*?\n---\n', '', content, flags=re.DOTALL)
    
    with open(file_path, "w") as f:
        f.write("---\n")
        f.write(f"title: \"{title}\"\n")
        f.write(f"weight: {weight}\n")
        f.write("---\n")
        f.write(content)

def generate_index_md(path, title, weight, collapse=False):
    with open(os.path.join(path, "_index.md"), "w") as f:
        f.write("---\n")
        f.write(f"title: \"{title}\"\n")
        f.write(f"weight: {weight}\n")
        if collapse:
            f.write("bookCollapseSection: false\n") # Keep them open by default for easier reading
        f.write("---\n")

def main():
    for mod_dir, mod_info in modules.items():
        mod_path = os.path.join(docs_dir, mod_dir)
        os.makedirs(mod_path, exist_ok=True)
        generate_index_md(mod_path, mod_info["title"], mod_info["weight"], collapse=True)
        
        weight_counter = 10
        for old_name, new_name, title in mod_info["folders"]:
            old_path = os.path.join(docs_dir, old_name)
            new_path = os.path.join(mod_path, new_name)
            
            if os.path.exists(old_path):
                if os.path.isfile(old_path):
                    os.makedirs(new_path, exist_ok=True)
                    new_file_path = os.path.join(new_path, "_index.md")
                    shutil.move(old_path, new_file_path)
                    prepend_frontmatter(new_file_path, title, weight_counter)
                else:
                    shutil.move(old_path, new_path)
                    # Modify existing _index.md or create one
                    index_path = os.path.join(new_path, "_index.md")
                    if os.path.exists(index_path):
                        prepend_frontmatter(index_path, title, weight_counter)
                    else:
                        generate_index_md(new_path, title, weight_counter)
            else:
                print(f"Warning: {old_path} does not exist!")
            weight_counter += 10

if __name__ == "__main__":
    main()
