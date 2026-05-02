import re

# Update styles.css
with open("assets/styles.css", "r") as f:
    css = f.read()

css = re.sub(r"--font-serif:.*?;", "--font-serif: -apple-system, BlinkMacSystemFont, 'SF Pro Display', 'Helvetica Neue', sans-serif;", css)
css = re.sub(r"--font-sans:.*?;", "--font-sans: -apple-system, BlinkMacSystemFont, 'SF Pro Text', 'Helvetica Neue', sans-serif;", css)
css = re.sub(r"--radius:.*?;", "--radius: 10px;", css)

# Light theme
css = re.sub(r"--accent: #1d4ed8;", "--accent: #007aff;", css)
css = re.sub(r"--accent-hover: #1e3a8a;", "--accent-hover: #005bb5;", css)

# Dark theme
css = re.sub(r"--accent: #60a5fa;", "--accent: #0a84ff;", css)
css = re.sub(r"--accent-hover: #93c5fd;", "--accent-hover: #5ac8fa;", css)

with open("assets/styles.css", "w") as f:
    f.write(css)

# Update HTML favicons
for html_file in ["index.html", "week.html"]:
    with open(html_file, "r") as f:
        html = f.read()
    
    html = html.replace("%233DDC84", "%23007aff")
    
    with open(html_file, "w") as f:
        f.write(html)
