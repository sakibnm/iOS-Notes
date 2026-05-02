/* ============================================================
   Lesson page: fetch the topic's markdown, render, highlight,
   and build an expandable in-page table of contents.
   ============================================================ */

(function () {
  'use strict';

  // --- Manifest: topic param → file name + title ---------------
    const TOPICS = {
    '01': { file: 'Topic_01_Getting_Started.md', title: 'Getting Started', prev: null, next: '02' },
    '02': { file: 'Topic_02_Collections.md', title: 'Collections', prev: '01', next: '03' },
    '03': { file: 'Topic_03_Operators.md', title: 'Operators', prev: '02', next: '04' },
    '04': { file: 'Topic_04_Conditionals.md', title: 'Conditionals', prev: '03', next: '05' },
    '05': { file: 'Topic_05_Loops.md', title: 'Loops', prev: '04', next: '06' },
    '06': { file: 'Topic_06_Functions.md', title: 'Functions', prev: '05', next: '07' },
    '07': { file: 'Topic_07_Closures.md', title: 'Closures', prev: '06', next: '08' },
    '08': { file: 'Topic_08_Optionals.md', title: 'Optionals', prev: '07', next: '09' },
    '09': { file: 'Topic_09_Protocols.md', title: 'Protocols', prev: '08', next: '10' },
    '10': { file: 'Topic_10_Sorting_Arrays.md', title: 'Sorting Arrays', prev: '09', next: '11' },
    '11': { file: 'Topic_11_91_Structs.md', title: '9.1. Structs', prev: '10', next: '12' },
    '12': { file: 'Topic_12_92_Classes.md', title: '9.2. Classes', prev: '11', next: '13' },
    '13': { file: 'Topic_13_Unknown.md', title: 'Unknown', prev: '12', next: '14' },
    '14': { file: 'Topic_14_Designing_Without_Storyboards.md', title: 'Designing Without Storyboards', prev: '13', next: '15' },
    '15': { file: 'Topic_15_MultiScreen_Apps.md', title: 'Multi-Screen Apps', prev: '14', next: '16' },
    '16': { file: 'Topic_16_MVC_Architecture.md', title: 'MVC Architecture', prev: '15', next: '17' },
    '17': { file: 'Topic_17_33_Send_data_back_from_Screen_2_to_Screen_1.md', title: '3.3. Send data back from Screen 2 to Screen 1', prev: '16', next: '18' },
    '18': { file: 'Topic_18_Unknown.md', title: 'Unknown', prev: '17', next: '19' },
    '19': { file: 'Topic_19_UITableView.md', title: 'UITableView', prev: '18', next: '20' },
    '20': { file: 'Topic_20_UIScrollView.md', title: 'UIScrollView', prev: '19', next: '21' },
    '21': { file: 'Topic_21_UIMenu__Image_Pickers.md', title: 'UIMenu & Image Pickers', prev: '20', next: '22' },
    '22': { file: 'Topic_22_Useful_UI_Elements.md', title: 'Useful UI Elements', prev: '21', next: '23' },
    '23': { file: 'Topic_23_Unknown.md', title: 'Unknown', prev: '22', next: '24' },
    '24': { file: 'Topic_24_Unknown.md', title: 'Unknown', prev: '23', next: '25' },
    '25': { file: 'Topic_25_Unknown.md', title: 'Unknown', prev: '24', next: '26' },
    '26': { file: 'Topic_26_HTTP__Networking.md', title: 'HTTP & Networking', prev: '25', next: '27' },
    '27': { file: 'Topic_27_Working_with_JSON.md', title: 'Working with JSON', prev: '26', next: '28' },
    '28': { file: 'Topic_28_Notification_Center.md', title: 'Notification Center', prev: '27', next: '29' },
    '29': { file: 'Topic_29_Clean_Code__Async.md', title: 'Clean Code & Async', prev: '28', next: '30' },
    '30': { file: 'Topic_30_1_Writing_Clean_Code_For_Asynchronous_Operations.md', title: '1. Writing Clean Code For Asynchronous Operations', prev: '29', next: '31' },
    '31': { file: 'Topic_31_CocoaPods.md', title: 'CocoaPods', prev: '30', next: '32' },
    '32': { file: 'Topic_32_Firebase_Auth__Firestore.md', title: 'Firebase Auth & Firestore', prev: '31', next: '33' },
    '33': { file: 'Topic_33_Firebase_Storage.md', title: 'Firebase Storage', prev: '32', next: '34' },
    '34': { file: 'Topic_34_MapKit__Location.md', title: 'MapKit & Location', prev: '33', next: '35' },
    '35': { file: 'Topic_35_125_Implementing_Register_and_Sign_In.md', title: '12.5. Implementing Register and Sign In', prev: '34', next: null },
  };

  // --- Helpers ------------------------------------------------
  const $ = (sel) => document.querySelector(sel);

  function getParam(name) {
    const params = new URLSearchParams(window.location.search);
    return (params.get(name) || '').toLowerCase().trim();
  }

  function setText(sel, text) {
    const el = $(sel);
    if (el) el.textContent = text;
  }

  function renderError(message) {
    const article = $('#article');
    if (article) {
      article.innerHTML =
        '<div class="error-panel"><strong>Could not load topic.</strong><br />' +
        message + '</div>';
    }
    setText('#loading-hint', '');
  }

  function escapeHtml(s) {
    return String(s).replace(/[&<>"']/g, (c) => ({
      '&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'
    }[c]));
  }

  // --- Heading ID normalisation --------------------------------
  // marked v13 headerIds generates IDs but their exact format can
  // vary. We ensure every H2/H3 has a stable, clean ID after render
  // so the TOC links and scroll spy always work.

  function headingToId(text) {
    return text
      .toLowerCase()
      .replace(/[^a-z0-9\s-]/g, '')
      .trim()
      .replace(/\s+/g, '-')
      .replace(/-+/g, '-');
  }

  function ensureHeadingIds() {
    const seen = {};
    
    // Promote <p><strong>Text</strong></p> into pseudo-headings 
    // so they can be deep-linked just like normal headings.
    document.querySelectorAll('.article p').forEach(p => {
      if (p.childNodes.length === 1 && p.firstChild.tagName === 'STRONG') {
        p.classList.add('pseudo-heading');
      }
    });

    document.querySelectorAll('.article h1, .article h2, .article h3, .article h4, .article h5, .article p.pseudo-heading').forEach((el) => {
      if (!el.id) {
        let id = headingToId(el.textContent);
        if (seen[id]) { seen[id]++; id = id + '-' + seen[id]; } else { seen[id] = 1; }
        el.id = id;
      }
    });
  }

  // --- Heading anchor links -----------------------------------
  // Adds a clickable # after each H2 and H3. Clicking it copies
  // the full URL (with fragment) to the clipboard.

  function attachHeadingAnchors() {
    document.querySelectorAll('.article h2, .article h3, .article h4, .article h5, .article p.pseudo-heading').forEach((el) => {
      if (el.querySelector('.heading-anchor')) return; // already added
      if (!el.id) return;

      const anchor = document.createElement('a');
      anchor.className = 'heading-anchor';
      anchor.href = '#' + el.id;
      anchor.setAttribute('aria-label', 'Copy link to this section');
      anchor.textContent = '#';

      anchor.addEventListener('click', async (e) => {
        e.preventDefault();
        // Update the URL bar
        window.history.pushState(null, '', '#' + el.id);
        // Copy the full URL to clipboard
        try {
          await navigator.clipboard.writeText(window.location.href);
          anchor.classList.add('anchor-copied');
          setTimeout(() => anchor.classList.remove('anchor-copied'), 1800);
        } catch (_e) {
          // Clipboard not available — at least the URL bar updated
        }
      });

      el.appendChild(anchor);
    });
  }

  // --- Expandable TOC + tabbed nav ----------------------------

  function buildToc() {
    const nav = document.querySelector('.lesson-nav');
    if (!nav) return;

    const headings = document.querySelectorAll('.article h2, .article h3');
    if (!headings.length) return;

    // Build section tree
    const sections = [];
    let current = null;
    headings.forEach((el) => {
      if (el.tagName === 'H2') {
        current = { el, id: el.id, text: el.textContent, children: [] };
        sections.push(current);
      } else if (el.tagName === 'H3' && current) {
        current.children.push({ el, id: el.id, text: el.textContent });
      }
    });
    if (!sections.length) return;

    // --- Topics panel: move existing nav content into it -------
    const topicsPanel = document.createElement('div');
    topicsPanel.id = 'nav-panel-topics';
    topicsPanel.className = 'nav-panel';
    topicsPanel.setAttribute('role', 'tabpanel');
    topicsPanel.setAttribute('aria-labelledby', 'nav-tab-topics');
    topicsPanel.setAttribute('tabindex', '0');
    while (nav.firstChild) topicsPanel.appendChild(nav.firstChild);

    // --- Contents panel: the TOC ---
    const contentsPanel = document.createElement('div');
    contentsPanel.id = 'nav-panel-contents';
    contentsPanel.className = 'nav-panel nav-panel-active';
    contentsPanel.setAttribute('role', 'tabpanel');
    contentsPanel.setAttribute('aria-labelledby', 'nav-tab-contents');
    contentsPanel.setAttribute('tabindex', '0');

    const tocList = document.createElement('ol');
    tocList.className = 'toc-list';
    tocList.setAttribute('aria-label', 'Table of contents');

    sections.forEach((section) => {
      const li = document.createElement('li');
      li.dataset.tocId = section.id;
      const hasChildren = section.children.length > 0;

      const item = document.createElement('a');
      item.href = '#' + section.id;
      item.className = 'toc-h2-item' + (hasChildren ? ' has-children' : '');

      if (hasChildren) {
        // aria-expanded reflects whether children are visible
        item.setAttribute('aria-expanded', 'false');
      }

      const textSpan = document.createElement('span');
      textSpan.className = 'toc-item-text';
      textSpan.textContent = section.text;
      item.appendChild(textSpan);

      if (hasChildren) {
        const indicator = document.createElement('span');
        indicator.className = 'toc-item-indicator';
        indicator.setAttribute('aria-hidden', 'true');
        indicator.textContent = '▾';
        item.appendChild(indicator);

        // Clicking opens this section and collapses all others
        item.addEventListener('click', () => {
          const isOpen = li.classList.contains('toc-open');
          // Close all others
          tocList.querySelectorAll('li.toc-open').forEach((other) => {
            other.classList.remove('toc-open');
            const otherItem = other.querySelector('.toc-h2-item');
            if (otherItem) otherItem.setAttribute('aria-expanded', 'false');
          });
          // Toggle this one
          if (!isOpen) {
            li.classList.add('toc-open');
            item.setAttribute('aria-expanded', 'true');
          }
        });
      }

      li.appendChild(item);

      if (hasChildren) {
        const childList = document.createElement('ol');
        childList.className = 'toc-children';
        // Give the child list an id so aria-controls can reference it
        const childListId = 'toc-children-' + section.id;
        childList.id = childListId;
        item.setAttribute('aria-controls', childListId);

        section.children.forEach((child) => {
          const childLi = document.createElement('li');
          childLi.dataset.tocId = child.id;
          const childLink = document.createElement('a');
          childLink.href = '#' + child.id;
          childLink.className = 'toc-h3-link';
          childLink.textContent = child.text;
          childLi.appendChild(childLink);
          childList.appendChild(childLi);
        });
        li.appendChild(childList);
      }

      tocList.appendChild(li);
    });

    contentsPanel.appendChild(tocList);

    // --- Tab bar with proper ARIA tablist pattern ---------------
    const tabBar = document.createElement('div');
    tabBar.className = 'nav-tab-bar';
    tabBar.setAttribute('role', 'tablist');
    tabBar.setAttribute('aria-label', 'Navigation panels');

    function makeTab(label, tabId, panelId, active) {
      const btn = document.createElement('button');
      btn.className = 'nav-tab' + (active ? ' nav-tab-active' : '');
      btn.type = 'button';
      btn.id = tabId;
      btn.textContent = label;
      btn.setAttribute('role', 'tab');
      btn.setAttribute('aria-selected', active ? 'true' : 'false');
      btn.setAttribute('aria-controls', panelId);
      btn.setAttribute('tabindex', active ? '0' : '-1');

      btn.addEventListener('click', () => activateTab(btn, tabBar, nav));
      return btn;
    }

    // Derive label from the ?w= query param so the tab reads "Topic 1", "Topic 2", etc.
    const _key   = new URLSearchParams(window.location.search).get('w') || '';
    const _num   = parseInt(_key, 10);
    // Special label format for KMP, AI, Cloud AI, or numbered topics.
    const _label = _key === 'kmp' ? 'KMP' : _key === 'ai' ? 'Local AI' : _key === 'cloud_ai' ? 'Cloud AI' : (!isNaN(_num) ? 'Topic ' + _num : 'Contents');
    const contentsTab = makeTab(_label, 'nav-tab-contents', 'nav-panel-contents', true);
    const topicsTab   = makeTab('All Topics', 'nav-tab-topics', 'nav-panel-topics', false);
    tabBar.appendChild(contentsTab);
    tabBar.appendChild(topicsTab);

    // Keyboard navigation within tablist (arrow keys)
    tabBar.addEventListener('keydown', (e) => {
      const tabs = [...tabBar.querySelectorAll('[role="tab"]')];
      const idx  = tabs.indexOf(document.activeElement);
      if (idx === -1) return;
      let next = -1;
      if (e.key === 'ArrowRight' || e.key === 'ArrowDown') {
        e.preventDefault();
        next = (idx + 1) % tabs.length;
      } else if (e.key === 'ArrowLeft' || e.key === 'ArrowUp') {
        e.preventDefault();
        next = (idx - 1 + tabs.length) % tabs.length;
      } else if (e.key === 'Home') {
        e.preventDefault(); next = 0;
      } else if (e.key === 'End') {
        e.preventDefault(); next = tabs.length - 1;
      }
      if (next !== -1) { activateTab(tabs[next], tabBar, nav); tabs[next].focus(); }
    });

    // --- Assemble ---
    nav.appendChild(tabBar);
    nav.appendChild(contentsPanel);
    nav.appendChild(topicsPanel);

    setupScrollSpy(sections);
  }

  // Shared tab activation logic
  function activateTab(btn, tabBar, nav) {
    tabBar.querySelectorAll('[role="tab"]').forEach((t) => {
      t.classList.remove('nav-tab-active');
      t.setAttribute('aria-selected', 'false');
      t.setAttribute('tabindex', '-1');
    });
    btn.classList.add('nav-tab-active');
    btn.setAttribute('aria-selected', 'true');
    btn.setAttribute('tabindex', '0');
    const panelId = btn.getAttribute('aria-controls');
    nav.querySelectorAll('.nav-panel').forEach((p) => p.classList.remove('nav-panel-active'));
    const panel = document.getElementById(panelId);
    if (panel) panel.classList.add('nav-panel-active');
  }

  // --- Scroll spy ---------------------------------------------

  function setupScrollSpy(sections) {
    const allItems = [];
    sections.forEach((s) => {
      allItems.push({ id: s.id, isChild: false, parentId: null });
      s.children.forEach((c) => allItems.push({ id: c.id, isChild: true, parentId: s.id }));
    });

    let activeId = null;

    const observer = new IntersectionObserver((entries) => {
      entries.forEach((entry) => {
        if (!entry.isIntersecting) return;
        if (entry.target.id === activeId) return;
        activeId = entry.target.id;
        setActiveTocItem(activeId, allItems);
      });
    }, {
      // Trigger when the heading crosses the top third of the viewport
      rootMargin: '0px 0px -65% 0px',
      threshold: 0
    });

    allItems.forEach((item) => {
      const el = document.getElementById(item.id);
      if (el) observer.observe(el);
    });
  }

  function setActiveTocItem(id, allItems) {
    // Remove all active states and aria-current
    document.querySelectorAll('.toc-h2-item.toc-active, .toc-h3-link.toc-active')
      .forEach((el) => {
        el.classList.remove('toc-active');
        el.removeAttribute('aria-current');
      });

    const item = allItems.find((i) => i.id === id);
    if (!item) return;

    if (item.isChild) {
      const childLink = document.querySelector('.toc-h3-link[href="#' + id + '"]');
      if (childLink) {
        childLink.classList.add('toc-active');
        childLink.setAttribute('aria-current', 'true');
      }
      const parentLi = document.querySelector('.toc-list > li[data-toc-id="' + item.parentId + '"]');
      if (parentLi) {
        // Collapse others, expand this parent
        document.querySelectorAll('.toc-list > li.toc-open').forEach((other) => {
          if (other !== parentLi) {
            other.classList.remove('toc-open');
            const otherItem = other.querySelector('.toc-h2-item');
            if (otherItem) otherItem.setAttribute('aria-expanded', 'false');
          }
        });
        parentLi.classList.add('toc-open');
        const parentItem = parentLi.querySelector('.toc-h2-item');
        if (parentItem) {
          parentItem.classList.add('toc-active');
          parentItem.setAttribute('aria-expanded', 'true');
        }
      }
    } else {
      const h2Item = document.querySelector('.toc-h2-item[href="#' + id + '"]');
      if (h2Item) {
        h2Item.classList.add('toc-active');
        h2Item.setAttribute('aria-current', 'true');
      }
    }
  }

  // --- Copy buttons -------------------------------------------

  function attachCopyButtons() {
    document.querySelectorAll('.article pre').forEach((pre) => {
      if (pre.querySelector('.copy-btn')) return;
      const btn = document.createElement('button');
      btn.className = 'copy-btn';
      btn.type = 'button';
      btn.setAttribute('aria-label', 'Copy code to clipboard');
      btn.textContent = 'Copy';
      btn.addEventListener('click', async () => {
        const code = pre.querySelector('code');
        if (!code) return;
        try {
          await navigator.clipboard.writeText(code.innerText);
          btn.textContent = 'Copied';
          btn.classList.add('copied');
          setTimeout(() => { btn.textContent = 'Copy'; btn.classList.remove('copied'); }, 1600);
        } catch (_e) {
          btn.textContent = 'Error';
          setTimeout(() => { btn.textContent = 'Copy'; }, 1600);
        }
      });
      pre.appendChild(btn);
    });
  }

  // --- Bottom prev/next nav -----------------------------------

  function buildBottomNav(wk) {
    const nav = $('#bottom-nav');
    if (!nav) return;
    nav.innerHTML = '';

    if (wk.prev) {
      const p = TOPICS[wk.prev];
      const a = document.createElement('a');
      a.className = 'prev';
      a.href = '/week.html?w=' + wk.prev;
      a.innerHTML =
        '<span class="label">← Previous</span>' +
        '<span class="title">' + (wk.prev === 'kmp' ? '' : 'Topic ' + wk.prev + ' · ') +
        escapeHtml(p.title) + '</span>';
      nav.appendChild(a);
    } else {
      nav.appendChild(document.createElement('span'));
    }

    if (wk.next) {
      const n = TOPICS[wk.next];
      const a = document.createElement('a');
      a.className = 'next';
      a.href = '/week.html?w=' + wk.next;
      a.innerHTML =
        '<span class="label">Next →</span>' +
        '<span class="title">' + (wk.next === 'kmp' ? '' : 'Topic ' + wk.next + ' · ') +
        escapeHtml(n.title) + '</span>';
      nav.appendChild(a);
    } else {
      nav.appendChild(document.createElement('span'));
    }

    nav.hidden = false;
  }

  // --- Active topic in "All topics" list ----------------------

  function highlightActiveNav(key) {
    document.querySelectorAll('#topic-nav-list a, .kmp-link a').forEach((a) => {
      if (a.dataset.w === key) {
        a.classList.add('active');
        a.setAttribute('aria-current', 'page');
      }
    });
  }

  // --- Syntax highlighting ------------------------------------

  function runHighlight() {
    if (typeof hljs !== 'undefined') {
      document.querySelectorAll('.article pre code').forEach((el) => {
        if (el.classList.contains('language-mermaid')) {
          const pre = el.parentElement;
          const div = document.createElement('div');
          div.className = 'mermaid';
          div.style.background = 'var(--paper-raised)';
          div.style.padding = '1rem';
          div.style.borderRadius = '8px';
          div.style.border = '1px solid var(--rule)';
          div.style.marginBottom = '2rem';
          div.style.overflowX = 'auto';
          div.style.textAlign = 'center';
          div.textContent = el.textContent;
          pre.replaceWith(div);
          return;
        }
        try { hljs.highlightElement(el); } catch (_e) {}
      });
    }

    if (document.querySelector('.mermaid')) {
      const runMermaid = () => {
        if (window.mermaid) {
          window.mermaid.run({ querySelector: '.mermaid' }).catch(e => console.error(e));
        } else {
          setTimeout(runMermaid, 100);
        }
      };
      runMermaid();
    }
  }

  // --- External Links -----------------------------------------

  function attachExternalLinks() {
    document.querySelectorAll('#article a').forEach((a) => {
      const href = a.getAttribute('href');
      if (!href) return;
      if (href.includes('play.kotlinlang.org') || href.endsWith('.zip')) {
        a.setAttribute('target', '_blank');
        a.setAttribute('rel', 'noopener noreferrer');
      }
    });
  }

  // --- Configure marked ---------------------------------------

  function configureMarked() {
    if (typeof marked === 'undefined') return;
    marked.setOptions({
      gfm: true,
      breaks: false,
      headerIds: true,
      mangle: false
    });
  }

  // --- Main ---------------------------------------------------

  async function boot() {
    configureMarked();

    const key = getParam('w');
    if (!key || !TOPICS[key]) {
      renderError('Unknown topic: <code>' + escapeHtml(key || '(none)') + '</code>. ' +
        '<a href="/">Return to the syllabus</a>.');
      return;
    }

    const wk = TOPICS[key];
    highlightActiveNav(key);

    if (key === 'kmp' || key === 'ai' || key === 'cloud_ai') {
      setText('#topic-eyebrow', 'Optional Module');
      const bTitle = key === 'kmp' ? 'Kotlin Multiplatform' : key === 'ai' ? 'On-Device AI' : 'Cloud AI';
      setText('#breadcrumb', bTitle);
    } else {
      setText('#topic-eyebrow', 'Topic ' + key + ' · CS 4520/5520');
      setText('#breadcrumb', 'Topic ' + key + ' · ' + wk.title);
    }
    document.title = wk.title + ' — CS 4520/5520';

    // Set up PDF download button
    const pdfBtn = $('#download-pdf-btn');
    if (pdfBtn && wk.file) {
      pdfBtn.style.display = 'inline-flex';
      pdfBtn.onclick = (e) => {
        e.preventDefault();
        const element = document.getElementById('article');
        const opt = {
          margin:       10,
          filename:     wk.file.replace('.md', '.pdf'),
          image:        { type: 'jpeg', quality: 0.98 },
          html2canvas:  { scale: 2 },
          jsPDF:        { unit: 'mm', format: 'a4', orientation: 'portrait' }
        };
        html2pdf().set(opt).from(element).save();
      };
    }

    // Fetch markdown
    let mdText;
    try {
      const res = await fetch('/lessons/' + wk.file, { cache: 'no-cache' });
      if (!res.ok) throw new Error('HTTP ' + res.status);
      mdText = await res.text();
    } catch (e) {
      renderError('Fetch failed: ' + escapeHtml(e.message));
      return;
    }

    // Render markdown to HTML
    try {
      const html = marked.parse(mdText);
      $('#article').innerHTML = html;
    } catch (e) {
      renderError('Markdown parse failed: ' + escapeHtml(e.message));
      return;
    }

    setText('#loading-hint', '');
    $('#loading-hint').remove();

    ensureHeadingIds();   // stable IDs before TOC builds
    attachHeadingAnchors();
    runHighlight();
    attachCopyButtons();
    buildBottomNav(wk);
    buildToc();           // must come after ensureHeadingIds
    attachExternalLinks();
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', boot);
  } else {
    boot();
  }
})();
