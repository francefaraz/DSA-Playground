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
iv_hex = 'ddf9bddec7dbdd5fbee3209165e30278'  # Initialization Vector (must be 16 bytes long)
encrypted_data = 'RFqxhv9yJ08nD5yQ3ju7zl8xy7Gd/oCPDCbyJoHo1n7OhBpIoEfMZZYcS3XMlIE+DMgbkxJVnUySxs+/OSHdAN5T0AxwJmFPHjHUCWp9UHCjLwdVt/+436B4qlu4fuDbTWaJ73bo8AhjnFNX2hCNNg1SCSYj4uS1Y8TOiHuMQnva9yAhnNH1no2hb9XTXhWsA5J98gMfxJ6AwPlxx3FCLLIgDpWNX0Udozp/R2AoIyf6q/3ycMa3xrjrrjAMlDXulv2Lb5YoNDCplpR/fo4+NIPdLA1hDphhciSBWGA27lF0a8g+/zit9Qj9pgKtYQv17qJnDPvjC5xYXEY0JTGs8xVsq/WNZ1A1OIoPdXFwCNeELrhIaMWh9Ix5SzlF43375eKVO+/idEw1ZoRbs07XIDOZCGfj/c0riZCAg3mhHuTB2gn8xOx5zJnI3DTSb/jQqjGwDfxnDxJDTbOzEPwGqsEn/+YjUbPD3RGoi7ekfIXXqeo279l/B9J9N7gE+n3EUu9q5XxGPtrWVkfSwjiyHtffqRS4mRWi8UK0CgrB7jZthV2EAMaDyU6ntc9zJskNBhwhUnXIbe6RKrF2AZWq1w6y8AyHYlj+OSkwzS9bpVn0JES06hvIQISETVUpAKkxuuTy2sFi5LTn+x7aFzZmsalQcT64SOsoUS99S+XgxOg='  # Your Base64-encoded encrypted data

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




# {"payload":"RFqxhv9yJ08nD5yQ3ju7zl8xy7Gd/oCPDCbyJoHo1n7OhBpIoEfMZZYcS3XMlIE+DMgbkxJVnUySxs+/OSHdAN5T0AxwJmFPHjHUCWp9UHCjLwdVt/+436B4qlu4fuDbTWaJ73bo8AhjnFNX2hCNNg1SCSYj4uS1Y8TOiHuMQnva9yAhnNH1no2hb9XTXhWsA5J98gMfxJ6AwPlxx3FCLLIgDpWNX0Udozp/R2AoIyf6q/3ycMa3xrjrrjAMlDXulv2Lb5YoNDCplpR/fo4+NIPdLA1hDphhciSBWGA27lF0a8g+/zit9Qj9pgKtYQv17qJnDPvjC5xYXEY0JTGs8xVsq/WNZ1A1OIoPdXFwCNeELrhIaMWh9Ix5SzlF43375eKVO+/idEw1ZoRbs07XIDOZCGfj/c0riZCAg3mhHuTB2gn8xOx5zJnI3DTSb/jQqjGwDfxnDxJDTbOzEPwGqsEn/+YjUbPD3RGoi7ekfIXXqeo279l/B9J9N7gE+n3EUu9q5XxGPtrWVkfSwjiyHtffqRS4mRWi8UK0CgrB7jZthV2EAMaDyU6ntc9zJskNBhwhUnXIbe6RKrF2AZWq1w6y8AyHYlj+OSkwzS9bpVn0JES06hvIQISETVUpAKkxuuTy2sFi5LTn+x7aFzZmsalQcT64SOsoUS99S+XgxOg=","iv":"ddf9bddec7dbdd5fbee3209165e30278"}