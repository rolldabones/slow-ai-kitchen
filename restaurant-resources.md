# Reference Resources for the Restaurant

> **Regulatory currency:** the legal and standards claims in this file were verified against primary and official sources on 14 July 2026 (KST), except where a status note below carries a later date. The EU entry was updated on 13 August 2026 (KST); the Korea and NIST entries were re-verified on 17 August 2026 (KST); the Singapore entry was added and the ISO entries were re-read against iso.org on 11 October 2026 (KST). Each status note carries its own verification date and controls over this line. Verify again before relying on this file in client-facing or regulatory submissions.

---

## A Note on Standards

**You do not need ISO/IEC 42001 certification to build a management system that works.**

Certification is a signal to regulators, clients, auditors and the market. It is a useful signal, and in certain procurement and regulatory contexts it will become an expected one. But the signal is not the substance. An organization that reads 42001 carefully, implements its requirements honestly and governs its AI systems with discipline has built a functioning AI management system regardless of whether a certification body has issued a certificate. The standards listed below are references, not prerequisites. Use what is load-bearing for your organization's context and leave the rest on the shelf.

That said, a frank institutional note is warranted. Every standard listed in the ISO section below sits behind a paywall. ISO operates on a licensing model that charges organizations, including small enterprises, public institutions, nonprofits and individual practitioners, to access the very governance documents they are expected to implement. The NIST resources listed in the following section are free, stable and authoritative. Where NIST and ISO cover the same ground, practitioners operating under resource constraints should start with NIST. The crosswalk between the AI RMF and ISO/IEC 42001 is itself free and will take most organizations further than the purchase price of the underlying standard suggests.

**The frameworks exist to serve the organization. The organization does not exist to serve the frameworks.**

---

## NIST Resources

### Centerpiece

**NIST Trustworthy and Responsible AI Resource Center (AIRC)**
`https://airc.nist.gov`

The authoritative hub for AI risk management resources maintained by the National Institute of Standards and Technology. Contains the AI RMF framework document, the Playbook, all publications in the NIST AI 100-series, crosswalk documents mapping the AI RMF to ISO 42001 and other frameworks and use case examples. The starting point for any organization implementing the Restaurant pillars.

> **Status note (17 August 2026, KST):** NIST AI RMF 1.0 remains the current published version. The revision tasked by the White House AI Action Plan (July 2025) is ongoing; AI RMF 1.1 has not been published as of this date. NIST released a concept note for an AI RMF Profile on Trustworthy AI in Critical Infrastructure in April 2026. Treat current Playbook actions as the working baseline and monitor `https://airc.nist.gov` for the updated release.

---

### Pillar 1: Governance Structure

**NIST SP 800-39.** Managing Information Security Risk: Organization, Mission and Information System View
Integrated, organization-wide framework for managing information security risk across three tiers: organization, mission/business process and information system. Governance architecture reference for the Restaurant.
`https://csrc.nist.gov/pubs/sp/800/39/final`

**NIST SP 800-37 Rev. 2.** Risk Management Framework for Information Systems and Organizations: A System Life Cycle Approach for Security and Privacy
Describes the Risk Management Framework (RMF) and provides guidelines for applying it to information systems and organizations. Disciplined, structured and flexible process for managing security and privacy risk.
`https://csrc.nist.gov/pubs/sp/800/37/r2/final`

---

### Pillar 2: Risk Management

**NIST AI 100-1.** Artificial Intelligence Risk Management Framework (AI RMF 1.0), January 2023
The core framework document. Voluntary framework for incorporating trustworthiness considerations into the design, development, use and evaluation of AI products, services and systems. Four functions: Govern, Map, Measure and Manage.
`https://doi.org/10.6028/NIST.AI.100-1`

**NIST AI RMF Playbook.** Suggested actions for achieving the outcomes in each AI RMF subcategory across all four functions
`https://airc.nist.gov/airmf-resources/playbook/`

**NIST Cybersecurity Framework (CSF) 2.0**
`https://www.nist.gov/cyberframework`

**NIST SP 800-30 Rev. 1.** Guide for Conducting Risk Assessments
Practical guidance for carrying out risk assessments at all three tiers of the risk management hierarchy.
`https://csrc.nist.gov/pubs/sp/800/30/r1/final`

**NISTIR 8286 series.** Integrating Cybersecurity and Enterprise Risk Management (ERM)
Four-document series covering the anchor framework and three supplementary volumes: identifying and estimating cybersecurity risk (8286A), prioritizing risk responses (8286B) and staging risks for ERM and governance oversight (8286C). Current revised editions are 8286r1, 8286Ar1 and 8286Cr1.
`https://csrc.nist.gov/pubs/ir/8286/r1/final`
`https://csrc.nist.gov/pubs/ir/8286a/r1/final`
`https://csrc.nist.gov/pubs/ir/8286b/final`
`https://csrc.nist.gov/pubs/ir/8286c/r1/final`

---

### Pillar 3: Regulatory Compliance

**NIST SP 800-161 Rev. 1.** Cybersecurity Supply Chain Risk Management Practices for Systems and Organizations
Guidance for organizations on identifying, assessing and mitigating cybersecurity risks throughout the supply chain. Relevant to AI vendor and third-party model governance.
`https://csrc.nist.gov/pubs/sp/800/161/r1/final`

---

### Pillar 4: AI Lifecycle Management

**NIST AI 600-1.** Artificial Intelligence Risk Management Framework: Generative AI Profile, July 2024
Extends AI RMF concepts to generative AI systems. Addresses unique risks including hallucination, data provenance, harmful content generation and intellectual property exposure.
`https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.600-1.pdf`

**NIST SP 800-160 Vol. 1.** Engineering Trustworthy Secure Systems
Systems security engineering guidance. Reference for building security and trustworthiness into AI systems from design through decommissioning.
`https://csrc.nist.gov/pubs/sp/800/160/v1/final`

**NIST SP 800-160 Vol. 2 Rev. 1.** Developing Cyber-Resilient Systems: A Systems Security Engineering Approach
Addresses cyber resiliency engineering. Relevant to AI system continuity, degraded-mode operation and recovery planning.
`https://csrc.nist.gov/pubs/sp/800/160/v2/r1/final`

---

### Pillar 5: Continuous Improvement

**NIST SP 800-55v1.** Measurement Guide for Information Security, Volume 1: Identifying and Selecting Measures (Final, December 2024)
Flexible approach to developing, selecting and prioritizing information security measures. Includes quantitative and qualitative assessment, data analysis techniques and impact and likelihood modeling.
`https://csrc.nist.gov/pubs/sp/800/55/v1/final`

**NIST SP 800-55v2.** Measurement Guide for Information Security, Volume 2: Developing an Information Security Measurement Program (Final, December 2024)
Methodology for developing and implementing an information security measurement program structure.
`https://csrc.nist.gov/pubs/sp/800/55/v2/final`

**NIST SP 800-61 Rev. 3.** Incident Response Recommendations and Considerations for Cybersecurity Risk Management: A CSF 2.0 Community Profile
Updated incident response guidance aligned to CSF 2.0. Reference for AI incident classification, response procedures and post-incident review.
`https://csrc.nist.gov/pubs/sp/800/61/r3/final`

**NIST SP 800-50 Rev. 1.** Building a Cybersecurity and Privacy Learning Program
Guidance for developing and managing cybersecurity and privacy learning programs. Applies to AI governance training design and workforce capability development.
`https://csrc.nist.gov/pubs/sp/800/50/r1/final`

---

### Crosswalks and Framework Index

**NIST AI RMF to ISO/IEC 42001 Crosswalk.** clause-level mapping between the AI RMF and ISO 42001, published by NIST. Free working reference for practitioners without access to the paywalled standard.
`https://airc.nist.gov/docs/NIST_AI_RMF_to_ISO_IEC_42001_Crosswalk.pdf`

**NIST AI RMF to ISO/IEC 23894 Crosswalk.** mapping between the AI RMF and the ISO AI risk management standard
`https://airc.nist.gov/documents/3/ai-2025-00109_revised_ISO_IEC_23894_Crosswalk_to_the_NIST_AI_RMF.pdf`

**NIST AI RMF Crosswalk Index.** full index of mappings between the AI RMF and ISO 42001, the OECD AI Principles, the EU AI Act and other frameworks
`https://airc.nist.gov/airmf-resources/crosswalks/`

**NIST AI Technical Reports Index.** complete NIST AI 100-series publication list
`https://airc.nist.gov/technical-reports/`

---

## Primary Regulatory Instruments and Foundational Principles

These are not operational frameworks or technical standards. They are the primary law and the intergovernmental principles that underpin the regulatory environment in which the Restaurant operates. They sit above the NIST and ISO layers in the authority hierarchy.

---

### EU AI Act

**Regulation (EU) 2024/1689 of the European Parliament and of the Council of 13 June 2024.** Laying Down Harmonised Rules on Artificial Intelligence (Artificial Intelligence Act)
Published in the Official Journal of the European Union on 12 July 2024. Entered into force 1 August 2024. Establishes a risk-based regulatory framework for AI systems placed on the market or put into service in the EU. Phased application timeline: prohibitions applicable from 2 February 2025; GPAI model obligations from 2 August 2025; most high-risk AI system requirements from 2 August 2026; remaining obligations from 2 August 2027.
Official text (EUR-Lex, English): `https://eur-lex.europa.eu/eli/reg/2024/1689/oj/eng`
Stable ELI permalink: `http://data.europa.eu/eli/reg/2024/1689/oj`

> **Status note, amended 13 August 2026 (KST).** This note previously recorded the Digital Omnibus on AI as awaiting publication in the Official Journal. That status is superseded. The Digital Omnibus on AI (amending Regulation (EU) 2024/1689) was adopted by the co-legislators (European Parliament 16 June 2026, Council 29 June 2026) and **entered into force on 27 July 2026**. The changes below are therefore operative law, not pending changes. Article 5 sits in Chapter II. Under **Article 113, third paragraph, point (a)**, as replaced by Regulation (EU) 2026/1744, Chapters I and II apply from **2 February 2025**, **with the exception of Article 5(1), first subparagraph, points (ba) and (bb), and Article 5(1a) and (1b), which apply from 2 December 2026**. So the general Article 5 date is 2 February 2025 and the prohibitions added by the Omnibus are deferred to 2 December 2026. Do not state the Article 5 date without that carve-out. Key changes: high-risk obligations for stand-alone Annex III systems are deferred to 2 December 2027 and for Annex I embedded systems to 2 August 2028; most Article 50 transparency obligations still apply from 2 August 2026, with the Article 50(2) watermarking obligation for systems already on the market deferred to 2 December 2026; a new Article 5 prohibition on AI generation of non-consensual intimate imagery and CSAM applies from 2 December 2026. **Citation.** The amending act is **Regulation (EU) 2026/1744** of the European Parliament and of the Council of 8 July 2026, OJ L, 2026/1744, 24.7.2026, ELI http://data.europa.eu/eli/reg/2026/1744/oj, in force 27 July 2026. Its Article 1, point (40) amends the **third paragraph of Article 113** of Regulation (EU) 2024/1689. **Article 113 has unnumbered paragraphs with lettered points, so the correct pinpoint form is "Article 113, third paragraph, point (c)", not "Article 113(3)".** Amended point (c) provides that Chapter III, Sections 1, 2 and 3, with the exception of Article 6(5), apply from (i) 2 December 2027 for AI systems classified as high-risk pursuant to Article 6(2) and Annex III, and (ii) 2 August 2028 for those classified pursuant to Article 6(1) and Annex I. A new point (d) provides that Articles 102 to 110 apply from 27 July 2026. Read against the consolidated text of Regulation (EU) 2024/1689 on EUR-Lex, as at 13 August 2026 (KST).

---

### Korea AI Basic Act

**Framework Act on the Development of Artificial Intelligence and Establishment of Trust** (인공지능 발전과 신뢰 기반 조성 등에 관한 기본법)
Act No. 21311 of 20 January 2026 (partial amendment), in force 21 July 2026. Originally enacted as Act No. 20676, promulgated 21 January 2025, effective 22 January 2026. The first comprehensive AI legislation in the Asia-Pacific region. Establishes a dual-track structure distinguishing general AI governance from High-Impact AI obligations in critical sectors including healthcare, energy and public services. Requires mandatory labeling for certain generative AI applications. Provides for a national AI safety research institute and AI ethics committees. The Enforcement Decree in force is Presidential Decree No. 36506 of 20 July 2026 (partial amendment), in force 21 July 2026; the original Decree, Presidential Decree No. 36053, promulgated 21 January 2026, took effect alongside the Act on 22 January 2026. The Decree sets, among other things, the high-performance AI compute threshold (cumulative training compute of at least 10^26 FLOPs) and the domestic-representative thresholds for foreign operators.

Official Korean text (Korean Law Information Center):
`https://www.law.go.kr/법령/인공지능발전과신뢰기반조성등에관한기본법`

English translation (CSET Georgetown, July 2025):
`https://cset.georgetown.edu/publication/south-korea-ai-law-2025/`

> **Status note (17 August 2026, KST):** The Act and its Enforcement Decree have been in force since 22 January 2026. Both have since been amended: the operative texts are Act No. 21311 of 20 January 2026 and Presidential Decree No. 36506 of 20 July 2026, both in force 21 July 2026. Earlier editions of this file cited the original enactments as current. MSIT is operating a grace period of at least one year before imposing administrative fines, except in exceptional cases involving serious social harm, and continues to supplement guidance on High-Impact AI assessment and operator obligations during that period. Substantive obligations apply notwithstanding the fine grace period. Monitor MSIT (`https://www.msit.go.kr`) for updated guidelines.

---

### OECD AI Principles

**OECD Recommendation of the Council on Artificial Intelligence.** First adopted May 2019, updated May 2024
The first intergovernmental standard on AI. Endorsed by 47 jurisdictions including the EU, the United States, Korea and all OECD member countries. Five values-based principles (inclusive growth and well-being; rule of law, human rights and democratic values; transparency and explainability; robustness, security and safety; accountability) and five recommendations for policymakers. The 2024 update added explicit coverage of generative AI risks, environmental sustainability, information integrity and responsible business conduct throughout the AI lifecycle.

The OECD's definition of an AI system and its lifecycle are the definitional foundation of the EU AI Act, the NIST AI RMF and the Korea AI Basic Act. Citing the Principles situates the Restaurant within the global policy consensus from which downstream regulatory obligations derive.

OECD AI Principles overview: `https://oecd.ai/en/ai-principles`
Full Recommendation text: `https://legalinstruments.oecd.org/en/instruments/OECD-LEGAL-0449`

---

## Supervisory Guidance

Guidance issued by a financial regulator under its supervisory powers. It is not primary law. It states the expectations the regulator supervises against for the institutions it licenses, and it sits below the instruments above and beside the NIST layer in authority.

---

### Singapore: MAS Guidelines on AI Risk Management

**Guidelines on Artificial Intelligence Risk Management**, Monetary Authority of Singapore (MAS), issued 7 October 2026. Published on mas.gov.sg under the title *Guidelines on Artificial Intelligence Risk Management for Financial Institutions*. Supervisory guidelines for MAS-regulated financial institutions, applied in proportion to size and risk profile (para 2.1). They take effect on 7 October 2027; Sections 3 and 4 may be met from that date and Sections 5 and 6 by 7 October 2028 (para 1.8).

Section 4 requires an institution to identify AI use across the business, including AI embedded in material third-party services (para 4.2), to keep an AI inventory (paras 4.5 to 4.9) and to assess the risk materiality of each use case on impact, complexity and reliance, applying controls proportionate to the rating (paras 4.10 to 4.13). Section 6 makes the competence and capacity of the people who develop, deploy and use AI a supervisory expectation (paras 6.1 and 6.2), with adequate technology infrastructure (para 6.3). The institution retains primary accountability for its use of third-party AI (para 5.11); the board is to understand AI well enough to provide oversight and challenge (para 3.4(d)); local senior management remains accountable where a group framework is adopted (para 3.6).

**The minimum set, paragraph 2.5.** Where poor performance or unavailability of an AI tool is unlikely to have a material adverse impact on the institution, its customers or other stakeholders (para 2.3; the examples in para 2.4 include drafting, summarizing and initial document review for internal reference and chatbots that locate internal resources, with footnote 13 expecting human review of outputs before use), basic AI governance policies and procedures should minimally include: (a) clear accountability for AI oversight, such as a designated member of senior management; (b) permitted and prohibited uses of AI, together with effective human oversight, including when human review and validation of outputs before use is mandatory; (c) an approved list of AI tools and a defined process for approving new ones; (d) staff education on the AI policies; (e) regular compliance checks; and (f) periodic and trigger-based review of whether the use still meets the para 2.3 criteria.

Read against the Feast (the author's mapping, not anything MAS states): (a) is the AI Owner and Executive Sponsor named at Step 10, Gate 8; (b) and (c) are the deployment policy and the authorized tool registry of Step 10, Gate 8, with the human review of outputs carried by the Tier Application Map; (d) is Step 11, Gate 9, the competency and authorization record; (e) and (f) are Step 12, Gate 10, the operational audit and review cycle and the revised registry.

Author's view: for practical guidance, Singapore is the benchmark for AI governance, risk management and compliance in Asia-Pacific.

Guidelines page: `https://www.mas.gov.sg/regulation/guidelines/guidelines-on-artificial-intelligence-risk-management-for-financial-institutions`

The nine sources linked in the Guidelines' footnotes, each read and resolving on 11 October 2026 (KST). Footnote 3 also names, without links, the Cyber Security Agency of Singapore's Guidelines and Companion Guide on Securing AI Systems, IMDA's Model AI Governance Framework and the AI Verify Foundation.

MAS, Principles to Promote Fairness, Ethics, Accountability and Transparency (FEAT) (fn 2, 35): `https://www.mas.gov.sg/publications/monographs-or-information-paper/2018/feat`
MAS, Cyber Risks Associated with Generative Artificial Intelligence, MAS/TCRS/2024/05 (fn 9): `https://www.mas.gov.sg/regulation/circulars/cyber-risks-associated-with-generative-artificial-intelligence`
MAS, Guidelines on Risk Management Practices, Technology Risk (fn 47, 50): `https://www.mas.gov.sg/regulation/guidelines/technology-risk-management-guidelines`
PDPC, Advisory Guidelines on use of Personal Data in AI Recommendation and Decision Systems (fn 30): `https://www.pdpc.gov.sg/organisations/regulations-decisions/regulatory-guidance/advisory-guidelines-on-use-of-personal-data-in-ai-recommendation-and-decision-systems`
PDPC, Advisory Guidelines on use of Personal Data in Generative AI (fn 30): `https://www.pdpc.gov.sg/organisations/regulations-decisions/regulatory-guidance/advisory-guidelines-on-use-of-personal-data-in-generative-ai`
IMDA, Model AI Governance Framework for Agentic AI (fn 11): `https://www.imda.gov.sg/-/media/imda/files/about/emerging-tech-and-research/artificial-intelligence/mgf-for-agentic-ai.pdf`
IMDA, Transparency Guidelines for Generative AI Chatbots (fn 34): `https://www.imda.gov.sg/-/media/imda/file/emerging-technologies-and-research/artificial-intelligence/transparency-guidelines-for-generative-ai-chatbots.pdf`
IMDA, Starter Kit for Testing LLM-Based Applications for Safety and Reliability (fn 43, 46): `https://www.imda.gov.sg/-/media/imda/files/about/emerging-tech-and-research/artificial-intelligence/large-language-model-starter-kit.pdf`
NIST, AI Risk Management Framework, AI 100-1 (fn 31, 51): `https://doi.org/10.6028/NIST.AI.100-1`

> **Status note (11 October 2026, KST):** Verified against the Guidelines PDF linked from the MAS page above, 30 pages, dated 7 October 2026 on every page. Not yet in effect; the first compliance date is 7 October 2027. MAS states that the Guidelines will be updated or augmented as necessary (para 1.12).

---

## ISO Standards

All ISO/IEC standards listed below are available for purchase at `https://www.iso.org`. Individual standard pages are accessible by searching the standard designation at that address. National standards bodies, including the Korean Agency for Technology and Standards (KATS), may offer Korean-language editions or subsidized access for domestic organizations.

The ISO AI Standards Hub maintained by BSI provides a publicly accessible catalogue of SC 42 standards with current publication status indicators: `https://aistandardshub.org`

---

### ISO Anchor

**ISO/IEC 42001:2023.** Information technology — Artificial intelligence — Management system
The world's first certifiable AI management system standard. Specifies requirements for establishing, implementing, maintaining and continually improving an AI Management System (AIMS) within organizations. Anchor standard for the Restaurant addendum across all five pillars. Integrates with ISO/IEC 27001 and ISO 31000 through shared Plan-Do-Check-Act architecture.
`https://www.iso.org/standard/81230.html`

---

### Pillar 1: Governance Structure

**ISO/IEC 38507:2022.** Information technology — Governance of IT — Governance implications of the use of artificial intelligence by organizations
Board-level governance standard. Addresses how governing bodies should direct and oversee AI use within their organizations. The governance layer above the AIMS established by 42001.
Search: `https://www.iso.org` for ISO/IEC 38507

**ISO 31000:2018.** Risk management — Guidelines
General-purpose enterprise risk management framework. Foundation for ISO/IEC 23894: understanding 31000 clarifies how the AI-specific risk guidance in 23894 is structured and layered.
Search: `https://www.iso.org` for ISO 31000

---

### Pillar 2: Risk Management

**ISO/IEC 23894:2023.** Information technology — Artificial intelligence — Guidance on risk management
Guidance on AI-related risk management for organizations. The operational risk layer beneath the management system architecture of 42001. Adapts and develops the principles of ISO 31000 with AI-specific application. Use alongside NIST AI RMF; the two frameworks are complementary at the practice level.
Search: `https://www.iso.org` for ISO/IEC 23894

**ISO/IEC 42005:2025.** Information technology — Artificial intelligence (AI) — AI system impact assessment
Structured approach for organizations to assess the impacts of their AI systems: documenting, assessing and monitoring effects including sensitive or restricted uses, foreseeable misuse and unintended applications. Distinct from, and complementary to, risk assessment under 42001. Impact assessment evaluates effects on individuals and society; risk assessment evaluates organizational exposure.
Search: `https://www.iso.org` for ISO/IEC 42005

---

### Pillar 3: Regulatory Compliance

**ISO/IEC 27001:2022.** Information security, cybersecurity and privacy protection — Information security management systems — Requirements
The foundational ISMS standard. ISO/IEC 42001 builds on this foundation by introducing AI-specific governance covering risks related to AI lifecycle management, transparency, accountability and human oversight. Organizations already certified to 27001 can fold AI governance into existing audit cadences.
Search: `https://www.iso.org` for ISO/IEC 27001

**ISO/IEC 27701:2025.** Information security, cybersecurity and privacy protection — Privacy information management systems — Requirements and guidance
Extends the ISMS to a Privacy Information Management System (PIMS). Relevant where AI systems process personal data; maps to GDPR and Korea's PIPA compliance infrastructure.

> **Status note (11 October 2026, KST):** ~~ISO/IEC 27701:2019~~ is withdrawn. The current edition is ISO/IEC 27701:2025 (Edition 2), titled as above, read on iso.org on this date. The description above was written against the 2019 edition and has not been re-read against the 2025 text.
Search: `https://www.iso.org` for ISO/IEC 27701

**ISO/IEC 29100:2024.** Information technology — Security techniques — Privacy framework
Foundational privacy terminology and framework. Reference standard for privacy-by-design requirements in AI system development and procurement.

> **Status note (11 October 2026, KST):** ~~ISO/IEC 29100:2011 and its Amendment 1:2018~~ are withdrawn. The current edition is ISO/IEC 29100:2024 (Edition 2), read on iso.org on this date. The description above has not been re-read against the 2024 text.
Search: `https://www.iso.org` for ISO/IEC 29100

---

### Pillar 4: AI Lifecycle Management

**ISO/IEC 5338:2023.** Information technology — Artificial intelligence — AI system life cycle processes
Defines processes and associated concepts for describing the life cycle of AI systems based on machine learning and heuristic systems. Based on ISO/IEC/IEEE 15288 and ISO/IEC/IEEE 12207 with AI-specific additions. Provides processes supporting the definition, control, management, execution and improvement of AI systems across life cycle stages. Operational companion to the governance architecture in 42001.
Search: `https://www.iso.org` for ISO/IEC 5338

**ISO/IEC 22989:2022.** Information technology — Artificial intelligence — Artificial intelligence concepts and terminology
Foundational vocabulary standard. Defines AI concepts and terminology so teams and auditors share the same language. Required orientation before citing or auditing against any other SC 42 standard.
Search: `https://www.iso.org` for ISO/IEC 22989

**ISO/IEC 23053:2022.** Framework for Artificial Intelligence (AI) Systems Using Machine Learning (ML)
Describes how ML components fit into AI system architectures. Helps teams design modular, testable solutions by distinguishing datasets, training pipelines, models, serving layers and feedback loops. Use to structure documentation and align engineering with governance expectations in 42001 and 23894.
Search: `https://www.iso.org` for ISO/IEC 23053

**ISO/IEC 42006:2025.** Information technology — Artificial intelligence — Requirements for bodies providing audit and certification of artificial intelligence management systems
Conformity assessment companion to 42001. Published July 2025. Specifies additional requirements to ISO/IEC 17021-1 for certification bodies conducting 42001 audits. Relevant for AI audit positioning and for organizations preparing for third-party certification; accreditation bodies have begun transitioning AIMS accreditation to the published standard.
Search: `https://www.iso.org` for ISO/IEC 42006

---

### Pillar 5: Continuous Improvement

**ISO/IEC TR 24028:2020.** Information technology — Artificial intelligence — Overview of trustworthiness in artificial intelligence
Technical report covering trustworthiness concepts, threats and mitigation approaches across the AI lifecycle. Orientation document for continuous improvement programs targeting explainability, robustness and fairness.
Search: `https://www.iso.org` for ISO/IEC TR 24028

**ISO/IEC 12792:2025.** Information technology — Artificial intelligence (AI) — Transparency taxonomy of AI systems
Published November 2025 and adopted by CEN-CENELEC as EN ISO/IEC 12792:2025. Specifies a taxonomy of information elements to help AI stakeholders identify and address transparency needs. Reference standard for building transparency metrics into improvement cycles.
Search: `https://www.iso.org` for ISO/IEC 12792

---

## URL Stability Notes

NIST links point to official `.gov` domains. NIST periodically revises publications; if a CSRC link resolves to a redirect, navigate from the AIRC centerpiece at `https://airc.nist.gov` to locate the current version. The AI RMF and Playbook remain under active revision as of July 2026; monitor the AIRC for updated versions.

ISO links point to purchase pages on `iso.org`. Content does not change without a formal revision cycle. ISO/IEC 42006:2025 and ISO/IEC 12792:2025 are both published; verify edition currency at `https://www.iso.org` or `https://aistandardshub.org` before citing in client-facing or regulatory submissions.

---

*Son-U Michael Paik, GRC Solutions Korea*

**Final Liability rests with the Human.**
