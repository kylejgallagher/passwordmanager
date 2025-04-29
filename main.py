
from tkinter import *
from tkinter import messagebox
import random
import json


letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


def pass_gen():
    password =""
    for letter in range(random.randint(3,10)):
        password += random.choice(letters)

    for sym in range(random.randint(3,10)):
        password += random.choice(symbols)

    for num in range(random.randint(0,10)):
        password += random.choice(numbers)
    input_password.insert(0, password)

    print(password)

def make_password():
    get_website = input_website.get()
    get_email = input_email.get()
    get_password = input_password.get()

    new_data = {
        get_website: {
            'email': get_email,
            'password': get_password
        }
    }

    if len(input_website.get()) == 0 or len(input_password.get()) == 0 or len(input_email.get()) == 0:
        messagebox.showinfo(message="Please fill out all fields")
    else:
        try:
            with open("data.json", 'r') as data_file:
                # read data
                data = json.load(data_file)
                # update old data

        except FileNotFoundError:
            with open('data.json', 'w') as data_file:
                json.dump(new_data, data_file, indent=4)
                print('file created')
        else:
            data.update(new_data)
            with open('data.json', 'w') as data_file:
                json.dump(data, data_file, indent=4)

                messagebox.showinfo(message="Password saved")
                input_password.delete(0,END)
                input_website.delete(0,END)

def search():
    try:
        with open('data.json') as file:
            data = json.load(file)
            messagebox.showinfo(message=f"Email: {data[input_website.get()]['email']} \n Password: {data[input_website.get()]['password']}")
    except KeyError:
        messagebox.showinfo(message="Website not found")
    else:
        input_website.delete(0,END)

window = Tk()
window.title("Password Manager")
window.config(padx=20,pady=20)

canvas = Canvas(width=200, height=200)

lock_pic = PhotoImage(file="logo.png")
canvas.create_image(100,100,image=lock_pic)
canvas.grid(column=2,row=1)

website = Label(text="Website:")
website.grid(column=1,row=2)

website = Label(text="Email/Username:")
website.grid(column=1,row=3)

website = Label(text="Password:")
website.grid(column=1,row=4)

input_website = Entry(width=35)
input_website.grid(column=2, row=2, columnspan=35)
input_website.get()

website_button = Button(text='Search', width=9, command=search)
website_button.grid(column=3, row=2,columnspan = 14)

input_email = Entry(width=35)
input_email.grid(column=2, row=3, columnspan=35)
input_email.insert(0,"name@email.com")
input_email.get()

input_password = Entry(width=35)
input_password.grid(column=2, row=4, columnspan=35)
input_password.get()


generate_button = Button(text="Generate Password", width=11, command=pass_gen)
generate_button.grid(column=3, row=4, columnspan=14)

add_button = Button(text="Add", width=33, command=make_password)
add_button.grid(column=2, row=5, columnspan=36)


window.mainloop()