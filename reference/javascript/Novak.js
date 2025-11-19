// NOVAK Protocol Demo
// Matthew Novak – 2025
// Implements: NIPS, HARMONEE, REVELATION, Equal Execution Law

// SHA-256 function (browser + Node compatible)
async function sha256(text) {
  const enc = new TextEncoder().encode(text);
  const hashBuffer = await crypto.subtle.digest("SHA-256", enc);
  return [...new Uint8Array(hashBuffer)]
    .map(b => b.toString(16).padStart(2, "0"))
    .join("");
}

// ----------------------
// 1) NIPS — Input Proof
// ----------------------
async function NIPS(input) {
  if (!input) throw new Error("NIPS FAIL: Missing input");
  if (typeof input !== "object") throw new Error("NIPS FAIL: Must be object");

  // Simulated signature + schema check
  if (!input.attested) throw new Error("NIPS FAIL: Input not attested");
  if (!input.schemaVersion) throw new Error("NIPS FAIL: Bad schema");

  return {
    input,
    inputHash: await sha256(JSON.stringify(input))
  };
}

// ----------------------
// 2) HARMONEE — Execution Receipt
// ----------------------
async function HARMONEE(ruleId, inputHash, output, actor="system") {
  const outputHash = await sha256(JSON.stringify(output));
  const timestamp = Date.now().toString();

  const receiptString = `${ruleId}|${inputHash}|${outputHash}|${actor}|${timestamp}`;
  const receiptHash = await sha256(receiptString);

  return {
    ruleId,
    inputHash,
    outputHash,
    actor,
    timestamp,
    receiptHash
  };
}

// ----------------------
// 3) REVELATION — Global Chain
// ----------------------
async function REVELATION(prev, receiptHash) {
  const chainHash = await sha256(prev + "|" + receiptHash);
  return chainHash;
}

// ----------------------
// 4) NOVAK Equal Execution Law
// ----------------------
function equalExecutionCheck(D1, D2, O1, O2) {
  const inputsEqual = JSON.stringify(D1) === JSON.stringify(D2);
  const outputsEqual = JSON.stringify(O1) === JSON.stringify(O2);

  if (inputsEqual && !outputsEqual) {
    throw new Error("NOVAK VIOLATION: Identical inputs produced different outputs");
  }

  return true;
}

// ----------------------
// DEMO RUN
// ----------------------
async function demoNOVAK() {
  console.log("=== NOVAK DEMO START ===");

  // 1. NIPS input
  const input = {
    claimant: "12345",
    condition: "hearing_loss",
    attested: true,
    schemaVersion: 1
  };

  const nips = await NIPS(input);

  // 2. Fake rule engine
  function ruleEngine(input) {
    return {
      approved: true,
      rating: 10
    };
  }

  const output = ruleEngine(input);

  // 3. Equal execution check
  equalExecutionCheck(input, input, output, output);

  // 4. HARMONEE receipt
  const receipt = await HARMONEE("RULE-VA-2025", nips.inputHash, output);

  // 5. REVELATION chain
  const chain = await REVELATION("GENESIS", receipt.receiptHash);

  console.log({ nips, receipt, chain });
  console.log("=== NOVAK DEMO COMPLETE ===");
}

demoNOVAK();
