import { blake2bHex, blake2sHex } from "blakejs";

export async function digest(algo, input) {
  const data = new TextEncoder().encode(input);

  if (algo.startsWith("BLAKE")) {
    return algo === "BLAKE2B" ? blake2bHex(data) : blake2sHex(data);
  }

  const hash = await crypto.subtle.digest(algo, data);
  return [...new Uint8Array(hash)]
    .map(b => b.toString(16).padStart(2, "0"))
    .join("");
}

export async function hmac(algo, secret, message) {
  const key = await crypto.subtle.importKey(
    "raw",
    new TextEncoder().encode(secret),
    { name: "HMAC", hash: algo },
    false,
    ["sign"]
  );
  const sig = await crypto.subtle.sign(
    "HMAC",
    key,
    new TextEncoder().encode(message)
  );
  return [...new Uint8Array(sig)].map(b => b.toString(16).padStart(2, "0")).join("");
}
