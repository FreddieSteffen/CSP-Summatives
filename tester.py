import tkinter as tk
root = tk.Tk()
root.configure(bg="#8C1515")
root.title("Fredddie Steffen Create Task")
root.columnconfigure(0, weight=1)
root.rowconfigure(3, weight=1)

def on_enter(event):
  entry.grid_remove()

entry = tk.Entry(root, bg="#FFFFFF", fg="#8C1515", font=("Source Sans 3", 14))
StartingTextBet = "Enter Bet Here:"
entry.insert(0, StartingTextBet)
entry.bind("<Return>", on_enter)
entry.grid(row=1, column=0, padx=10, pady=10)

# --- Start the Tkinter event loop ---
root.mainloop()