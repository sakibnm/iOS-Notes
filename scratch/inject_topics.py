import re

with open("scratch/topics_js.txt", "r") as f:
    topics_js = f.read()

with open("assets/lesson.js", "r") as f:
    lesson_js = f.read()

# Replace the TOPICS object
new_lesson_js = re.sub(r'const TOPICS = \{[\s\S]*?\};\n', topics_js, lesson_js)

with open("assets/lesson.js", "w") as f:
    f.write(new_lesson_js)
