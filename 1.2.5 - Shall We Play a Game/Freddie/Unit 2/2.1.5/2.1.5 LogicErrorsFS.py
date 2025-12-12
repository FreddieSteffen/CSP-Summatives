##############################################################################
# a215_security_checklist.py
##############################################################################

print("Let's check your security. Answer y or n to each of the questions.")

phish = input("Can you recognize phishing emails? ")
pw = input("Is your passord strong? ")
auth = input("Do you use multi-factor authentication? ")
enc = input("Do you know how to encrypt sensitive information? ")

#Original not working
'''if (phish =='y'):
  if (pw =='y'):
    if (auth == 'y'):
      if (enc == "y"):
        print("You have good security habits.")
else:
  print("You can improve your security habits.")'''

#And Version
if (phish =='y' and pw =='y' and auth == 'y' and enc == 'y'):
  print("You have good security habits.")
else:
  print("You can improve your security habits.")

#Or Version
'''if (phish !='y' or pw !='y' or auth != 'y' or enc != 'y'):
  print("You can improve your security habits.")
else:
  print("You have good security habits.")'''
