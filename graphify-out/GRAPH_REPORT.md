# Graph Report - .  (2026-05-01)

## Corpus Check
- Large corpus: 741 files · ~692,222 words. Semantic extraction will be expensive (many Claude tokens). Consider running on a subfolder, or use --no-semantic to run AST-only.

## Summary
- 5143 nodes · 18185 edges · 45 communities detected
- Extraction: 92% EXTRACTED · 8% INFERRED · 0% AMBIGUOUS · INFERRED: 1497 edges (avg confidence: 0.8)
- Token cost: 0 input · 0 output

## Community Hubs (Navigation)
- [[_COMMUNITY_Module 0|Module 0]]
- [[_COMMUNITY_Module 1|Module 1]]
- [[_COMMUNITY_Module 2|Module 2]]
- [[_COMMUNITY_Module 3|Module 3]]
- [[_COMMUNITY_Module 4|Module 4]]
- [[_COMMUNITY_Module 5|Module 5]]
- [[_COMMUNITY_Module 6|Module 6]]
- [[_COMMUNITY_Module 7|Module 7]]
- [[_COMMUNITY_Module 8|Module 8]]
- [[_COMMUNITY_Module 9|Module 9]]
- [[_COMMUNITY_Module 10|Module 10]]
- [[_COMMUNITY_Module 11|Module 11]]
- [[_COMMUNITY_Module 12|Module 12]]
- [[_COMMUNITY_Module 13|Module 13]]
- [[_COMMUNITY_Module 14|Module 14]]
- [[_COMMUNITY_Module 15|Module 15]]
- [[_COMMUNITY_Module 16|Module 16]]
- [[_COMMUNITY_Module 17|Module 17]]
- [[_COMMUNITY_Module 18|Module 18]]
- [[_COMMUNITY_Module 19|Module 19]]
- [[_COMMUNITY_Module 20|Module 20]]
- [[_COMMUNITY_Module 21|Module 21]]
- [[_COMMUNITY_Module 22|Module 22]]
- [[_COMMUNITY_Module 23|Module 23]]
- [[_COMMUNITY_Module 24|Module 24]]
- [[_COMMUNITY_Module 25|Module 25]]
- [[_COMMUNITY_Module 26|Module 26]]
- [[_COMMUNITY_Module 27|Module 27]]
- [[_COMMUNITY_Module 28|Module 28]]
- [[_COMMUNITY_Module 29|Module 29]]
- [[_COMMUNITY_Module 30|Module 30]]
- [[_COMMUNITY_Module 31|Module 31]]
- [[_COMMUNITY_Module 32|Module 32]]
- [[_COMMUNITY_Module 33|Module 33]]
- [[_COMMUNITY_Module 34|Module 34]]
- [[_COMMUNITY_Module 35|Module 35]]
- [[_COMMUNITY_Module 36|Module 36]]
- [[_COMMUNITY_Module 37|Module 37]]
- [[_COMMUNITY_Module 38|Module 38]]
- [[_COMMUNITY_Module 39|Module 39]]
- [[_COMMUNITY_Module 40|Module 40]]
- [[_COMMUNITY_Module 41|Module 41]]
- [[_COMMUNITY_Module 42|Module 42]]
- [[_COMMUNITY_Module 43|Module 43]]
- [[_COMMUNITY_Module 44|Module 44]]

## God Nodes (most connected - your core abstractions)
1. `Js()` - 2327 edges
2. `push()` - 281 edges
3. `push()` - 280 edges
4. `O()` - 243 edges
5. `e()` - 167 edges
6. `get()` - 103 edges
7. `get()` - 103 edges
8. `forEach()` - 98 edges
9. `Ht()` - 95 edges
10. `forEach()` - 84 edges

## Surprising Connections (you probably didn't know these)
- `copy_contents()` --calls--> `join()`  [INFERRED]
  scratch/migrate.py → themes/hugo-book/static/mermaid.min.js
- `process_markdown_files()` --calls--> `walk()`  [INFERRED]
  scratch/migrate.py → themes/hugo-book/static/mermaid.min.js
- `add_frontmatter()` --calls--> `search()`  [INFERRED]
  scratch/migrate.py → themes/hugo-book/assets/search.js
- `add_frontmatter()` --calls--> `group()`  [INFERRED]
  scratch/migrate.py → themes/hugo-book/static/mermaid.min.js
- `add_frontmatter()` --calls--> `write()`  [INFERRED]
  scratch/migrate.py → themes/hugo-book/static/mermaid.min.js

## Communities

### Community 0 - "Module 0"
Cohesion: 0.01
Nodes (232): Ah(), alternatives(), Am(), AT_LEAST_ONE(), AT_LEAST_ONE1(), AT_LEAST_ONE2(), AT_LEAST_ONE3(), AT_LEAST_ONE4() (+224 more)

### Community 1 - "Module 1"
Cohesion: 0.01
Nodes (191): alternatives(), AT_LEAST_ONE(), AT_LEAST_ONE1(), AT_LEAST_ONE2(), AT_LEAST_ONE3(), AT_LEAST_ONE4(), AT_LEAST_ONE5(), AT_LEAST_ONE6() (+183 more)

### Community 2 - "Module 2"
Cohesion: 0.02
Nodes (285): _7e(), A2(), ad(), addNode(), AEe(), AL(), aMe(), AQ() (+277 more)

### Community 3 - "Module 3"
Cohesion: 0.02
Nodes (285): $2(), $9(), AAe(), aC(), accept(), addToResyncTokens(), _Ae(), aF() (+277 more)

### Community 4 - "Module 4"
Cohesion: 0.02
Nodes (170): _, AA(), Ag(), B, bA(), Bg(), BI(), C() (+162 more)

### Community 5 - "Module 5"
Cohesion: 0.03
Nodes (81): F, element(), focusSearchFieldOnKeyPress(), init(), isHotkey(), search(), _, an() (+73 more)

### Community 6 - "Module 6"
Cohesion: 0.03
Nodes (201): each(), Ht(), mt(), _8(), e8(), k8(), s8(), x8() (+193 more)

### Community 7 - "Module 7"
Cohesion: 0.04
Nodes (181): $2(), $9(), AAe(), aC(), accept(), _Ae(), aF(), aFe() (+173 more)

### Community 8 - "Module 8"
Cohesion: 0.02
Nodes (179): $6e(), addAll(), addAnnotation(), addAttributes(), addClass(), addClassesToNamespace(), addCssStyles(), addDescription() (+171 more)

### Community 9 - "Module 9"
Cohesion: 0.02
Nodes (173): $6e(), addAnnotation(), addAttributes(), addClass(), addClassesToNamespace(), addCssStyles(), addDescription(), addElement() (+165 more)

### Community 10 - "Module 10"
Cohesion: 0.02
Nodes (158): $A(), O(), s(), $0e(), a(), addAstNodeRegionWithAssignmentsTo(), ale(), b$() (+150 more)

### Community 11 - "Module 11"
Cohesion: 0.02
Nodes (134): __(), _0(), A7e(), a8(), ACTION(), activationCount(), add(), addActor() (+126 more)

### Community 12 - "Module 12"
Cohesion: 0.02
Nodes (125): U, hHe(), $0e(), _7e(), a(), addAll(), Ah(), Am() (+117 more)

### Community 13 - "Module 13"
Cohesion: 0.03
Nodes (116): ACTION(), addParents(), addTokenUsingPush(), ADe(), after(), assignWithoutOverride(), before(), buildCompositeNode() (+108 more)

### Community 14 - "Module 14"
Cohesion: 0.04
Nodes (101): acquireParserWorker(), addHiddenNodes(), addParents(), AG(), beginGroup(), bh(), blockquote(), blockTokens() (+93 more)

### Community 15 - "Module 15"
Cohesion: 0.04
Nodes (104): ie(), _5(), A5(), aa(), AK(), bBe(), bl(), c1() (+96 more)

### Community 16 - "Module 16"
Cohesion: 0.03
Nodes (102): $(), __(), _0(), A7e(), a8(), activationCount(), add(), addActor() (+94 more)

### Community 17 - "Module 17"
Cohesion: 0.03
Nodes (101): addAstNodeRegionWithAssignmentsTo(), all(), allElements(), ap(), Bse(), build(), buildKeywordTokens(), buildReference() (+93 more)

### Community 18 - "Module 18"
Cohesion: 0.06
Nodes (99): addALink(), addDetails(), addLinks(), addProperties(), alternative(), assertion(), atom(), atomEscape() (+91 more)

### Community 19 - "Module 19"
Cohesion: 0.04
Nodes (96): addEntry(), AK(), bBe(), buildDuplicateRuleNameError(), buildKeywordPattern(), cN(), computeIsSubtype(), computeRuleType() (+88 more)

### Community 20 - "Module 20"
Cohesion: 0.04
Nodes (85): e(), pt(), Abe(), checkSingleRoot(), EEe(), gy(), H1(), H3() (+77 more)

### Community 21 - "Module 21"
Cohesion: 0.03
Nodes (73): Abe(), addALink(), addDetails(), addDocument(), addLinks(), addPoints(), addProperties(), buildDocuments() (+65 more)

### Community 22 - "Module 22"
Cohesion: 0.04
Nodes (76): addToResyncTokens(), atLeastOneInternalLogic(), atLeastOneSepFirstInternalLogic(), attemptInRepetitionRecovery(), BACKTRACK(), buildDuplicateRuleNameError(), buildEarlyExitMessage(), buildFullFollowKeyStack() (+68 more)

### Community 23 - "Module 23"
Cohesion: 0.04
Nodes (76): A_e(), all(), allElements(), aUe(), b2(), b_e(), bK(), bue() (+68 more)

### Community 24 - "Module 24"
Cohesion: 0.07
Nodes (69): acquireParserWorker(), addHiddenNodes(), AG(), beginGroup(), bh(), buildLeafNode(), buildRootNode(), callFunction() (+61 more)

### Community 25 - "Module 25"
Cohesion: 0.04
Nodes (66): age(), bezierCurveTo(), bje(), closePath(), cqe(), D_e(), dqe(), eet() (+58 more)

### Community 26 - "Module 26"
Cohesion: 0.05
Nodes (58): autolink(), blockquote(), blockTokens(), buildKeywordToken(), buildTerminalToken(), code(), codespan(), def() (+50 more)

### Community 27 - "Module 27"
Cohesion: 0.05
Nodes (56): A_e(), aI(), Ax(), b2(), b_e(), bCe(), bK(), bLe() (+48 more)

### Community 28 - "Module 28"
Cohesion: 0.04
Nodes (55): addMembers(), ADe(), bindFunctions(), Bse(), buildKeywordTokens(), buildTerminalTokens(), buildTokens(), D2() (+47 more)

### Community 29 - "Module 29"
Cohesion: 0.06
Nodes (53): bLe(), bM(), buildLeftRecursionError(), buildRuleNotFoundError(), C2(), C_e(), checkIsTarget(), concat() (+45 more)

### Community 30 - "Module 30"
Cohesion: 0.05
Nodes (51): ap(), buildReference(), calculate(), computeLocalScopes(), createDescription(), createLinkingError(), createScope(), dD() (+43 more)

### Community 31 - "Module 31"
Cohesion: 0.05
Nodes (51): autolink(), codespan(), createDescriptions(), cue(), del(), em(), emStrong(), eQ() (+43 more)

### Community 32 - "Module 32"
Cohesion: 0.1
Nodes (45): _5(), $8e(), A0(), A5(), b8e(), bl(), C5(), clamp() (+37 more)

### Community 33 - "Module 33"
Cohesion: 0.11
Nodes (42): $8e(), A0(), b8e(), clamp(), f8e(), FK(), formatHsl(), g8e() (+34 more)

### Community 34 - "Module 34"
Cohesion: 0.08
Nodes (42): II(), $4(), Axe(), Cl(), cM(), D9e(), dCe(), dit() (+34 more)

### Community 35 - "Module 35"
Cohesion: 0.06
Nodes (42): addNode(), bEe(), c1e(), count(), cW(), cwe(), decorateNode(), _Ee() (+34 more)

### Community 36 - "Module 36"
Cohesion: 0.08
Nodes (42): $4(), Axe(), B7e(), Bn(), Cl(), cM(), Cxe(), dEe() (+34 more)

### Community 37 - "Module 37"
Cohesion: 0.06
Nodes (41): aI(), Ax(), bCe(), Bg(), c6e(), cramp(), eT(), extend() (+33 more)

### Community 38 - "Module 38"
Cohesion: 0.07
Nodes (36): bezierCurveTo(), c1e(), closePath(), cW(), eet(), Eje(), eMe(), f_() (+28 more)

### Community 39 - "Module 39"
Cohesion: 0.08
Nodes (33): AN(), B4e(), BI(), bt(), constructor(), df(), _Ee(), errors() (+25 more)

### Community 40 - "Module 40"
Cohesion: 0.08
Nodes (33): Bg(), cramp(), Dxe(), eT(), extend(), fontMetrics(), g3(), G9() (+25 more)

### Community 41 - "Module 41"
Cohesion: 0.08
Nodes (30): age(), bje(), cqe(), D_e(), dqe(), FJe(), fqe(), Gb() (+22 more)

### Community 42 - "Module 42"
Cohesion: 0.1
Nodes (26): aUe(), bue(), C2e(), cde(), E2e(), eH(), eUe(), iue() (+18 more)

### Community 43 - "Module 43"
Cohesion: 0.15
Nodes (23): calculateHorizontalSpace(), calculateSpace(), calculateSpaceIfDrawnHorizontally(), calculateSpaceIfDrawnVertical(), calculateVerticalSpace(), getAxisOuterPadding(), getDrawableElement(), getDrawableElements() (+15 more)

### Community 44 - "Module 44"
Cohesion: 0.67
Nodes (1): r()

## Knowledge Gaps
- **Thin community `Module 44`** (3 nodes): `r()`, `auto-render.min.js`, `auto-render.min.js`
  Too small to be a meaningful cluster - may be noise or needs more connections extracted.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `Js()` connect `Module 0` to `Module 2`, `Module 4`, `Module 5`, `Module 6`, `Module 7`, `Module 8`, `Module 10`, `Module 11`, `Module 12`, `Module 14`, `Module 15`, `Module 18`, `Module 20`, `Module 22`, `Module 23`, `Module 28`, `Module 29`, `Module 30`, `Module 31`, `Module 33`, `Module 34`, `Module 37`, `Module 38`, `Module 39`, `Module 41`?**
  _High betweenness centrality (0.603) - this node is a cross-community bridge._
- **Why does `O()` connect `Module 10` to `Module 0`, `Module 1`, `Module 2`, `Module 3`, `Module 4`, `Module 6`, `Module 7`, `Module 8`, `Module 9`, `Module 11`, `Module 12`, `Module 13`, `Module 14`, `Module 15`, `Module 16`, `Module 17`, `Module 18`, `Module 19`, `Module 20`, `Module 21`, `Module 22`, `Module 23`, `Module 24`, `Module 25`, `Module 26`, `Module 27`, `Module 28`, `Module 30`, `Module 31`, `Module 32`, `Module 33`, `Module 34`, `Module 35`, `Module 36`, `Module 38`, `Module 39`, `Module 42`?**
  _High betweenness centrality (0.290) - this node is a cross-community bridge._
- **Why does `e()` connect `Module 20` to `Module 0`, `Module 1`, `Module 2`, `Module 3`, `Module 4`, `Module 6`, `Module 7`, `Module 8`, `Module 9`, `Module 10`, `Module 11`, `Module 12`, `Module 13`, `Module 15`, `Module 16`, `Module 17`, `Module 21`, `Module 25`, `Module 26`, `Module 27`, `Module 28`, `Module 29`, `Module 30`, `Module 32`, `Module 33`, `Module 35`, `Module 37`, `Module 38`, `Module 41`?**
  _High betweenness centrality (0.039) - this node is a cross-community bridge._
- **Are the 235 inferred relationships involving `O()` (e.g. with `b$()` and `w$()`) actually correct?**
  _`O()` has 235 INFERRED edges - model-reasoned connections that need verification._
- **Are the 160 inferred relationships involving `e()` (e.g. with `UV()` and `iTe()`) actually correct?**
  _`e()` has 160 INFERRED edges - model-reasoned connections that need verification._
- **Should `Module 0` be split into smaller, more focused modules?**
  _Cohesion score 0.01 - nodes in this community are weakly interconnected._
- **Should `Module 1` be split into smaller, more focused modules?**
  _Cohesion score 0.01 - nodes in this community are weakly interconnected._