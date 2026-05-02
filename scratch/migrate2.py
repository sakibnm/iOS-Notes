import re
from pathlib import Path

ios_dir = Path('/Users/nsm/iOS-Notes')

# --- 1. Modify styles.css ---
css_path = ios_dir / 'assets' / 'styles.css'
css = css_path.read_text()
# Android blue/green accents:
# --accent: #1d4ed8;
# --accent-hover: #1e3a8a;
# --accent: #60a5fa;
# --accent-hover: #93c5fd;

css = css.replace('--accent: #1d4ed8;', '--accent: #007AFF;')
css = css.replace('--accent-hover: #1e3a8a;', '--accent-hover: #0056b3;')
css = css.replace('--accent: #60a5fa;', '--accent: #0A84FF;')
css = css.replace('--accent-hover: #93c5fd;', '--accent-hover: #409CFF;')
css_path.write_text(css)

# --- 2. Modify lesson.js ---
lesson_js_path = ios_dir / 'assets' / 'lesson.js'
js = lesson_js_path.read_text()

# Replace TOPICS object
new_topics = '''  const TOPICS = {
    '01': { file: 'Module_01_Getting_Started.md',              title: 'Getting Started',      prev: null, next: '02' },
    '02': { file: 'Module_02_Swift_Fundamentals.md',           title: 'Swift Fundamentals',   prev: '01', next: '03' },
    '03': { file: 'Module_03_Introduction_To_Uikit.md',        title: 'Introduction to UIKit',prev: '02', next: '04' },
    '04': { file: 'Module_04_Advanced_Ui_Components.md',       title: 'Advanced UI Components',prev: '03', next: '05' },
    '05': { file: 'Module_05_Networking_And_Apis.md',          title: 'Networking & APIs',    prev: '04', next: '06' },
    '06': { file: 'Module_06_Data_Persistence_And_Architecture.md', title: 'Data Persistence & Architecture', prev: '05', next: '07' },
    '07': { file: 'Module_07_Cloud_Integrations_And_Maps.md',  title: 'Cloud Integrations & Maps', prev: '06', next: null }
  };'''

js = re.sub(r'const TOPICS = \{.*?\};', new_topics, js, flags=re.DOTALL)
js = js.replace('CS 4520/5520', 'iOS Development')
lesson_js_path.write_text(js)

# --- 3. Modify week.html ---
week_html_path = ios_dir / 'week.html'
week = week_html_path.read_text()
week = week.replace('CS 4520/5520', 'iOS Development')

# iOS Icon path (Apple blue)
apple_svg = r"data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24' fill='%23007AFF'%3E%3Cpath d='M12 2C6.477 2 2 6.477 2 12s4.477 10 10 10 10-4.477 10-10S17.523 2 12 2zm1 15h-2v-6h2v6zm0-8h-2V7h2v2z'/%3E%3C/svg%3E"
week = re.sub(r'data:image/svg\+xml,.*?%3E%3C/svg%3E', apple_svg, week)

nav_html = '''<ol id="topic-nav-list">
      <li><a href="/week.html?w=01" data-w="01">Getting Started</a></li>
      <li><a href="/week.html?w=02" data-w="02">Swift Fundamentals</a></li>
      <li><a href="/week.html?w=03" data-w="03">Introduction to UIKit</a></li>
      <li><a href="/week.html?w=04" data-w="04">Advanced UI Components</a></li>
      <li><a href="/week.html?w=05" data-w="05">Networking & APIs</a></li>
      <li><a href="/week.html?w=06" data-w="06">Data Persistence & Architecture</a></li>
      <li><a href="/week.html?w=07" data-w="07">Cloud Integrations & Maps</a></li>
    </ol>'''
week = re.sub(r'<ol id="topic-nav-list">.*?</ol>', nav_html, week, flags=re.DOTALL)
# Remove optional modules
week = re.sub(r'<div class="kmp-link">.*?</div>', '', week, flags=re.DOTALL)
week_html_path.write_text(week)

# --- 4. Modify index.html ---
index_path = ios_dir / 'index.html'
index = index_path.read_text()
index = index.replace('CS 4520/5520 — Mobile Application Development', 'iOS Application Development')
index = index.replace('CS&nbsp;4520/5520 · Summer&nbsp;I&nbsp;2026', 'iOS Development')
index = index.replace('CS 4520/5520', 'iOS Development')
index = index.replace('Android &amp; Kotlin', 'iOS & Swift')
index = index.replace('Course materials · Android · Kotlin', 'Course materials · iOS · Swift')
index = index.replace('Mobile Application Development', 'iOS Application Development')
index = index.replace('Kotlin and Jetpack Compose', 'Swift and UIKit')
index = index.replace('Kotlin · Compose · Firebase', 'Swift · UIKit · Firebase')
index = index.replace('15 topics', '7 modules')
index = re.sub(r'data:image/svg\+xml,.*?%3E%3C/svg%3E', apple_svg, index)

mermaid = '''<pre class="mermaid">
      graph LR
          A[Foundations<br>Swift] --> B[Architecture<br>UIKit & MVC]
          B --> C[Data & Network<br>APIs & JSON]
          C --> D[Advanced<br>Persistence & CoreData]
          D --> E[Cloud<br>Firebase & Maps]
    </pre>'''
index = re.sub(r'<pre class="mermaid">.*?</pre>', mermaid, index, flags=re.DOTALL)

topics_grid = '''<div class="topics">
      <a href="/week.html?w=01" class="topic-card">
        <div class="num">01</div>
        <h3>Getting Started</h3>
        <div class="kicker">Xcode, Playgrounds, and the Basics.</div>
      </a>
      <a href="/week.html?w=02" class="topic-card">
        <div class="num">02</div>
        <h3>Swift Fundamentals</h3>
        <div class="kicker">Variables, Collections, and Control Flow.</div>
      </a>
      <a href="/week.html?w=03" class="topic-card">
        <div class="num">03</div>
        <h3>Introduction to UIKit</h3>
        <div class="kicker">ViewControllers, MVC, and IB.</div>
      </a>
      <a href="/week.html?w=04" class="topic-card">
        <div class="num">04</div>
        <h3>Advanced UI Components</h3>
        <div class="kicker">TableViews, ScrollViews, and Menus.</div>
      </a>
      <a href="/week.html?w=05" class="topic-card">
        <div class="num">05</div>
        <h3>Networking & APIs</h3>
        <div class="kicker">HTTP, JSON parsing, and Alamofire.</div>
      </a>
      <a href="/week.html?w=06" class="topic-card">
        <div class="num">06</div>
        <h3>Data Persistence</h3>
        <div class="kicker">NotificationCenter and Local Storage.</div>
      </a>
      <a href="/week.html?w=07" class="topic-card">
        <div class="num">07</div>
        <h3>Cloud & Maps</h3>
        <div class="kicker">Firebase Auth, Firestore, and MapKit.</div>
      </a>
    </div>'''
index = re.sub(r'<div class="topics">.*?</div>\s*(?=</section>|<div class="optional-modules-container")', topics_grid, index, flags=re.DOTALL)
# Remove optional modules container
index = re.sub(r'<div class="optional-modules-container".*?</div>', '', index, flags=re.DOTALL)

index_path.write_text(index)

print('Modifications applied.')
