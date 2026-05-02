import os
import re

directory = 'lessons'

def swap_sections(filepath):
    with open(filepath, 'r') as file:
        content = file.read()
    
    # We use a regex that matches `\n## ` or `^## `
    # However, a simpler way is to split by `\n## `
    
    # Let's find the boundaries using regex
    # We want to find the exact text of both sections.
    # A section starts with `## SectionTitle` and ends before the next `## ` or EOF.
    
    pattern = re.compile(r'^## (.*?)(?=\n## |\Z)', re.MULTILINE | re.DOTALL)
    
    # We can't just split because we want to preserve everything exactly, including `---`.
    # Let's split by `\n## ` and manually prepend it back.
    # First, let's normalize the file to make sure it doesn't start with `## ` (it shouldn't, it starts with `# `)
    
    parts = re.split(r'\n## ', content)
    
    if len(parts) <= 1:
        return
        
    guided_idx = -1
    code_idx = -1
    
    for i in range(1, len(parts)):
        if parts[i].startswith('Guided Practice Challenges'):
            guided_idx = i
        elif parts[i].startswith('Code Walkthrough'):
            code_idx = i
            
    if guided_idx != -1 and code_idx != -1:
        print(f"Swapping in {filepath}")
        # Swap the elements
        parts[guided_idx], parts[code_idx] = parts[code_idx], parts[guided_idx]
        
        # Rejoin
        new_content = parts[0] + '\n## ' + '\n## '.join(parts[1:])
        with open(filepath, 'w') as file:
            file.write(new_content)
    else:
        print(f"Could not find both sections in {filepath}")

for filename in os.listdir(directory):
    if filename.endswith('.md'):
        swap_sections(os.path.join(directory, filename))

print("Done")
