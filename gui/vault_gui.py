import tkinter as tk
from tkinter import simpledialog, filedialog, messagebox
from encryption.crypto import encrypt_file, decrypt_file
import os

def ask_password():
    return simpledialog.askstring("Password", "Enter encryption password/PIN:", show='*')

def encrypt_action():
    file_path = filedialog.askopenfilename()
    if file_path:
        password = ask_password()
        if password:
            encrypt_file(file_path, password)
            messagebox.showinfo("Success", f"Encrypted: {file_path}.vault")

def decrypt_action():
    file_path = filedialog.askopenfilename(filetypes=[("Vault Files", "*.vault")])
    if file_path:
        if not os.path.exists("vault.salt"):
            messagebox.showerror("Error", "Missing salt file. Cannot decrypt.")
            return
        password = ask_password()
        if password:
            try:
                from encryption.crypto import generate_key_from_password, load_salt
                from cryptography.fernet import Fernet

                salt = load_salt()
                key = generate_key_from_password(password, salt)
                f = Fernet(key)
                with open(file_path, "rb") as file:
                    decrypted_data = f.decrypt(file.read())

                original_filename = os.path.basename(file_path).replace(".vault", "")
                filename, ext = os.path.splitext(original_filename)
                suggested_name = f"{filename}_decrypted{ext}"
                save_path = filedialog.asksaveasfilename(initialfile=suggested_name, title="Save Decrypted File As")

                if save_path:
                    with open(save_path, "wb") as file:
                        file.write(decrypted_data)
                    messagebox.showinfo("Success", f"Decrypted and saved:\n{save_path}")
                else:
                    messagebox.showinfo("Cancelled", "Save cancelled.")
            except Exception as e:
                messagebox.showerror("Error", f"Decryption failed:\n{str(e)}")


def launch_app():
    root = tk.Tk()
    root.title("Vault - Password Protected")
    root.geometry("300x200")
    root.resizable(False, False)

    tk.Label(root, text="Vault", font=("Helvetica", 18, "bold")).pack(pady=10)
    tk.Button(root, text="Encrypt File", width=20, command=encrypt_action).pack(pady=10)
    tk.Button(root, text="Decrypt File", width=20, command=decrypt_action).pack(pady=10)

    root.mainloop()
