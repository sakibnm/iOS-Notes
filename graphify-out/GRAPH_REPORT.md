# Graph Report - .  (2026-05-02)

## Corpus Check
- 0 files · ~0 words
- Verdict: corpus is large enough that graph structure adds value.

## Summary
- 38 nodes · 66 edges · 7 communities detected
- Extraction: 100% EXTRACTED · 0% INFERRED · 0% AMBIGUOUS
- Token cost: 0 input · 0 output

## Community Hubs (Navigation)
- [[_COMMUNITY_Community 0|Community 0]]
- [[_COMMUNITY_Community 1|Community 1]]
- [[_COMMUNITY_Community 2|Community 2]]
- [[_COMMUNITY_Community 4|Community 4]]
- [[_COMMUNITY_Community 5|Community 5]]
- [[_COMMUNITY_Community 6|Community 6]]
- [[_COMMUNITY_Community 7|Community 7]]

## God Nodes (most connected - your core abstractions)
1. `boot()` - 15 edges
2. `render()` - 6 edges
3. `$()` - 5 edges
4. `setText()` - 4 edges
5. `renderError()` - 4 edges
6. `buildBottomNav()` - 4 edges
7. `runSearch()` - 4 edges
8. `escapeHtml()` - 3 edges
9. `buildToc()` - 3 edges
10. `openSearch()` - 3 edges

## Surprising Connections (you probably didn't know these)
- `$()` --calls--> `buildBottomNav()`  [EXTRACTED]
  lesson.js → lesson.js  _Bridges community 6 → community 7_
- `$()` --calls--> `boot()`  [EXTRACTED]
  lesson.js → lesson.js  _Bridges community 6 → community 1_
- `escapeHtml()` --calls--> `boot()`  [EXTRACTED]
  lesson.js → lesson.js  _Bridges community 7 → community 1_
- `ensureHeadingIds()` --calls--> `boot()`  [EXTRACTED]
  lesson.js → lesson.js  _Bridges community 0 → community 1_
- `buildSnippet()` --calls--> `render()`  [EXTRACTED]
  search.js → search.js  _Bridges community 2 → community 4_

## Communities

### Community 0 - "Community 0"
Cohesion: 0.29
Nodes (4): buildToc(), ensureHeadingIds(), highlightActiveNav(), setupScrollSpy()

### Community 1 - "Community 1"
Cohesion: 0.29
Nodes (7): attachCopyButtons(), attachExternalLinks(), attachHeadingAnchors(), boot(), configureMarked(), getParam(), runHighlight()

### Community 2 - "Community 2"
Cohesion: 0.47
Nodes (4): buildModal(), buildSnippet(), fetchIndex(), openSearch()

### Community 4 - "Community 4"
Cohesion: 0.67
Nodes (4): escapeHtml(), highlight(), render(), slug()

### Community 5 - "Community 5"
Cohesion: 0.5
Nodes (4): escapeRegex(), runSearch(), score(), tokenize()

### Community 6 - "Community 6"
Cohesion: 1.0
Nodes (3): $(), renderError(), setText()

### Community 7 - "Community 7"
Cohesion: 1.0
Nodes (2): buildBottomNav(), escapeHtml()

## Knowledge Gaps
- **Thin community `Community 7`** (2 nodes): `buildBottomNav()`, `escapeHtml()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `boot()` connect `Community 1` to `Community 0`, `Community 6`, `Community 7`?**
  _High betweenness centrality (0.064) - this node is a cross-community bridge._
- **Why does `render()` connect `Community 4` to `Community 2`, `Community 5`?**
  _High betweenness centrality (0.007) - this node is a cross-community bridge._
- **Why does `runSearch()` connect `Community 5` to `Community 2`, `Community 4`?**
  _High betweenness centrality (0.002) - this node is a cross-community bridge._