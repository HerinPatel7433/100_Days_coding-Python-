import tkinter as tk
from tkinter import messagebox
import random
import pyperclip


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

    if not website or not email or not password:
        messagebox.showwarning(title="Oops!", message="Please don't leave any fields empty.")
        return

    if messagebox.askokcancel(
        title=website,
        message=f"Email: {email}\nPassword: {password}\n\nSave?"
    ):
        with open("Day-29//data.txt", "a") as file:
            file.write(f"{website} | {email} | {password}\n")

        website_entry.delete(0, tk.END)
        password_entry.delete(0, tk.END)


# ---------------------------- UI SETUP ------------------------------- #
window = tk.Tk()
window.title("Password Manager")
window.config(padx=25, pady=25)

window.columnconfigure(0, weight=0)
window.columnconfigure(1, weight=1)
window.columnconfigure(2, weight=0)

# Logo
canvas = tk.Canvas(width=200, height=200, highlightthickness=0)
lock_img = tk.PhotoImage(file="Day-29\\logo.png")
canvas.create_image(100, 100, image=lock_img)
canvas.grid(column=0, row=0, columnspan=3, pady=(0, 10))

# Labels
website_label = tk.Label(text="Website:")
website_label.grid(column=0, row=1, sticky="e", padx=(0, 10), pady=5)

email_label = tk.Label(text="Email / Username:")
email_label.grid(column=0, row=2, sticky="e", padx=(0, 10), pady=5)

password_label = tk.Label(text="Password:")
password_label.grid(column=0, row=3, sticky="e", padx=(0, 10), pady=5)

# Entries
website_entry = tk.Entry(width=32)
website_entry.grid(column=1, row=1, sticky="ew", pady=5)
website_entry.focus()

email_entry = tk.Entry(width=32)
email_entry.grid(column=1, row=2, columnspan=2, sticky="ew", pady=5)
email_entry.insert(0, "example@email.com")

password_entry = tk.Entry(width=21)
password_entry.grid(column=1, row=3, sticky="ew", pady=5)

# Buttons
generate_password_btn = tk.Button(text="Generate", command=generate_password)
generate_password_btn.grid(column=2, row=3, padx=(10, 0), pady=5)

add_button = tk.Button(text="Add", width=36, command=save_password)
add_button.grid(column=0, row=4, columnspan=3, pady=(10, 0))

window.mainloop()
