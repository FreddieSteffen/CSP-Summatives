#   a212_rsa_decrypt.py
import rsa as rsa

key = int(input("Enter the Decryption Key (Your private key):"))
mod_value = int(input("Enter the Modulus:"))

#encrypted_msg = input("What message would you like to decrypt (No brackets):")
temp = input("What message would you like to decrypt (No brackets):")
while ("[" in temp or "]" in temp):
  temp = input("What message would you like to decrypt REMEMBER NO BRACKETS:")
encrypted_msg = temp

#break apart the list that is cut/copied over on ", "
msg = encrypted_msg.split(", ")
print (rsa.decrypt(key,mod_value , msg))
