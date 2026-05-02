import re

with open("scratch/topics_html.txt", "r") as f:
    topics_html = f.read()

with open("index.html", "r") as f:
    html = f.read()

# Replace topics grid
html = re.sub(r'<div class="topics">[\s\S]*?</div>\n\n      <div class="optional-modules-container">', f'<div class="topics">\n{topics_html}\n      </div>\n\n      <div class="optional-modules-container">', html)

# Replace Hero and Meta
html = html.replace("Android &amp; Kotlin course materials.", "iOS &amp; Swift course materials.")
html = html.replace("Course materials &middot; Android &middot; Kotlin", "Course materials &middot; iOS &middot; Swift")
html = html.replace("Course materials · Android · Kotlin", "Course materials · iOS · Swift")
html = html.replace("introductory mobile application development course using Kotlin and Jetpack Compose", "introductory mobile application development course using Swift and UIKit")
html = html.replace("<dd>Kotlin · Compose · Firebase</dd>", "<dd>Swift · UIKit · Firebase</dd>")
html = html.replace("build Android apps", "build iOS apps")
html = html.replace("modern Kotlin-first stack", "modern Swift stack")
html = html.replace("Jetpack&nbsp;Compose", "UIKit")
html = html.replace("coroutines with Flow, and ViewModels with StateFlow", "MVC Architecture, Delegates, and Storyboards")

with open("index.html", "w") as f:
    f.write(html)
