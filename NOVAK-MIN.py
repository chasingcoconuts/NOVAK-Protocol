import hashlib
import json
import time

# ============================================================
#  NOVAK-MIN REFERENCE IMPLEMENTATION
#  Novak Objective Verification of Autonomous Knowledge
#  Minimal standalone test implementation
# ============================================================

def sha256(data: str) -> str:
    return hashlib.sha256(data.encode("utf-8")).hexdigest()

# ------------------------------------------------------------
#  NIPS — Normalized Input Proof Set
# ------------------------------------------------------------

def nips_validate(input_dict: dict) -> bool:
    """NIPS: Verify input schema + signature fields exist."""
    required_fields = ["data", "signature", "provenance"]
    return all(f in input_dict for f in required_fields)

# ------------------------------------------------------------
#  HARMONEE — Execution Receipt
# ------------------------------------------------------------

def harmonee_receipt(rule_hash, data_hash, output_hash, actor="SYSTEM"):
    timestamp = str(time.time())
    payload = f"{rule_hash}|{data_hash}|{output_hash}|{actor}|{timestamp}"
    return sha256(payload)

# ------------------------------------------------------------
#  REVELATION — Recursive Global Chain
# ------------------------------------------------------------

revelation_chain = ["GENESIS"]

def revelation_append(receipt_hash):
    global revelation_chain
    new_hash = sha256(revelation_chain[-1] + receipt_hash)
    revelation_chain.append(new_hash)
    return new_hash

# ------------------------------------------------------------
#  NOVAK Equal Execution Law
# ------------------------------------------------------------

def novak_equal_outputs(output1, output2):
    """If inputs are equal but outputs differ — violation"""
    return sha256(output1) == sha256(output2)

# ------------------------------------------------------------
#  TEST HARNESS
# ------------------------------------------------------------

if __name__ == "__main__":

    rule = "IF veteran=true THEN approve"
    rule_hash = sha256(rule)

    request = {
        "data": {"veteran": True},
        "signature": "VALID",
        "provenance": "VA_SOURCE"
    }

    assert nips_validate(request), "❌ NIPS FAILED"

    data_hash = sha256(json.dumps(request))
    output = "APPROVED"
    output_hash = sha256(output)

    receipt = harmonee_receipt(rule_hash, data_hash, output_hash)
    rev = revelation_append(receipt)

    print("\n=== NOVAK-MIN TEST COMPLETE ===")
    print("Receipt:", receipt)
    print("Chain:", rev)
