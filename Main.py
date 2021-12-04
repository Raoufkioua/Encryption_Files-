from Encryption_Decryption import encrypt,decrypt,getKey

# The choice can be E for encrypton  or Decrypt

def Runnig_Crypt_process(choice,filename,password):
    if choice == 'E' or choice == 'e':
        encrypt(getKey(password), filename)
        print("Done.")
   

        
