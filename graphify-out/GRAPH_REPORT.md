# Graph Report - iOS-Notes  (2026-05-02)

## Corpus Check
- 10 files · ~66,322,773 words
- Verdict: corpus is large enough that graph structure adds value.

## Summary
- 51 nodes · 74 edges · 8 communities detected
- Extraction: 100% EXTRACTED · 0% INFERRED · 0% AMBIGUOUS
- Token cost: 0 input · 0 output

## Community Hubs (Navigation)
- [[_COMMUNITY_Community 0|Community 0]]
- [[_COMMUNITY_Community 1|Community 1]]
- [[_COMMUNITY_Community 2|Community 2]]
- [[_COMMUNITY_Community 3|Community 3]]
- [[_COMMUNITY_Community 5|Community 5]]
- [[_COMMUNITY_Community 6|Community 6]]
- [[_COMMUNITY_Community 8|Community 8]]
- [[_COMMUNITY_Community 10|Community 10]]

## God Nodes (most connected - your core abstractions)
1. `boot()` - 15 edges
2. `render()` - 6 edges
3. `$()` - 5 edges
4. `setText()` - 4 edges
5. `renderError()` - 4 edges
6. `buildBottomNav()` - 4 edges
7. `runSearch()` - 4 edges
8. `process_file()` - 3 edges
9. `escapeHtml()` - 3 edges
10. `buildToc()` - 3 edges

## Surprising Connections (you probably didn't know these)
- `buildBottomNav()` --calls--> `$()`  [EXTRACTED]
  assets/lesson.js → assets/lesson.js  _Bridges community 8 → community 10_
- `boot()` --calls--> `$()`  [EXTRACTED]
  assets/lesson.js → assets/lesson.js  _Bridges community 8 → community 1_
- `boot()` --calls--> `escapeHtml()`  [EXTRACTED]
  assets/lesson.js → assets/lesson.js  _Bridges community 10 → community 1_
- `boot()` --calls--> `buildToc()`  [EXTRACTED]
  assets/lesson.js → assets/lesson.js  _Bridges community 0 → community 1_
- `render()` --calls--> `slug()`  [EXTRACTED]
  assets/search.js → assets/search.js  _Bridges community 6 → community 2_

## Communities

### Community 0 - "Community 0"
Cohesion: 0.29
Nodes (4): attachCopyButtons(), buildToc(), runHighlight(), setupScrollSpy()

### Community 1 - "Community 1"
Cohesion: 0.29
Nodes (7): attachExternalLinks(), attachHeadingAnchors(), boot(), configureMarked(), ensureHeadingIds(), getParam(), highlightActiveNav()

### Community 2 - "Community 2"
Cohesion: 0.47
Nodes (4): buildModal(), fetchIndex(), openSearch(), slug()

### Community 3 - "Community 3"
Cohesion: 0.83
Nodes (3): process_file(), replace_alamofire_get_data(), replace_alamofire_get_params()

### Community 5 - "Community 5"
Cohesion: 0.5
Nodes (4): escapeRegex(), runSearch(), score(), tokenize()

### Community 6 - "Community 6"
Cohesion: 0.67
Nodes (4): buildSnippet(), escapeHtml(), highlight(), render()

### Community 8 - "Community 8"
Cohesion: 1.0
Nodes (3): $(), renderError(), setText()

### Community 10 - "Community 10"
Cohesion: 1.0
Nodes (2): buildBottomNav(), escapeHtml()

## Knowledge Gaps
- **Thin community `Community 10`** (2 nodes): `buildBottomNav()`, `escapeHtml()`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `boot()` connect `Community 1` to `Community 0`, `Community 8`, `Community 10`?**
  _High betweenness centrality (0.035) - this node is a cross-community bridge._
- **Why does `render()` connect `Community 6` to `Community 2`, `Community 5`?**
  _High betweenness centrality (0.004) - this node is a cross-community bridge._
- **Why does `runSearch()` connect `Community 5` to `Community 2`, `Community 6`?**
  _High betweenness centrality (0.001) - this node is a cross-community bridge._