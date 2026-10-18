---
id: F12
title: "Retrieval design specification"
owner: "Architect."
trigger: "At design; revised on any change to corpus, chunker, embedding model or filter."
signatory: "Architect; data owner for the filter design."
source: "Enterprise AI Architecture Primer, Appendix F"
---

# F12. Retrieval design specification

**Purpose.** Record the chunking, indexing, filtering and citation decisions with the input that drove each, so that a bad answer can be localized to a stage.
**Owner.** Architect.
**Produced.** At design; revised on any change to corpus, chunker, embedding model or filter.
**Signed by.** Architect; data owner for the filter design.

```
SYSTEM / corpus / version / date

0 PRECONDITION
  Corpus size in tokens: __________
  Under roughly 200,000 tokens and rarely changing?
  If yes, do not build retrieval. Cache the corpus in the
  prefix and record that decision here instead.
  Questions that are counts or aggregations over the corpus
  are routed to a structured query, not to retrieval

1 CHUNKING, chosen by what the corpus is
  Corpus structure: [clause-numbered legal documents]
  Strategy: fixed-size | semantic | hierarchical
  Chosen: hierarchical      Because: the corpus has a stable
  clause hierarchy and mid-clause cuts destroy meaning
  Size / overlap / table handling / heading retention

2 INDEXING, chosen by how queries are phrased
  Observed query pattern: [mixed. exact clause identifiers
  and paraphrased concepts]
  Strategy: dense | sparse | hybrid
  Chosen: hybrid, merged by reciprocal rank fusion
  Because: identifiers need lexical, concepts need semantic
  Embedding model and version: __________ (registered in F8)

3 RETRIEVAL
  k retrieved: 150   passed after rerank: 20   in context: 8
  Reranker and version: __________
  Filters, and the order they run in:
    tenant -> access labels -> effective date -> jurisdiction
    -> similarity
  **Filters run before ranking, never after.** Post-filtering
  leaks through result counts, latency and citations
  Identity used for filtering: the end user, not a service
  account

4 ASSEMBLY AND CITATION
  Context budget and what is dropped first
  Ordering rule
  Chunk identity preserved end to end: yes
  Citation granularity: sentence to chunk to document offset
  Grounding and citation are separate requirements. State
  which is enforced and how

5 TENANCY
  Logical | namespace | physical.  Chosen: __________
  Test: if one misconfigured filter could expose one tenant
  to another and that exposure would be notifiable, logical
  separation is insufficient

6 MEASUREMENT, retrieval measured separately from generation
  Recall at k __ | Precision at k __ | Mean reciprocal rank __
  Groundedness __ | Citation accuracy __ | Faithfulness __
  Never report a single accuracy number for this system
```

**Final Liability rests with the Human.**
