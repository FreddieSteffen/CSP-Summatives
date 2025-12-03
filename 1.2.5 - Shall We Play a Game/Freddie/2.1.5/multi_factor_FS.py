# a215_multi_factor.py
import tkinter as tk
import multifactorgui as mfg

# create a multi-factor interface to a restircted app
my_auth = mfg.MultiFactorAuth()

UsernameQuestion = input("What is your username (Must be less than 24 Characters)?")
PasswordQuestion = input("What is your password?")
if len(UsernameQuestion) <= 24 and len(PasswordQuestion) <= 24 and len(PasswordQuestion) >= 8 and len(UsernameQuestion) >= 8 and PasswordQuestion.isalpha() == False and PasswordQuestion.isdigit()== False:
  my_auth.set_authorization(UsernameQuestion,PasswordQuestion)

# confirm authorization info
auth_info = my_auth.get_authorization()
print(auth_info)

# set the users authentication information
question = "What is your favorite color?"
answer = "purple"
my_auth.set_authentication(question, answer)

# start the GUI
my_auth.mainloop()
