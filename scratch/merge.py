import os
import re

def natural_sort_key(s):
    return [int(text) if text.isdigit() else text.lower() for text in re.split('([0-9]+)', s)]

def process_directory(dir_path):
    subdirs = []
    md_files = []
    
    for item in os.listdir(dir_path):
        item_path = os.path.join(dir_path, item)
        if os.path.isdir(item_path):
            subdirs.append(item_path)
            process_directory(item_path)
        elif item.endswith('.md') and item != '_index.md':
            md_files.append(item_path)
            
    index_file = os.path.join(dir_path, '_index.md')
    if not os.path.exists(index_file):
        with open(index_file, 'w') as f:
            title = os.path.basename(dir_path).replace('-', ' ').title()
            f.write(f"---\ntitle: \"{title}\"\n---\n\n")
            
    md_files.sort(key=lambda x: natural_sort_key(os.path.basename(x)))
    
    if md_files:
        with open(index_file, 'a') as f:
            f.write('\n\n')
            for md_file in md_files:
                with open(md_file, 'r') as mf:
                    content = mf.read()
                    # strip frontmatter if present
                    content = re.sub(r'^---\n.*?\n---\n', '', content, flags=re.DOTALL)
                    f.write(f"\n\n<!-- Merged from {os.path.basename(md_file)} -->\n\n")
                    f.write(content.strip())
                    f.write('\n\n')
                os.remove(md_file)
            
    # If this directory has subdirectories, append {{< section >}} so it lists them!
    if subdirs:
        with open(index_file, 'a') as f:
            f.write('\n\n## Table of Contents\n\n{{< section >}}\n')

docs_dir = "/Users/nsm/iOS-Notes/content/docs"
for mod in os.listdir(docs_dir):
    mod_path = os.path.join(docs_dir, mod)
    # Only process the 7 modules we created
    if os.path.isdir(mod_path) and mod.startswith("0"):
        process_directory(mod_path)

print("Merging complete.")
