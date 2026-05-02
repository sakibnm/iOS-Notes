import os
import re
from pathlib import Path

docs_dir = Path("/Users/nsm/iOS-Notes/content/docs")

def adjust_file(file_path):
    text = file_path.read_text()
    
    # 1. Remove <!-- Merged from ... --> comments
    text = re.sub(r'<!-- Merged from .*? -->\n*', '', text)
    
    # 2. Adjust headers
    lines = text.splitlines()
    new_lines = []
    
    for line in lines:
        if line.startswith("## Walkthrough:"):
            new_lines.append(line)
            continue
            
        if line.startswith("## Guided Practice Challenges") or line.startswith("## References") or line.startswith("## Getting Help"):
            new_lines.append(line)
            continue
            
        m = re.match(r'^(#{1,6})\s+(?:(\d+(?:\.\d+)*)\.?\s+)?(.*)', line)
        if m:
            level_str = m.group(1)
            number_str = m.group(2)
            title_str = m.group(3)
            
            if title_str in ["Learning Objectives", "The Story So Far...", "Table of Contents", "Guided Practice Challenges", "References", "Getting Help"]:
                new_lines.append(line)
                continue
                
            level = len(level_str)
            if number_str or level < 3:
                new_lines.append(f"### {title_str.strip()}")
            else:
                new_lines.append(f"{'#' * level} {title_str.strip()}")
        else:
            new_lines.append(line)
            
    file_path.write_text('\n'.join(new_lines) + '\n')

def main():
    for f in docs_dir.glob("*/_index.md"):
        adjust_file(f)
        print(f"Adjusted {f.name} in {f.parent.name}")

if __name__ == "__main__":
    main()
