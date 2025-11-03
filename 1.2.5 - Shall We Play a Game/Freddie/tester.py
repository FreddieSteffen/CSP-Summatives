import tkinter as tk
from tkinter import messagebox

def on_yes():
    messagebox.showinfo("Response", "You clicked YES!")
    root.destroy()  #closes window

def on_no():
    messagebox.showinfo("Response", "You clicked NO!")
    root.destroy()  #closes window

root = tk.Tk()
root.title("Yes or No")

label = tk.Label(root, text="Do you want to continue?")
label.pack(pady=10)

yes_button = tk.Button(root, text="Yes", width=10, command=on_yes)
yes_button.pack(side="left", padx=20, pady=10)

no_button = tk.Button(root, text="No", width=10, command=on_no)
no_button.pack(side="right", padx=20, pady=10)

root.mainloop()