import random
import tkinter as tk
from tkinter import messagebox

def generate_password():
    low = "abcdefghijklmnopqrstuvwxyz"
    upp = "ABCDEFGHIJKLMNOPQRSTUVWXZ"
    num = "0123456789"
    sym ="!@#$%^&*"

    all_chars = low + upp + num +sym
    password = random.choice(low) + random.choice(upp) + random.choice(num) +random.choice(sym)
    length=12
    remaining_chars = random.sample(all_chars, length - 4)
    password += "".join(remaining_chars)

    password_entry.delete(0, tk.END)
    password_entry.insert(tk.END,password)

def copy_password():
    password = password_entry.get()
    if password:
        root.clipboard_clear()
        root.clipboard_append(password)
        root.update()
        messagebox.showinfo("Password copied", "password has been copied to clipboard. ")

    else:
        messagebox.showinfo("No password", "No password generated. ")  

root = tk.Tk()
root.title("Password Generator")


#password label and entry 
password_label = tk.Label(root , text="Generated Password : ")
password_label.pack()

password_entry =tk.Entry(root , width=30)
password_entry.pack()

#buttons
generate_button =tk.Button(root, text="Generate Password", command=generate_password)
generate_button.pack(pady=10)

copy_button=tk.Button(root,text="Copy Password",command=copy_password)
copy_button.pack(pady=10)

root.mainloop()
