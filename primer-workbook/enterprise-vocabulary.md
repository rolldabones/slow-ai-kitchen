# Enterprise Vocabulary, by Domain

*Primer Workbook, slow-ai-kitchen v3.0.0. Moved from the Enterprise AI Architecture Primer v1.0.0, Appendix H (the enterprise vocabulary run; the core terms stay in the Primer), on 18 October 2026, so that the Primer is a reference and this folder the practice set; text unchanged except the corrections itemized in the slow-ai-kitchen CHANGELOG at v3.0.0; section references are to the [Primer](https://github.com/rolldabones/slow-ai-kitchen/blob/main/enterprise-ai-architecture-primer.md).*

Grouped by domain. Where a term is commonly confused with another, the distinction is stated in the same line.

## Enterprise architecture and operating model

**Application portfolio management.** The discipline of holding an inventory of every application with its owner, cost, lifecycle stage and business capability, and making invest, tolerate, migrate or eliminate decisions against it.

**Architecture review board.** The standing body that approves designs against standards and grants exceptions. Distinct from a governance committee, which decides risk acceptance; the board decides technical conformance.

**Business capability map.** A hierarchy of what an organization does, expressed independently of how it is organized or which systems it runs. The stable frame against which shifting systems and structures are compared.

**Center of excellence.** A central team that sets standards, holds scarce expertise and enables delivery teams. Fails in four recognizable ways: the **bottleneck**, where every team queues behind it; the **ivory tower**, where it publishes standards nobody consults; the **demo factory**, where it produces pilots and no production system; and the **tollbooth**, where it charges for permission rather than supplying capability. The tollbooth is the most damaging, because teams route around it and the result is a shadow estate the organization cannot see.

**Conway's law.** A system's structure mirrors the communication structure of the organization that built it. The practical consequence is that a boundary you want in the architecture needs a corresponding boundary in the org chart, or it will erode.

**Domain-driven design.** Modeling software around business domains with explicit bounded contexts and a shared language per context. Its value here is the bounded context, which is the natural unit for a corpus, a tool set and an owner.

**Federated operating model.** Central standards with local delivery. Contrast with centralized, where one team builds everything, and with fully devolved, where each function does as it wishes. The federated model is the common landing point and it fails when the standards have no teeth.

**Golden path.** The paved, supported and pre-approved way to build something, where choosing it removes work rather than adding it. A golden path that is slower than the unofficial route will not be used.

**Landing zone.** A pre-configured, pre-approved environment with identity, networking, logging and guardrails already in place, into which a workload can be deployed without renegotiating the controls.

**Operating model.** How work is organized, decided, funded and supported: the arrangement of people, decision rights, processes and platforms. Distinct from the organization chart, which shows reporting lines only.

**Platform team.** A team whose product is an internal capability used by delivery teams, measured on adoption and on the time it removes. Distinct from an embedded team, which sits inside a business function and delivers that function's outcomes.

**Target operating model.** The intended future arrangement of capability, process, decision rights, technology and people, with the transition path stated. Without the transition path it is a picture rather than a plan.

**Technical debt versus architectural debt.** Technical debt is local and repayable by a team in a sprint. Architectural debt is structural, crosses teams and is repaid only by a funded program. Reporting the second as the first is how it becomes permanent.

**Value stream.** The end-to-end sequence of activities delivering a result to a customer, cutting across functions. The unit that reveals queues between departments, which is where most cycle time lives.

## Integration engineering

**Anti-corruption layer.** A translation boundary that keeps a legacy system's model from leaking into a new one. The correct place to normalize an enterprise resource planning system's identifiers before they reach a tool schema.

**API gateway versus AI gateway.** An API gateway does routing, authentication, rate limiting and protocol translation for services generally. An AI gateway adds model routing by classification, prompt and response logging, redaction, token budgets, cache orchestration and cost attribution. They can be the same product; they are not the same control set.

**Backpressure.** A downstream component signaling upstream to slow down rather than dropping work. The mechanism that turns an overload into degraded throughput instead of a cascade.

**Bulkhead.** Isolating resources so that exhaustion in one path cannot starve another. In practice, separate connection pools and separate queues per use case on a shared gateway.

**Choreography versus orchestration.** In choreography each service reacts to events with no central coordinator. In orchestration one component directs the sequence. Orchestration is easier to observe and to gate, which is why agentic systems that must be auditable are orchestrated.

**Circuit breaker.** A component that stops calling a failing dependency after a threshold and fails fast, then probes for recovery. Prevents a slow dependency from consuming every thread upstream.

**Confused deputy.** A privileged component tricked into using its authority on behalf of a less privileged caller. The canonical agentic form: an agent holding a broad service-account scope acting on instructions that arrived inside retrieved content.

**Contract test.** A test asserting that a provider still satisfies the expectations a specific consumer holds. Distinct from an integration test, which exercises the wiring; the contract test fails the provider's build, not the consumer's.

**Dead letter queue.** Where messages go after exhausting retries. A dead letter queue nobody monitors is a silent data loss channel with a reassuring name.

**Exactly-once versus at-least-once delivery.** At-least-once is what messaging systems actually provide and duplicates are normal. Exactly-once is achieved at the consumer through idempotency, not at the transport. Any design assuming the transport provides it is wrong.

**Idempotency key.** A caller-supplied identifier letting a server recognize a retry and return the original result rather than acting twice. The single control that makes retries safe on state-changing calls.

**N+1 problem.** Issuing one query for a list and then one per item. In agentic systems it appears as a tool that returns identifiers followed by a per-identifier lookup loop, which is a latency and cost defect the tool schema should have prevented by returning the batch.

**Outbox pattern.** Writing a message to a database table in the same transaction as the state change, with a separate process publishing it. Removes the dual-write failure where the state changed and the event did not.

**Poison message.** A message that fails every time it is processed and blocks the queue behind it. Handled by attempt counting and routing to a dead letter queue, not by retrying harder.

**Rate limit versus quota.** A rate limit bounds requests per unit of time and protects the service. A quota bounds consumption over a period and protects the budget. They are enforced in different places and breaching them means different things.

**Saga.** A sequence of local transactions with compensating actions for rollback, used where a distributed transaction is impossible. The compensating action is the design work; most sagas fail because someone assumed a step was reversible.

**Schema registry.** A governed store of message and payload schemas with compatibility rules, so that a producer cannot ship a breaking change unnoticed. The enterprise control that makes additive-only evolution enforceable rather than aspirational.

**Strangler fig.** Replacing a legacy system incrementally by routing slices of traffic to the new implementation until nothing reaches the old one. The realistic migration pattern where a big-bang cutover is unacceptable.

**Webhook signature verification.** Validating that an inbound callback genuinely came from the claimed sender, using a shared secret over the raw body. Omitting it turns a webhook endpoint into an unauthenticated write path.

## Data and knowledge architecture

**Authoritative source.** The one artifact designated as correct for a knowledge domain, with every other artifact in that domain labeled derived or copy. Related to but not identical with system of record: a system of record is a system, an authoritative source may be a document, and a domain with two authoritative sources is not ready for retrieval.

**Conceptual, logical and physical model.** Three levels of data modeling: what the business means, how it is structured independently of technology and how it is implemented. An artificial intelligence system needs all three, because retrieval filters are written against the logical level and business meaning is what the model must reproduce.

**Controlled vocabulary.** A fixed list of permitted terms for a field, with synonyms mapped to preferred terms. Makes filtering reliable and makes an enumeration meaningful rather than decorative.

**Data contract.** An agreement between a data producer and its consumers covering schema, semantics, freshness, quality thresholds and change notice. Turns an implicit dependency into an obligation someone owns.

**Data lake, warehouse and lakehouse.** A lake stores raw files with schema applied on read. A warehouse stores modeled, curated tables with schema applied on write. A lakehouse combines file storage with table semantics and transactions. The distinction matters here because retrieval evaluation needs reproducible snapshots, which the lake does not give for free.

**Data mesh.** An operating model treating data as a product owned by the domain that produces it, with central standards and self-serve infrastructure. Its relevance is ownership: it names the person accountable for a corpus.

**Data product.** A curated, documented, versioned and owned data asset with stated quality and freshness commitments and a consumer-facing interface. A corpus intended for retrieval should be built as one.

**Data steward versus data owner.** The owner is accountable for the data and can authorize its use. The steward operates it day to day, maintains quality and definitions and has no authority to permit a new purpose. Confusing the two produces approvals from people who cannot give them.

**Derived artifact.** Anything computed from a source record: chunks, embeddings, index entries, caches, assembled-context logs, evaluation sets, analytics extracts and memory stores. The set an erasure request must reach and the set a decommissioning must dispose of.

**Document engineering.** Deliberately structuring documents so that a machine can use them: stable headings, one idea per section, tables as tables, explicit effective dates, explicit supersession and no meaning carried by layout alone.

**Entity resolution.** Determining that two records refer to the same real-world thing. The step where identifier mismatch across systems becomes visible, and the step where an agent must ask rather than guess when multiple candidates match.

**Freshness requirement.** The maximum acceptable lag between a change at source and its appearance in the retrievable set, stated in time rather than in effort. Drives the reindexing strategy and belongs in the user interface as a published commitment.

**Golden record.** The single reconciled version of an entity assembled from multiple sources by master data management. The thing an agent should resolve against rather than any one contributing system.

**Information lifecycle management.** Governing data from creation through active use, archive and destruction, with the basis for each transition recorded. The frame that turns retention from a storage setting into a control.

**Knowledge estate.** Everything an organization knows, across systems nobody inventoried, in states nobody recorded, owned by people who have mostly left. The thing retrieval reads from, whose every property becomes a property of the answer.

**Master data management.** The discipline of maintaining a single authoritative version of core entities such as customer, supplier, product and employee across systems. Its absence is why identifier resolution is the quiet cost in most integrations.

**Metadata, five categories.** As section 6.3 of the Primer names them: Descriptive (title, author, subject, keywords, summary), Structural (position, section path, neighbors), Administrative (format, ingest date, index version, embedding model, retention class), Provenance (origin and transformation history) and Governance (classification, permission set, jurisdiction, legal hold, owner, effective and expiry dates). Retrieval systems fail on the last three most often.

**Ontology versus taxonomy.** A taxonomy is a hierarchy of categories. An ontology adds typed relationships between entities, so it can express that a policy supersedes another policy or applies to a jurisdiction. Retrieval filters need a taxonomy; reasoning over relationships needs an ontology.

**Records schedule.** The formal statement of how long each class of record is kept, on what basis and how it is disposed of. The document that answers a retention question with authority rather than with a default.

**Semantic layer.** A governed mapping from physical tables to business concepts and metrics, so that "revenue" means one thing. The prerequisite for letting any system, human or otherwise, query the warehouse without inventing definitions.

**Supersession.** The explicit statement that one artifact replaces another from a given date. Must be machine-readable and must remove the superseded content from the retrievable set rather than merely marking it, or the model will cite both.

**Tacit versus embedded knowledge.** Tacit knowledge is in people's heads and requires elicitation before any pipeline can use it. Embedded knowledge is encoded in system behavior such as validation rules and workflow branches, is frequently the authoritative version and must be extracted into a tool call rather than described in a document. Only explicit knowledge is a retrieval problem.

## Governance, risk management and compliance

**Assurance map.** A view of which risks are covered by which controls and which line of defense tests each, showing gaps and duplication. The artifact that reveals a risk everyone assumed someone else was testing.

**Attestation.** A formal statement by a named person that something is true as at a date, made on the record. Cheap, weak on its own and valuable because it creates an addressee.

**Control design versus operating effectiveness.** Design asks whether the control would address the risk if it operated. Operating effectiveness asks whether it operated as designed throughout a period. An organization can pass every design test and fail every operating test, and this is the normal first-year outcome for artificial intelligence controls.

**Control mapping.** Relating one control set to another framework's requirements so that one implementation satisfies several external expectations. Done once and maintained, it prevents the same control being built three times under three names.

**Control objective.** What a control is supposed to achieve, stated as an outcome rather than as an activity. "Only authorized users retrieve privileged material" is an objective; "run a quarterly access review" is an activity that may or may not achieve it.

**Effective challenge.** Substantive, independent questioning of a design or a result by someone competent to do so and empowered to make it stick. Breaks in artificial intelligence programs because the first line is often the only line that understands the system.

**Exception and waiver.** An approved, time-bounded departure from a standard, with a named approver, a stated compensating measure and an expiry. An exception with no expiry is a silent standard change.

**Inherent versus residual risk.** Inherent is the risk before controls. Residual is what remains after them. Residual risk is the number that gets accepted, and the acceptance names a person, not a committee.

**Issue and action tracking.** The register of known control weaknesses with owners, severities and due dates. The measure that matters is aging: an issue register whose average age is rising describes an organization that finds problems and does not fix them.

**Key risk indicator versus key control indicator.** A risk indicator moves before the risk materializes, such as reviewer queue depth. A control indicator says whether the control operated, such as the proportion of changes with an eval run. Reporting the second while calling it the first is common and misleading.

**Legal hold.** A directive to preserve material relevant to anticipated or actual proceedings, overriding normal deletion. For artificial intelligence systems it must reach prompts, outputs, logs, retrieved sets and evaluation artifacts, not only documents.

**Materiality.** The threshold above which an error or omission would change a reasonable user's decision. Sets sampling depth and reporting thresholds, and it is a judgment made by the accountable function rather than a fixed number.

**Model risk management.** The established discipline for governing quantitative models, covering development standards, independent validation, ongoing monitoring and an inventory. Predates generative systems, applies unevenly to them and is where many regulated organizations will place artificial intelligence governance whether or not it fits.

**Non-delegable decision.** A decision the accountable person must take personally, listed explicitly in the charter. Typically top-tier classification, acceptance of residual risk above appetite, deployment without a required control and any position on privilege or regulatory classification.

**Policy, standard, procedure and guideline.** Policy states what is required or prohibited and is mandatory. Standard states the mandatory how, at a measurable level. Procedure states the steps. Guideline recommends and is not mandatory. Mislabeling a guideline as policy is the most common source of over-refusal in enterprise assistants.

**Population, sample and completeness.** The population is every event subject to a control in the period. Completeness is the demonstration that the population is whole, by reconciliation to an independent count. Sampling tests operating effectiveness once the population is established. Most first audits fail on completeness rather than on quality.

**Preventive, detective and corrective control.** Preventive stops the event. Detective reveals that it happened. Corrective restores the position afterward. A detective control presented as protection for an irreversible action is the most common control-design error in artificial intelligence designs. Related to compensating control in the core terms above, which names the same trap.

**Risk appetite versus risk tolerance.** Appetite is how much risk the organization seeks to take in pursuit of objectives, set at board level. Tolerance is the acceptable variation around a specific objective, set operationally. Appetite is a sentence; tolerance is a number.

**Second line.** The functions that set the standard and challenge the first line: risk, compliance, privacy, security and the governance committee. Not an approval queue and not a delivery team, though it is routinely used as both.

**Self-tiering.** A team assessing the risk tier of its own system. The largest single failure point in any tiering model, because the team scoring the system is the team whose delivery date depends on a low score. Mitigated by calibration sampling and by objective triggers that bypass scoring entirely.

**Three lines of defense.** First line owns and runs the risk, second line sets standards and challenges, third line provides independent assurance. Widely used, widely criticized, and the vocabulary any assurance conversation will be conducted in.

**Tier drift.** The gap between the tier a system was assessed at and the tier its current behavior warrants. Four causes: scope creep, corpus creep, usage creep and dependency creep. Only the first is dishonest.

**Work product.** Material prepared in anticipation of litigation, which in many jurisdictions attracts a protection distinct from legal advice privilege. Whether either applies to prompts, retrieved sets or outputs is a determination for counsel; the architectural obligation is to segregate and label so that a determination is possible.

## Security and identity

**Attribute-based access control.** Authorization decided from attributes of the subject, the resource, the action and the context. More expressive than roles and the only workable model when retrieval must filter by clearance, matter, jurisdiction and date simultaneously.

**Authentication versus authorization.** Authentication establishes who is calling. Authorization decides what they may do. In agentic systems the second is where designs fail, because the model is asked to enforce it and a probabilistic component cannot enforce a deterministic rule.

**Break-glass access.** A pre-approved emergency path granting elevated access outside normal process, with automatic alerting, a mandatory reason and a post-hoc review. Its absence produces shared credentials, which is break-glass with no record.

**Client credentials versus authorization code flow.** Client credentials authenticates an application acting as itself, with no user context. Authorization code obtains delegated authority to act as a specific user. Using the first where the second is required is how an agent ends up holding more access than any of its users.

**Egress control.** Restricting where a system may send data, by destination, protocol and content. The control that turns an exfiltration attempt into a blocked request rather than a successful one.

**Entitlement review.** Periodic confirmation by an accountable person that each identity's access is still required, with revocation as the default for anything unconfirmed. Must cover non-human identities, which is where it is routinely incomplete.

**Key rotation.** Replacing credentials on a schedule and on compromise. Distributed provider keys cannot be rotated without coordinated releases, which is the practical argument for holding them once at the gateway.

**Non-human identity.** A credentialed principal that is not a person: a service account, workload identity or agent. Now typically the majority of identities in an environment and the least reviewed. Every agent action should be attributable to both a non-human identity and the human on whose behalf it acted.

**Post-filtering versus pre-filtering.** Pre-filtering applies entitlement before ranking, so unauthorized content is never a candidate. Post-filtering ranks first and removes afterward, leaking through result counts, latency, ranking behavior and citations. Only pre-filtering is a control.

**Red team versus penetration test.** A penetration test looks for exploitable technical weaknesses against a defined scope. A red team pursues an objective by any available route, including social and content-based ones. For artificial intelligence systems indirect injection must be explicitly in scope, because it is the threat a team testing its own design omits.

**Role-based access control.** Authorization by assigned role. Simple, auditable and insufficient alone when access depends on the relationship between a person and a specific matter or record.

**Secrets management.** Centralized storage, issuance, rotation and revocation of credentials, with no secret in source, configuration or a prompt. The failure mode is a credential in a shared configuration file that nobody can revoke without an outage.

**Secure default.** The safe configuration is what you get without doing anything: no retention, no training use, no tools, no external network access, minimum scope, logging on. Every relaxation is a decision with an owner and a record.

**Segregation of duties.** No single person can both initiate and approve a consequential action. Applies to agents: the identity that drafts a payment instruction must not be the identity that releases it.

**STRIDE.** A threat classification covering spoofing, tampering, repudiation, information disclosure, denial of service and elevation of privilege. Adapted for artificial intelligence systems by adding content-borne instruction, corpus poisoning, model substitution and inference of protected attributes.

**Tenant isolation.** Enforced separation of one customer's or department's data, keys, caches, logs and quotas from another's. A cache shared across principals is a disclosure channel that no access control review will find, because the access control is correct and the cache sits beneath it.

**Threat model.** A structured statement of what an attacker would want, how they could get it and which controls stand in the way, produced at design and revised on architecture change. A threat model with no remediation tracking is a document.

**Zero trust.** Designing on the assumption that no network position confers trust, so every request is authenticated, authorized and encrypted. The relevant consequence here is that the orchestrator does not trust the model merely because the model is inside the perimeter.

## Privacy and data protection

**Aggregation and inference problem.** A synthesis of individually non-sensitive sources can be more sensitive than any input. Classification schemes inherit from inputs, which is exactly wrong here, so the output's classification is set by purpose as well as by inheritance.

**Anonymization versus pseudonymization.** Pseudonymization replaces identifiers with tokens and is reversible with the key, so the data generally remains personal data. Anonymization aims at irreversibility. Treating the first as the second is the most common and most consequential privacy error in data pipelines.

**Controller versus processor.** The controller determines the purposes and means of processing; the processor acts on the controller's instructions. The distinction drives contractual obligations and liability, and the analysis for any specific arrangement belongs to counsel.

**Cross-border transfer.** Movement of personal data between jurisdictions, which typically requires a specific lawful mechanism. Architecturally it means naming the region where processing occurs and the region where data rests, and confirming that failover does not silently cross the boundary.

**Data minimization.** Processing only what is necessary for the stated purpose. Structurally opposed by the context window, which rewards supplying more, so minimization has to be a design constraint with a test rather than an intention.

**Data protection impact assessment.** A structured assessment of privacy risk to individuals with mitigations and a residual risk acceptance by a named person. Treated here as an architecture artifact because its output should be design changes with owners and tests.

**Data residency versus data sovereignty.** Residency is where data physically sits. Sovereignty is whose law reaches it, which can differ from residency because of the provider's corporate structure. A residency commitment does not by itself answer a sovereignty question.

**Data subject rights.** The rights individuals hold over their personal data, commonly including access, rectification, erasure, objection and portability. As engineering requirements they mean: can we find everything, can a correction propagate, can we delete across derived artifacts, can we stop processing for one person and can we explain an outcome.

**Erasure propagation.** Executing a deletion across every derived artifact rather than only at source. A deletion that reaches only the source is not a deletion, and the derived-artifact map has to exist before the first request arrives.

**Personal data versus special category.** Special categories attract heightened obligations and vary by jurisdiction. The architectural consequence is fixed even where the legal detail is not: special-category content must be detectable at ingest, recorded as metadata so routing and logging respond and kept inside a defined boundary.

**Privacy by design.** Building privacy into the architecture rather than reviewing for it afterward. Its operational form here is that every privacy risk in the assessment maps to a named design element with a test.

**Purpose limitation.** Data collected for one purpose is not freely available for another. Structurally opposed by the pull of reuse, since a corpus assembled for one assistant is the obvious input to the next one.

**Re-identification risk.** The possibility that supposedly anonymized data can be linked back to individuals, often through combination with other datasets. Rises as the number of available auxiliary sources rises, which means an assessment made two years ago may no longer hold.

**Retention schedule.** Per-artifact retention periods with the basis for each. For artificial intelligence systems it must name logs, caches, embeddings, evaluation sets and memory stores separately, because they have different bases and different destruction methods.

**Subprocessor.** A third party engaged by a processor to carry out part of the processing. Relevant because the subprocessor list changes, notice periods are short and nobody owns reading the notice.

## Operations, reliability and measurement

**Canary release.** Exposing a change to a small traffic slice with guardrail metrics before full rollout. For non-deterministic systems the canary must be evaluated by segment, because an aggregate pass hides the segment that regressed.

**Degraded mode.** A defined reduced-capability operating state with an automatic trigger, not an aspiration. Four levels: full service, reduced capability, human-only and suspended, each with a named authority to declare it.

**Detection latency.** Time from the first bad output to someone noticing. The number that converts an abstract quality argument into a quantity of harm, and the best predictor of the severity of the next incident.

**Drift.** Behavior changing without a change to the system. Section 8.5 of the Primer separates five kinds: input drift, output drift, behavior drift on model upgrade, corpus drift and user drift. Judge drift, the grader itself moving, is not one of the five and is watched separately wherever an automated grader is used.

**Error budget.** The gap between a quality objective and one hundred percent, spent by regressions. While intact, ship changes; when exhausted, only remediation ships. Converts an argument about slowing down into arithmetic, which is its entire value.

**Exposure window.** The interval between a defect reaching production and its containment, which for quality defects includes the grading lag and cannot be reduced to zero. The reason fast proxies exist.

**Feature flag.** A runtime switch changing behavior without a deployment. The mechanism that makes prompt rollback, tool disablement and kill switches executable in minutes.

**Golden set.** A frozen, human-labeled set of known-correct cases used to measure absolute quality over time. Maintained by addition only; editing it breaks comparability across the entire history.

**Judge calibration.** Measuring a model grader's agreement with human graders per class, not overall. A judge agreeing ninety percent overall may agree twenty percent on the rare failure class that was the reason for building it.

**Kill switch.** A single control that stops the system immediately, executable without a deployment by an on-call person who holds the authority to use it. One that requires a release is not a kill switch.

**Monitoring versus observability.** Monitoring watches known indicators against thresholds. Observability is the property of being able to answer a question you did not anticipate from the data already emitted. Observability is not only a system property; in enterprise operations it is also a funded capability with an owner, a retention policy and a cost line.

**On-call and escalation policy.** Who is paged, in what order, with what response commitment and what authority. An incident commander appointed during an incident is appointed by whoever is in the room, which is why the role is pre-named per tier.

**Post-incident review.** A blameless, timeboxed review producing exactly four artifacts: a timeline, a root cause reaching past the proximate trigger, actions with owners and dates and at least one new evaluation case. The last is what makes it compound rather than repeat.

**Recovery time and recovery point objective.** Maximum acceptable downtime and maximum acceptable data loss. Both transfer intact to artificial intelligence systems and both are insufficient alone.

**Recovery quality objective.** The minimum acceptable output quality during degraded operation, expressed against the evaluation suite. Without it, a system that is available while producing materially worse output is reported as recovered. No standard name exists; define it locally.

**Regression suite.** A set that must keep passing, run blocking on every change. Distinct from a golden set, which measures absolute quality; the regression suite measures that nothing which worked stopped working.

**Runbook versus playbook.** A runbook says what to do when a specific named thing happens or breaks, and is triggered rather than browsed. A playbook structures judgment for a situation class. A runbook is executable; a playbook bounds a decision.

**Severity versus priority.** Severity is the magnitude of impact. Priority is the order of work. They diverge legitimately, and conflating them is how a low-frequency severity-one class gets deprioritized permanently.

**Shadow deployment.** Running a candidate against live traffic with no user-visible output, to compare behavior at zero user risk. The only honest way to assess a model version change before exposure.

**Stratified capture.** Sampling by stratum rather than uniformly: full capture for errors, escalations and thin segments, a meaningful rate for low-confidence outputs and a smaller rate for high-confidence ones. Uniform sampling spends the review budget on the common case.

## Commercial, sourcing and cost

**Benefits realization.** Tracking whether the benefits claimed in a business case actually materialized, attributed to the business owner's own metric. A benefit the business owner claims in their own review survives; a benefit claimed by the program is contested.

**Build, buy or partner.** Three genuinely different commitments assessed on weighted criteria rather than on cost alone. The useful output is not a verdict but the relocation of the argument from "build or buy" to "is differentiation really a five here".

**Business associate agreement.** In United States health privacy practice, the contract required with a vendor handling protected health information. Notable architecturally because one configuration being covered does not mean another is, and because it is the fastest way to find a vendor nobody inventoried.

**Chargeback versus showback.** Chargeback moves cost to the consuming business unit's budget. Showback reports it without moving it. Showback changes behavior less and is often the right first step, because chargeback without accurate attribution produces disputes rather than efficiency.

**Commit and drawdown pricing.** A negotiated spend commitment consumed over a period, usually at a discount. Creates an incentive to consume the commitment that has nothing to do with value, which is worth naming before it distorts the roadmap.

**Concentration risk.** Exposure from dependence on a single supplier, region or model family. Routinely understated because it is counted at the wrong level: three products on the same provider, region and model family are one dependency, not three.

**Cost per completed task.** The only cost figure that belongs in a business case: cost per attempt multiplied by attempts per completed task, plus human minutes per completed task at a loaded rate. Cost per call is an engineering number.

**Critical third party.** A supplier whose failure would prevent delivery of an important business service. Attracts heightened assessment, monitoring, exit and, in some regulated sectors, notification treatment. The model provider generally qualifies.

**Substitutability.** The honest measure of exit capability, in four levels: locked, portable with rework, substitutable and dual-run. The maintained evaluation suite is what makes substitution possible, so exit planning that does not fund evaluation is a document rather than a capability.

**Total cost of ownership.** All costs over the asset's life including build, run, support, evaluation, human review, enablement, evidence production and exit. The three most often omitted for artificial intelligence systems are human review minutes, continuous evaluation and the exit.

**Unit economics.** The cost and value of one unit of output, where the unit is a completed task and never a request or a token. A system halving model cost while adding two review minutes per case has made the outcome more expensive.

**Vendor viability.** Assessment of whether a supplier will still exist and still support the product over the commitment period, from funding, customer concentration and category maturity. Immature categories justify shorter commitments and higher substitutability targets.

## Organizational change and adoption

**Automation bias.** The tendency to accept a machine-generated output that would have been challenged had a person produced it. Countered by presenting outputs without confidence signals the reviewer cannot calibrate, and by blind re-review on a sample.

**Breadth versus depth.** Breadth is the proportion of the eligible population using the system. Depth is the proportion of a given user's relevant work passing through it. Independent, requiring different interventions, and depth should be pursued first because it produces evidence while breadth produces a number.

**Champion network.** Named practitioners with funded time who support colleagues in their own segment. Fails when it is voluntary, unfunded and staffed entirely by early enthusiasts, whose experience does not transfer to the skeptical majority.

**Cohort retention.** Tracking each starting group's continued use over time rather than aggregate activity. Aggregate usage can rise while every cohort decays, which is what a growing program with a retention problem looks like.

**Enablement versus training.** Training transfers knowledge in a session. Enablement changes the conditions of work so the capability is usable: access, triggers in the workflow, support routes, templates and permission. Training without enablement produces an activated population that never becomes habitual.

**Internal credential.** A formal, revocable license to perform a role with the system, such as reviewing outputs or configuring prompt assets. Turns competence from an assumption into a recorded fact, which is also what makes the human oversight control assertable.

**Job design.** Deliberate redefinition of a role when a system absorbs part of its work, covering what the person now does, what they are measured on and what career path follows. Left undone, the redesign happens informally and badly.

**Pilot, proof of concept and production.** A proof of concept tests feasibility and should be thrown away. A pilot tests value with real users on real work under real constraints, with pre-registered success criteria and a kill criterion. Production is neither. Calling a proof of concept a pilot is how pilot purgatory starts.

**Pilot purgatory.** A state where pilots succeed, nothing scales and the program accumulates demonstrations. Designed out by fixing the scale decision criteria and the funding route before the pilot begins, not after it succeeds.

**Resistance analysis.** Distinguishing the two legitimate resistances, meaning the person who is right about a defect and the person whose interests are genuinely harmed, from resistance that is fear or inertia. The first two require design or negotiation, not communication.

**Rubber-stamping.** Approval at or near one hundred percent with review times far below reading time. Root cause is measuring reviewers on throughput. Measured by override rate against an investigation threshold rather than a target.

**Sponsor.** The executive who holds the mandate, the budget and the political cover. The failure mode worth naming separately is the enthusiastic sponsor who wants the wrong thing, which is harder to manage than an absent one.

**Stakeholder map.** Who is affected, what each stands to gain or lose, what each controls and what each needs to hear. Distinct from a communications plan, which is the output; the map is the analysis that makes the output correct.

**Steering committee.** The body that resolves cross-functional conflict and decides what the program cannot decide alone. Works when it holds decisions and a short standing agenda; fails when it receives status reports.

**Trust calibration.** Users holding an accurate model of what the system is reliable at and where it fails. The goal is neither maximum trust nor minimum trust, and the first ninety days set it asymmetrically because early errors cost far more confidence than early successes gain.

**Works council.** In some jurisdictions a formally constituted employee representative body with consultation or co-determination rights over changes affecting work. Whether an obligation applies, and what it requires, is a determination for counsel and human resources and must be settled before communication rather than after.

**Final Liability rests with the Human.**
