import tkinter as tk
from tkinter import messagebox

# It Creates a Window Page
form=tk.Tk()
form.title("Login System")
form.geometry("500x500")

# It takes information from user about username
username=tk.Label(form,text="Username:")
username.pack()
entry=tk.Entry()
entry.pack()
entry.get()

# It takes information from user about his/her password
Password= tk.Label(form,text="Password:")
Password.pack()
entry2=tk.Entry()
entry2.pack()
entry2.get()
label3=tk.Label(form,text="Success")

# This function for Login Button .
def loginsystem():
# if defined Username and Password are True prints out "Success" to the Screen.
    if entry.get()== "Ahmed" and entry2.get() =="1234567":
        label3.pack()
# if username or password is wrong it gives an error message to user.
    else:
        messagebox.showinfo(title ="error 404", message="You messed up try again")

# When you click this button it controls Username or Password are True or False
login_buton=tk.Button(text="Login",bg="Red",command=loginsystem)
login_buton.pack()

# The last line of code for keep open to window page for long time.
form.mainloop()
