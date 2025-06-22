import os
import base64
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.fernet import Fernet

def generate_key_from_password(password: str, salt: bytes):
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=390000,
    )
    return base64.urlsafe_b64encode(kdf.derive(password.encode()))

def create_salt():
    salt = os.urandom(16)
    with open("vault.salt", "wb") as f:
        f.write(salt)
    return salt

def load_salt():
    with open("vault.salt", "rb") as f:
        return f.read()

def encrypt_file(file_path, password):
    salt = create_salt()
    key = generate_key_from_password(password, salt)
    f = Fernet(key)
    with open(file_path, "rb") as file:
        encrypted_data = f.encrypt(file.read())
    with open(file_path + ".vault", "wb") as file:
        file.write(encrypted_data)

def decrypt_file(file_path, password):
    salt = load_salt()
    key = generate_key_from_password(password, salt)
    f = Fernet(key)
    with open(file_path, "rb") as file:
        decrypted_data = f.decrypt(file.read())
    original_path = file_path.replace(".vault", "")
    with open(original_path, "wb") as file:
        file.write(decrypted_data)
