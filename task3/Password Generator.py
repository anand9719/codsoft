from tkinter import *
from tkinter import messagebox
import string
import pyperclip
import random


def generate():
    small_alphabets = string.ascii_lowercase
    capital_alphabets = string.ascii_uppercase
    numbers = string.digits
    special_characters = string.punctuation
    all_char = small_alphabets + capital_alphabets + numbers + special_characters

    pass_length = int(length_Box.get())

    clear()
    entry.insert(0, random.sample(all_char, pass_length))


def copy():
    random_password = entry.get()
    pyperclip.copy(random_password)
    messagebox.showinfo('Copied!', 'Password copied to clipboard!')


def clear():
    entry.delete(0, 'end')


root = Tk()
root.geometry('400x330')
root.configure(background='lightgreen')


lbl1 = Label(root, text='PASSWORD GENERATOR', font=('arial', 24, 'bold'), bg='lightgreen')
lbl1.grid(pady=10)

lbl2 = Label(root, text='Select the length of password:', font='none', bg='lightgreen')
lbl2.grid(pady=10)

length_Box = Spinbox(root, from_=5, to=20, width=10, font=8, bd=2)
length_Box.grid(pady=4)

btn = Button(root, text='GENERATE', bg='green', command=generate)
btn.grid(pady=10)

lbl3 = Label(root, text='Generated Password:', font='none', bg='lightgreen')
lbl3.grid(pady=(20, 10))

entry = Entry(root, font='arial')
entry.grid(pady=(0, 11))

btn1 = Button(root, text='COPY', bg='green', command=copy)
btn1.grid(row=5, padx=(0, 42), pady=(0, 10), sticky='e')

btn1 = Button(root, text='CLEAR', bg='green', command=clear)
btn1.grid(row=6)

root.mainloop()
