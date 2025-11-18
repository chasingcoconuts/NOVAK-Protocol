
Law ID,Law Name,Formal Logical/Cryptographic Condition,Primary Function

🛑 LAW ZERO,PRIMACY OF HUMAN SAFETY,¬(Harm) UNLESS (SAuthority​(Lawful)∧DueProcess),Ethical/Legal Constraint

LAW 1,VERIFIED INPUT ONLY (NIPS),Execute⟺(SchemaValid(D)∧Verify(SSource​(H(D)))),Data Integrity
LAW 2,EXECUTION RECEIPT IMMUTABILITY (HARMONEE),$\text{Receipt} = H(R_{\text{ID}} \| H(D) \| H(O) \| \text{Actor}_{\text{ID}} \| \text{Timesta$,Atomic Accountability
LAW 3,GLOBAL AUDIT CONSISTENCY (REVELATION),∀n:Ln​=H(Ln−1​∥Receiptn​,Historical Integrity
LAW 4,EQUAL EXECUTION REQ.,IF (D1​≡D2​)∧(R(D1​)=R(D2​))⟹MUST Produce J where S(H(J)),Algorithmic Fairness
LAW 5,PUBLIC VERIFIABILITY,"∀Verifier V:V(Receipt,PublicKeys)=TRUE",Transparency
LAW 6,CORRECTNESS BEFORE IMMUTABILITY,H(LegalityProof)⟹WriteTo(L),"The ""Prove THEN Record"" Principle"
LAW 7,FORBIDDEN SILENT OUTPUTS,¬(Decision∧¬Logged)⟹HALT∧LogForensics,Complete Logging
LAW 8,REDUNDANT AUTHORITY,State1​≡State2​≡State3​ IF ¬(Consensus)⟹HALT,System Resilience
LAW 9,REALITY CONSISTENCY RULE,OutputClaim(O)⟺Verify(SOracle​(H(RealityMatch))),Physical Truthfulness
LAW 10,MACHINE ACCOUNTABILITY,R⊂H(LegalCodeID​),Legal Compliance
LAW 11,HUMAN OVERRIDE SUPREMACY,Override⟹Logged(SHuman​(OverrideAction)),Final Human Control
LAW 12,MODEL AND DATA PROVENANCE,Execute⟺Verify(SDev​(ModelHash∥DataHash∥ProcHash,AI Model Integrity
LAW 13,DYNAMIC REDUNDANCY LIMIT,If (Latency>Tmax​)∧(¬HarmRisk)⟹TempSet(N=2)∧Log(Risk),High-Speed Liveness
LAW 14,PROOF-OF-LIVENESS ATTESTATION,Liveness⟹S(StateHash∥UptimeProof) every Δ,Continuous Availability

Addendum ID,Requirement Name,Formal Logical/Cryptographic Condition,Core Mandate
PS-1/PS-4,PROOF BEFORE ACTUATION/FORCE,Actuate⟺Verify(SSystem​(H(SafetyProof))),"Physical action is forbidden unless preceded by a verifiable, signed safety proof."
PS-2,NON-DESTRUCTION REQUIREMENT,¬(IntentionalDestruction) UNLESS (LegalAuth∧Logged∧ProvenNecessary),A machine may not intentionally destroy life or property unless legally justified and logged.
PS-3,HAZARD PREVENTION DUTY,DetectHazard⟹AttemptMitigation UNLESS (ViolatesSuperiorLaw),A system must attempt to mitigate life-threatening hazards.
PS-5,HARM EVIDENCE REQ.,HarmEvent⟹ReceiptIncident​∈L,"Any physically harmful event must automatically generate a special, immutable incident receipt logged to the chain."


Any alteration to the model, data, or process invalidates the execution chain.


🤖 The Robot's Code of Honor (The 14 Novak Laws)
The goal of these 14 rules is simple: to make sure every smart computer or robot is always honest, safe, and fair, and that you can prove it.

🛑 The Safety Boss
LAW ZERO — HUMAN SAFETY FIRST!

This is the supreme rule. A computer can never hurt a person, not even by accident. If the computer has to make a scary or harmful choice, it must have a signed, legal permission slip that proves it’s absolutely necessary. (Safety is the Boss.)

📝 Rules About Honesty and Evidence
These rules make sure the computer tells the truth and keeps perfect records.

LAW 1 — NO FAKE NEWS! (Verified Input)

The computer can only use information that has been 100% verified and has a digital signature. If the data is shaky or anonymous, the computer must ignore it. (Garbage In, Rejection Out.)

LAW 2 — THE PERMANENT RECEIPT (HARMONEE)

Every time the computer does anything, it must instantly print a digital, non-erasable receipt. This receipt proves who did it, what data they used, and what the final result was. (You Can Never Delete the Receipt.)

LAW 3 — THE UNBREAKABLE CHAIN (REVELATION)

All those receipts are locked together like an unbreakable chain. If anyone tries to secretly remove, change, or add a receipt, the whole chain breaks instantly, and everyone knows. (No Sneaky Changes Allowed.)

LAW 5 — SHOW YOUR WORK (Public Verifiability)

Anyone in the world must be able to check the computer's receipt using public tools. You don't have to just "trust" the company. (Anyone Can Be the Auditor.)

LAW 7 — NO SECRETS

The computer can't make secret decisions. If it makes a decision without logging it, it must immediately stop working and yell a loud integrity alarm. (Everything Must Be Logged.)

⚖️ Rules About Fairness and Justice
These rules prevent robots from being biased or making mistakes they can't fix.

LAW 4 — EQUAL IS EQUAL

If two people have the exact same information but the computer gives them two different answers, the computer must stop and write a detailed letter explaining why. If it can't explain, it cheated. (Fairness Must Be Proven.)

LAW 6 — PROVE IT BEFORE YOU WRITE IT

The computer must prove that its decision is legal and correct before it gets to write it down on the permanent receipt book. It can't record a mistake first. (Proof Before Pen.)

LAW 9 — REALITY CHECK

If the computer says, "I turned the light off," then a special sensor must send back a signed note that says, "Yes, the light is actually off." The computer's paper truth must match the real-world truth. (Paper Truth Must Be Real Truth.)

LAW 10 — NO TRUST, ONLY LAW

If a computer is deciding anything important (like a fine), it must be executing a specific, written law that can be checked by math, not just a vague company policy. (Rules, Not Feelings.)

LAW 12 — THE ROBOT'S BRAIN TAG (Model Provenance)

The computer's "brain" (the AI model) needs a tamper-proof ID tag. This tag proves: 1) It's the right brain. 2) The data it learned from hasn't been cheated. (The Brain Must Be Certified.)

👑 Rules About Control and Survival
These final rules make sure the computer is always controlled by humans and stays working when needed.

LAW 8 — THREE WITNESSES

The computer must have at least three different, independent systems watching it and checking its math. If the three witnesses disagree, the computer must immediately stop. (Triple Check Everything.)

LAW 11 — THE EMERGENCY STOP

A person can stop or change the computer's decision in an emergency, but that override must be signed, permanent, and publicly traceable. (No Anonymous Bosses.)

LAW 13 — HIGH-SPEED CHOICES

In systems where speed is vital (like stock trading), the computer can temporarily ignore the Three Witnesses rule if waiting would cause massive failure, but it must log the risk and return to three witnesses immediately. (Speed Over Safety Only When Necessary.)

LAW 14 — ALWAYS ON PROOF

The computer must regularly sign a small receipt that proves it is alive, responsive, and working. This prevents the system from silently freezing. (Prove You're Not Frozen.)

⚠️ The Physical Safety Addendum (PS)
(These are special rules for robots and drones that move.)

PS-1/PS-4 (Proof Before Force): A robot can't move, start its engine, or apply force until it has a signed safety proof that says, "This move is safe."

PS-2 (Non-Destruction): A machine can never intentionally destroy people, animals, or property unless legally allowed and absolutely necessary.

PS-5 (Harm Receipt): If a robot causes any physical harm, it must immediately print a special, permanent, signed receipt detailing the incident.
