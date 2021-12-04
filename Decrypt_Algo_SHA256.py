from Encryption_Decryption import decrypt,getKey

filename ="C:\\Users\\Raouf\\Desktop\\Signature\\Encrypted_New_Employee_Guide_Accueil_Rappel_N9_Preconisations_Annexes_21K01.pdf"
password = "To_Test"
decrypt(getKey(password), filename)
print("Done.")