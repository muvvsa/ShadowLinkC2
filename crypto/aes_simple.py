from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
import base64 as ba

AES_KEY = b"Sixteen byte key"

def pad(data: bytes) -> bytes:
    padding = AES.block_size - len(data) % AES.block_size
    return data + bytes([padding] * padding)

def unpad(data: bytes) -> bytes:
    padding = data[-1]
    return data[:-padding]

def encrypt(plaintext: str) -> str:
    iv = get_random_bytes(16)
    cipher = AES.new(AES_KEY, AES.MODE_CBC, iv)
    padded = pad(plaintext.encode())
    encrypted = cipher.encrypt(padded)
    return ba.b64encode(iv + encrypted).decode()

def decrypt(ciphertext: str) -> str:
    raw = ba.b64decode(ciphertext)
    iv = raw[:16]
    encrypted = raw[16:]
    cipher = AES.new(AES_KEY, AES.MODE_CBC, iv)
    decrypted = cipher.decrypt(encrypted)
    return unpad(decrypted).decode()

if __name__ == "__main__":
    msg = "Test message to encrypt"
    enc = encrypt(msg)
    print(f"Encrypted: {enc}")
    dec = decrypt(enc)
    print(f"Decrypted: {dec}")