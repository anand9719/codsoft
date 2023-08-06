import tkinter as tk
from tkinter import *
from tkinter import messagebox

tasks = []


def add_task():
    task = task_entry.get()
    if task:
        tasks.append(task)
        task_listbox.insert(tk.END, task)
        task_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Empty Task", "Please enter a task.")


def update_task():
    selected_task = task_listbox.curselection()
    if selected_task:
        new_task = task_entry.get()
        tasks[selected_task[0]] = new_task
        task_listbox.delete(selected_task)
        task_listbox.insert(selected_task, new_task)
        task_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("No Task Selected", "Please select a task to update.")


def delete_task():
    selected_task = task_listbox.curselection()
    if selected_task:
        tasks.pop(selected_task[0])
        task_listbox.delete(selected_task)
    else:
        messagebox.showwarning("No Task Selected", "Please select a task to delete.")


# Create the main window
root = tk.Tk()
root.title("ToDo List")
root.configure(background='lightgreen')
root.geometry('280x380')

lbl = Label(root, text='Enter Task:')
lbl.grid(row=0, column=0, pady=(15, 5))
lbl.configure(bg='lightgreen', font=('verdana', 12, 'bold'))

# Create and configure the task entry widget
task_entry = tk.Entry(root, width=40, border=2)
task_entry.grid(row=2, column=0, padx=20, pady=(3, 15))

# Create and configure the buttons
add_button = tk.Button(root, text="Add", command=add_task)
add_button.grid(row=5, column=0, sticky='w', padx=(50, 0), ipadx=9, ipady=1)
add_button.config(bg='green', font=('none', 10, 'bold'))

update_button = tk.Button(root, text="Update ", command=update_task)
update_button.grid(row=5, column=0, sticky='e', padx=(0, 50), ipady=1)
update_button.config(bg='green', font=('none', 10, 'bold'),)

delete_button = tk.Button(root, text="Delete ", command=delete_task)
delete_button.grid(row=9, column=0, pady=(10, 0), ipadx=7, ipady=1)
delete_button.config(bg='green', font=('none', 10, 'bold'))

lbl = Label(root, text='List:')
lbl.grid(row=7, column=0, pady=(15, 0))
lbl.configure(bg='lightgreen', font=('verdana', 12, 'bold'))

# Create and configure the task listbox widget
task_listbox = tk.Listbox(root, width=40)
task_listbox.grid(row=8, column=0)

# Start the main event loop
root.mainloop()
