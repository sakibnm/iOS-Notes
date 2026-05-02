import os
import re

directory = 'lessons'

for filename in os.listdir(directory):
    if filename.endswith('.md'):
        filepath = os.path.join(directory, filename)
        with open(filepath, 'r') as file:
            content = file.read()
        
        # Remove "1. " from "## 1. Learning Objectives"
        content = re.sub(r'^##\s+\d+\.\s*', '## ', content, flags=re.MULTILINE)
        
        # Remove "Chapter 1 — " from "### Chapter 1 — Topic"
        content = re.sub(r'^###\s+Chapter\s+\d+\s*[-—:]\s*', '### ', content, flags=re.MULTILINE)
        
        with open(filepath, 'w') as file:
            file.write(content)

print("Done")
