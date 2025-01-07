from tkinter import *
from tkinter import messagebox
import random as rd
import pyperclip as pclip
import json
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v',
               'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q',
               'R',
               'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
    password_entry.delete(0, "end")
    # my solution
    password_letter = [rd.choice(letters) for letter in range(rd.randint(2, 8))]
    password_number = [rd.choice(numbers) for number in range(rd.randint(2, 4))]
    password_symbols = [rd.choice(symbols)for symbol in range(rd.randint(2, 4))]
    password = password_letter + password_number + password_symbols
    rd.shuffle(password)  # this is the password_list
    password = "".join(password)
    password_entry.insert(0, password)
    # messagebox.showwarning(title="Password Manager", message="Password in the clipboard.")
    pclip.copy(password)
# ---------------------------- SAVE PASSWORD ------------------------------- #
def add_password():
    name = name_entry.get()
    link = link_entry.get()
    user = user_entry.get()
    password = password_entry.get()
    new_data = {
        name.title(): {
            "link": link,
            "user": user,
            "password": password,
        },
    }
    if len(link) == 0 or len(user) == 0 or len(password) == 0 or len(name) == 0 :
        messagebox.showwarning(title="Password Manager", message="Please fill out all the fields.")
    else:
        try:
             with open("data.json", "r") as data_file:
                data = json.load(data_file)
        except FileNotFoundError:
            with open("data.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)
                # data_file.write(f"Link: {link} | User: {user} | Password: {password}\n")
        #else only exec if try is successful
        else:
            data.update(new_data)
            with open("data.json", "w") as data_file:
                json.dump(data, data_file, indent=4)
        finally:
            with open("data.txt", mode="a") as data_file:
                data_file.write(f"Name: {name} | Link: {link} | User: {user} | Password: {password}\n")
            link_entry.delete(0, "end")
            password_entry.delete(0, "end")
            link_entry.focus()
# ---------------------------- SEARCH PASSWORD ------------------------------- #
def look():
    name = name_entry.get().title()
    try:
        with open("data.json", "r") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showwarning(title="Password Manager", message="No data file found!")
    else:
        if name in data:
            link_entry.delete(0, "end")
            user_entry.delete(0, "end")
            password_entry.delete(0, "end")
            link_entry.insert(0, f"{data[name]["link"]}")
            user_entry.insert(0, f"{data[name]["user"]}")
            password_entry.insert(0, f"{data[name]["password"]}")
        else:
            messagebox.showwarning(title="Password Manager", message= f'{name} not found')
# ---------------------------- UI SETUP ------------------------------- #
# main window
root = Tk()
root.title("Password Manager")
root.config(padx=20, pady=20)
canvas = Canvas(width=200, height=200, highlightthickness=0)
image = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=image)
canvas.grid(row=0, column=1)
# labels and entries
name_label = Label(text="Name", pady=5)
name_label.grid(row=1, column=0)
name_entry =  Entry(width=45)
name_entry.grid(row=1, column=1, columnspan=2)
name_entry.focus()
link_label = Label(text="Link", pady=5)
link_label.grid(row=2, column=0)
link_entry =  Entry(width=45)
link_entry.grid(row=2, column=1, columnspan=2)
user_label = Label(text="Username:", pady=5)
user_label.grid(row=3, column=0)
user_entry =  Entry(width=45)
user_entry.grid(row=3, column=1, columnspan=2)
user_entry.insert(0, "@gmail.com")
password_label = Label(text="Password:", pady=5)
password_label.grid(row=4, column=0)
password_entry =  Entry(width=27)
password_entry.grid(row=4, column=1)
# buttons
generator_button = Button(text="Generate Password", command=generate, padx= 5)
generator_button.grid(row=4, column=2)
add_button = Button(text="Add", command=add_password, width=38, pady=5)
add_button.grid(row=5, column=1, columnspan=2)
search_button = Button(text="Search for link/Name", command=look, width=38, pady=5)
search_button.grid(row=6, column=1, columnspan=2 )
copy_link = Button(text="Copy",command=lambda:pclip.copy(link_entry.get()), padx=5)
copy_link.grid(row=2, column=3)
copy_user = Button(text="Copy", command=lambda:pclip.copy(user_entry.get()), padx=5)
copy_user.grid(row=3, column=3)
copy_pass = Button(text="Copy", command=lambda:pclip.copy(password_entry.get()), padx=5)
copy_pass.grid(row=4, column=3)
root.mainloop()
