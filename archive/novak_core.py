import json, hashlib, time, sys

def sha256(x: bytes) -> str:
    return hashlib.sha256(x).hexdigest()

def hash_json(obj) -> str:
    return sha256(json.dumps(obj, sort_keys=True).encode())

def nips_validate(data, schema):
    """Simulated NIPS check — in reality you’d validate sigs & provenance."""
    return set(data.keys()) <= set(schema["fields"])

def harmonee_receipt(rule_hash, data_hash, output_hash, actor="NOVAK-DEMO"):
    return {
        "rule": rule_hash,
        "data": data_hash,
        "output": output_hash,
        "actor": actor,
        "time": int(time.time()),
    }

def revelation_chain(prev_hash, receipt):
    return sha256((prev_hash + hash_json(receipt)).encode())

def execute(rule, data):
    """Deterministic execution-output simulation."""
    return {"approved": sum(data.values()) % 2 == 0}

if __name__ == "__main__":
    rule_file, data_file = sys.argv[1], sys.argv[2]

    rule = json.load(open(rule_file))
    data = json.load(open(data_file))

    rule_hash = hash_json(rule)
    data_hash = hash_json(data)

    if not nips_validate(data, rule):
        print("❌ NIPS REJECT — invalid schema")
        sys.exit(1)

    output = execute(rule, data)
    output_hash = hash_json(output)

    receipt = harmonee_receipt(rule_hash, data_hash, output_hash)
    chain_head = revelation_chain("GENESIS", receipt)

    print("✔ VALID EXECUTION")
    print("NOVAK_PROOF_HASH:", chain_head)
