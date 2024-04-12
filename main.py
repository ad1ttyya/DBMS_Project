import tkinter as tk
from tkinter import messagebox

from backend import *
curr = mydb.cursor()
curr.execute("use company_1;")
curr.execute("select * from USER_LOGIN_DATA")


def login():
    username = username_entry.get()
    password = password_entry.get()
    # Check if username and password are correct
    for i in curr:
        print(i[1],i[2])
        if username == i[1] and password == i[2]:
            messagebox.showinfo("Login Successful", "Welcome, Admin!")
                # messagebox.showinfo("Login Successful", "Welcome, Admin!")
    messagebox.showerror("Login Failed", "Invalid username or password")
			

# Create main window
root = tk.Tk()
root.title("Login Page")

# Create labels
username_label = tk.Label(root, text="Username:")
username_label.grid(row=0, column=0, padx=10, pady=5, sticky="e")

password_label = tk.Label(root, text="Password:")
password_label.grid(row=1, column=0, padx=10, pady=5, sticky="e")

# Create entry widgets
username_entry = tk.Entry(root)
username_entry.grid(row=0, column=1, padx=10, pady=5)

password_entry = tk.Entry(root, show="*")
password_entry.grid(row=1, column=1, padx=10, pady=5)

# Create login button
login_button = tk.Button(root, text="Login", command=login)
login_button.grid(row=2, columnspan=2, padx=10, pady=10)

root.mainloop()
