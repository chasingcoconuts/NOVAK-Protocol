import hashlib
import json
import time

# ------------------------
# Helper: SHA-256 hash
# ------------------------
def _h(value):
    return hashlib.sha256(json.dumps(value, sort_keys=True).encode()).hexdigest()

# ------------------------
# NIPS: Input Verification
# ------------------------
def verify_nips(inputs, schema):
    # 1. schema must match
    for field in schema:
        if field not in inputs:
            return False
    
    # 2. placeholder "signature/provenance" check
    # In real systems, you verify cryptographic signatures here.
    if not inputs.get("attested", False):
        return False

    return True

# ------------------------
# HARMONEE: Execution Receipt
# ------------------------
def harmonee_receipt(rule, inputs, output):
    return _h({
        "rule_id": rule["id"],
        "input_hash": _h(inputs),
        "output_hash": _h(output),
        "actor": "NOVAK_KERNEL",
        "timestamp": int(time.time())
    })

# ------------------------
# REVELATION: Global Chain
# ------------------------
def revelation_chain(previous_hash, receipt_hash):
    return _h(previous_hash + receipt_hash)

# ------------------------
# NOVAK Equal Execution Law
# ------------------------
def equal_execution_check(rule, inputs, output, reference_table):
    key = _h({"rule": rule, "inputs": inputs})
    if key in reference_table:
        prior_output = reference_table[key]
        if prior_output != output:
            return {
                "violation": True,
                "expected": prior_output,
                "actual": output,
                "justification_required": True
            }
    else:
        reference_table[key] = output

    return {"violation": False}

# ------------------------
# DETERMINISTIC EXECUTION KERNEL (NOVAK)
# ------------------------
def novak_execute(rule, inputs, schema, reference_table, prev_chain_hash):
    # 1. NIPS enforcement
    if not verify_nips(inputs, schema):
        raise ValueError("NIPS Violation: Inputs are not attested or schema-valid.")
    
    # 2. Deterministic rule application
    cond = rule["logic"]["if"]
    if inputs["disability_rating"] >= cond["value"]:
        output = rule["logic"]["then"]
    else:
        output = rule["logic"]["else"]

    # 3. HARMONEE execution receipt
    receipt = harmonee_receipt(rule, inputs, output)

    # 4. REVELATION recursive audit hash
    chain_hash = revelation_chain(prev_chain_hash, receipt)

    # 5. Equal Execution Principle
    eq = equal_execution_check(rule, inputs, output, reference_table)

    return {
        "output": output,
        "receipt": receipt,
        "chain_hash": chain_hash,
        "equal_execution": eq
    }
