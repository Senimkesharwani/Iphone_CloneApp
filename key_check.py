from cryptography.hazmat.primitives.asymmetric import ed25519
from cryptography.hazmat.primitives import serialization
import base64

public_key_b64 = "lGNSPxkxQPUjdzIsge5N0Kgu/opPKbnoY7MF4GML3yE="
private_key_b64 = "kKczooIS7a96ye9QGr4/e6ymPlOAOcRDjNl51+92UkmUY1I/GTFA9SN3MiyB7k3QqC7+ik8puehjswXgYwvfIQ=="

public_key_bytes = base64.b64decode(public_key_b64)
private_key_bytes = base64.b64decode(private_key_b64)

private_key = ed25519.Ed25519PrivateKey.from_private_bytes(private_key_bytes[:32])
derived_public_key = private_key.public_key().public_bytes(
    encoding=serialization.Encoding.Raw,
    format=serialization.PublicFormat.Raw
)

if derived_public_key == public_key_bytes:
    print("✅ Public and private keys match!")
else:
    print("❌ Keys do not match.")
