# Changelog

All notable changes to the Slow AI Kitchen repository. Versions apply to the repository as a whole; README.md carries the current version in its title block. Prior versions are superseded, never silently overwritten.

## v2.2 (2026-08-20)

Addition. `enterprise-ai-architecture-primer.md` joins the repository as a companion reference: enterprise AI architecture across ten competencies, with a practice layer (review sequence, defect and misdiagnosis catalogs, evidence register), twenty-five artifact templates, an eighteen-diagram set and a vocabulary. The document carries its own masthead (v1.0.0, 2026-08-20 KST) and a license-and-third-party-materials convention: quoted third-party material remains its owners' and is excluded from the CC BY-NC-SA 4.0 grant. README updated accordingly: the primer registered in Repository Contents, an architect entry added to How to Use This Repository and a third-party-materials sentence added to the License section. How to Cite corrected from a stale version number. GitHub truncates the rendered view of the file at this size; Raw and download carry the full document. On method questions the README controls, per the repository rule. No change to the twelve steps, the ten gates, the three tiers, the workshop design or the Your Restaurant addendum.

## v2.1.5 (2026-08-17)

Maintenance. Korea instrument citations corrected to the texts in force; two status notes re-dated on re-verification.

**Correction of substance.** *[Binding law. Pinpoint: Act No. 21311; Presidential Decree No. 36506. As at 17 August 2026 (KST).]* The Korea AI Basic Act entry in `restaurant-resources.md` presented **Law No. 20676** and **Presidential Decree No. 36053** as the instruments in force. **That is struck.** Both have been amended. The Act in force is **Act No. 21311 of 20 January 2026**, in force 21 July 2026. The Enforcement Decree in force is **Presidential Decree No. 36506 of 20 July 2026**, in force 21 July 2026. The original enactments are retained in the entry as the commencement record, not as the operative texts. This correction was made in `ai-governance-for-boards` v1.5.0 on 13 August 2026 and did not propagate to this repository at the time.

**Status notes re-dated on re-verification, not silently.**

- **Korea note, 14 July 2026 to 17 August 2026 (KST).** The grace-period position is unchanged. The note now records the amendment.
- **NIST note, 14 July 2026 to 17 August 2026 (KST).** Re-checked against NIST: AI RMF 1.0 remains the current published version, the AI Action Plan revision is still in progress and AI RMF 1.1 has not been published. Substance unchanged; the date moves because the claim was re-verified, not because the file was touched.

**Unchanged.** The twelve steps, the ten gates, the three tiers, the workshop design and the Your Restaurant addendum.

## v2.1.4 (2026-08-13)

OJ text of the amending regulation obtained; Article 5 date corrected.

**Correction, not a currency update.** The release earlier today stated that the Article 5 application date of 2 February 2025 was "settled and not affected by the Omnibus". Having now read the Official Journal text, that is **wrong in part** and is corrected here.

- **The amending act is identified.** Regulation (EU) 2026/1744 of the European Parliament and of the Council of 8 July 2026, OJ L, 2026/1744, 24.7.2026, ELI http://data.europa.eu/eli/reg/2026/1744/oj, in force 27 July 2026. Article 1, point (40) amends the third paragraph of Article 113 of Regulation (EU) 2024/1689.
- **The pinpoint question is answered.** Article 113 is structured in unnumbered paragraphs with lettered points. The correct citation form is **"Article 113, third paragraph, point (c)"**. "Article 113(3)" is wrong and always was. The prohibition on that form, adopted this morning as a precaution, is now replaced by a positive rule.
- **Article 5 carve-out.** Amended point (a) provides that Chapters I and II apply from 2 February 2025 **with the exception of Article 5(1), first subparagraph, points (ba) and (bb), and Article 5(1a) and (1b), which apply from 2 December 2026**. The general Article 5 date stands; the prohibitions the Omnibus added are deferred. The earlier unqualified statement is struck.
- **High-risk deferrals, verbatim.** Amended point (c): Chapter III, Sections 1, 2 and 3, with the exception of Article 6(5), apply from (i) 2 December 2027 for AI systems classified as high-risk pursuant to Article 6(2) and Annex III, and (ii) 2 August 2028 for those classified pursuant to Article 6(1) and Annex I.
- **New point (d).** Articles 102 to 110 apply from 27 July 2026.
- The OJ-text gap flag is removed from every file that carried it. That outstanding item is closed.

## v2.1.3 (2026-08-13)

License metadata sweep. An `SPDX-License-Identifier: CC-BY-NC-SA-4.0` line and the canonical Creative Commons legal code are now carried inside the existing license file. The filename is unchanged and the human-readable summary is retained above the legal code.

- The primary audience is automated intake and provenance tooling, which reads the SPDX tag rather than prose. Automated license detection previously reported nothing across all twenty-one repositories in this account.
- No change to the licence in force. The identifier records what was already true.

## v2.1.2 (2026-08-13)

Omnibus currency remediation. The Digital Omnibus on AI entered into force on 27 July 2026; notes that described Official Journal publication as pending are recast as operative law with dated amendment notes. The Article 5 application date of 2 February 2025 is stated as fact (Article 113, point (a), Article 5 sitting in Chapter II), resolving one of the standing counsel Unknowns. No pinpoint to a numbered subsection of Article 113 is given: the amending regulation's Official Journal text has not been read and its renumbering is unconfirmed, so the consolidated text is cited with an as-at date and the gap is flagged in the file.

- restaurant-resources.md: EU AI Act status note recast from awaiting Official Journal publication to entered into force 27 July 2026, with a dated amendment note. The listed changes are restated as operative law rather than pending changes.
- Also carried in this release: the BABL AI role lines recast to former, committed separately.

## v2.1.1 (2026-07-30)

Patch release. Trademark rendering and a web-application pointer.

### Added
- How to Use This Repository now points to the web application implementing the twelve steps at https://slow-ai-kitchen.msagent.ai/, available in English, Korean, Vietnamese and Japanese. The application has existed alongside this repository and was undocumented here; Japanese was added to it on 26 to 27 July 2026. The repository is the canonical statement of the method and the application implements it, so the two version independently.

### Changed
- Trademark rendering corrected to the canonical closed-up form GRCnext™. The retired spaced form "GRC next" is withdrawn from repository prose. One occurrence, in the grc line of the Part of the ecosystem section.
- Version table row, How to Cite reference and version pointer updated in lockstep.

### Unchanged
- The twelve steps, the ten gates, the three tiers, the workshop design and the Your Restaurant addendum.

## v2.1.0 (2026-07-14)

- Added the standard Part of the ecosystem section to README.md, linking the canonical [ECOSYSTEM.md](https://github.com/rolldabones/rolldabones/blob/main/ECOSYSTEM.md) and five nearest neighbors (definition-of-done, origami-method, grc, grc-workbook, the-ai-generalist). The former Related Work section is superseded by it; its entries are carried into the neighbor list and the canonical map.
- Moved the version history from README.md to this CHANGELOG.md; README.md now carries a pointer and the current-version summary.
- Corrected a stale version reference in How to Cite (read v2.0.1 while the title block read v2.0.2).
- Refreshed all regulatory-currency content in restaurant-resources.md to a 14 July 2026 (KST) verification date: EU AI Act status note updated for the adopted Digital Omnibus on AI (Parliament 16 June 2026, Council 29 June 2026; Annex III high-risk obligations deferred to 2 December 2027, Annex I to 2 August 2028, legacy watermarking to 2 December 2026, new NCII/CSAM prohibition from 2 December 2026); Korea AI Basic Act entry corrected to reflect the Enforcement Decree (Presidential Decree No. 36053) in force since 22 January 2026 with the one-year-plus fine grace period; NIST AI RMF status note re-dated (1.0 remains current, revision ongoing, April 2026 critical-infrastructure profile concept note); ISO/IEC 42006:2025 (published July 2025) and ISO/IEC 12792:2025 (published November 2025) confirmed published and their [VERIFY] flags resolved; a dated regulatory-currency banner added at the top of the file.
- Added a dated regulatory-currency note to federal-workforce-literacy-bridge.md confirming TEN 07-25 verified live and unamended on 14 July 2026, and reworded a stale cross-reference in its Scope Boundaries section (the undefined "AI GRC System" now points to the Korea AI Basic Act entry in restaurant-resources.md and the Your Restaurant addendum's Pillar 3).
- No change to the twelve steps, the ten gates, the three tiers, the workshop design, the Your Restaurant addendum, the Slow AI Cookbook or the two sample kitchen prompts.

## v2.0.2 (2026-07-14)

- Merged the slow-ai-cookbook-starter repository into this one. slow-ai-cookbook.md is now the sole canonical Starter Edition and the standalone repository is retired; its two editorial corrections to the card field descriptions are incorporated.
- Executed the kebab-case .md companion-file renames recorded in the v2.0 changelog but not previously applied, so all Repository Contents links now resolve.
- Renamed the license file to LICENSE.
- Removed a stray upload-artifact link line from the README.
- No change to the twelve steps, the ten gates, the three tiers, the workshop design or the Your Restaurant addendum.

## v2.0.1 (2026-07-10)

- Added *The Definition of Done Is the Work of the Human* (the depth companion to Gates 1, 6 and 7) to Related Work and updated the title block.
- No change to the twelve steps, the ten gates, the three tiers, the workshop design or the Your Restaurant addendum.

## v2.0 (2026-06-11)

- Added linked table of contents, repository contents index, gate map, Tier Application Map, role tables, checkbox Definition of Done, Related Work, citation, license and changelog sections.
- Licensed the repository under CC BY-NC-SA 4.0 and added a LICENSE file.
- Renamed the companion files to kebab-case with .md extensions and updated the internal cross-reference in federal-workforce-literacy-bridge.md accordingly.
- Corrected the standard designation to ISO/IEC 42001.
- Consolidated to a single title block.
- No change to the twelve steps, the ten gates, the three tiers, the workshop design or the Your Restaurant addendum.

## v1.0 (2026)

- Initial publication: method, risk tiers, roles, workshop guide, the Feast and the Your Restaurant addendum.

---

**Final Liability rests with the Human.**
