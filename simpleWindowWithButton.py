#   a226_simple_window_with_button.py
#   A program creates a window on your screen using Tkinter.
import tkinter as tk
import tkinter.scrolledtext as tksc

#functions
def test_my_button():
    user_pass = ent_password.get()
    lbl_display.config(text=user_pass)
    frame_auth.tkraise()

# main window
root = tk.Tk()
root.title('Authorization')
root.wm_geometry("500x350")

# create empty frame
frame_login = tk.Frame(root, bg='azure2')
frame_login.grid(row=0, column=0, sticky='news')

frame_auth = tk.Frame(root, bg='plum4')
frame_auth.grid(row=0, column=0, sticky='news')

lbl_username = tk.Label(frame_login,text='Username:', bg='azure2')
lbl_username.pack(pady=5)

ent_username = tk.Entry(frame_login, bd=3)
ent_username.pack(pady=5)

lbl_password = tk.Label(frame_login,text='Password:', font='Arial', bg='azure2')
lbl_password.pack(padx=5)

ent_password = tk.Entry(frame_login, bd=3, show='*')
ent_password.pack(pady=5)

bt_image = tk.PhotoImage(file="Button.gif")#https://maitaicharters.com/home/click-here-red-button0/
bt_image = bt_image.subsample(10,10)

btn_login = tk.Button(frame_login, text='Login', command=test_my_button, bg='azure2', image=bt_image)
btn_login.pack(padx=175, pady=20)

# TODO: Add a label to frame_auth
lbl_display = tk.Label(frame_auth,text='Password:', font='Arial')
lbl_display.pack(padx=5)

frame_login.tkraise()
test_textbox = tksc.ScrolledText(frame_auth)
test_textbox.configure(height=10, width=50, state='disabled')
test_textbox.pack(pady=10)
startingText = "Starting text here"
test_textbox.insert(tk.INSERT, startingText)
root.mainloop()
