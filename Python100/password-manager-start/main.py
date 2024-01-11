from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
import json


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v',
               'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q',
               'R',
               'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    letter_pw = [choice(letters) for _ in range(randint(8, 10))]
    symbol_pw = [choice(symbols) for _ in range(randint(2, 4))]
    number_pw = [choice(numbers) for _ in range(randint(2, 4))]
    password_list = letter_pw + symbol_pw + number_pw

    shuffle(password_list)

    generated_password = "".join(password_list)
    password_entry.insert(0, generated_password)
    pyperclip.copy(generated_password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    new_data = {
        website: {
            "email": email,
            "password": password,
        }
    }

    if len(website) == 0 or len(email) == 0 or len(password) == 0:
        messagebox.showerror(title="Oops", message="Please don't leave any fields empty!")
    else:
        is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered:"
                                                              f"\nEmail: {email}\nPassword: {password}")
        data = ""
        if is_ok:
            try:
                with open("data.json", "r") as file:
                    # file.write(f"{website} | {email} | {password}\n")
                    data = json.load(file)
            except FileNotFoundError:
                data = new_data
            finally:
                data.update(new_data)
                with open("data.json", "w") as file:
                    json.dump(data, file, indent=4)
                    website_entry.delete(0, END)
                    password_entry.delete(0, END)


def find_password():
    website = website_entry.get()
    try:
        with open("data.json", "r") as file:
            data = json.load(file)
    except FileNotFoundError:
        messagebox.showerror(title="Error", message="No Data File Found")
    else:
        if website in data.keys():
            email = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(title=website, message=f"Email: {email}\n Password: {password}")
        else:
            messagebox.showinfo(message="No details for the website exists")

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

logo_canvas = Canvas(width=200, height=200)
logo_img = PhotoImage(file="logo.png")
logo_canvas.create_image(100, 100, image=logo_img)
logo_canvas.grid(row=0, column=1)

website_label = Label(text="Website:")
website_label.grid(row=1, column=0)

email_label = Label(text="Email/Username:")
email_label.grid(row=2, column=0)

password_label = Label(text="Password:")
password_label.grid(row=3, column=0)

website_entry = Entry(width=21)
website_entry.grid(row=1, column=1)
website_entry.focus()

generate = Button(text="Search", width=13, font=("Arial", 12), command=find_password)
generate.grid(row=1, column=2)

email_entry = Entry(width=35)
email_entry.grid(row=2, column=1, columnspan=2)
email_entry.insert(0, "user123@gmail.com")

password_entry = Entry(width=21)
password_entry.grid(row=3, column=1)

generate = Button(text="Generate Password", width=13, font=("Arial", 12), command=generate_password)
generate.grid(row=3, column=2)

add = Button(text="Add", width=33, command=save_password)
add.grid(row=4, column=1, columnspan=2)

window.mainloop()
