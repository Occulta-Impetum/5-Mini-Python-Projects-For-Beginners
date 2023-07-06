import base64
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC

# Global Variables
PWD_FILE_NAME = "passwords.txt"
SALT_FILE_NAME = "salt.key"


#Functions

def load_key():
    master_pwd = input("What is the master password? ")
    
    try:
        file = open(SALT_FILE_NAME, "rb")
        salt = file.read()
        file.close()
    except:
        salt = Fernet.generate_key()
        with open(SALT_FILE_NAME, "wb") as f:
            f.write(salt)
    
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=480000,
    )
    key = base64.urlsafe_b64encode(kdf.derive(master_pwd.encode()))
    
    return key

def check_master(fer):
    try:
        with open(PWD_FILE_NAME, "rb") as f:
            for line in f.readlines():
                try:
                    encrypted_data = line.rstrip()
                    fer.decrypt(encrypted_data)
                except: #not sure how to check specifically that it is the wrong key error
                    print("Wrong master password.")
                    quit()
                break # I break here because I only need to check the first line
    except FileNotFoundError: #there are no passwords saved yet so there is no need to check the master password
        return

def view(fer):
    with open(PWD_FILE_NAME, "r") as f:
        print("")
        for line in f.readlines():
            encrypted_data = line.rstrip() #rstrip pull off the \n that we added to store the data cleaner
            data = fer.decrypt(encrypted_data.encode()).decode()
            user, pwd = data.split("|")
            print(f"User Name: {user}")
            print(f"Password: {pwd}\n")         

def add(fer):
    name = input("User Name: ")
    pwd = input("Password: ")
    
    data = name + "|" + pwd
    
    with open(PWD_FILE_NAME, "a") as f:
        f.write(fer.encrypt(data.encode()).decode() + "\n") #.encode() changes to bytes for encryption || .decode() changes back to string

#Main Script
def main():
    key = load_key()
    
    fer = Fernet(key)
    
    check_master(fer)
    
    while True:
        mode = input("Would you like to add a new password or view existing passowrds? (add/view/q to quit) ")
        
        if mode == "view":
            view(fer)
        elif mode == "add":
            add(fer)
        elif mode == "q":
            quit()
        else:
            print("Invalid mode.")
            continue

#Allows calling functions from other scripts wihtout running code
if __name__ == "__main__":
    main()

#Sample of pulling in arguments from the command line if needed
""" if __name__ == "__main__":
    args = sys.argv
    if len(args) != 3:
        raise Exception("You must pass a source and target directory - only.")
    
    source, target = args[1:]
    main(source, target) """