import os
import re
import shutil

docs_dir = "/Users/nsm/iOS-Notes/content/docs"

for module_name in os.listdir(docs_dir):
    module_path = os.path.join(docs_dir, module_name)
    if not os.path.isdir(module_path):
        continue
        
    parent_index = os.path.join(module_path, "_index.md")
    if not os.path.exists(parent_index):
        continue
        
    print(f"Processing module: {module_name}")
    
    with open(parent_index, "r") as f:
        parent_content = f.read()
        
    children = []
    
    for root, dirs, files in os.walk(module_path):
        if "_index.md" in files:
            child_index = os.path.join(root, "_index.md")
            
            if child_index == parent_index:
                continue
                
            with open(child_index, "r") as f:
                content = f.read()
                
            title_match = re.search(r'^title:\s*"(.*?)"', content, flags=re.MULTILINE)
            title = title_match.group(1) if title_match else os.path.basename(root)
            
            weight_match = re.search(r'^weight:\s*([0-9]+)', content, flags=re.MULTILINE)
            weight = int(weight_match.group(1)) if weight_match else 999
            
            clean_content = re.sub(r'^---\n.*?\n---\n', '', content, flags=re.DOTALL).strip()
            
            children.append({
                "dir": root,
                "title": title,
                "weight": weight,
                "content": clean_content
            })
            
    children.sort(key=lambda x: x["weight"])
    
    if not children:
        continue
        
    parent_content = parent_content.replace("{{< section >}}", "")
    
    appended_text = ""
    for child in children:
        appended_text += f"\n\n## {child['title']}\n\n{child['content']}\n"
        
    with open(parent_index, "w") as f:
        f.write(parent_content + appended_text)
        
    for item in os.listdir(module_path):
        item_path = os.path.join(module_path, item)
        if os.path.isdir(item_path):
            shutil.rmtree(item_path)
            print(f"  Deleted nested directory: {item}")

print("Done merging!")
