import os
import re
import shutil

src_dir = '.'
dest_dir = 'content/docs'
summary_file = 'SUMMARY.md'

# Directories to ignore
ignore_dirs = {'.git', '.gitbook', 'content', 'themes', 'public', 'static', 'layouts', 'scratch', 'hugo.toml'}

def copy_contents():
    for item in os.listdir(src_dir):
        if item in ignore_dirs or item == summary_file or item == "migrate.py":
            continue
            
        s = os.path.join(src_dir, item)
        d = os.path.join(dest_dir, item)
        
        if os.path.isdir(s):
            shutil.copytree(s, d, dirs_exist_ok=True)
        else:
            os.makedirs(os.path.dirname(d), exist_ok=True)
            shutil.copy2(s, d)

def process_markdown_files():
    # Rename README.md to _index.md
    for root, dirs, files in os.walk(dest_dir):
        for file in files:
            if file.lower() == 'readme.md':
                os.rename(os.path.join(root, file), os.path.join(root, '_index.md'))

def add_frontmatter():
    if not os.path.exists(summary_file):
        print(f"{summary_file} not found!")
        return

    with open(summary_file, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    weight = 10
    link_pattern = re.compile(r'\[(.*?)\]\((.*?)\)')
    
    for line in lines:
        match = link_pattern.search(line)
        if match:
            title = match.group(1).replace('"', '\\"')
            path = match.group(2)
            
            # Map README.md to _index.md
            if path.lower().endswith('readme.md'):
                path = path[:-9] + '_index.md'
                
            target_path = os.path.join(dest_dir, path)
            
            if os.path.exists(target_path):
                with open(target_path, 'r', encoding='utf-8') as tf:
                    content = tf.read()
                    
                # Only add frontmatter if not already there
                if not content.startswith('---'):
                    frontmatter = f"---\ntitle: \"{title}\"\nweight: {weight}\n---\n\n"
                    with open(target_path, 'w', encoding='utf-8') as tf:
                        tf.write(frontmatter + content)
            else:
                print(f"Warning: Target file {target_path} not found.")
                
            weight += 10

if __name__ == '__main__':
    print("Copying contents...")
    os.makedirs(dest_dir, exist_ok=True)
    copy_contents()
    
    print("Processing markdown files...")
    process_markdown_files()
    
    print("Adding frontmatter based on SUMMARY.md...")
    add_frontmatter()
    
    # Finally, if SUMMARY.md itself has an entry for the root README, handle it.
    # We should probably copy SUMMARY.md? No, Hugo uses the directory structure.
    print("Migration complete!")
