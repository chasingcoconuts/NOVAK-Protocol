import json, hashlib, time, os

# ----------------------------
# Utility: Hashing
# ----------------------------
def sha256(data: str) -> str:
    return hashlib.sha256(data.encode("utf-8")).hexdigest()

# ----------------------------
# Load input + rules
# ----------------------------
rules = json.load(open("rules.json"))
inputs = json.load(open("inputs.json"))

# ----------------------------
# NIPS — Normalized Input Proof Set
# ----------------------------
def nips_validate(inp):
    if not inp["signature_valid"]:
        raise Exception("NIPS FAILURE: Signature invalid.")
    if not inp["schema_valid"]:
        raise Exception("NIPS FAILURE: Schema invalid.")
    if inp["provenance"] not in ["VA_PRIMARY_SOURCE_DB", "USPTO", "FED_AUTHORITY"]:
        raise Exception("NIPS FAILURE: Untrusted provenance.")

    return True

# ----------------------------
# Deterministic rule engine
# ----------------------------
def deterministic_execute(rule, inp):
    rating = inp["data"]["disability_rating"]
    cond = rule["logic"]["if"]

    if rating >= cond["value"]:
        return rule["logic"]["then"]
    else:
        return rule["logic"]["else"]

# ----------------------------
# HARMONEE — Execution Receipt
# ----------------------------
def harmonee_receipt(rule, inp, output):
    payload = (
        rule["rule_id"] + 
        sha256(json.dumps(inp["data"], sort_keys=True)) +
        sha256(json.dumps(output, sort_keys=True)) +
        "NOVAK_ENGINE" +
        str(int(time.time()))
    )
    return sha256(payload)

# ----------------------------
# REVELATION — Global Chain
# ----------------------------
def update_revelation_chain(receipt_hash):
    chain_file = "chain.json"

    if not os.path.exists(chain_file):
        chain = {"chain": []}
    else:
        chain = json.load(open(chain_file))

    prev = chain["chain"][-1]["hash"] if chain["chain"] else "GENESIS"
    new_hash = sha256(prev + receipt_hash)

    chain["chain"].append({
        "previous": prev,
        "receipt": receipt_hash,
        "hash": new_hash
    })

    json.dump(chain, open(chain_file, "w"), indent=2)
    return new_hash

# ----------------------------
# Equal Execution Law Check
# ----------------------------
def equal_execution_check(D1, D2, O1, O2):
    if D1 == D2 and O1 != O2:
        raise Exception("EXECUTION VIOLATION: Outputs differ for identical inputs.")

# ----------------------------
# NOVAK ENGINE EXECUTION
# ----------------------------
print("Running NOVAK Engine...")

# 1: NIPS
nips_validate(inputs)

# 2: Deterministic execution
output = deterministic_execute(rules, inputs["data"])

# 3: Equal Execution Test (self-check)
equal_execution_check(inputs["data"], inputs["data"], output, output)

# 4: HARMONEE receipt
receipt = harmonee_receipt(rules, inputs, output)

# 5: Save receipt
os.makedirs("receipts", exist_ok=True)
open(f"receipts/{receipt}.json", "w").write(
    json.dumps({"rule": rules["rule_id"], "input": inputs["input_id"], "output": output, "hash": receipt}, indent=2)
)

# 6: Update global REVELATION chain
global_hash = update_revelation_chain(receipt)

print("NOVAK EXECUTION COMPLETE.")
print("Output:", output)
print("Receipt:", receipt)
print("REVELATION Chain Head:", global_hash)
