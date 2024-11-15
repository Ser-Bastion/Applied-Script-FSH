# ╔════════════════════════════════════════════════════════════════════════════╗
# ║▀█████████▄     ▄████████    ▄████████     ███      ▄█   ▄██████▄  ███▄▄▄▄  ║    A program made my [Bastion]
# ║  ███    ███   ███    ███   ███    ███ ▀█████████▄ ███  ███    ███ ███▀▀▀██▄║    Designed to generate a key that allows the user to:
# ║  ███    ███   ███    ███   ███    █▀     ▀███▀▀██ ███▌ ███    ███ ███   ███║    -Encrypt a file
# ║ ▄███▄▄▄██▀    ███    ███   ███            ███   ▀ ███▌ ███    ███ ███   ███║    -Decrypt a file
# ║▀▀███▀▀▀██▄  ▀███████████ ▀███████████     ███     ███▌ ███    ███ ███   ███║    -How to use: 
# ║  ███    ██▄   ███    ███          ███     ███     ███  ███    ███ ███   ███║    - type "py Bastion_cry -a "[Choose Key, Lock or Unlock]
# ║  ███    ███   ███    ███    ▄█    ███     ███     ███  ███    ███ ███   ███║    - Type "py Bastion_cry -a -f "[Choose a file]"
# ║▄█████████▀    ███    █▀   ▄████████▀     ▄████▀   █▀    ▀██████▀   ▀█   █▀ ║    - Type "py Bastion_cry --help [For more detaljed descriptions]
# ╚════════════════════════════════════════════════════════════════════════════╝    
##########################################################################################################################################################

import argparse #Needed inorder to use terminal commands
from cryptography.fernet import Fernet #Required for encrypting, decrypting and generating key
import os #In order to prevent the user from overwriting an exisitng file without being asked if they wish to proceed aswell as troubleshooting
from cryptography.fernet import InvalidToken #Inorder to give an error message when user uses the wrong key to decrypt a file.


parser = argparse.ArgumentParser(description= "A program that creates a symmetric key that encrypts and decrypts file.")

#Function that generates a new key. Allows the user to name the key file. 
def new_key():
    while True:
      name = input("\\[T]/ Name your key my Lord :")
      if not name.endswith (".key"): #Checks if user added .key in their input, if not, adds .key.
          name += ".key"
#If the user creates a key with the same name as one that already exists, asks if they wish to overwrite it or exit.          
      if os.path.exists(name):
          overwrite = input (f"\\[T]/ My lord, a key named {name} already exist. Do you wish to overwrite it? [y/n]:")
          # if input is "y", overwrites the old key
          if overwrite == "y":
              break
          #If input is "n" stops the key creation command.
          elif overwrite == "n":
              print ("\\[T]/ As you wish my lord! Key creation is cancelled")
              return
          #if input is neither "y" or "n" begins the key creation from the start. 
          else:
              print ("\\[T]/ My lord! You gave me an invalid input! Alas, let us begin from the start.")
              
      else:
           break 
    
     
    key = Fernet.generate_key()
    with open(name, "wb") as key_file:
        key_file.write(key)
        print(f"**********\n\\[T]/ Your new key is created my lord!\\[T)/!\n********** {key.decode()}**********")
    
#Function that allows a user to choose a key to use when encrypting or decrypting a file.         
def load_key():
    name = input ("\\[T]/ My lord, Enter the name of your key :")
    #If the user did not write "".key" in input, adds ".key"
    if not name.endswith(".key"):
        name += ".key" 
    #If the key does not exist, gives an error message and ends the program.
    if not os.path.exists(name):
          print (f"\\[T]/ ERROR my lord! No key with the name {name} exist!")
          return None
    try:
          with open(name, "rb") as key_file:
            key = key_file.read()
    #If an error occurs: 
    except (FileNotFoundError, TypeError):
        print(f"\\[T]/ An ERROR has occured my lord! Please try again!")
            
    return key
            
#Function that encrypts a file of the users choosing. uses the function Load_key so that the user can choose which key to use.     
def encrypt_file():
    key = load_key()
    if key is None: #Ends the program if load_key function does not find a key
        return
    
    try:
        with open(args.file, "rb") as file_to_encrypt:
            file_data = file_to_encrypt.read()
        
        cipher_suite = Fernet(key)
        cipher_text = cipher_suite.encrypt(file_data)
    
    
        with open(args.file +".enc", "wb") as enc_file:
            enc_file.write(cipher_text)
        print(f"\\[T]/ Your file has been encrypted my lord \\[T]/! \n********** '{args.file}' **********")
        
    #If the file that the user wishes to encrypt does not exist
    except FileNotFoundError:
         print(f"\\[T]/ ERROR my lord! The file '{args.file}' does not exist.")
  
#Function that decrypts a file of the users choosing. uses the function Load_key so that the user can choose which key to use.   
def decrypt_file():
    key = load_key()
    if key is None: #Ends the program if the load_key functions does not work
        return
    
    if not args.file.endswith(".enc"): #If the user did not write .enc when inputing which file to decrypt, adds .".enc"
        args.file += ".enc"
    try:
        cipher_suite = Fernet(key)
        encrypted_file = args.file
        with open(encrypted_file, "rb") as enc_file:
            encrypted_message = enc_file.read()
            plain_text = cipher_suite.decrypt(encrypted_message)
        
            decrypted_file = encrypted_file.replace(".enc", "")
            with open (decrypted_file, "wb") as dec_file:
                dec_file.write(plain_text)
            print(f"\\[T]/ Your file has been decrypted my lord \\[T]/! \n********** '{args.file}'**********")
    #If the file that the user wishes to decrypt does not exist
    except FileNotFoundError:
        print(f"\\[T]/ ERROR my lord! The file '{args.file}' does not exist.")
    
    except InvalidToken:
        print(f"\\[T/ ERROR my lord! You've used the wrong key to decrypt the file! Please choose the right key and try again!]")
    

#Add options with both Higher and Lower letters to execute commands, which is why "lock" and "Lock" are both in choices. 
parser.add_argument( "-action", choices=["key", "Key", "lock","Lock","unlock", "Unlock"], help= "Use [Key] to generate a new key. Use [lock] to encrypt Use [unlock] to decrypt")
parser.add_argument("-file", "-f", help="Write which file you wish to encrypt or decrypt")


args = parser.parse_args()

if args.action == "key" or args.action == "Key":
    key = new_key()
    
elif args.action == "lock" or args.action == "Lock":
    encrypt = encrypt_file()
    
elif args.action == "unlock" or args.action =="Unlock":
    decrypt = decrypt_file()

#If the user simply runs the program :P    
else:
    print(f"\\[T]/ My lord! Thou has not giveth me a proper task to perform! Please choose 'key', 'lock', or 'unlock'. If thou requireth aid, simply ask...with -h or -help \\[T]/")