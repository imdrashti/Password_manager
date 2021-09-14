from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
import json


# ----------------PASSWORD GENERATOR-------------

def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers

    shuffle(password_list)

    password = "".join(password_list)

    password_entry.insert(0, password)
    pyperclip.copy(password)


# ------------------SAVE PASSWORD-----------------
def save():
    website = website_entry.get()
    email = username_entry.get()
    password = password_entry.get()
    new_data = {
        website: {
            "email": email,
            "password": password,

        }
    }

    if len(website) == 0 or len(password) == 0:
        pop_up = messagebox.showinfo(title="OOPS", message="Please don't leave any fields empty")

    else:
        try:
            with open("data.json", "r") as file:
                # json.dump(new_data, file, indent=4)     #to write
                data = json.load(file)  # to read
        except FileNotFoundError:
            with open("data.json", "w") as file:
                json.dump(new_data, data, indent=4)
        else:
            data.update(new_data)  # to update
            with open("data.json", "w") as file:
                json.dump(data, file, indent=4)  # saving updated data
        finally:
            website_entry.delete(0, END)
            password_entry.delete(0, END)


# -----------------------FIND PASSWORD--------------------
def find_password():
    website = website_entry.get()
    try:
        with open("data.json") as file:
            data = json.load(file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No Data File Found")
    else:
        if website in data:
            email = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(title=website, message=f"Email: {email}\nPassword: {password}")
        else:
            messagebox.showinfo(title="Error", message=f"No details for {website} exists.")



# -----------------------UI SETUP--------------------

window = Tk()
window.title("Password manager")
window.config(padx=40, pady=40)

canvas = Canvas(height=200, width=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=0)

# labels
website_label = Label(text="Website:", font=("Arial", 10, "normal"))
website_label.grid(column=0, row=1)
website_entry = Entry(width=21)
website_entry.grid(column=1, row=1)
website_entry.focus()

username_label = Label(text="Email/Username:", font=("Arial", 10, "normal"))
username_label.grid(column=0, row=2)
username_entry = Entry(width=40)
username_entry.grid(column=1, columnspan=2, row=2)
username_entry.insert(0, "imdrashtii@gmail.com")

password_label = Label(text="Password:", font=("Arial", 10, "normal"))
password_label.grid(column=0, row=3)
password_entry = Entry(width=21)
password_entry.grid(column=1, row=3)

# buttons
generate_password_button = Button(text="Generate Password", command=generate_password)
generate_password_button.grid(row=3, column=2)

add_button = Button(text="Add", width=36, command=save)
add_button.grid(row=4, column=1, columnspan=2)

search_button = Button(text="Search", width=13, command= find_password)
search_button.grid(row=1, column=2)




window.mainloop()
