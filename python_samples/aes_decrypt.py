# from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
# from cryptography.hazmat.backends import default_backend
# import base64
# import binascii
# import json
# # Example values; replace with your actual key, IV, and encrypted data
# secret_key_hex = '0123456789abcdef0123456789abcdef'  # 24-byte key for AES-192
# iv_hex = 'bdebab5e90b87f9a88e264266f58193d'  # Initialization Vector (must be 16 bytes long)
# encrypted_data = 'k4EFwoiIrCs7UBKXGRKel3XbUm7iZmUjq3d8AstI0nY='  # Your Base64-encoded encrypted data

# # Decode Base64-encoded encrypted data
# ciphertext = base64.b64decode(encrypted_data)
# print(f"cipher text is {ciphertext}")
# # Convert hex key and IV to bytes
# secret_key = binascii.unhexlify(secret_key_hex)
# print("secrete key is ", secret_key)
# iv = binascii.unhexlify(iv_hex)
# print("iv is ", iv)
# # Ensure the key length is correct
# if len(secret_key) not in [16, 24, 32]:
#     raise ValueError("Invalid key size")

# # Create the AES cipher object
# cipher = Cipher(algorithms.AES(secret_key),
#                 modes.CBC(iv),
#                 backend=default_backend())

# print("cipher obejct is ", cipher)
# decryptor = cipher.decryptor()
# print("decrpytor is ", decryptor)
# # Decrypt the data
# decrypted_padded = decryptor.update(ciphertext) + decryptor.finalize()
# print("data decrypt is ", decrypted_padded)
# # Print decrypted data (assuming it was a UTF-8 string)
# print(decrypted_padded.decode('utf-8'))
# print(type(decrypted_padded.decode('utf-8')))
# decrypted_str = decrypted_padded.decode('utf-8').rstrip(
#     '\x01')  # Remove padding byte if needed
# print(f"cleaned decrypted string: {decrypted_str}")

# # Manually fix the malformed JSON string
# # Here, replace the erroneous character(s) and ensure valid JSON format
# fixed_json_string = decrypted_str.replace('|', '').replace("'", '"')

# print(f"fixed JSON string: {fixed_json_string} {type(fixed_json_string)}")

# # Parse JSON
# try:
#     json_data = json.loads(str(fixed_json_string))
#     print("Parsed JSON data:", json_data)
# except json.JSONDecodeError as e:
#     print(f"Error decoding JSON: {e}")

from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
import base64
import binascii
import json

# Example values; replace with your actual key, IV, and encrypted data
secret_key_hex = '0123456789abcdef0123456789abcdef'  # 24-byte key for AES-192
iv_hex = 'b160f187f1211308b3cb77acfd57d76c'  # Initialization Vector (must be 16 bytes long)
encrypted_data = '2/bXSi57xQoTxMbg9UUIXWjgInQ+rosYOGBlQ48doCqFszkpuez/8ohpraLAl2Do3tN6zku0Dx7STLK4KgWV8lv7Xi3hn2YiSpKzVTlf+YlcgnHuChKSWlyaGZl6ImMYg6lAIu11AKMb1/5LTHWVP9uzbSTC47sA1rDI/R0BbezqV1OOciU3bLlMIHR09IV33Hd/9uY+WYyQLD70TpFMvduWt+JYR1pyT41udg5/sAmMRCrr+cfJyIYU7GI0n24ysvf8LV0H5+ZoRvKjsmqLRm05Z+pydHuePLTk1RjrYTNAgzCZOQGUCsBTmfU8sATwI9nOOj58arQXGoUReVQB95XwJ+EjHjTjAopDKaNqYKcsLX+OgoCi2gy5dWbsmf0TVZHAipbBSMwbxx7/oiQIQw=='  # Your Base64-encoded encrypted data

# Decode Base64-encoded encrypted data
ciphertext = base64.b64decode(encrypted_data)
print(f"cipher text is {ciphertext}")

# Convert hex key and IV to bytes
secret_key = binascii.unhexlify(secret_key_hex)
print("secrete key is ", secret_key)
iv = binascii.unhexlify(iv_hex)
print("iv is ", iv)

# Ensure the key length is correct
if len(secret_key) not in [16, 24, 32]:
    raise ValueError("Invalid key size")

# Create the AES cipher object
cipher = Cipher(algorithms.AES(secret_key),
                modes.CBC(iv),
                backend=default_backend())

print("cipher obejct is ", cipher)
decryptor = cipher.decryptor()
print("decrpytor is ", decryptor)

# Decrypt the data
decrypted_padded = decryptor.update(ciphertext) + decryptor.finalize()
print("data decrypt is ", decrypted_padded)

# Remove PKCS#7 padding
padding_length = decrypted_padded[-1]
if padding_length > 0 and padding_length <= 16:
    decrypted_padded = decrypted_padded[:-padding_length]

# Print decrypted data (assuming it was a UTF-8 string)
decrypted_str = decrypted_padded.decode('utf-8')
print(f"decrypted string: {decrypted_str}")

# Manually fix the malformed JSON string
# Here, replace the erroneous character(s) and ensure valid JSON format
fixed_json_string = decrypted_str.replace('|', '').replace("'", '"')

print(f"fixed JSON string: {fixed_json_string} {type(fixed_json_string)}")

# Parse JSON
try:
    json_data = json.loads(fixed_json_string)
    print("Parsed JSON data:", json_data)
except json.JSONDecodeError as e:
    print(f"Error decoding JSON: {e}")


