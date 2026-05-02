import os
import re

docs_dir = "/Users/nsm/iOS-Notes/content/docs"

template = """
**Estimated effort:** 1-2 hours this topic
**Format:** Asynchronous online
**Prerequisites:** Previous iOS topics

{{< hint info >}}
**🎯 Topic Mission:** 
In this module, we will explore **{title}** and learn how to integrate it into our iOS applications. Your mission is to understand the mechanics behind this concept and write robust Swift code.
{{< /hint >}}

---

## Learning Objectives

By the end of this session, you will be able to:
1. Understand the core concepts of {title}.
2. Implement {title} in an Xcode project.
3. Apply best practices to ensure clean and maintainable code.

---

## The Story So Far...

We have been progressively building our knowledge of iOS and Swift. In this module, we will expand our toolkit by diving into {title}. 
Open your current Xcode project or start a new Playground to follow along with the hands-on material.

---

## Walkthrough: Exploring {title}

> 📁 **Target Project** — Follow along by building the mini-app presented in the steps below, or integrate these concepts into your own ongoing projects.

{content}

---

## Guided Practice Challenges

Before moving on to the next topic, try these low-stakes practice challenges in Xcode. They will build the exact muscle memory you need:

### Challenge 1: Experimentation
**The Scenario:** You've just learned about {title}.
**The Task:** Experiment with the code snippets provided above. Can you alter the behavior by changing the parameters or combining it with concepts from previous modules?

### Challenge 2: From Scratch
**The Task:** Try implementing the core feature of this module in a completely blank Xcode project without looking at the reference code. Rely on Xcode's autocomplete and standard Apple documentation.

---

## References

1. [Apple Developer Documentation](https://developer.apple.com/documentation/)
2. [Swift Language Guide](https://docs.swift.org/swift-book/)
3. [Human Interface Guidelines](https://developer.apple.com/design/human-interface-guidelines/)

---

## Getting Help

Because this course is fully asynchronous, here's how to get unstuck:

- **Piazza** is the primary help channel. When asking a question, include: (1) what you're trying to do, (2) what you've tried, (3) the exact Xcode error message.
- **TA office hours** — check the Canvas calendar. Show up, share your screen, and get help.
- **Instructor office hours** — by appointment for deeper issues (design questions, project direction).
"""

def process_file(file_path):
    with open(file_path, 'r') as f:
        text = f.read()

    # If the file is just a structural container with {{< section >}}, ignore it.
    if "{{< section >}}" in text and len(text) < 500:
        return

    # Extract title from frontmatter
    title = "this topic"
    match = re.search(r'^---\n.*?title:\s*"(.*?)".*?\n---', text, flags=re.DOTALL)
    if match:
        title = match.group(1)

    # Separate frontmatter and content
    parts = re.split(r'^---\n.*?\n---\n', text, maxsplit=1, flags=re.DOTALL)
    if len(parts) == 2:
        frontmatter_block = re.match(r'^---\n.*?\n---\n', text, flags=re.DOTALL).group(0)
        content = parts[1].strip()
    else:
        return # invalid format

    # If it already has the pedagogy template, skip it
    if "Topic Mission" in content or "Getting Help" in content:
        return

    # Generate new content
    new_content = template.format(title=title, content=content)

    # Write back
    with open(file_path, 'w') as f:
        f.write(frontmatter_block)
        f.write(new_content)
        f.write("\n")

def main():
    for root, dirs, files in os.walk(docs_dir):
        for file in files:
            if file == "_index.md":
                process_file(os.path.join(root, file))

if __name__ == "__main__":
    main()
