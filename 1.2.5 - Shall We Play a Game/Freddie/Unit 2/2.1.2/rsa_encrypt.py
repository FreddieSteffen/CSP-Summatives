#   a212_rsa_encrypt.py
import rsa as rsa

#key = int(input("Enter the Encryption Key (Thier Public Key): " ))
temp = input("Enter the Encryption Key (Thier Public Key):")
while (not temp.isdigit()):
  temp = input("With only numbers, enter the Encryption Key (Thier Public Key):")
key = int(temp)

#mod_value = int(input("Enter the Modulus: " ))
temp = input("Enter the Modulus:")
while (not temp.isdigit()):
  temp = input("With only numbers enter the Modulus:")
mod_value = int(temp)

plaintext = input("Enter a message to encrypt:")
encrypted_msg = rsa.encrypt(key, mod_value, plaintext)
print("Encrypted Message: ", encrypted_msg)
