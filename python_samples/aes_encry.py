import json
import os
import base64
import binascii
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend


async def payload_encryption(request_body):
    #yte key for AES-192
    secret_key_hex = "0123456789abcdef0123456789abcdef"
    iv = os.urandom(16)

    # Convert the data to JSON and encode as a UTF-8 byte string
    json_data = json.dumps(request_body).encode('utf-8')

    # Add PKCS#7 padding
    padding_length = 16 - (len(json_data) % 16)
    padded_data = json_data + bytes([padding_length] * padding_length)

    # Convert hex key to bytes
    secret_key = binascii.unhexlify(secret_key_hex)

    # Create the AES cipher object
    cipher = Cipher(algorithms.AES(secret_key),
                    modes.CBC(iv),
                    backend=default_backend())
    encryptor = cipher.encryptor()

    # Encrypt the data
    encrypted_padded = encryptor.update(padded_data) + encryptor.finalize()

    # Encode to Base64 for transmission/storage
    encrypted_base64 = base64.b64encode(encrypted_padded).decode('utf-8')
    return encrypted_base64, binascii.hexlify(iv).decode('utf-8')


# Example usage
request_body =  {'accountNumber': 9450000001, 'subAccountType': '103090369', 'routingNumber': '107001481', 'regionId': '9'}


async def main():
    encrypted_payload, iv_hex = await payload_encryption(request_body)
    request_body_out = {"payload": encrypted_payload, "iv": iv_hex}
    req_body = json.dumps(request_body_out)
    print("Request Body:", request_body_out, "\t orginal request body ",
          request_body, "th", req_body, "tye is ", type(req_body))


# Run the main function if using asyncio
import asyncio

asyncio.run(main())
