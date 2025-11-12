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
iv_hex = 'f81e785fec25732a36960b964eb527a5'  # Initialization Vector (must be 16 bytes long)
encrypted_data = '4XZ3xQ481qD00LvPHWDhWKP1WxL5ek7HeSbmryMjmOLr9J09MztcN/okfZcQZseVCFxZIORKXI0xiX2YzE0kLniL8KBVfKZ6ctEWj87mfg0Esu12cWu9NjICS7NgUZkuJ016CXa9Ef6aIa5jPtwzfnqe9WgPjmiIrGeszAo/AzKqS+KGctIgTs876waGgw2fyLAiSmQdgVD/4Duz5Ad3NB4T0ZPqsJzAbmwvi686jplLCeDvd+JgAr4hvHk4JEEjHbswLhNZoK+x2J8BdrGdtxi1yTucKSQqk9RS/kH/rP52sOCkjwI+Sv7OD8KYnori1L4LnlmLM2L6kyfwFGtvRh7BJHZ2Cj/98FfF2pMm3WFbDP7AaFJ+TLT1GCaqWKU3vDA2Fctnd6ofk/5K+i57NakCdim0+/azRJYciCD8wrsrOye7Po3fs5OGZmw7CTTag7+Dx30GcC4EUasIFvj8gA=='  # Your Base64-encoded encrypted data

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


# {"payload":"ciA0VifzoULO5qyTc/H/qM0luDNkXRw7PdyZfLWcHGO9akJipxxQLJLcUc8t7dPIDIy7FJhrNku6b3DH2ry3zGhnb0PfA/uC+WIPonpcqEhvkE1L+SXMXiblY5P+2F+6aGQu93hESH2dPd1CCJlWFfVrmnvvlIa8AoNmew6C9Vi7SIaGrOgoRTq0Tyc9DXNPK2F4lEWzUUpi2mHOnOFafOu0kp8QTkFqSPvI56/SX49jyJWlvJRKY3MeZyDWSCdtFlXL7+3vvcyWMZL9w4SclWcGuroS3KRuvrx8gqQZH1vAUDdG+rUl9UrOiPnmndbw01h8umcJzVyGmZtgCB8i1QlwecMCKjo7ufkHUSKTXryp0Xh78tTPf9LtzGwT3V0/gLH4Jb5+YfaW+6EXRPHcaLarQumZADGbs7fjT7+LzW/gj7T8B+QHYYLODn5uTZmapZV/gXOjcnvZHeLwv30uuH+m+/iYTW++hR3hx1RFvDUKkefr+xadkN6jKRQhNwWuaIn9ezmUhxcjHiELFSGcX/jBaytUdLH6bzOT+uRp37U=","iv":"cd42b0de00b48cb6d5e2f6222efc9f6f"}
#{"payload":"O1D6usSLVOQMLLd1ogS3XmfjONdBEi/DPyFvUvJ4eruVsh4sjqUWilSONAYOWwu7czZ8MW0nuEVRODAmjxzcc+V5+HVo46pWPm3+u0w8QN58HOYK86XQADRVX7hHSlYklg0xhYxDQ0Z74ERMslgNrZxaoinl8uXZLL44iiOoRxLXjVy/6qWBGvTs63PGUFmY5LB+c4FKXMoZMQkKahKz3Q/MafovlDwXOe3XfawykCriLpneBb9dIIpgcVJZMCw1NDi8S822OFzij2QY76hpmuMWOWZVJM12H8ZRJFzScRj34HDPsEe91GI5w0Eao45wjrQOvfGSFrGueUVLJsjSaXEyuL1Nqdpd/pqvjhLNKCrB3fStNPhuPOU+QaXuQHmO","iv":"d98cc5714b5ac92b79ac6f500e7741fb"}

# {"payload":"7WmPuPF0KZ7sA1X3nBc3ZHyqfsGb0lzxUxEczpxZgjkw3zKGdBHqOYQt1/WaznC0bxZSMxjIQ8+ej4YaXIMrTFdPBsixnb3G39A33Wfkrif6bhGTfXo0VEqURk0GATHawTPGyPjNwmZeWCanJR0uWqhmWCRtRK2dvzdwQRJT9NR1w4ISU0iHega/lEGLQu/Dzq+QPt/JHNBc7b7qHf1KLkjhXFn3QUuGj1JOO/QL+hSDvL9ANaY7IRXIS1tUsZkCsO1dY1pqXTrVd+mhKrw6Mpt3RbLDeBpngWYNgceDB2AM1hKv5VcSSbb0EWTBfTr+wOyLfSq8/NNEvFXvhKW5T9vUavrDy5am+2En4CXEqR41G1RjkZosvCJcZEvXgvKlkVPUGAaO6fh8/PyPXaWVDiWGdGc3TPqFf2Lkake2K42fBXlOuQXWwGlVbddIxqNWJZx6YacUz4VuwVOARJL3//eG2GhhzIS0W7O6lmo+UZeu1hZ+dMB3ez+qFVcPG6tu7QR0N+UzNbTpZGXyEFl/2+gAd5vDkvqthiAi3emwQZo=","iv":"53f3f86f42248c46e7da43c7308bf392"}


# {"payload":"NyH+TMqAh4Et7/Q5V7x1JqzcPy/0FZXUWTuuI4Mw5xU=","iv":"89b52fac9d8d6f5fd448782d9c7becb2"}

# {"payload":"P0tFQ4uU8PytDSEjTL/+6jX9sDZuPoJ0NqGy+PkKMUK8S6V7p89qo5sL6yS9gBjf2+qj9/CRfIJtd3LC/2x6np1xveMeU5raqOCbc5T9PcV8oAhDQvwQm0qZEWtdjenScnE2KNDetIw1bOEA8EAoMbcGmPMvBxYrokK858bMVgSMJ03zPongpl33lgnB6VPxYMP3b+q4wIHcw1Bp8qINbh6d4ydJmAfRf3ePvhY98yR0fxtBx8s0ZA9AaZ84xcw5p2DMjrujeKPeXqefsGRG/LdGTTpE5mjJC7zInOBW/gGwMzoems1ZPWDhnxgJPeZ5Te8j8GQz3JfiQoHpGVrfuMwJOLOUvzgdCJQGHkU3dLEtOrFP0ljOqAT4rzp6Rzl0qwIeMKZRKyps3F+6BmJj5IhzVB/4kTp1kWw1WHN3mQqjENLu7dQQP4PxZrFl1Sv2CRuH6fkVTVWZug4iDzRzzBUg4dpBcHTARyeyAozCtyDwWtVu0nwk9N2hDgpGJcBpxLINnQfZW7uj8kLoKykRBwtFfdgCwGAHn+zdUZuqj/U=","iv":"8091343bb24d4fa027b991bf66d4fea2"}

# {"payload":"4XZ3xQ481qD00LvPHWDhWKP1WxL5ek7HeSbmryMjmOLr9J09MztcN/okfZcQZseVCFxZIORKXI0xiX2YzE0kLniL8KBVfKZ6ctEWj87mfg0Esu12cWu9NjICS7NgUZkuJ016CXa9Ef6aIa5jPtwzfnqe9WgPjmiIrGeszAo/AzKqS+KGctIgTs876waGgw2fyLAiSmQdgVD/4Duz5Ad3NB4T0ZPqsJzAbmwvi686jplLCeDvd+JgAr4hvHk4JEEjHbswLhNZoK+x2J8BdrGdtxi1yTucKSQqk9RS/kH/rP52sOCkjwI+Sv7OD8KYnori1L4LnlmLM2L6kyfwFGtvRh7BJHZ2Cj/98FfF2pMm3WFbDP7AaFJ+TLT1GCaqWKU3vDA2Fctnd6ofk/5K+i57NakCdim0+/azRJYciCD8wrsrOye7Po3fs5OGZmw7CTTag7+Dx30GcC4EUasIFvj8gA==","iv":"f81e785fec25732a36960b964eb527a5"}