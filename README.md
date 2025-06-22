# 🔐 Vault - File & Image Encryption Tool

Vault is a user-friendly Python application that allows you to encrypt and decrypt any file (documents, images, etc.) with a password or PIN using a secure GUI. It uses industry-standard cryptography and supports password-based key derivation for added security.

![Vault Banner](https://img.shields.io/badge/Built%20With-Python%203-blue?style=flat&logo=python)
![License](https://img.shields.io/badge/License-MIT-green.svg)
![Status](https://img.shields.io/badge/Status-Stable-brightgreen)

---

## 🚀 Features

- 🔒 Encrypt files securely with a password
- 🔓 Decrypt `.vault` files with the same password
- 🧠 Passwords are never stored — only derived keys are used
- 💾 Decrypted files saved as `filename_decrypted.ext`
- 🖼️ Works with images, PDFs, docs, and more
- 📦 Built with `cryptography` and `tkinter`
- 💻 Cross-platform (Windows, macOS, Linux)

---

## 🧰 Tech Stack

- Python 3.x
- Tkinter (GUI)
- cryptography (Fernet + PBKDF2HMAC)

---

## 📁 Folder Structure

Vault/
├── main.py
├── encryption/
│ └── crypto.py
├── gui/
│ └── vault_gui.py
├── requirements.txt
├── .gitignore
├── README.md
├── assets/
├── test_files/


---

## 🛠️ Installation

```bash
# Clone this repository
git clone https://github.com/SameerBiradar7/Vault.git
cd Vault

# (Optional) Create a virtual environment
python3 -m venv venv
source venv/bin/activate  # On Windows use: venv\\Scripts\\activate

# Install dependencies
pip install -r requirements.txt

# Run the application
python main.py


Future Enhancements
Encrypt entire folders

Add drag-and-drop support

Auto-delete decrypted files after a session

Biometric or hardware unlock options
