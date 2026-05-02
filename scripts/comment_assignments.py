import os
import re

directory = 'lessons'

for filename in os.listdir(directory):
    if filename.endswith('.md'):
        filepath = os.path.join(directory, filename)
        with open(filepath, 'r') as file:
            content = file.read()
        
        # Check if already commented out
        if '<!--\n## Weekly Assignment' in content or '<!--\n\n## Weekly Assignment' in content:
            continue
            
        # The regex captures the "## Weekly Assignment" and everything up to the next "## " or end of file
        # Using a lookahead (?=\n## |\Z) ensures we don't consume the next section's heading
        pattern = re.compile(r'(^## Weekly Assignment.*?(?=\n## |\Z))', re.MULTILINE | re.DOTALL)
        
        new_content = pattern.sub(r'<!--\n\1\n-->', content)
        
        if new_content != content:
            print(f"Commented out Weekly Assignment in {filepath}")
            with open(filepath, 'w') as file:
                file.write(new_content)

print("Done")
