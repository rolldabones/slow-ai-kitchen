---
id: F11
title: "Knowledge source register and ingestion contract"
owner: "Knowledge owner per domain."
trigger: "Before ingestion of any source; reviewed on the freshness cadence."
signatory: "Knowledge owner for authority, data owner for access permission and whoever holds the license for the right to index. Those are three different signatures and the third is the one most often assumed."
source: "Enterprise AI Architecture Primer, Appendix F"
---

# F11. Knowledge source register and ingestion contract

**Purpose.** Record what is in the estate, who owns it, whether it is authoritative and on what terms it enters the index.
**Owner.** Knowledge owner per domain.
**Produced.** Before ingestion of any source; reviewed on the freshness cadence.
**Signed by.** Knowledge owner for authority, data owner for access permission and whoever holds the license for the right to index. Those are three different signatures and the third is the one most often assumed.

**Right to index** is a separate column from sensitivity and from access permission, and it is the field 4.14 requires. Access permission answers whether people here may read the work. Right to index answers whether the organization may copy it, derive representations of it and expose its substance through an assistant, which a reading license does not by itself permit. Populate it before ingestion, from the license or the contract, and record the basis rather than a yes.

| Knowledge domain | Location | Named owner | Authority | Right to index | State | Effective dates | Sensitivity | Query traffic | Ingest decision |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Approval thresholds for outbound payments | ERP configuration table | Finance systems lead | Authoritative | Own content | Current | Live | Internal | High | **Do not index.** Route to a tool call |
| Approval thresholds, wiki page | Confluence | Unowned | Copy | Own content | Contradicted | Unknown | Internal | High | Deprecate and redirect |
| Standard contract playbook | Document management, /legal/playbooks | Contract counsel | Authoritative | Own content | Current | From 2025-07-01 | Confidential | High | Ingest |
| Historic negotiation notes | Shared drive | Departed | Derived | Own content | Aging | Unknown | Confidential | Low | Elicit and rewrite, or exclude |
| Subscribed standards library | Vendor portal | Compliance lead | Authoritative | **Read license only, no index right** ⚠ | Current | Per subscription term | Confidential | Medium | **Do not index.** Link out, or negotiate an index right at renewal |

```
INGESTION CONTRACT, per source that is ingested
 Source ID / connector / credential / owner of the credential
 Freshness requirement    stated in time: [4 hours | 30 days]
 Reindex strategy         continuous incremental | scheduled
                          full rebuild
 Parse method             table-aware | text | OCR
 Parse fidelity check     sampled at __%, by whom, cadence
 Reconciliation           document count at source vs count in
                          index, run daily, alert on drift
 Required metadata, all nine present or the chunk is rejected
   document id | version | effective from | effective until |
   supersedes | jurisdiction | classification | access labels
   | authority flag
 Access labels            propagated to chunk level, applied as
                          a pre-filter at query time
 Deletion propagation     source delete removes chunk,
                          embedding, index entry, cache entry
                          within __ hours, evidenced
 Supersession behavior    superseded content is removed from
                          the retrievable set, not merely
                          marked
 Advisory labeling        guidelines carry an explicit advisory
                          label in the retrieved text
 Freshness published      to the user interface: yes
 Write path owner         who may put content into this index
```

**The write path owner is the field most often blank and the largest quiet security gap.** Retrieval is treated as a read-side concern while the set of principals who can put content into the index is larger and less reviewed than the set who can read from it.

**Final Liability rests with the Human.**
