import argparse
from cryptography.fernet import Fernet

def load_key():
    try:
        with open ("encryption_key.key", "rb") as key_file:
            key =  key_file.read()
            return key
    except FileNotFoundError:
         print ("The file encryption_key.key was not found")
         return None 
        

def encrypt_file(filename):
    key = load_key()
    if key is None:
        print("Encryption aborted. No key found.")
        return
    
    fernet = Fernet(key)
    try:
        with open (filename, "rb") as file:
            file_data = file.read()

        encrypted_data = fernet.encrypt(file_data)

        with open (filename + ".encrypted", "wb") as file:
            file.write(encrypted_data)

        print (f"Your file has been encrypted and saved as {filename}.encrypted")
    except FileNotFoundError:
        print(f" The file '{filename}' was not found.")


def decrypt_file(filename):
    key = load_key()
    if key is None:
        print("Decryption aborted. No key found.")
        return
    
    fernet = Fernet(key)
    try:
        with open (filename, "rb") as file:
            encrpted_data = file.read()

        decrypted_data = fernet.decrypt(encrpted_data)

        with open (filename.replace(".encrypted", "") + ".decrypted", "wb") as file:
            file.write(decrypted_data)

        print(f"Your file was decrypted and saved as {filename}.decrypted")
    except FileNotFoundError:
        print(f" The file '{filename}' was not found.")




if __name__ == "__main__":

    parser = argparse.ArgumentParser(description = "Encryption tool")
    parser.add_argument("action", choices= ["encrypt", "decrypt"], help = "Select your choice bewtweeb encrypt or decrypt")
    parser.add_argument("filename", help= "Enter the file name you want to work with")

    args = parser.parse_args()

    if args.action =="encrypt":
        encrypt_file(args.filename)
    elif args.action =="decrypt":
        decrypt_file(args.filename)


