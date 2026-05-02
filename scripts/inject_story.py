import re
import os

topics = [
    {
        "file": "Topic_05_Layouts_Dialogs_Navigation.md",
        "prev_zip": "topic_04_compose_basics.zip",
        "story": "built the basic SkyCast prototype with static Composables like the WeatherCard and CitySearchBar."
    },
    {
        "file": "Topic_06_ViewModel_StateFlow_Notifications.md",
        "prev_zip": "topic_05_layouts_dialogs_navigation.zip",
        "story": "wrapped the SkyCast prototype in a Material Scaffold and set up navigation routes to move between screens."
    },
    {
        "file": "Topic_07_Lists_LazyColumn.md",
        "prev_zip": "topic_06_viewmodel_stateflow.zip",
        "story": "moved our weather data out of the UI and into a ViewModel to survive configuration changes and introduced StateFlow."
    },
    {
        "file": "Topic_08_Gradle_Retrofit_Networking.md",
        "prev_zip": "topic_07_lists_lazycolumn.zip",
        "story": "implemented a LazyColumn to display a scrollable list of saved cities and forecast days."
    },
    {
        "file": "Topic_09_JSON_Robust_APIs.md",
        "prev_zip": "topic_08_networking_retrofit.zip",
        "story": "set up Gradle dependencies and configured Retrofit to fetch real weather data from the internet."
    },
    {
        "file": "Topic_10_Firebase_Auth_Firestore.md",
        "prev_zip": "topic_09_json_robust_apis.zip",
        "story": "parsed real JSON responses using Kotlinx Serialization and handled robust API errors."
    },
    {
        "file": "Topic_11_Storage_Room_DataStore.md",
        "prev_zip": "topic_10_firebase.zip",
        "story": "integrated Firebase Authentication so users can log in, and Firestore to save their favorite cities in the cloud."
    },
    {
        "file": "Topic_12_Location_Maps.md",
        "prev_zip": "topic_11_storage_room_datastore.zip",
        "story": "implemented Room Database and DataStore for local offline caching of weather data and user preferences."
    },
    {
        "file": "Topic_13_CameraX_Animations.md",
        "prev_zip": "topic_12_location_maps.zip",
        "story": "added location permissions and integrated Google Maps to show the user's current weather context."
    },
    {
        "file": "Topic_14_Project_Work_KMP_Kickoff.md",
        "prev_zip": "topic_13_camerax_animations.zip",
        "story": "used CameraX to let users snap a photo of the sky and added smooth Compose animations to our UI."
    },
    {
        "file": "Topic_15_Project_Work_Polish_Testing.md",
        "prev_zip": "topic_14_debugging_accessibility.zip",
        "story": "began migrating our core networking and data logic into a Kotlin Multiplatform shared module to prepare for an iOS release."
    }
]

base_dir = "/Users/nsm/cs4520/lessons"

for topic in topics:
    filepath = os.path.join(base_dir, topic["file"])
    if not os.path.exists(filepath):
        print(f"File not found: {filepath}")
        continue
        
    with open(filepath, "r") as f:
        content = f.read()
        
    # Check if already injected
    if "## The Story So Far..." in content:
        print(f"Already injected in {topic['file']}")
        continue

    # Create the block to inject
    story_block = f"""## The Story So Far...

In the previous topic, we {topic['story']}

To continue the story, **open your existing Android Studio project from the previous topic**. We will be directly building upon the code you wrote previously. 

> 🆘 **Lost your code?** If your previous project is broken or missing, don't worry! You can download a clean starting point here: [Starter Project: {topic['prev_zip']}](/downloads/{topic['prev_zip']}). 

---

"""
    
    # We want to insert this right before "## Code Walkthrough" or "## Walkthrough: Building SkyCast"
    # Topic 05 uses "## Walkthrough: Building SkyCast"
    # Topics 06-15 use "## Code Walkthrough"
    
    match = re.search(r'^(## Code Walkthrough|## Walkthrough: Building SkyCast)', content, re.MULTILINE)
    if match:
        idx = match.start()
        new_content = content[:idx] + story_block + content[idx:]
        
        # We also need to update the Walkthrough block to refer to the "Target Project" instead of just "Complete Walkthrough"
        # Often it looks like:
        # > 📁 **Download the complete walkthrough project** — [topic_XX.zip](/downloads/topic_XX.zip)
        # > Every code fragment in this section is taken from this project, which is a complete, runnable SkyCast snapshot at Topic X. Import into Android Studio and click Run.
        
        # Let's do a regex substitution for that common pattern in Topics 06-15
        new_content = re.sub(
            r"> 📁 \*\*Download the complete walkthrough project\*\* — \[.*?\.zip\]\(/downloads/.*\.zip\)\n>\n> Every code fragment in this section is taken from this project, which is a complete, runnable SkyCast snapshot at Topic \d+\. Import into Android Studio and click Run\.",
            r"> 📁 **Target Project Reference** — If you want to see the final, completed code for this specific module, you can download it here: [\g<0> -> actually I need to keep the zip name.",
            new_content
        )
        
        # A safer approach: just replace "Download the complete walkthrough project" with "Target Project Reference (Completed Code)"
        new_content = new_content.replace("> 📁 **Download the complete walkthrough project**", "> 📁 **Target Project Reference (Completed Code)**")
        new_content = new_content.replace("> Every code fragment in this section is taken from this project, which is a complete, runnable SkyCast snapshot", "> This project contains the complete, runnable SkyCast snapshot")
        
        with open(filepath, "w") as f:
            f.write(new_content)
        print(f"Updated {topic['file']}")
    else:
        print(f"Walkthrough heading not found in {topic['file']}")
