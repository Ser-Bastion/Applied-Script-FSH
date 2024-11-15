####ALPHA VERSION####
####OLD VERSION#######
#####CHECK LIVE VERSION###########


from cryptography.fernet import Fernet

print ("\\[T]/ Greetings fellow! Säg mig, vad vill du göra? ")
meny = int(input("*****************************\n[1]Skapa en Krypteringsnyckel \n[2]Ladda en Krypteringsnyckel \n[3]Kryptera en fil \n[4]Avkryptera en fil \n[0]Avsluta programmet :"))


while True:
  if meny == 0:
    print("*****************************\n\\[T]/ Hej då my fellow!")
    break

  elif meny == 1:
    key = Fernet.generate_key()
    with open("TrueKey.key", "wb") as key_file:
      key_file.write(key)
      print(f"Generated nyckel: {key.decode()}")
      print("*****************************\n\\[T]/ Nyckeln är skapad, min Herre! Vad vill du göra?")
      meny = int(input("*****************************\n[1]Skapa en Krypteringsnyckel \n[2]Ladda en Krypteringsnyckel \n[3]Kryptera en fil \n[4]Avkryptera en fil \n[0]Avsluta programmet :"))
      
  elif meny == 2:
    with open("TrueKey.key", "rb") as key_file:
     key = key_file.read()
     print(f"Nyckel laddad : {key.decode()}")
     print("*****************************\n\\[T]/ Nyckeln är Laddad, min Herre! Vad vill du göra?")
     
     cipher_suite = Fernet(key)
     print(cipher_suite)
     meny = int(input("*****************************\n[1]Skapa en Krypteringsnyckel \n[2]Ladda en Krypteringsnyckel \n[3]Kryptera en fil \n[4]Avkryptera en fil \n[0]Avsluta programmet :"))
     
         
  elif meny == 3: #Krypterar en fil
    message = "Praise the Sun! Detta var mitt hemliga meddelande.".encode()
    cipher_text = cipher_suite.encrypt(message)
    print(f"Krypterad text: {cipher_text}")

    with open("True_Secret.enc", "wb") as enc_file:
      enc_file.write(cipher_text)
      print("Krypterat meddelande har sparats som 'True_Secret.enc'")
      print("*****************************\n\\[T]/ Filen är krypterad, min Herre! Vad vill du göra?")
      meny = int(input("*****************************\n[1]Skapa en Krypteringsnyckel \n[2]Ladda en Krypteringsnyckel \n[3]Kryptera en fil \n[4] Avkryptera en fil \n[0] Avsluta programmet :"))
  
  elif meny == 4: #Avkrypterar en fil
    with open("True_Secret.enc", "rb") as enc_file:
     encrypted_message = enc_file.read()
     print(f"Läs in krypterad text från fil: {encrypted_message}")

    plain_text = cipher_suite.decrypt(encrypted_message)
    print(f"Dekrypterad text: {plain_text.decode()}")
    print("*****************************\n\\[T]/ Filen är AvKrypterad, min Herre! Vad vill du göra?")
    meny = int(input("*****************************\n[1]Skapa en Krypteringsnyckel \n[2]Ladda en Krypteringsnyckel \n[3]Kryptera en fil \n[4] Avkryptera en fil \n[0] Avsluta programmet :")) 
    
  else:
    print ("*****************************\n[T]/ Du har gett mig ett felaktigt kommando! Försök igen!")
    meny = int(input("*****************************\n[1]Skapa en Krypteringsnyckel \n[2]Ladda en Krypteringsnyckel \n[3]Kryptera en fil \n[4] Avkryptera en fil \n[0] Avsluta programmet :"))
    
        