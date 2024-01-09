from tkinter import *

root = Tk()
root.title("Calculator")

e = Entry(root, width=30, borderwidth=5)
e.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

def clear():
    e.delete(0,END)
def click(number):

    current = e.get()
    e.delete(0,END)
    e.insert(0, str(current) + str(number))
    counter = ""
def add():
    first = e.get()
    global firstnumber
    firstnumber = int(first)
    e.delete(0,END)

    global operation
    operation = "add"


def sub():
    first = e.get()
    global firstnumber
    firstnumber = int(first)
    e.delete(0, END)

    global operation
    operation = "sub"


def mult():
    first = e.get()
    global firstnumber
    firstnumber = int(first)
    e.delete(0, END)

    global operation
    operation = "mult"


def div():
    first = e.get()
    global firstnumber
    firstnumber = int(first)
    e.delete(0, END)

    global operation
    operation = "div"

def equal():
    if operation == "add":
        secondnumber = e.get()
        e.delete(0,END)
        e.insert(0, firstnumber + int(secondnumber))
    elif operation == "sub":
        secondnumber = e.get()
        e.delete(0, END)
        e.insert(0, firstnumber - int(secondnumber))
    elif operation == "mult":
        secondnumber = e.get()
        e.delete(0, END)
        e.insert(0, firstnumber * int(secondnumber))
    elif operation == "div":
        secondnumber = e.get()
        e.delete(0, END)
        e.insert(0, firstnumber / int(secondnumber))





one = Button(root, text="1", padx=30, pady=10, command=lambda: click(1)).grid(row=3, column=0)
two = Button(root, text="2", padx=30, pady=10, command=lambda: click(2)).grid(row=3, column=1)
three = Button(root, text="3", padx=30, pady=10, command=lambda: click(3)).grid(row=3, column=2)

four = Button(root, text="4", padx=30, pady=10, command=lambda: click(4)).grid(row=2, column=0)
five = Button(root, text="5", padx=30, pady=10, command=lambda: click(5)).grid(row=2, column=1)
six = Button(root, text="6", padx=30, pady=10, command=lambda: click(6)).grid(row=2, column=2)

seven = Button(root, text="7", padx=30, pady=10, command=lambda: click(7)).grid(row=1, column=0)
eight = Button(root, text="8", padx=30, pady=10, command=lambda: click(8)).grid(row=1, column=1)
nine = Button(root, text="9", padx=30, pady=10, command=lambda: click(9)).grid(row=1, column=2)

zero = Button(root, text="0", padx=30, pady=10, command=lambda: click(0)).grid(row=4, column=0)


clear = Button(root, text="AC", padx=10, pady=10,command= clear).grid(row=0, column=3)
equal = Button(root, text="=", padx=30, pady=10, command = equal).grid(row=4, column=2)
decimal = Button(root, text=".", padx=30, pady=10).grid(row=4, column=1)

add = Button(root, text="+", padx=10, pady=10, command= add).grid(row=4, column=3)
sub = Button(root, text="-", padx=10, pady=10, command= sub).grid(row=3, column=3)
mult = Button(root, text="*", padx=10, pady=10, command= mult).grid(row=2, column=3)
div = Button(root, text="/", padx=10, pady=10, command= div).grid(row=1, column=3)

root.mainloop()
