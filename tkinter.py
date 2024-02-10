import tkinter as tki
from tkinter import messagebox

# Define a function for validating the login
def validate_login():
    # Write the correct username and password
    valid_username = "manasa"
    valid_password = "manasa123"

    # Get the entered username and password
    entered_username = username_entry.get()
    entered_password = password_entry.get()

    # Check if the entered credentials are correct
    if entered_username == valid_username and entered_password == valid_password:
        messagebox.showinfo("Welcome!", "Login successfully completed")
    else:
        messagebox.showerror("Incorrect Credentials", "Please check your username and password")

# Create the main window
root = tki.Tk()
root.title("Login form")

# Create and place the username label and entry
username_label = tki.Label(root, text="Username:")
username_label.pack()

username_entry = tki.Entry(root)
username_entry.pack()

# Create and place the password label and entry
password_label = tki.Label(root, text="Password:")
password_label.pack()

password_entry = tki.Entry(root, show="*")  # Show asterisks for password
password_entry.pack()

# Create and place the login button
login_button = tki.Button(root, text="Login", command=validate_login)
login_button.pack()

# Start the Tkinter event loop
root.mainloop()
