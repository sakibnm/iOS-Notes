import os
import re
import shutil

docs_dir = "/Users/nsm/iOS-Notes/content/docs"
lessons_dir = "/Users/nsm/iOS-Notes/lessons"

if not os.path.exists(lessons_dir):
    os.makedirs(lessons_dir)

topics = []

for root, dirs, files in os.walk(docs_dir):
    if "_index.md" in files:
        path = os.path.join(root, "_index.md")
        with open(path, "r") as f:
            content = f.read()
            
        if "{{< section >}}" in content and len(content) < 500:
            continue
            
        title_match = re.search(r'^title:\s*"(.*?)"', content, flags=re.MULTILINE)
        title = title_match.group(1) if title_match else "Unknown"
        
        weight_match = re.search(r'^weight:\s*([0-9]+)', content, flags=re.MULTILINE)
        weight = int(weight_match.group(1)) if weight_match else 999
        
        module = path.split(docs_dir + "/")[1].split("/")[0]
        module_weight = int(module.split("-")[0]) if module[0].isdigit() else 99
        
        global_weight = module_weight * 10000 + weight
        
        topics.append({
            "path": path,
            "title": title,
            "weight": global_weight
        })

topics.sort(key=lambda x: x["weight"])

topics_map = []
for i, topic in enumerate(topics):
    topic_num = str(i + 1).zfill(2)
    clean_title = re.sub(r'[^A-Za-z0-9_]', '', topic['title'].replace(' ', '_'))
    new_filename = f"Topic_{topic_num}_{clean_title}.md"
    new_path = os.path.join(lessons_dir, new_filename)
    
    with open(topic["path"], "r") as f:
        content = f.read()
        
    content = re.sub(r'^---\n.*?\n---\n', '', content, flags=re.DOTALL)
    
    # Optional: replace hugo shortcodes
    content = content.replace("{{< hint info >}}", "> [!TIP]")
    content = content.replace("{{< /hint >}}", "")
    
    with open(new_path, "w") as f:
        f.write(f"# {topic['title']}\n\n{content}")
        
    topics_map.append({
        "key": topic_num,
        "file": new_filename,
        "title": topic['title']
    })

# Write the mapping output to a temp file so we can read it and inject it
with open("scratch/topics_js.txt", "w") as f:
    f.write("  const TOPICS = {\n")
    for i, t in enumerate(topics_map):
        prev_key = f"'{topics_map[i-1]['key']}'" if i > 0 else "null"
        next_key = f"'{topics_map[i+1]['key']}'" if i < len(topics_map) - 1 else "null"
        safe_title = t['title'].replace("'", "\\'")
        f.write(f"    '{t['key']}': {{ file: '{t['file']}', title: '{safe_title}', prev: {prev_key}, next: {next_key} }},\n")
    f.write("  };\n")

with open("scratch/topics_html.txt", "w") as f:
    for t in topics_map:
        f.write(f"""        <a class="topic-card" href="/week.html?w={t['key']}">
          <div class="num">{t['key']}</div>
          <h3>{t['title']}</h3>
          <div class="kicker">Read chapter</div>
        </a>\n""")

print(f"Successfully migrated {len(topics_map)} topics!")
