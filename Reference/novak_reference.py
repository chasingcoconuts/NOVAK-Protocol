import hashlib
import json
import time

# ----------------------------------------------
# NIPS — Normalized Input Proof Set
# ----------------------------------------------
def hash_data(data):
    return hashlib.sha256(json.dumps(data, sort_keys=True).encode()).hexdigest()

def nips_validate(data, schema):
    # 1) Schema match
    if set(data.keys()) != set(schema.keys()):
        return False, "SCHEMA MISMATCH"

    # 2) Fake signature check (placeholder)
    if "signature" not in data:
        return False, "NO SIGNATURE"

    # 3) Provenance (just hash check here)
    return True, hash_data(data)

# ----------------------------------------------
# HARMONEE — Execution Receipt
# ----------------------------------------------
def harmonee_receipt(rule_id, input_hash, output_hash, actor="system"):
    payload = f"{rule_id}|{input_hash}|{output_hash}|{actor}|{int(time.time())}"
    return hashlib.sha256(payload.encode()).hexdigest()

# ----------------------------------------------
# REVELATION — Global Checksum Chain
# ----------------------------------------------
class RevelationChain:
    def __init__(self):
        self.chain = []

    def add(self, receipt_hash):
        prev = self.chain[-1] if self.chain else "GENESIS"
        new_hash = hashlib.sha256(f"{prev}|{receipt_hash}".encode()).hexdigest()
        self.chain.append(new_hash)
        return new_hash

# ----------------------------------------------
# Deterministic Equal Execution Check
# ----------------------------------------------
def deterministic_check(rule, data1, data2):
    out1 = rule(data1)
    out2 = rule(data2)

    if data1 == data2 and out1 != out2:
        return False, "EXECUTION VIOLATION — NO JUSTIFICATION"

    return True, "VALID"

# ----------------------------------------------
# DEMO EXECUTION
# ----------------------------------------------
if __name__ == "__main__":

    schema = {"x": 0, "y": 0, "signature": ""}

    data = {"x": 2, "y": 3, "signature": "VALID"}
    ok, input_hash = nips_validate(data, schema)
    assert ok

    output = {"sum": data["x"] + data["y"]}
    output_hash = hash_data(output)

    receipt = harmonee_receipt("RULE_SUM", input_hash, output_hash)
    chain = RevelationChain()
    global_hash = chain.add(receipt)

    print("INPUT HASH:", input_hash)
    print("OUTPUT HASH:", output_hash)
    print("RECEIPT:", receipt)
    print("CHAIN HEAD:", global_hash)
    print("NOVAK PROOF COMPLETE ✅")
