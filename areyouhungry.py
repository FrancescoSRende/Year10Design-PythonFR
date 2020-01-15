import tkinter as tk
from tkinter import ttk


def is_hungry():

	output.config(state = "normal")
	output.delete('1.0', END)
	output.insert(tk.INSERT, "You are hungry.\n")
	output.config(state = "disabled")

def is_not_hungry():

	output.config(state = "normal")
	output.delete('1.0', END)
	output.insert(tk.INSERT, "You are not hungry.\n")
	output.config(state = "disabled")

root = tk.Tk()
root.title("Hunger Detector")

title = tk.Label(root, text = "Are you hungry?")
title.config(font = ("Arrus BT", 20))
title.grid(row = 0, column = 0, columnspan = 2, sticky = "NESW")

yes_button = tk.Button(root, text="Yes", bg="red", command = is_hungry)
yes_button.grid(row = 1, column = 0, columnspan = 1, sticky = "NESW")

no_button = tk.Button(root, text="No", bg="red", command = is_not_hungry)
no_button.grid(row = 1, column = 1, columnspan = 1, sticky = "NESW")

output = tk.Text(root, width=20, height=10, borderwidth=1, relief=tk.GROOVE)
output.config(state="disabled", bg = "black", foreground="white", font=("Courier"))
output.grid(row = 2, column = 0, columnspan = 2, sticky = "NESW")

root.mainloop()