# p227_starter_one_button_shell.py
# Note this will not run in the code editor and must be downloaded

import subprocess
import tkinter as tk
import tkinter.scrolledtext as tksc
from tkinter import filedialog
from tkinter.filedialog import asksaveasfilename

def do_command(command):
    global command_textbox, url_entry

    # If url_entry is blank, use localhost IP address 
    url_val = url_entry.get()
    if (len(url_val) == 0):
        # url_val = "127.0.0.1"
        url_val = "::1"
    
    command_textbox.delete(1.0, tk.END)
    command_textbox.insert(tk.END, command + " working....\n")
    command_textbox.update()

    p = subprocess.Popen(command + ' ' + url_val, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)

    cmd_results, cmd_errors = p.communicate()
    command_textbox.insert(tk.END, cmd_results)
    command_textbox.insert(tk.END, cmd_errors)

def clear_on_click(event):
  if url_entry.get() == startingTextURL:
      url_entry.delete(0, tk.END)

root = tk.Tk()
frame = tk.Frame(root)
frame.pack()

# creates the frame with label for the text box
frame_URL = tk.Frame(root, pady=10,  bg="black") # change frame color
frame_URL.pack()

url_entry= tk.Entry(frame_URL, font=("comic sans", 14)) # change font
startingTextURL = "Enter Website URL Here"
url_entry.insert(tk.INSERT, startingTextURL)
url_entry.bind("<Button-1>", clear_on_click)
url_entry.pack(side=tk.LEFT)
url_entry.pack(side=tk.LEFT)
frame = tk.Frame(root,  bg="black") # change frame color
frame.pack()

# set up button to run the do_command function
ping_btn = tk.Button(frame, text="Ping URL", command=lambda:do_command("ping -c 10"))
ping_btn.pack()
nsLookup_btn = tk.Button(frame, text="NSLookup", command=lambda:do_command("NSLookup"))
nsLookup_btn.pack()
traceRoute_btn = tk.Button(frame, text="Trace Route", command=lambda:do_command("Trace Route"))
traceRoute_btn.pack()

# Adds an output box to GUI.
command_textbox = tksc.ScrolledText(frame, height=10, width=100)
command_textbox.pack(side=tk.LEFT)
startingTextTerminal = "Terminal: This is where things you do will show up."
command_textbox.insert(tk.INSERT, startingTextTerminal)

root.mainloop()
