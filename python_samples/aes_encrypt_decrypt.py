from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
import binascii
import base64
import json
import os


class AESEncryption:

    def __init__(self, key_hex, iv=None):
        self.secret_key = binascii.unhexlify(key_hex)
        self.iv = iv or os.urandom(16)  # Generate a random IV if not provided

    def encode_payload(self, data):
        # Convert the data to JSON and encode as a UTF-8 byte string
        json_data = json.dumps(data).replace('"', "'").encode('utf-8')

        # Add PKCS#7 padding
        padding_length = 16 - (len(json_data) % 16)
        padded_data = json_data + bytes([padding_length] * padding_length)

        # Create the AES cipher object
        print("secret", self.secret_key, "iv ", self.iv)
        cipher = Cipher(algorithms.AES(self.secret_key),
                        modes.CBC(self.iv),
                        backend=default_backend())
        encryptor = cipher.encryptor()

        # Encrypt the data
        encrypted_padded = encryptor.update(padded_data) + encryptor.finalize()

        # Encode to Base64 for transmission/storage
        encrypted_base64 = base64.b64encode(encrypted_padded).decode('utf-8')

        return {
            "payload": encrypted_base64,
            "iv": binascii.hexlify(self.iv).decode('utf-8')
        }


# Example usage
key_hex = "0123456789abcdef0123456789abcdef"  # 24-byte key for AES-192
aes_encryption = AESEncryption(key_hex)

# Example data to encrypt
data = {
    "type": "shakib",
    "request": {
        "account_number": "418056756",
        "account_type": "S",
        "primary_customer_ssn": "213719371",
        "customer_group_id": 3
    }
}

# encrypted_payload, iv_hex = aes_encryption.encode_payload(data)
iv_hex="a"
encrypted_payload= aes_encryption.encode_payload(data)
print(f"Encrypted Payload: {encrypted_payload} {type(encrypted_payload)=}")
print(f"IV (Hex): {iv_hex}")
