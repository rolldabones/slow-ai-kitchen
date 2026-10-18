# Changelog

All notable changes to the Slow AI Kitchen repository. Versions apply to the repository as a whole; README.md carries the current version in its title block. Prior versions are superseded, never silently overwritten.

## v2.13.0 (2026-10-18)

Consultant Workbook release, session T5 of the whole-account review of 15 October 2026 (KST), 18 October 2026 (KST). Minor, because instrument text changes: the Workbook gains six delivery instruments and a completion test on every record. No step, gate, tier, role or principle changes.

- **`consultant-workbook.md`, v1.4.0, dated amendment note.** Doc section 5 found it could not be run cold. Added, as new sections with their own Done when lines: a thirty-day calendar (day 1 to day 30, each day's work and records); a discovery interview guide (who, how long, nine question topics keyed to the records they feed, interviewer rules); a benefit scale for W02 (four factors scored 0 to 3 from evidence, ranked only after the mandatory entry screen); a defect severity scale (S1 to S4, material defect = S1 or S2, first pass accepted only without one, response per grade); a synthetic case kit (structure from real work and none of its content, four difficulty groups, planted conditions, human-written answer keys, separated tuning, workshop and test sets, labeling and the limit of synthetic results); and a sponsor report for days 15, 20 and 28. Every working record, W01 to W24A, carries a Done when line; W01's inline test moves to it and W03's completion test stays. W02, W12, W15, W16, W19, the cadence table and the worked case point to the new instruments. W13 states the README's Gate 6 rule that a model's review of its own output in the same session is not verification. The worked case's effort table uses W16's five categories, totals unchanged (900 and 600 minutes); the combined rows are divided between the categories they now span (manual 250 and 350, review 170 and approval 30; AI-assisted 100 and 130, review 190 and approval 30). The resource register is re-verified on 18 October 2026: GRC Workbook v4.3.3, Definition of Done v1.2.5, AI Impact Assessment Tool v1.4.0, AI GRC Copilot v1.2.1, grc v2.3.0; DOCTRINE.md v1.2.0 unchanged. Links to other files in this repository are absolute, so they resolve from the derived parts. No existing heading is renamed, so the eight inbound links (seven anchors) from AI-Governance-Academy and Take-Out resolve. Doc section 5; reviewer report 02, items 25, 27 and 28 and idea 2.
- **`workbook/`, new.** The Workbook as 48 derived parts with a reading index, one section or working record per file, generated with `account-maintenance/tools/split_markdown.py consultant-workbook.md workbook --title "Consultant Workbook" --h2-split "Consultant Workbook" --max-bytes 240000` and verified to rebuild the master byte for byte. File names follow the tool's form (`15-w01-engagement-charter.md` to `40-w24a-monitoring-and-ninety-day-actions.md`). The master remains the file of record; parts are regenerated, never edited.
- **`README.md`.** The two Workbook descriptions name the calendar, the six instruments and the Done when lines; Repository Contents gains the `workbook/` row. No heading changes, so the inbound anchors resolve.
- Title block, How to Cite, Current version and `CITATION.cff` move to v2.13.0 in lockstep. `enterprise-ai-architecture-primer.md` and `primer/` are unchanged byte for byte (the Primer split is session T8). The Kitchen application is not rebuilt for this release (D8: one rebuild after T8).
- **Findings by class.** Confirmed and edited: doc section 5 Workbook row (interview guide, benefit scale, defect severity scale, synthetic-case guidance, sponsor report, day calendar, effort categories, derived parts with Done when lines); report 02 items 25, 27 and 28 and idea 2. Already fixed (v1.3.0, 17 October 2026): report 02 items 17 to 20 and 33. Not reproducible: none. Deferred: none.

## v2.12.0 (2026-10-17)

Doctrine conformance and mechanical release, session T3 of the whole-account review of 15 October 2026 (KST). Minor, because the step table changes: the Owner is named at Step 1 and confirmed at Step 6 (Gate 5), the sequence DOCTRINE.md section 3.1 ("named at specification"), the Consultant Workbook and Take-Out already state. No step, gate, tier or role is added or removed.

- **`README.md`.** Step table: Step 1 output "Task brief, with the named Owner"; Step 6 primary role "Owner (named at Step 1, confirmed here)"; the null gate marker "—" reads "none". Step 1 names the Owner; Step 6 confirms the human named in the task brief and names reviewer, approver and escalation path. Step 12 states that ten Service Records trigger a method review under it, as the Service Record and Take-Out already say. "Five principles govern the method" reads "Five operating rules follow from that principle", matching the one principle of the opening. The two role headings lose their en dashes ("Steps 1 to 9", "Steps 10 to 12"); no inbound anchor in the account used the old slugs. The ecosystem section gains the DOCTRINE.md pointer sentence with the short forms, and the grc neighbor line places the GRCnext™ primitives' engine in GRCnext-Copilot. The bridge is named for the framework it maps. Doc sections 1 and 8; reviewer report 01, items 1, 8, 10, 25 and 28.
- **Derivation modules, v1.1.0 each, dated amendment notes.** One doctrine block in all three, pointing to the DOCTRINE.md short forms. `karpathys-kitchen.md`: Informed Intent's four elements replace "objective, permitted use, constraints and acceptance criteria"; the five-layer correspondence maps Intent, Boundary and Authority to Informed Intent; the gate map follows the README (Steps 1 and 7 gateless, Step 3 at Gate 2); GRCnext™ is no longer counted a doctrine; the Link Register's ecosystem row is re-checked; the closing line is last. `newtons-kitchen.md`: Law I names the authorizer's five conditions and uses the Informed Intent short form; Law III states that the task-level owner is named in the Step 1 brief and confirmed at Gate 5; "Human gates" is the common noun; the closing line is last. `coetzees-kitchen.md`: section VII asks on whose authority and whether the authorizer meets the five conditions; Final Liability carries decision rights, oversight and the power to intervene and governs the whole span, not exit; the scope note counts five gates. Doc section 1; reviewer report 02, items 1 to 4, 7, 10 to 15 and 32.
- **`consultant-workbook.md`, v1.3.0, dated amendment note.** The doctrine paragraph copies the three DOCTRINE.md short forms, dropping the two attributes appended to Final Liability; the resource register is re-verified on 17 October 2026 against the versions shipped in the same session (DOCTRINE.md v1.2.0, Definition of Done v1.2.4, GRC Workbook v4.3.2, AI Impact Assessment Tool v1.2.12, AI GRC Copilot v1.1.8, grc v2.2.4), whose T3 changes touch none of the parts the register cites, and the GRC Workbook's tiering is described as it states it; Cognitive Provenance is attributed to Coetzee's Kitchen; seven headings and labels regain stripped hyphens and commas, with slugs unchanged. Doc section 8; reviewer report 02, items 17 to 20 and 33.
- **`slow-ai-cookbook.md`.** The card's Who Signs field confirms the owner named before the work began; Done Means reads three to seven checks, as the One Sheet and Gate 1 say; the authorizer sentence names the five conditions. Reviewer report 01, item 12.
- **Sample prompts, both.** Task Frame names the human Owner; step 6 confirms that Owner; "Final liability" reads "Final Liability"; the header records the 11 October scope amendment and this one. The compressed prompt gains the closing line; the two-layer method file heading loses a leading space that kept it from rendering. Reviewer report 01, items 9, 17 and 29.
- **`service-record.md`, v1.1.0, dated amendment note.** Header: "Reviewer (Tier 2 and 3) · Approver (Tier 3)", matching the Tier Application Map; the owner is the one named at Step 1 and confirmed at Gate 5. Reviewer report 01, item 11.
- **`take-out-delivery-and-vending-machines.md`.** Two em dashes in author's prose replaced; status "Final"; the closing line moved to the end. No masthead move (style edits, rule of 11 October 2026). Reviewer report 01, items 25 and 27.
- **`federal-workforce-literacy-bridge.md`.** Retitled "Workforce AI Literacy Bridge (DOL TEN 07-25)", completing the re-scope of v2.11.3; the file name is unchanged for link stability. Three em dash pairs and "catalogue" corrected. Reviewer report 02, items 21 and 32.
- Title block, How to Cite, Current version and `CITATION.cff` move to v2.12.0 in lockstep. `enterprise-ai-architecture-primer.md`, `primer/` and `restaurant-resources.md` are unchanged byte for byte; the Primer's house-style lines wait for the v3.0.0 split (session T8).

## v2.11.3 (2026-10-15)

Legal currency patch, session T1 of the whole-account review of 15 October 2026 (KST). Two companion files change; the method is untouched, so patch. Every correction of substance is struck in place and dated.

- **`restaurant-resources.md`.** The EU AI Act entry's body sentence stated the pre-Omnibus timeline ("most high-risk AI system requirements from 2 August 2026; remaining obligations from 2 August 2027") as fact above a status note that superseded it; struck, and the entry now points to the account's canonical [EU AI Act currency note](https://github.com/rolldabones/ai-governance-for-boards/blob/main/05-jurisdictions/eu.md#eu-ai-act-currency-note) in ai-governance-for-boards, published the same day. The status note's "a new Article 5 prohibition" reads as the two prohibitions, points (ba) and (bb), and its Article 50 sentence carries the provider carve-out as verified. NIST IR 8286 is a five-document series (8286D, November 2022, added); SP 800-160 Vol. 1 is cited as Rev. 1 at the current CSRC address. "Every standard ... sits behind a paywall" corrected: ISO/IEC 22989:2022 is free on ISO's Publicly Available Standards page. The "ISO AI Standards Hub maintained by BSI" is the UK AI Standards Hub, led by NPL and BSI, and as at 15 October 2026 (KST) shows only a transition notice, so the two verification pointers to it are re-routed to iso.org. The MAS transition sentence reads "Sections 3 and 4 by 7 October 2027" as the 11 October 2026 read recorded. "under active revision as of July 2026" re-dated to the NIST entries' last re-verification, 17 August 2026. Reviewer report 01, items 2 to 7, 13 and 14.
- **`federal-workforce-literacy-bridge.md`.** Scope note added: TEN 07-25 is addressed, by its own distribution line, to state workforce agencies, boards, American Job Centers, ETA grantees, colleges, apprenticeship agencies and Job Corps centers, "as a resource for program design" for the public workforce and education systems; it is not a federal-workforce literacy standard, and the federal-employee duty (OMB M-25-21) is named as out of scope. The advisory was re-read on 15 October 2026 (KST), no rescissions. "WIOA funding eligibility" struck as unsupported by the TEN. The Article 4 sentence described the pre-Omnibus "ensure" duty; struck and restated from Article 4(1) as amended by Regulation (EU) 2026/1744, read in the Official Journal text the same day. The file name is unchanged for link stability. Reviewer report 02, items 21 to 23.
- **`README.md`.** The two sentences describing the bridge follow its scope note; version table, How to Cite and Current version to v2.11.3; `CITATION.cff` in lockstep. Primer, modules, prompts, Cookbook and Workbook unchanged byte for byte.

## v2.11.2 (2026-10-15)

Byline correction, on the author's instruction of 15 October 2026 (KST). No instrument changes, so patch.

- **Credit line, five files** (`README.md`, `consultant-workbook.md`, `karpathys-kitchen.md`, `coetzees-kitchen.md`, `newtons-kitchen.md`): "CEO, GRC Solutions Korea | former General Counsel, BABL AI" now reads "CEO, GRC Solutions Korea". Name, credit line and website link remain a three-line block.
- **`federal-workforce-literacy-bridge.md`:** the separate byline line "Former General Counsel, BABL AI" is removed, so the block reads name, "CEO, GRC Solutions Korea" and the website link, as in the other modules.
- **Module mastheads do not move.** A credit-line edit is not a change of substance under the module masthead rule of 11 October 2026. The About the author section, which names the former role in prose, is unchanged. No heading is added, removed or renamed in any file.
- Title block, Changelog section, How to Cite and `CITATION.cff` move to v2.11.2 in lockstep. `enterprise-ai-architecture-primer.md` and `primer/` are unchanged byte for byte. No step, gate, tier, role or principle changes.

## v2.11.1 (2026-10-11)

A description correction. The web application was rebuilt on 11 October 2026 against README v2.11.0 and now carries most of the repository, not the twelve steps alone. No instrument changes, so patch.

- **`README.md`, How to Use This Repository, the guided-tool entry:** names what the application carries since the rebuild (the twelve steps, the Cookbook, the sample prompts, the Consultant Workbook, the agent companion, the three derivation modules, the federal bridge and the reference resources), states that this repository is the text of record, and states that the application declares the release its text follows and is rebuilt only after a human release. Read from the deployed bundle on 11 October 2026 (KST).
- Title block, Changelog section, How to Cite and `CITATION.cff` move to v2.11.1 in lockstep. No step, gate, tier, role or principle changes; every other file unchanged byte for byte.

## v2.11.0 (2026-10-11)

Three additions from the author's LinkedIn posts of 9, 29 and 30 September 2026, and the style and currency corrections to `restaurant-resources.md` prepared the same day. The README and two modules gain content, so minor. No gate is added or removed; no step, tier, role or principle changes.

- **`README.md`, Step 9 (Gate 7): the whiteboard test of ownership.** One paragraph after "Release or act only within defined scope.": the owner can stand at a whiteboard and explain to another human what was done, how and why, including what was tried and rejected, with no model in the room; if not, the work is not owned, however good the output looks; and the listener must come equally prepared, because an explanation no one is equipped to question is a performance, not a check. From the post of 9 September 2026 and its second use on 29 September. The post's restatement of Slow AI is not imported; the test is stated as a test of ownership at the release decision.
- **`consultant-workbook.md`, v1.1.0 to v1.2.0.** W22 gains one row in the practical capability table: explain the work to a prepared listener, without the model. W03's existing completion test and the companion's existing sentence on explaining a material outcome are unchanged and now have the canonical form behind them.
- **`slow-ai-cookbook.md`: the One Sheet**, a new section before Recipe 1. The A4 fold, four boxes a side; the front four as fields 1 to 4 of the card and Steps 1 to 4 of the Kitchen; the authorization strip as Informed Intent on paper, its four elements and the authorizer's five conditions in the post's paraphrase, which matches `DOCTRINE.md` v1.1.1; the reverse as fields 5 to 8. From the post of 30 September 2026. The Cookbook carries no masthead; its Repository Contents row names the sheet. The v2.10.0 fence on the Cookbook was lifted by the author's ruling of 11 October 2026.
- **`take-out-delivery-and-vending-machines.md`, v1.1.0 to v1.2.0.** Two sentences in the materiality paragraph of the service ticket section: set limits on counts, not rates, since a tenfold better error rate at a hundredfold volume is ten times the errors; and a grant may authorize a bounded first batch and count its errors before it is extended. From the post of 29 September 2026. The legend, the trajectory figures and the post's four-item statement of Slow AI stay out. Source basis re-pinned to README v2.11.0 by tag.
- **Considered and declined:** a third-party "AI System Specification Sheet" presented as an operationalization of the author's doctrine. It attributes to the author phrases that appear nowhere in the canon or this repository, states Final Liability as a transfer of legal liability by signature against `DOCTRINE.md` section 3.2, adds a C-suite bypass the method does not have and names a vendor model. Nothing from it enters.
- **Em dashes removed from the author's own prose in `restaurant-resources.md`.** The file carried 67 on 53 lines. Removed, 57: 10 in the Pillar headings, now "Pillar 1: Governance Structure" and so on; 34 separators after the bold designation of an entry, now "**Designation.** Title"; 13 in prose and the closing byline, recast with commas, parentheses or semicolons.
- **The fourteen ISO entry titles are restated in ISO's own form**, read on iso.org on 11 October 2026 (KST), on the author's ruling of the same day: the file had rendered them in its own casing with ISO's title-part em dash kept, which was neither a quotation nor house style. Each title is now the catalogue title verbatim, em dashes included, which the repository's rule for quotations exempts from the house style. The 25 em dashes that remain are all inside those titles, on 13 lines, and are the whole residue.
- **Correction of substance, itemized.** ~~ISO/IEC 27701:2019~~ is withdrawn; the current edition is **ISO/IEC 27701:2025** (Edition 2), *Information security, cybersecurity and privacy protection — Privacy information management systems — Requirements and guidance*. ~~ISO/IEC 29100:2011 (Amd 1:2018)~~ is withdrawn; the current edition is **ISO/IEC 29100:2024** (Edition 2). Both read on iso.org on 11 October 2026 (KST); both carry a dated status note; neither description has been re-read against the new text and each note says so. Both supersessions are registered in the account's supersession register at the moment of correction, and no other file in the account carried either superseded designation.
- The regulatory currency line records the ISO re-read. The headings' anchors change; no file in this repository or in `AI-Governance-Academy` links to them.

- Title block, Changelog section, How to Cite and `CITATION.cff` move to v2.11.0 in lockstep. The Primer and its derived parts, the three derivation modules, the Service Record, the sample prompts, the federal bridge and the LICENSE are unchanged byte for byte.

## v2.10.0 (2026-10-11)

An augmentation from four of the author's LinkedIn posts of 7 to 11 October 2026. Two of the changes touch the canonical method, so minor. No gate is added or removed, and no step, role or principle changes. What changes is stated exactly below.

- **`README.md`, Step 8 (Gate 6): a clarification of how the gate is performed.** One paragraph after "fit for use." states what the step table and the Tier Application Map already require: Gate 6 is performed by the human Reviewer against something outside the model; a model's review of its own output in the same session is not verification and does not pass the gate, though it may inform review. A dated evidence note beneath it cites Kamoi et al., TACL 12 (2024), and Huang et al., ICLR 2024, each read on 11 October 2026 and cited only for what its abstract states, and records the author's test of 7 October 2026 with its figures and its limits. The figures were reconciled by running them: 39+52+30, 34+57+32 and 39+55+29 give 121, 123 and 123 of 288; 82+7+5 gives 94; and the difference of 0.7 points between the gate and the plain condition is a difference in accuracy, stated as such. The test covered same-session self-review only; the Primer's "Self-review is not review. Use an independent instance" is unchanged, and whether an independent instance suffices is left open.
- **`README.md`, Risk Tiers: an assignment rule added.** Two sentences after "never looser ones for Tier 3 work": the tier is assigned before the work begins, by a named human, with the reason recorded; in organizational use the registry under Step 10 sets it, and a team does not classify its own work down. Checked against Step 10, which already lists risk tier assignments as registry content, the Cookbook's "floor, not a ceiling" and workbook W05, which records the selected tier with reasons and an accountable owner. The four statements agree.
- **`README.md`, Common Failure Modes:** one bullet, "asking the model to check its own work and calling that verification".
- **Both sample prompts, scope notes only:** one sentence each stating that the prompt's own verification step (step 8 VERIFY in the compressed version; the Verification gate in the two-layer version) is performed by the model on its own output, is a completeness check against the Definition of Done and is not Gate 6. The prompt bodies are unchanged byte for byte.
- **`restaurant-resources.md`: a Singapore entry under a new Supervisory Guidance heading**, placed between the primary instruments and the ISO section so that its authority level is plain. The Monetary Authority of Singapore's Guidelines on Artificial Intelligence Risk Management, issued 7 October 2026, taking effect 7 October 2027 with Sections 5 and 6 by 7 October 2028; what Sections 4 and 6 require; the six minimum items of paragraph 2.5; the nine sources linked in the Guidelines' footnotes, each resolving on 11 October 2026; a mapping of the paragraph 2.5 items to Steps 10 to 12 labeled as the author's reading; one sentence of the author's view on Singapore, labeled as such; a dated status note; and the regulatory currency line extended. Every date, paragraph number and count was read in the primary PDF linked from the MAS page, 30 pages, dated 7 October 2026 on every page. Two things the source corrected: the MAS web page titles the instrument "for Financial Institutions" and the PDF does not, so both forms are recorded; and the nine sources are the nine the footnotes link, with footnote 3 naming three more without links, which the entry says.
- **`take-out-delivery-and-vending-machines.md`, v1.0.0 to v1.1.0: a refusal is a stop condition.** One line in the service ticket under Exit for the refusals that are final, placed beside the existing failed-or-refused-delivery line. One paragraph at the head of Stop, reconcile and hand back on goal-directed runs: a loop held to the ticket's completion criteria within its limits; a failed check may be retried within those limits; a refusal is a stop condition, reported, neither retried nor routed around; an exhausted budget is not success and the receipt reconciles the run as it ended. Anchored to the four elements of Informed Intent and the four-property test the module already uses. The capability is named, not the product; OpenAI's guide *Using Goals in Codex* appears only in Source basis and attribution, read on 11 October 2026 and cited for three things it states. One cross-reference paragraph on Tiny Servants, the term linked to its first public use in the author's essay *Made to Hold* (28 July 2026). The Source basis line is re-pinned to README v2.10.0 by tag, with the v2.8.0 pin kept as history. No vendor product is named in the body.
- **`consultant-workbook.md`, v1.0.0 to v1.1.0: the end point of elapsed turnaround fixed.** One sentence in W15's Definitions to settle before measurement: elapsed turnaround ends at the recorded human release decision under Gate 7 (W13), not at the first draft. W16's End field and W17's turnaround row read consistently with it.
- **Module mastheads.** The two modules whose instrument content changes move to v1.1.0, dated this release; Karpathy's Kitchen, Newton's Kitchen, Coetzee's Kitchen and the Service Record are untouched. Rule applied, on the author's ruling of 11 October 2026: a module's version moves when its substance moves, minor when its instrument content changes, and not for style or link edits. The style edits of v2.9.1 and the link edit of v2.9.2 moved no module masthead and are left as shipped.
- **Carried forward, not in this release:** the whiteboard rule (posts of 9 and 29 September 2026) and the one-sheet exercise (30 September 2026). Vendor survey figures from the post of 9 October 2026 are not evidence for a method and were not added.
- Repository Contents: the `restaurant-resources.md` description now names supervisory guidance. Title block, Changelog section, How to Cite and `CITATION.cff` move to v2.10.0 in lockstep. The Primer and its derived parts, the three derivation modules, the Service Record, the Cookbook, the federal bridge and the LICENSE are unchanged byte for byte. The 31 links from `AI-Governance-Academy/slow-ai-for-the-chief-legal-officer.md` into this repository were checked against the edited tree: 31 of 31 resolve.

## v2.9.2 (2026-09-30)

A link correction. The web application implementing the twelve steps now runs at https://kitchen.grcskorea.com/. No instrument changes, so patch.

- **`README.md`**, How to Use This Repository: application link repointed to https://kitchen.grcskorea.com/.
- **`consultant-workbook.md`**, Resource navigator for delivery: application link repointed.
- The prior address, `slow-ai-kitchen.msagent.ai`, is superseded. The v2.1.1 entry that introduced it is shipped history and is unchanged.
- Title block, Changelog section, How to Cite and `CITATION.cff` move to v2.9.2 in lockstep. No step, gate, tier, role or principle changes.

## v2.9.1 (2026-09-08)

A style correction. Twenty-three serial commas are removed from the author's own prose across nine module files. No instrument changes, so patch.

- ~~"Client capitalized, no Oxford commas, no em dashes, completion spaces rendered as escaped underscore lines so that GitHub does not read them as horizontal rules, sheet headings navigable in the browser."~~ **STRUCK**, as to the words "no Oxford commas" only. The v2.8.0 bullet **House style applied in conversion** asserted that the house style was applied to `consultant-workbook.md` in its conversion. It was not applied completely. `consultant-workbook.md` line 746 carried a serial comma on the day that assertion shipped, and carried it through v2.8.0 and v2.9.0. The rest of that bullet is unaffected and stands. The v2.8.0 entry is left as written rather than rewritten, per the repository rule that prior versions are superseded and never silently overwritten.
- **The three lawful outcomes of Gate 7 carried the comma in every file that states them, and the defect was recorded as one instance.** `consultant-workbook.md` line 746, `service-record.md` line 17 and `newtons-kitchen.md` line 124 all read "confirm, refuse, or amend and confirm" and now read "confirm, refuse or amend and confirm". Only the first was registered. The formula is doctrinal and appears nowhere else in the repository in either form, so the three are corrected together and the statement of the three outcomes is now identical wherever it is made.
- **Twenty further corrections in the author's own prose**, each the removal of one comma and nothing else: `karpathys-kitchen.md` ten, `coetzees-kitchen.md` three, `service-record.md` one, `federal-workforce-literacy-bridge.md` two and one each in `README.md`, `restaurant-resources.md` and `take-out-delivery-and-vending-machines.md`. Every changed line was verified to differ from its predecessor by exactly one deleted comma and by no other byte.
- **Four categories carry a serial comma and are deliberately unchanged**, because none of them is the author's own prose in the sense the house style governs. Direct quotations, including Defoe at `coetzees-kitchen.md` line 50 and Karpathy at `karpathys-kitchen.md` line 408, because altering a quotation misquotes its source. `LICENSE`, which carries the canonical Creative Commons legal code that governs by its own terms. Shipped changelog entries, which are superseded and not rewritten. EU AI Act pinpoint citations, whose commas are the citation form required by the account convention and not a style choice.
- **The Enterprise AI Architecture Primer and its twenty-four derived parts are unchanged byte for byte**, and the rebuild was verified before the commit. The Primer carries serial commas of the same class in an order of magnitude not proportionate to a patch, and correcting them is registered for a release of its own rather than folded in here.
- **README and `CITATION.cff` in lockstep.** Version table, How to Cite, current-version pointer and `CITATION.cff` move to v2.9.1.
- The twelve steps, the ten gates, the three tiers, the workshop, the Your Restaurant addendum, the Primer with its derived parts, the Service Record, the Consultant Workbook and Take-Out, Delivery & Vending Machines are otherwise unchanged byte for byte.

## v2.9.0 (2026-09-07)

Take-Out, Delivery & Vending Machines joins the repository as a standalone operating companion for AI agents. A new instrument enters the repository, so minor.

- **`take-out-delivery-and-vending-machines.md` added**, flat in the repository root like the other modules (decision D-D3 of 6 September 2026). Governed delegation for AI agents across three service patterns: take-out, where the agent prepares work for a human to collect and carry into use; delivery, where the agent is also authorized to carry released work to a specified destination and act there; and vending machines, where a bounded service is available for repeated use at distributed points of access. Prepared against README v2.8.0 at commit `7869f35` and DOCTRINE.md v1.1.1. The manuscript carries its own v1.0.0 and final status; the repository version is this release.
- **Two instruments, both keyed to existing records.** The service ticket is written under the four headings of Informed Intent (purpose, authority, boundaries, exit) and indexes existing briefs, evidence and workbook sheets rather than duplicating them. The service receipt is the run record, reconciling approved actions as successful, failed, unknown or not attempted, and it feeds the Service Record added at v2.7.0. No new gate, no new form to complete twice.
- **The preparation and release distinction made concrete.** Step 10 and Gate 8 authorize the system, Step 5 and Gate 4 bound its use, Steps 8 and 9 with Gates 6 and 7 carry verification and the human release decision. Approval may cover a verified batch identified by exact targets, content, permitted effects and validity conditions; a material change to content, recipients or source conditions returns for review. A completion summary cannot supply missing prior authority.
- **Newton's four-property test applied to the executing system.** Bounded, observable, interruptible and attributable, each with the evidence required before live execution. Restrictions are placed where actions occur rather than in the prompt, encountered content cannot grant permissions, delegation to subagents stays inside the ticket and an uncertain action is not blindly retried.
- **Tiering unchanged.** Automation tied to action is Tier 3 under the existing tiers, with the distinct Reviewer, Approver and Owner, second review, sign-off, escalation and rollback the README already requires. Drafting-only work follows its actual stakes and consequences are counted across related agents and runs.
- **Fictional worked order.** A stalled-onboarding investigation carried into an authorized three-message send batch, then extended to the same service at three branch portals. One confirmed arrival, one unknown outcome, one action withdrawn after a source change, and an Owner who refuses to confirm the batch as complete. All people, identifiers, addresses, evidence records and test results are illustrative and are labelled as such.
- **README, three touches plus lockstep.** "How to Use This Repository" gains the professional or team delegating to agents line; "Repository Contents" gains the row; the Changelog paragraph is brought forward. Version table, How to Cite and `CITATION.cff` move to v2.9.0.
- **ECOSYSTEM.md.** The slow-ai-kitchen role line in the profile repository is updated in the same commit series under maintenance protocol item 2.
- The twelve steps, the ten gates, the three tiers, the workshop, the Your Restaurant addendum, the Primer with its derived parts, the three derivation modules, the Service Record and the Consultant Workbook are otherwise unchanged byte for byte.

## v2.8.0 (2026-09-06)

The Consultant Workbook joins the repository as a standalone delivery instrument. A new instrument enters the repository, so minor.

- **`consultant-workbook.md` added**, flat in the repository root like the other modules (decision D-D3 of 6 September 2026 for service-record.md, applied here). The 30-day initial engagement on one priority workflow for a named business owner: consultant operating brief, delivery cadence, the method and the Feast mapped to twenty-six working records (W01 to W24 with W05A and W24A), the canonical full-day agenda with the evidence each session produces, facilitator instructions and weekly clinics, a measurement protocol that counts all human effort once, a fictional supplier-dossier teaching case that fails expansion on first-pass quality while passing on effort, the delivery acceptance check and a resource register. Converted from the author's working draft of 6 September 2026; the markdown is the file of record and no other format is published.
- **Sources cited by name.** The working draft pinned source versions in 29 "Source basis" lines, 58 pins in all, and every one was stale on the day the draft was dated: Slow AI Kitchen v2.4.0 against v2.7.0, GRC Workbook v4.2.1 against v4.2.2, Definition of Done v1.1.0 against v1.1.2, grc v2.2.1 against v2.2.2, with the AI Impact Assessment Tool and AI GRC Copilot unpinned. The committed file cites sources by name and URL and pins versions once, in a dated currency table in the resource register, with an engagement-level field for adopted versions. Same pattern as law-firm-ai-deployment-spec.md in AI-Governance-Academy, which carries no pins.
- **Doctrine alignment.** W10 carries both limbs of Informed Intent as stated in DOCTRINE.md v1.1.1: the instrument (purpose, authority, boundaries, exit) above the authorizer's five conditions (Knowledge, Evidence, Authority, Time, Permission). The doctrine paragraph in the organizational deployment section uses the canonical formulations and cites DOCTRINE.md. Doctrine delta rule, ECOSYSTEM.md protocol item 6.
- **Service Record wired in.** The Step 9 evidence cell, the W05 tier depths, the W13 footer, the worked case and the delivery acceptance check name the Service Record added at v2.7.0: required Tier 3, recommended Tier 2, optional Tier 1.
- **External-counsel guardrail.** W07 and the consultant operating brief state that applicability determinations rest with the Client's counsel or qualified local counsel and that items with legal effect carry the note "confirm with external counsel", the guardrail the AI-Governance-Academy templates already carry. The file closes with the informational-purposes disclaimer used in karpathys-kitchen.md.
- **House style applied in conversion.** Client capitalized, no Oxford commas, no em dashes, completion spaces rendered as escaped underscore lines so that GitHub does not read them as horizontal rules, sheet headings navigable in the browser.
- **README, three touches plus lockstep.** "How to Use This Repository" gains the consultant or facilitator line; "Repository Contents" gains the row; the Changelog paragraph is brought forward. Version table, How to Cite and `CITATION.cff` move to v2.8.0.
- The twelve steps, the ten gates, the three tiers, the workshop, the Your Restaurant addendum, the Primer with its derived parts, the three derivation modules and the Service Record are otherwise unchanged byte for byte.

## v2.7.0 (2026-09-06)

The Service Record joins the repository as a standalone module. Session D2 of the September 2026 improvement pack. A new instrument enters the method, so minor.

- **`service-record.md` added**, flat in the repository root like the other modules, per decision D-D3 of 6 September 2026. The one-page close-out of a single service: header, steps skipped or abbreviated, gates argued, what the owner would not sign, what the service changes in the method, the judgment and the carry-forward. Written by the named owner under Gate 5 within one day of release and kept with the evidence log. Ten records trigger a method review under Step 12, Gate 10.
- **Tier rule.** Required for Tier 3 work, recommended for Tier 2, optional for Tier 1. Tiering adjusts depth; nothing is deleted at the lower tiers and the record is not optional at Tier 3.
- **README, four touches.** "Repository Contents" gains the row; the Tier Application Map gains the row "Service Record (close-out after Gate 7) | Optional | Recommended | Required"; Step 9 gains one sentence naming the record and pointing at the file; "Definition of Done for the Method Itself" gains one test, that every Tier 3 service in the review period has a Service Record on file.
- **The Tier Application Map's first column is now headed "Gate or close-out"** rather than "Gate". The Service Record is a close-out written after Gate 7, not a gate, and a row under a column headed "Gate" would have asserted an eleventh gate. The ten gates are unchanged.
- **`CITATION.cff` and the How to Cite block** moved to v2.7.0 in lockstep with the README, per the D-C1 house form.
- The twelve steps, the ten gates, the three tiers, the workshop, the Your Restaurant addendum, the Primer with its derived parts and the three derivation modules are otherwise unchanged byte for byte.

## v2.6.2 (2026-09-06)

Citation infrastructure, doctrine citation line and lockstep maintenance. Session C of the September 2026 improvement pack, one patch release per repository across all 21 public repositories.

- **`CITATION.cff` added** in the house form settled at D-C1: no `type` field, `version` and `date-released` in lockstep with the README, `license` as the SPDX identifier for this repository's licence, `abstract` taken from this repository's ECOSYSTEM.md role line rather than newly written.
- **How to Cite block** aligned to this release and pointing at `CITATION.cff`.
- **Company name corrected.** `BABL.ai` to `BABL AI` in the About the author section, both occurrences.
- All other files in this repository are unchanged byte for byte.

## v2.6.1 (2026-09-06)

Patch. v2.6.0 shipped one part that GitHub will not render, which is the one
thing that release existed to fix. No change to the Primer text and no change to
the method.

**Correction of substance.** *[Author's doctrine. As at 6 September 2026 (KST).]*
v2.6.0 stated that the Primer is "published in parts for reading". For
`primer/02-part-2-solution-architecture.md`, 311,517 bytes, **that was not
true.** GitHub returned `richText: null` and `richTextTruncated: true` for it,
which is GitHub declining to render the file. Queried twice, twenty seconds
apart, while the other 22 parts rendered on the first query. The claim is struck
for that part and made good here rather than re-dated.

**Why the guard passed.** The pre-release check tested a ceiling of 512,000
bytes, which is the figure GitHub's own documentation and every secondary source
give for the markdown rendering limit. Measured directly against this account on
6 September 2026, that figure is wrong:

| File | Bytes | GitHub |
|---|---|---|
| `final-liability-rests-with-the-human-book-wip/AI_GRC_Master_Reference_v7_9.md` | 242,312 | RENDERED |
| `primer/02-part-2-solution-architecture.md` (v2.6.0) | 311,517 | NOT RENDERED |

The true limit lies in (242,312, 311,517]. 262,144 bytes, being 256 KiB, is the
obvious candidate and is **not established**. It is recorded as Unknown and
bounded rather than asserted, and the ceiling is set inside the proven-safe
range instead of at a guessed boundary.

**What changed.**

- `split_markdown.py` gains `--max-bytes`, default 200,000, invoked here at
  **240,000**, below the largest size this account has directly observed GitHub
  render. Any section above the ceiling is subdivided at H2, then at H3 if still
  over, and the subdivisions are repacked up to the ceiling so a section that
  only just exceeds it becomes two parts rather than one per heading. If a part
  is still over after that, the run **dies before writing anything**.
- `primer/` regenerated: **23 parts to 24**. Part 2 is now two files. Largest
  part 236,696 bytes. Every other part is unchanged in content.
- **Part filenames are renumbered from `02-` onward**, because the parts are
  numbered in reading order. Links to individual v2.6.0 part files therefore do
  not resolve at v2.6.1. The index at
  [primer/README.md](primer/README.md) is the stable entry point and is
  unchanged in that role. v2.6.0 was published the same day, so the exposure is
  one day.
- **A second defect, found while testing the first.** The verifier's
  navigation-block stripper set a flag on `nav:start` and cleared it on
  `nav:end`, and did nothing if `nav:end` never arrived. Everything after an
  unterminated block was silently discarded, so a part whose tail had been
  appended to, truncated, or had its closing marker deleted **verified clean**.
  Found by deliberately breaking the condition the check tests. Markers must now
  balance and no block may be left open, or the verify fails closed. Five cases
  are exercised: clean round trip, mid-body tamper, append past the closing
  marker, closing marker removed, part file missing. Before the fix, cases three
  and four reported OK.

**Unchanged, byte for byte.** `enterprise-ai-architecture-primer.md`, SHA-256
`58fd015b29ad463643ee845f7d181539d13ba8c58fa24efb1545b310f70e2d72`, the same
hash as at v2.6.0 and before it. Its own version table stays at v1.0.0,
2026-08-20. The twelve steps, the ten gates, the three tiers, the workshop
design, the Your Restaurant addendum, Karpathy's Kitchen, Newton's Kitchen and
Coetzee's Kitchen. Nothing in the method moves in this release.

## v2.6.0 (2026-09-06)

Structure release. The Practice Primer is published in parts that GitHub renders. No change to the Primer text and no change to the method.

- **`primer/` added: 23 derived parts and a reading index.** Generated by
  `split_markdown.py` in the private `account-maintenance` toolchain, splitting
  at every H1 and additionally at every H2 inside APPENDICES. The parts carry
  the Primer text unchanged; the only inserted lines are the navigation blocks
  fenced by sentinels at the head and foot of each part, which the verifier
  strips. The 23 parts rebuild `enterprise-ai-architecture-primer.md` byte for
  byte, 1,721,877 bytes, verified before this release. Largest part is
  311,517 bytes, inside GitHub's render limit.
- **Why.** GitHub does not render a markdown file above its size limit. At
  1.7 MB the Primer returned no rendered view and no source view, so it could
  be downloaded but not read from the repository page. Verified 4 September
  2026 against GitHub's blob payload.
- **`enterprise-ai-architecture-primer.md` is unchanged byte for byte**,
  SHA-256 `58fd015b29ad463643ee845f7d181539d13ba8c58fa24efb1545b310f70e2d72`.
  It remains the file of record, the file to cite and the file to download,
  and its own version table stays at v1.0.0, 2026-08-20.
- **README**, lockstep to v2.6.0: title block, How to Cite and the current
  version paragraph. Repository Contents gains a `primer/` row and the Primer
  row names the parts.
- **Standing rule.** The parts are derived, never edited. Any change to the
  Primer is followed by regenerating `primer/` from it in the same release, and
  the weekly account sweep verifies that the parts rebuild the Primer byte for
  byte. A part edited by hand is a defect, not a variant.
- **Unchanged.** The twelve steps, the ten gates, the three tiers, the workshop
  design, the Your Restaurant addendum, Karpathy's Kitchen, Newton's Kitchen
  and Coetzee's Kitchen. Nothing in the method moves in this release.

## v2.5.1 (2026-08-30)

Maintenance. One formulation aligned to doctrine; nothing of substance moves.

- **`karpathys-kitchen.md`**, v1.0.0 to v1.0.1. The module closed on "attach
  consequential decisions to an identifiable human principal" where DOCTRINE.md
  says "named human owner". The line now reads "attach consequential decisions
  to a named human owner", per the doctrine delta rule. Logged out of scope at
  the v2.4.0 release for the weekly sweep; executed in this release round
  instead by decision of 30 August 2026. Sole occurrence account-wide,
  confirmed by grep before the edit; the v2.4.0 changelog line recording the
  defect stands as written. Link register untouched: links are re-dated only
  when re-verified, and none was.
- **`README.md`**: title block, How to Cite and current-version paragraph to
  v2.5.1 in lockstep.
- No change to the twelve steps, the ten gates, the three tiers, the workshop
  design, the Your Restaurant addendum, the primer, Newton's Kitchen or
  Coetzee's Kitchen.

## v2.5.0 (2026-08-30)

New module. Coetzee's Kitchen (`coetzees-kitchen.md`) joins as a standalone
add-on module: the epistemics of the human-AI working session, read through
J. M. Coetzee's 2003 Nobel lecture *He and His Man*. It names the three
problems the method's gates answer (the report is not the world, the report
lands in a system, the report changes its reader), introduces **Return to
Source** and **Cognitive Provenance** as disciplines operationalizing the
doctrines inside the loop, supplies the socio-technical warrant for Gate 3
(Read the Kitchen) and maps the doctrines onto the loop: Informed Intent
governs entry, Slow AI the interaction, Final Liability the exit. Restates the
doctrines at the altitude of the working session under the doctrine delta
rule; varies no rule. The two disciplines are disciplines of the module, not
doctrine; DOCTRINE.md is unchanged. No change to the twelve steps, the ten
gates, the three tiers, the workshop design, the Your Restaurant addendum, the
primer, Karpathy's Kitchen or Newton's Kitchen.

- **`coetzees-kitchen.md`**, new, v1.0.0, Final, CC BY-NC-SA 4.0. Preface and
  twelve sections in continuous prose, a method-mapping apparatus and four
  third-party sources verified 2026-08-29 (KST): the Pursuit of Wonder video
  under its current title (retitled by its creator since first circulation),
  the Nobel lecture (Swedish Academy, 7 December 2003), Trist and Bamforth
  1951 and NIST AI 100-1. Two short quotations only, "a kind of parrot" (the
  lecture) and "inherently socio-technical in nature" (NIST); the Defoe
  epigraph is public domain. Declines to adopt a socio-technical versus
  socio-technological suffix distinction for want of authority, and says so
  in its own text.
- **`README.md`**: title block to v2.5.0; reader path added after the
  compression reader's; file table row added after `newtons-kitchen.md`;
  current-version paragraph updated.
- **Correction, itemised.** README How to Cite read v2.3.1 and had not moved
  at the v2.4.0 release; corrected to v2.5.0. Same defect class as the v2.2
  How to Cite correction.

## v2.4.0 (2026-08-27)

New module. Newton's Kitchen (`newtons-kitchen.md`) joins as a standalone
add-on module: the three doctrines compressed into three laws of consequential
motion (Intent, Motion, Liability), each stated as an axiom beneath the doctrine
it restates, set out in the order of the *Principia* (definitions, laws,
corollaries, scholia), with a corollary on materiality and README registration
(reader path, file table, current-version paragraph). Restates Slow AI,
Informed Intent and Final Liability at the altitude of mechanics under the
doctrine delta rule; varies no rule. No change to the twelve steps, the ten
gates, the three tiers, the workshop design, the Your Restaurant addendum, the
primer or Karpathy's Kitchen.

- **`newtons-kitchen.md`**, new, v1.0.0, Final, CC BY-NC-SA 4.0. Eight
  definitions, three laws, five corollaries, a scholium on the limits of the
  Newtonian correspondence and a general scholium carrying the proposition:
  do not govern intelligence in the abstract, govern consequential motion
  through the world. No third-party citations; internal links checked
  2026-08-27 (KST).
- **`README.md`**: title block to v2.4.0; reader path added after the
  skeptic's; file table row added after `karpathys-kitchen.md`;
  current-version paragraph updated.
- Not in scope, logged for the weekly sweep: `karpathys-kitchen.md` closes on
  "identifiable human principal" where DOCTRINE.md says "named human owner".

## v2.3.1 (2026-08-24)

Maintenance. One perishable figure recast so that it does not go stale on a
known date. No change to the twelve steps, the ten gates, the three tiers, the
workshop design, the Your Restaurant addendum or Karpathy's Kitchen.

- **`enterprise-ai-architecture-primer.md`, Appendix I, Claude Sonnet 5 pricing
  row.** The row read "$2 / $10 to 31 Aug 2026, then $3 / $15". That phrasing is
  correct only while read before 31 August 2026; from 1 September the
  promotional rate reads as current when it is not. Recast to state both rates
  against explicit date boundaries, to carry the 2026-08-11 verification date
  for both, and to record that the 1 September rate was documented as scheduled
  at that date and has not been re-verified since. **The figures themselves are
  unchanged and were not re-verified for this release.** Only the framing moves,
  per the rule that claims are re-dated only when re-verified.
- Sole occurrence account-wide, confirmed by grep before the edit.

**Version numbering.** This release also moves the repository to a
three-component version. `v2.2` and `v2.3` were two-component, which the account
maintenance sweep silently excluded from its tag comparisons; the sweep was
corrected the same day and now reports the inconsistency rather than dropping
it. See `account-maintenance` v1.1.0 and runbook trap 16. The earlier tags
stand as released.

## v2.3 (2026-08-24)

Addition. `karpathys-kitchen.md` joins the repository as a standalone add-on module: *Karpathy's Kitchen*, a technical reading and viewing guide deriving the method's core principles from twelve works by Andrej Karpathy, running from the Intro to Large Language Models lecture through Software 2.0, the training-recipe essay, Zero to Hero, microgpt (February 2026) and Software Is Changing (Again) to the Tesla talks, the Verifiability post and Animals vs Ghosts. The module states the method's origin in the author's voice: the limitations Karpathy documents in order to build well are the limits an institution has to control for in order to deploy safely. It carries a seven-point governance synthesis, a five-layer architecture read against the twelve steps, the demo-to-product gap and the march of nines as the standard of evidence for raising an autonomy level, verifiability as the triage rule for a use-case inventory, a study sequence in three passes plus a one-hour short pass for executives and vendor meetings, a derivation table whose owner column names only the task and organizational roles already fixed in the README, and a link register recording the browser-checked status of all twenty-nine external citations as at 24 August 2026 (KST), including one that does not resolve and is recorded rather than dropped. The document carries its own masthead (v1.0.0, 2026-08-24 KST) and the license-and-third-party-materials convention adopted at v2.2. It is an independent reading: Andrej Karpathy has no involvement in it, has not reviewed it and does not endorse it. Record note: the module file was committed to `main` earlier on 24 August 2026 under a commit message carrying the superseded working version number v2.1, from a draft release plan written against a stale reading of this repository. That message is left as written rather than rewritten. The version in force for this addition is v2.3. README updated accordingly: the module registered in Repository Contents, a reader entry added to How to Use This Repository, and the version table, How to Cite and current-version pointer moved in lockstep. On method questions the README controls, per the repository rule. No change to the twelve steps, the ten gates, the three tiers, the workshop design or the Your Restaurant addendum.

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
