import tkinter as tk
import tkinter.messagebox
from tkinter import END, ttk
import numpy as np

global to_do_list
to_do_list = []


def add(text):
    with open("toDoList", "w") as f:
        f.write(text)
    add_txt.delete(0, END)
    update()


def update():
    global to_do_list
    with open("toDoList", 'r') as f:
        for line in f:
            to_do_list.append(line)
    print(to_do_list)


root = tk.Tk()
root.geometry("300x300")
root.title("To Do List")
tab_control = ttk.Notebook(root)

add_tab = ttk.Frame(tab_control)
tab_control.add(add_tab, text='Add')
tab_control.pack(expand=1, fill="both")

rem_tab = ttk.Frame(tab_control)
tab_control.add(rem_tab, text='Remove')
tab_control.pack(expand=1, fill="both")

view_tab = ttk.Frame(tab_control)
tab_control.add(view_tab, text='View List')
tab_control.pack(expand=1, fill="both")

add_lbl = tk.Label(add_tab, bg='grey', text="Input tasks you want to add to the list")
add_lbl.pack()
add_txt = tk.Entry(add_tab, borderwidth=5)
add_txt.pack()
txt = add_txt.get()
add_btn = tk.Button(command=lambda: add(txt), text="Add to to do list.")
add_btn.pack()
boxes = {}
for item in to_do_list:
    boxes[item] = ttk.Checkbox(view_tab, text=item)

root.mainloop()
# with open("toDoList", "w") as f:
#   f.write(input())
