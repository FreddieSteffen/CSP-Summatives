#2.2.7 StanfordCommandGUI.py
#Note this will not run in the code editor and must be downloaded
import subprocess
import tkinter as tk
import tkinter.scrolledtext as tksc
from tkinter.filedialog import asksaveasfilename
from PIL import Image, ImageTk

#Runs the commands from the buttons the user clicks and the URL they type in
def do_command(command):
  global command_textbox, url_entry
  if command == "Save":
    mSave()

  #Gets rid of https://, http://, and www. from the user input
  user_input = url_entry.get().strip()
  for prefix in ("https://", "http://", "www."):
    while user_input.startswith(prefix):
      user_input = user_input[len(prefix):]
  user_input = user_input.rstrip("/")
  url_val = user_input if user_input != 0 else "::1"
  
  command_textbox.delete(1.0, tk.END)
  command_textbox.insert(tk.END, command + " working....\n")
  command_textbox.insert(tk.END, "If not fully loaded, please wait a few seconds\n")
  command_textbox.update()

  p = subprocess.Popen(command + ' ' + url_val, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)

  cmd_results, cmd_errors = p.communicate()
  command_textbox.insert(tk.END, cmd_results)
  command_textbox.insert(tk.END, cmd_errors)

  #Replaces whatevers in the teminal with the default trash text
  if command == "Trash":
    command_textbox.delete("1.0", tk.END)
    command_textbox.insert(tk.INSERT, "Terminal: This is where things you do will show up.")

def mSave():
  filename = asksaveasfilename(defaultextension='.txt',filetypes = (('Text files', '*.txt'),('Python files', '*.py *.pyw'),('All files', '*.*')))
  if filename is None:
    return
  file = open (filename, mode = 'w')
  text_to_save = command_textbox.get("1.0", tk.END)
  file.write(text_to_save)
  file.close()
    
#Clears what I have in the url text box whenever it's clicked
def clear_on_click(event):
  if url_entry.get() == startingTextURL:
    url_entry.delete(0, tk.END)

root = tk.Tk()
root.configure(bg="#8C1515")
root.title("Stanford Command GUI")
root.columnconfigure(0, weight=1)
root.rowconfigure(3, weight=1)

logo_img = ImageTk.PhotoImage(Image.open("Stanford.png").resize((85, 64)))
title_label = tk.Label(root, text="Stanford Command GUI", image=logo_img, compound="left", bg="#8C1515", fg="white", font=("Source Sans 3", 24, "bold"), padx=10)
title_label.grid(row=0, column=0, padx=10, pady=10)
title_label.image = logo_img

#Creates the frame with label for the text box
url_frame = tk.Frame(root, bg="#820000", pady=10)
url_frame.grid(row=1, column=0, sticky="ew")
url_frame.columnconfigure(0, weight=1)
startingTextURL = "Enter Website URL Here"
url_entry = tk.Entry(url_frame, bg="#FFFFFF", fg="#8C1515", font=("Source Sans 3", 14))
url_entry.insert(0, startingTextURL)
url_entry.bind("<Button-1>", clear_on_click)
url_entry.grid(row=0, column=0, padx=20, sticky="ew")

#Set up button to run the do_command function
button_frame = tk.Frame(root, bg="#820000")
button_frame.grid(row=2, column=0, pady=10)
ImageSize = (32, 32)
PingImage = ImageTk.PhotoImage(Image.open("Ping.png").resize(ImageSize))
NSLookupImage = ImageTk.PhotoImage(Image.open("NSLookup.png").resize(ImageSize))
GlobeImage = ImageTk.PhotoImage(Image.open("Globe.png").resize(ImageSize))
DigImage = ImageTk.PhotoImage(Image.open("Dig.png").resize(ImageSize))
SaveImage = ImageTk.PhotoImage(Image.open("Save.png").resize(ImageSize))
TrashImage = ImageTk.PhotoImage(Image.open("TrashBin.png").resize(ImageSize))

ping_btn = tk.Button(button_frame, image=PingImage, command=lambda:do_command("Ping -c 5"))
ping_btn.grid(row=2, column=1, padx=5)
nsLookup_btn = tk.Button(button_frame, image=NSLookupImage, command=lambda:do_command("NSLookup"))
nsLookup_btn.grid(row=2, column=2, padx=5)
traceRoute_btn = tk.Button(button_frame, image=GlobeImage, command=lambda:do_command("Traceroute -c 1"))
traceRoute_btn.grid(row=2, column=3, padx=5)
Dig_btn = tk.Button(button_frame, image=DigImage, command=lambda:do_command("Dig"))
Dig_btn.grid(row=2, column=4, padx=5)
save_btn = tk.Button(button_frame, image=SaveImage, command=lambda:do_command("Save"))
save_btn.grid(row=2, column=5, padx=5)
trash_btn = tk.Button(button_frame, image=TrashImage, command=lambda:do_command("Trash"))
trash_btn.grid(row=2, column=6, padx=5)

#Adds an output box to GUI.
output_frame = tk.Frame(root, bg="#820000")
output_frame.grid(row=3, column=0, sticky="nsew", padx=10, pady=10)
output_frame.rowconfigure(0, weight=1)
output_frame.columnconfigure(0, weight=1)
command_textbox = tksc.ScrolledText(output_frame, bg="#FFFFFF", fg="#8C1515", font=("Source Sans 3", 14), height=10, width=100)
command_textbox.grid(row=0, column=0, sticky="nsew")
command_textbox.insert(tk.END, "Terminal: This is where things you do will show up.")

root.mainloop()