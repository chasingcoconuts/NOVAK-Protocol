import hashlib
import json
import time

# -----------------------------------------
# SHA-256 helper (normalized representation)
# -----------------------------------------
def _h(value):
    """Hash any Python object deterministically."""
    if isinstance(value, (dict, list)):
        value = json.dumps(value, sort_keys=True).encode()
    elif isinstance(value, str):
        value = value.encode()
    else:
        value = str(value).encode()
    return hashlib.sha256(value).hexdigest()

# -----------------------------------------
# NOVAK GENESIS HASH
# -----------------------------------------
GENESIS_HASH = _h("NOVAK-GENESIS")

# -----------------------------------------
# NIPS: Input Verification
# -----------------------------------------
def verify_nips(inputs, schema):
    # Check required fields exist
    for field in schema:
        if field not in inputs:
            return False
    
    # Check attestation flag
    if not inputs.get("attested", False):
        return False

    return True

# -----------------------------------------
# HARMONEE: Execution Receipt
# -----------------------------------------
def harmonee_receipt(rule, inputs, output):
    receipt_obj = {
        "rule_id": rule["id"],
        "input_hash": _h(inputs),
        "output_hash": _h(output),
        "actor": "NOVAK_KERNEL",
        "timestamp": int(time.time())
    }
    return _h(receipt_obj), receipt_obj

# -----------------------------------------
# REVELATION: Global recursive hash chain
# -----------------------------------------
def revelation_chain(previous_hash, receipt_obj):
    chain_obj = {
        "prev_hash": previous_hash,
        "receipt": receipt_obj
    }
    return _h(chain_obj)

# -----------------------------------------
# Equal Execution Law (EEL)
# -----------------------------------------
def equal_execution_check(rule, inputs, output, reference_table):
    key = _h({"rule": rule["id"], "inputs": inputs})

    if key in reference_table:
        expected = reference_table[key]
        if expected != output:
            return {
                "violation": True,
                "expected": expected,
                "actual": output,
                "justification_required": True
            }
    else:
        reference_table[key] = output

    return {"violation": False}

# -----------------------------------------
# NOVAK EXECUTION KERNEL
# -----------------------------------------
def novak_execute(rule, inputs, schema, reference_table, prev_chain_hash=GENESIS_HASH):

    # 1. NIPS — Verified inputs only
    if not verify_nips(inputs, schema):
        raise ValueError("NIPS Violation: Inputs invalid or not attested.")

    # 2. Deterministic rule logic
    cond = rule["logic"]["if"]
    if inputs[cond["field"]] >= cond["value"]:
        output = rule["logic"]["then"]
    else:
        output = rule["logic"]["else"]

    # 3. HARMONEE receipt
    receipt_hash, receipt_obj = harmonee_receipt(rule, inputs, output)

    # 4. REVELATION global chain
    chain_hash = revelation_chain(prev_chain_hash, receipt_obj)

    # 5. Equal Execution Law
    eq_check = equal_execution_check(rule, inputs, output, reference_table)

    return {
        "output": output,
        "receipt_hash": receipt_hash,
        "receipt_obj": receipt_obj,
        "chain_hash": chain_hash,
        "equal_execution": eq_check
    }

# -----------------------------------------
# SIMPLE TEST EXECUTION (DEMO)
# -----------------------------------------

if __name__ == "__main__":

    # Example rule
    rule = {
        "id": "RULE-V1",
        "logic": {
            "if": {"field": "score", "value": 70},
            "then": {"approved": True, "level": "A"},
            "else": {"approved": False, "level": "F"}
        }
    }

    # Example schema required fields
    schema = ["score", "attested"]

    # Example inputs (valid)
    inputs = {
        "score": 85,
        "attested": True
    }

    # Equal execution reference table
    reference_table = {}

    # Execute NOVAK
    result = novak_execute(
        rule=rule,
        inputs=inputs,
        schema=schema,
        reference_table=reference_table
    )

    # Pretty print the result
    print("\n=== NOVAK EXECUTION RESULT ===")
    print(json.dumps(result, indent=4))

