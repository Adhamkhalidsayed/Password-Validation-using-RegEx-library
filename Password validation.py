from tkinter import *
import re
from tkinter import messagebox

def passwordValidation(password):
    if len(password) < 8:
        return False
    if not re.search(r"[A-Z]", password):
        return False
    if not re.search(r"[a-z]", password):
        return False
    if not re.search(r"\d", password):
        return False
    if not re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        return False
    return True

def validate_password():
    password = e1.get()
    if passwordValidation(password):
        messagebox.showinfo("Success", "Password accepted")
        root.destroy()
    else:
        messagebox.showerror("Error", "Password is not accepted. Try again!")

def toggle_password():
    if show_var.get():
        e1.config(show="")
    else:
        e1.config(show="*")

# Set up the GUI
root = Tk()
root.title("Password Validator")

# Center the window on the screen
window_width = 400
window_height = 150
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x_coordinate = int((screen_width / 2) - (window_width / 2))
y_coordinate = int((screen_height / 2) - (window_height / 2))
root.geometry(f"{window_width}x{window_height}+{x_coordinate}+{y_coordinate}")

Label(root, text="Enter Password:").grid(row=0, column=0, padx=10, pady=10)
e1 = Entry(root, show="*")
e1.grid(row=0, column=1, padx=10, pady=10)

show_var = IntVar()
show_checkbox = Checkbutton(root, text="Show Password", variable=show_var, command=toggle_password)
show_checkbox.grid(row=1, column=1, sticky="w")

button = Button(root, text='Check', width=40, command=validate_password)
button.grid(row=2, column=0, columnspan=2, pady=10)

root.mainloop()