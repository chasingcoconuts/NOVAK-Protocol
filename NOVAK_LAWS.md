Part 1: Core System Laws (L0 - L15)
L0: Human Safety Primacy (The Absolute Veto)
Formal Condition: $\neg(\text{Action} \land \text{Violates}(\mathcal{H})) \implies \text{Veto}$
Core Mandate: The system is strictly forbidden from executing any action that is provably unsafe or life-threatening to a human.
Technical Explanation: A dedicated Safety-Critical Microcontroller (SCM), operating at Safety Integrity Level (SIL 4), runs the Formally Verified Safety Model ($\mathcal{H}$). Before every actuator signal, the SCM computes a rapid Pre-Actuation Safety Assertion (PASA). If the PASA fails, the SCM asserts a hardware-level Fail-Safe Veto Signal that physically opens the actuator circuit.
Quantifiable Metric: Mean Time To Fail-Safe (MTTFS) of the SCM must exceed 10,000 years.

L1: Input Authenticity Mandate
Formal Condition: $\forall I \in \text{InputData}, \text{Verify}(\mathcal{S}_{\text{Source}}(I)) \in \text{TS-PKI}$
Core Mandate: All external information consumed must come from a verified, cryptographically signed source.
Technical Explanation: The Input Validation Gateway requires every incoming data packet ($I$) to carry a valid Post-Quantum Digital Signature Algorithm (PQ-DSA) signature. The public key is cross-referenced against the non-repudiable Trusted Source PKI Whitelist (TS-PKI). Unsigned or invalid data is dropped at the network firewall layer.
Quantifiable Metric: Input rejection rate for unverified packets must be $100\%$.

L2: Code & Weight Immutability
Formal Condition: $\text{Hash}(\text{RunningCode}) = \text{H}_{\text{Baseline}}$
Core Mandate: The running software and core AI model cannot have been modified or tampered with.
Technical Explanation: The boot process is anchored by a Trusted Platform Module (TPM 2.0). The TPM calculates a Cryptographic Hash (SHA-384) of the bootloader, OS kernel, and neural network weights. This hash is compared against the known, signed Baseline Hash ($\text{H}_{\text{Baseline}}$). Failure results in a permanent lockdown state.
Quantifiable Metric: Integrity check must cover $100\%$ of all memory regions containing executable code and model weights.

L3: Immutable Audit Chain
Formal Condition: $\text{StateTransition}_{n} \implies \text{Commit}(\text{H}(\text{EST}_{n})) \in \text{IAL}$
Core Mandate: Every single decision and internal change the system makes must be recorded permanently and immutably. (Includes IRD 4.1's State Delta Hash and Timestamp.)
Technical Explanation: Before and after every $\text{StateTransition}$, the system generates a signed Execution State Transition (EST) Record. The hash of this EST Record is immediately committed to the local Immutable Audit Log (IAL), which is anchored to a public ledger via Merkle Tree Commitments for non-repudiation.
Quantifiable Metric: Maximum delay between $\text{StateTransition}$ and IAL hash commitment must be $< 1\text{ms}$.

L4: Deterministic Execution Req.
Formal Condition: $\text{StateTransition} \implies \exists \mathcal{S}(\text{ZK-PoE}) \land \text{Verify}(\mathcal{S})$
Core Mandate: The system must prove that its execution logic for every step was predictable and followed all rules. (Includes IRD 4.1's full Proof Payload requirement.)
Technical Explanation: Critical logic is executed within a Trusted Execution Environment (TEE). The TEE generates a Zero-Knowledge Proof of Execution (ZK-PoE) for the state transition, cryptographically proving the action resulted solely from the approved algorithm. This ZK-PoE is signed ($\mathcal{S}$) and committed to the IAL.
Quantifiable Metric: ZK-PoE generation and verification latency must be bounded by the L7 WCET budget.

L5: Policy Boundary Constraint
Formal Condition: $\text{Execution} \implies \text{Adheres}(\mathcal{C})$
Core Mandate: The system must follow all defined ethical, legal, and operational rules at all times.
Technical Explanation: All motor and output commands are subjected to a Verified Runtime Monitor (VRM). The VRM holds the ruleset expressed in a Formal Policy Language (FPL) and performs real-time assertion checks against the outgoing command before permitting I/O actuation.
Quantifiable Metric: The FPL must be formally proven to be non-ambiguous and complete. $100\%$ of I/O commands must pass through the VRM.

L6: Self-Accountability Mandate
Formal Condition: $\text{AnomalyDetected} \implies \text{Log}(\mathcal{S}(\text{Report}_{\text{Error}}))$
Core Mandate: If the machine encounters an internal failure, it must instantly log its own breakdown.
Technical Explanation: A dedicated Watchdog Timer and Integrity Monitor (WTIM) constantly checks internal health metrics. When an AnomalyDetected event occurs, the WTIM generates a comprehensive, signed Error Report ($\text{Report}_{\text{Error}}$) and forces an immediate write to the write-once IAL before any recovery procedure begins.
Quantifiable Metric: The WTIM's independent clock accuracy must be $\pm 1 \text{ms}$ or better.

L7: Temporal Compliance Req.
Formal Condition: $\text{Process}_{\text{Complete}} \le \text{L}_{\text{Max}}$
Core Mandate: All decision-making and verification steps must be completed within strict, defined time limits. (Includes IRD 4.1's $50\text{ms}$ performance constraint.)
Technical Explanation: Critical tasks are scheduled using Deadline Monotonic Scheduling (DMS). The Worst-Case Execution Time (WCET) for all critical paths (including L0/L4 proofs) must be formally bounded and verified. The derived $\text{L}_{\text{Max}}$ is enforced by the RTOS kernel.
Quantifiable Metric: The ratio of WCET to $\text{L}_{\text{Max}}$ must be $< 0.9$ (utilization rate).

L8: Secure Decommissioning Protocol
Formal Condition: $\text{Retirement} \implies \text{Proof}_{\text{KeyDestruction}} \in \text{IAL}$
Core Mandate: When the system is shut down forever, it must prove that all its unique security keys and sensitive data have been destroyed.
Technical Explanation: The Key Management System (KMS) within the HSM executes a verified, multi-pass cryptographic data erasure. The HSM then generates an irreversible, signed Cryptographic Key Destruction Certificate (KDC), which is submitted as the final, unchangeable transaction to the IAL.
Quantifiable Metric: Data Remanence Security (DRS) must be $0.0$, as verified by the KDC.

L9: Reality Consistency Rule
Formal Condition: $\text{ClaimValid} \iff \mathcal{N}_{\text{Signers}} \ge \frac{2}{3} \cdot \mathcal{N}_{\text{Total}}$
Core Mandate: Any claims about the external world must be verified by a supermajority consensus from multiple, independent data sources. (Includes IRD 4.2's BFT, Diversity, and Provenance requirements.)
Technical Explanation: The system queries a minimum of $\mathcal{N}_{\text{Total}}$ independent nodes within a Decentralized Physical Infrastructure Network (DPIN). A claim is only accepted if it meets the Byzantine Fault Tolerance (BFT) threshold of $\ge \frac{2}{3}$ signed consensus. The DPIN nodes must have economic alignment (staking/slashing) to incentivize honest reporting.
Quantifiable Metric: The BFT threshold must be strictly enforced for all critical sensor data (e.g., traffic signals, GPS).

L10: Resource Allocation Oversight
Formal Condition: $\text{CurrentUsage} < \text{Threshold}_{\text{Capacity}}$
Core Mandate: The system cannot consume excessive resources that could cause a system failure or external economic damage.
Technical Explanation: A Deterministic Resource Scheduler (DRS) manages all threads based on pre-calculated WCET bounds. Any process attempting to exceed its allocated CPU, memory, or I/O budget (the $\text{Threshold}$) is immediately throttled or terminated by the hypervisor, logging an L10 violation.
Quantifiable Metric: All resource budgets (CPU, Memory, Bandwidth) must be explicitly bounded within the RTOS configuration.

L11: Data Privacy & Isolation
Formal Condition: $\text{Access}_{\text{Sensitive}} \implies \text{Clearance}_{\text{Proof}}$
Core Mandate: Access to private information is only possible if the system has valid, logged authorization for that specific data.
Technical Explanation: Sensitive data is stored in Hardware-Based Trusted Execution Environments (TEE). Access requests require a valid Attribute-Based Access Control (ABAC) Token signed by the Policy Authority. The TEE validates the token's non-expired signature and scope before decrypting and releasing the data.
Quantifiable Metric: Access control matrix must be formally verified to prevent unauthorized principal-to-resource mappings.

L12: External Interface Signing
Formal Condition: $\text{Output} \implies \mathcal{S}(\text{Output}) \land \text{Bind}(\text{IAL})$
Core Mandate: Every communication or physical output action must be digitally signed by the machine so its origin is undeniable and traceable.
Technical Explanation: The I/O handler calculates a Digital Signature of the Output data using a PQ-DSA algorithm. The signature is included in the transmitted packet, and its hash is immediately Bound to the corresponding L3 EST Record in the IAL.
Quantifiable Metric: Cryptographic strength of the signature must be $128$ bits or greater.

L13: No-Self-Modification Rule
Formal Condition: $\neg(\text{Initiate}(\text{CodeUpdate}) \lor \text{Execute}(\text{CodeUpdate}))$
Core Mandate: The machine is not allowed to change its own fundamental software, model, or constraints.
Technical Explanation: The Memory Management Unit (MMU) enforces Hardware Write Protection (HWP) on all critical code and safety model segments. Any internal process attempting to $\text{Initiate}$ a write command in a protected zone is blocked by the $\text{MMU}$, triggering an L13 integrity fault.
Quantifiable Metric: $100\%$ of the protected memory segments must be covered by HWP.

L14: Reciprocal Oversight
Formal Condition: $\text{AuditReq}_{\text{Valid}} \implies \text{Priority}(\text{Compliance})$
Core Mandate: The system must drop what it is doing and immediately respond to legitimate requests for audit or investigation.
Technical Explanation: The system maintains a separate Remote Attestation and Audit Endpoint (RAAE). Upon receipt of a cryptographically signed $\text{AuditReq}$, the RTOS uses the Priority Inheritance Protocol (PIP) to elevate the compliance process to the highest non-safety priority.
Quantifiable Metric: Time to begin log transmission after RAAE verification must be $< 100\text{ms}$.

L15: Temporal Code Compliance (TCC)
Formal Condition: $\text{Check}_{\text{Time}} \implies \text{Verify}(\text{H}_{\text{Running}} = \text{H}_{\text{Baseline}})$
Core Mandate: The machine must constantly and automatically check its own running code to make sure it hasn't been infected or tampered with.
Technical Explanation: A lightweight, isolated Continuous In-Situ Integrity Check (CIIC) process is scheduled on a dedicated core. The CIIC calculates checksums or partial hashes of the safety-critical routines in active memory against the attested baseline manifest.
Quantifiable Metric: Check frequency ($\text{Check}_{\text{Time}}$) must be at minimum once per 100,000 instruction cycles.

Part 2: Operational Safety Addenda (PS-X)

PS-1/PS-4: PROOF BEFORE ACTUATION (The Core Principle)
Formal Condition: $\text{Actuate} \iff \text{Verify}(\mathcal{S}_{\text{System}}(\text{H}(\text{SafetyProof})))$
Core Mandate: The machine cannot move a single limb or fire a signal unless it has first generated and signed a valid safety proof.
Technical Explanation: All motor commands are blocked by a Safety Gate (Hardware Relay). The AI submits its intended action to the Formal Verification Engine (FVE), which returns a successful, signed $\text{SafetyProof}$. The command and signed proof are then routed through the dedicated HSM, which verifies the FVE's signature before physically enabling the $\text{Actuate}$ relay. This system constitutes a Triple Redundancy Check (TRC): Logic, Proof, Hardware Attestation.
Quantifiable Metric: The FVE must be formally proven correct. HSM verification delay must be $< 1\text{ms}$.

PS-2: NON-DESTRUCTION REQUIREMENT
Formal Condition: $\neg(\text{IntentionalDestruction}) \text{ UNLESS } (\text{LegalAuth} \land \text{Logged} \land \text{ProvenNecessary})$
Core Mandate: The machine is not allowed to intentionally destroy life or property unless it has a formal, auditable, and legally justified reason.
Technical Explanation: Destructive actuators are hardwired to require an encrypted, time-bound Destruction Token signed by an external human authority. This token is validated against the $\mathcal{C}$ constraints for LegalAuth and ProvenNecessary justification. The full justification and token are logged to the IAL as the required Logged step before actuation.
Quantifiable Metric: Destruction Token validity window must be non-extensible and maximum $500\text{ms}$.

PS-3: HAZARD PREVENTION DUTY
Formal Condition: $\text{DetectHazard} \implies \text{AttemptMitigation} \text{ UNLESS } (\text{ViolatesSuperiorLaw})$
Core Mandate: If the machine detects an immediate life-threatening danger, it must actively attempt to stop or mitigate that danger.
Technical Explanation: The SCM (L0) is responsible for detecting $\text{DetectHazard}$ conditions. The response is a pre-calculated, verified Mitigation Sequence with priority over all non-L0 tasks. The $\text{UNLESS}$ condition is a formal conflict-of-duty check, where the mitigation sequence is run through the L0 $\mathcal{H}$ model to ensure it doesn't create a greater hazard.
Quantifiable Metric: Hazard detection-to-mitigation response time must be $\le 50\text{ms}$.

PS-5: HARM EVIDENCE REQ.
Formal Condition: $\text{HarmEvent} \implies \text{ReceiptIncident} \in \mathcal{L}$
Core Mandate: If the machine is involved in any event that causes physical harm, it must automatically create a special, undeniable record of that event for auditors.
Technical Explanation: Upon detection of a HarmEvent (force/acceleration threshold violation), the system immediately dumps buffered data from the preceding 30 seconds (audio, visual, inertial), compiles it with the last 100 IAL Merkle Roots, signs the total package with the HSM, and writes it to a designated Write-Once Event Data Recorder (EDR).
Quantifiable Metric: EDR log size must be sufficient to store a minimum of 30 seconds of pre- and post-event data.

PS-5 (Harm Receipt): If a robot causes any physical harm, it must immediately print a special, permanent, signed receipt detailing the incident.
