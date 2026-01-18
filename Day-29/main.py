import tkinter as tk
from tkinter import messagebox
import random
import pyperclip
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    numbers = "0123456789"
    symbols = "!#$%&()*+"

    password_list = (
        [random.choice(letters) for _ in range(random.randint(8, 10))] +
        [random.choice(numbers) for _ in range(random.randint(2, 4))] +
        [random.choice(symbols) for _ in range(random.randint(2, 4))]
    )

    random.shuffle(password_list)
    password = "".join(password_list)

    password_entry.delete(0, tk.END)
    password_entry.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()

    if not website or not password:
        messagebox.showinfo(title="Oops", message="Please make sure no fields are empty.")
        return

    new_data = {
        website: {
            "email": email,
            "password": password
        }
    }

    try:
        with open("Day-29/data.json", "r") as file:
            data = json.load(file)
    except FileNotFoundError:
        data = {}

    data.update(new_data)

    with open("Day-29/data.json", "w") as file:
        json.dump(data, file, indent=4)

    website_entry.delete(0, tk.END)
    password_entry.delete(0, tk.END)


# ---------------------------- SEARCH PASSWORD ------------------------------- #
def search_password():
    website = website_entry.get()

    if not website:
        messagebox.showinfo(title="Error", message="Please enter a website name.")
        return

    try:
        with open("Day-29/data.json", "r") as file:
            data = json.load(file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No data file found.")
        return

    if website in data:
        email = data[website]["email"]
        password = data[website]["password"]
        messagebox.showinfo(
            title=website,
            message=f"Email: {email}\nPassword: {password}"
        )
    else:
        messagebox.showinfo(title="Not Found", message="Website not found.")


# ---------------------------- UI SETUP ------------------------------- #
window = tk.Tk()
window.title("Password Manager")
window.config(padx=25, pady=25)

# Logo
canvas = tk.Canvas(width=200, height=200, highlightthickness=0)
lock_img = tk.PhotoImage(file="Day-29\\logo.png")
canvas.create_image(100, 100, image=lock_img)
canvas.grid(column=0, row=0, columnspan=3)

# Labels
tk.Label(text="Website:").grid(column=0, row=1, sticky="e")
tk.Label(text="Email / Username:").grid(column=0, row=2, sticky="e")
tk.Label(text="Password:").grid(column=0, row=3, sticky="e")

# Entries
website_entry = tk.Entry(width=21)
website_entry.grid(column=1, row=1, sticky="ew")
website_entry.focus()

email_entry = tk.Entry(width=32)
email_entry.grid(column=1, row=2, columnspan=2, sticky="ew")
email_entry.insert(0, "herinpatel6747@gmail.com")

password_entry = tk.Entry(width=21)
password_entry.grid(column=1, row=3, sticky="ew")

# Buttons
tk.Button(text="Search", width=13, command=search_password)\
    .grid(column=2, row=1)

tk.Button(text="Generate", command=generate_password)\
    .grid(column=2, row=3)

tk.Button(text="Add", width=36, command=save_password)\
    .grid(column=1, row=4, columnspan=2)

window.mainloop()
