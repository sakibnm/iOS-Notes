/* ============================================================
   Global Search Modal Overlay
   ============================================================ */

(function () {
  'use strict';

  let INDEX = null;
  let isOpen = false;
  let isFetching = false;
  let modalDom = null;
  let $q, $results, $status;

  // ---- Build Modal DOM dynamically ----
  function buildModal() {
    if (modalDom) return;

    modalDom = document.createElement('div');
    modalDom.className = 'search-modal-backdrop';
    modalDom.setAttribute('aria-hidden', 'true');
    
    modalDom.innerHTML = `
      <div class="search-modal" role="dialog" aria-modal="true" aria-labelledby="search-modal-title">
        <div class="search-header">
          <p class="eyebrow">Search the whole website</p>
          <h1 id="search-modal-title" class="search-title">Find anything across <em>the entire course site</em>.</h1>
          <form class="search-form" id="search-form" role="search" autocomplete="off" onsubmit="event.preventDefault();">
            <label for="q" class="visually-hidden">Search query</label>
            <input
              id="q"
              name="q"
              type="search"
              placeholder="Try: callbackFlow, sealed class, Room migration, Material 3&hellip;"
              spellcheck="false"
            />
            <p class="search-status" id="status">Loading index&hellip;</p>
          </form>
        </div>
        <section class="search-results" id="results" aria-live="polite"></section>
      </div>
    `;

    document.body.appendChild(modalDom);

    $q = document.getElementById('q');
    $results = document.getElementById('results');
    $status = document.getElementById('status');

    $q.addEventListener('input', (e) => runSearch(e.target.value));
    
    // Close on backdrop click
    modalDom.addEventListener('mousedown', (e) => {
      if (e.target === modalDom) closeSearch();
    });
  }

  // ---- Fetch Index (Lazy) ----
  function fetchIndex() {
    if (INDEX || isFetching) return;
    isFetching = true;
    fetch('/search-index.json', { cache: 'no-cache' })
      .then((r) => {
        if (!r.ok) throw new Error('HTTP ' + r.status);
        return r.json();
      })
      .then((data) => {
        INDEX = data;
        $status.textContent = `Ready · ${data.length} sections indexed.`;
        // Run any queued search
        if ($q.value.trim()) runSearch($q.value);
      })
      .catch((e) => {
        $status.textContent = 'Failed to load index: ' + e.message;
      });
  }

  // ---- Open/Close ----
  function openSearch() {
    if (isOpen) return;
    buildModal();
    isOpen = true;
    modalDom.classList.add('search-open');
    modalDom.setAttribute('aria-hidden', 'false');
    document.body.style.overflow = 'hidden';
    
    fetchIndex();
    
    setTimeout(() => {
      $q.focus();
      $q.select();
    }, 50);
  }

  function closeSearch() {
    if (!isOpen) return;
    isOpen = false;
    modalDom.classList.remove('search-open');
    modalDom.setAttribute('aria-hidden', 'true');
    document.body.style.overflow = '';
  }

  // ---- Tokenize & Score ----
  function tokenize(s) {
    return String(s)
      .toLowerCase()
      .match(/[a-z0-9_]+/gi) || [];
  }

  function score(entry, rawQuery, queryTokens) {
    const haystackBody = entry.body.toLowerCase();
    const haystackTitle = entry.section.toLowerCase();
    let total = 0;

    if (rawQuery.length >= 3) {
      if (haystackTitle.includes(rawQuery)) total += 30;
      if (haystackBody.includes(rawQuery)) total += 15;
    }

    for (const tok of queryTokens) {
      const len = tok.length;
      const wordBoundary = new RegExp('\\b' + escapeRegex(tok) + '\\b', 'i');

      if (wordBoundary.test(entry.section)) total += 8 + Math.min(len, 8);
      else if (haystackTitle.includes(tok)) total += 3;

      const wordMatches = (haystackBody.match(new RegExp('\\b' + escapeRegex(tok) + '\\b', 'gi')) || []).length;
      total += wordMatches * (2 + Math.min(len / 4, 3));

      if (wordMatches === 0 && haystackBody.includes(tok)) total += 1;
    }

    return total;
  }

  function escapeRegex(s) {
    return s.replace(/[.*+?^${}()|[\]\\]/g, '\\$&');
  }

  function escapeHtml(s) {
    return String(s).replace(/[&<>"']/g, (c) => ({
      '&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'
    }[c]));
  }

  function buildSnippet(body, rawQuery, tokens, maxLen = 240) {
    const lower = body.toLowerCase();
    let hitIdx = -1;
    if (rawQuery.length >= 3) hitIdx = lower.indexOf(rawQuery);
    if (hitIdx === -1) {
      for (const tok of tokens) {
        const i = lower.indexOf(tok);
        if (i !== -1) { hitIdx = i; break; }
      }
    }
    if (hitIdx === -1) {
      return body.slice(0, maxLen) + (body.length > maxLen ? '…' : '');
    }
    const contextBefore = 60;
    const start = Math.max(0, hitIdx - contextBefore);
    const end = Math.min(body.length, start + maxLen);
    let snippet = body.slice(start, end);
    if (start > 0) snippet = '…' + snippet;
    if (end < body.length) snippet = snippet + '…';
    return snippet;
  }

  function highlight(snippet, rawQuery, tokens) {
    let html = escapeHtml(snippet);
    const terms = new Set();
    if (rawQuery.length >= 3) terms.add(rawQuery);
    for (const t of tokens) terms.add(t);
    const sorted = [...terms].sort((a, b) => b.length - a.length);
    if (!sorted.length) return html;
    const pattern = new RegExp('(' + sorted.map(escapeRegex).join('|') + ')', 'gi');
    return html.replace(pattern, '<mark>$1</mark>');
  }

  // ---- Render ----
  function render(matches, rawQuery, tokens) {
    if (!matches.length) {
      $results.innerHTML = '<div class="empty-state">No matches. Try a broader term.</div>';
      return;
    }
    const frag = document.createDocumentFragment();
    for (const m of matches) {
      const a = document.createElement('a');
      a.className = 'search-result';
      // When a result is clicked, close the modal immediately.
      // (If on the same page, the anchor jumps; if different page, it navigates)
      a.addEventListener('click', () => closeSearch());
      a.href = m.url + '#' + slug(m.section);

      const snippet = buildSnippet(m.body, rawQuery, tokens);
      a.innerHTML =
        '<div class="topic-label">' + escapeHtml(m.topic_label) + '</div>' +
        '<div class="section-name">' + highlight(m.section, rawQuery, tokens) + '</div>' +
        '<div class="snippet">' + highlight(snippet, rawQuery, tokens) + '</div>';
      frag.appendChild(a);
    }
    $results.innerHTML = '';
    $results.appendChild(frag);
  }

  function slug(s) {
    return String(s).toLowerCase()
      .replace(/[^a-z0-9]+/g, '-')
      .replace(/^-|-$/g, '');
  }

  // ---- Run a search ----
  function runSearch(raw) {
    if (!INDEX) {
        $status.textContent = 'Loading index...';
        return;
    }
    const rawQuery = raw.trim().toLowerCase();
    if (!rawQuery) {
      $results.innerHTML = '';
      $status.textContent = `Ready · ${INDEX.length} sections indexed.`;
      return;
    }
    const tokens = tokenize(rawQuery);
    if (!tokens.length) {
      $results.innerHTML = '';
      return;
    }

    const scored = [];
    for (const entry of INDEX) {
      const s = score(entry, rawQuery, tokens);
      if (s > 0) scored.push({ entry, s });
    }
    scored.sort((a, b) => b.s - a.s);
    const top = scored.slice(0, 40).map((x) => x.entry);

    $status.textContent = `${scored.length} match${scored.length === 1 ? '' : 'es'} for "${raw.trim()}"`;
    render(top, rawQuery, tokens);
  }

  // ---- Global Events ----
  window.addEventListener('keydown', (e) => {
    // Cmd+K or Ctrl+K to open
    if ((e.metaKey || e.ctrlKey) && e.key === 'k') {
      e.preventDefault();
      openSearch();
    }
    // Escape to close
    if (e.key === 'Escape') {
      closeSearch();
    }
  });

  // Expose to window so we can hook up UI buttons easily
  window.CS5520Search = {
    open: openSearch,
    close: closeSearch
  };

  // Auto-wire up any element with class 'search-trigger'
  document.addEventListener('click', (e) => {
      if (e.target && e.target.closest('.search-trigger')) {
          e.preventDefault();
          openSearch();
      }
  });

})();
