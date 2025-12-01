#2.1.4. SimpleWindowFS.py
#A program creates a window on your screen using Tkinter.
import tkinter as tk

def test_login_button():
  frame_auth.tkraise()
  password_value = ent_password.get()
  user_password = tk.Label(frame_auth, text=str(password_value), font="Times")
  user_password.pack()
  color_grid = tk.Frame(frame_auth)
  color_grid.pack(pady=10)

  red = tk.Frame(color_grid, bg="red",    width=80, height=80)
  blue = tk.Frame(color_grid, bg="blue",   width=80, height=80)
  green = tk.Frame(color_grid, bg="green",  width=80, height=80)
  yellow = tk.Frame(color_grid, bg="yellow", width=80, height=80)
  red.grid(row=0, column=0)
  blue.grid(row=0, column=1)
  green.grid(row=1, column=0)
  yellow.grid(row=1, column=1)

# Main Window
root = tk.Tk()
root.wm_geometry("200x300")
root.wm_title("Authorization")

root.rowconfigure(0, weight=1)
root.columnconfigure(0, weight=1)

frame_auth = tk.Frame(root)
frame_auth.grid(row=0, column=0, sticky="nsew")

password_label = tk.Label(frame_auth, text="Password:", font="Times")
password_label.pack()

frame_login = tk.Frame(root)
frame_login.grid(row=0, column=0, sticky="nsew")

lbl_username = tk.Label(frame_login, text='Username:', font="Times")
lbl_username.pack()
ent_username = tk.Entry(frame_login, bd=3)
ent_username.pack(pady=5)

lbl_password = tk.Label(frame_login, text="Password:", font="Times")
lbl_password.pack()
ent_password = tk.Entry(frame_login, bd=3)
ent_password.pack(pady=5)

login_button = tk.Button(frame_login, text="Login", command=test_login_button)
login_button.pack(pady=5)

frame_login.tkraise()
root.mainloop()