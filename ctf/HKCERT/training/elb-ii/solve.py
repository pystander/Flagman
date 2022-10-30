import os, base64, hashlib

while True:
    password = os.urandom(8).hex()

    # SHA-1 hash
    h = base64.b64encode(hashlib.sha1(password.encode()).digest())  

    if len(set(h) & set(b'0123456789')) == 0:
        break

print(password)