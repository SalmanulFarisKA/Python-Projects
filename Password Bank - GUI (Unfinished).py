# create a database called "PasswordManager"
# create a table called masterpassword (mpassword: admin)
# create a table called savedpasswords (account: google, password: 1234)

"""
first you have to change the password and username of the conn variable then
you have to enter these commands:
CREATE DATABASE PasswordManager;
USE DATABASE PasswordManager;
CREATE TABLE mPassword(mPassword VARCHAR(50));
INSERT INTO mPassword VALUES("admin")
CREATE TABLE sPasswords(Account VARCHAR(50), Password VARCHAR(50));
INSERT INTO sPasswords VALUES("google", "1234")
"""

import mysql.connector
from tkinter import *
from tkinter import ttk
from tkinter.ttk import *
import random

# Connecting to database
conn = mysql.connector.connect(
    host="localhost", user="root", passwd="1234", database="PasswordManager", auth_plugin='mysql_native_password')

# Creating cursor
c = conn.cursor()


def raise_frame(frame):  # to change frames
    frame.tkraise()


def close(window):  # to close the window
    window.destroy()


def placeholder():
    print("It works")


# root window
root = Tk()
root.geometry("350x200")  # size of the window width: 350, height: 200
root.resizable(0, 0)  # this prevents from resizing the window
root.title("Password Manager")  # title

# Functions #

# Create a Function to Login


def login():

    # Connect to a database
    conn = mysql.connector.connect(host="localhost", user="root", passwd="1234",
                                   database="PasswordManager", auth_plugin='mysql_native_password')
    # Create cursor
    c = conn.cursor()

    # Getting information from text box
    pass_id = mpassword.get()

    # Query the database
    c.execute("SELECT * FROM MPassword")
    records = c.fetchall()

    # Loop through the results
    mpassFound = False
    for record in records:
        if record[0] == pass_id:
            mpassFound = True
            mpassword.delete(0, END)
            openfStart()
    if not mpassFound:
        mpassword.delete(0, END)
        mpass_error_label.config(text="Wrong password, try again.")

    conn.commit()

    conn.close()


# GUI #


# Master Password Login Page
fmPassLogin = Frame(root)
fmPassLogin.pack()

# Create labels for login page
mpassword_label = Label(fmPassLogin, text="Master password")
mpassword_label.grid(row=0, column=0, pady=50)
mpass_error_label = Label(fmPassLogin, text="")
mpass_error_label.grid(row=1, column=0)
# Create text boxes for login page
mpassword = Entry(fmPassLogin, width=30)
mpassword.grid(row=0, column=1, padx=20, pady=50, columnspan=2)
# Create a login button
login_btn = Button(fmPassLogin, text="Login", command=login)
login_btn.grid(row=3, column=2, pady=20)


def openfStart():

    close(root)

    # Starting Page

    fStart = Tk()
    fStart.title("Password Bank")
    fStart.geometry("385x370")
    fStart.resizable(0, 0)

    # Notebook

    my_notebook = ttk.Notebook(fStart)
    my_notebook.grid(row=0, column=0, pady=5)

    # Saving passwords tab

    fSavePass = Frame(my_notebook, width=500, height=700)
    fSavePass.pack(fill="both", expand=1)
    my_notebook.add(fSavePass, text="Save Passwords")

    # Retrieving passwords tab

    fRetrievePass = Frame(my_notebook, width=500, height=500)
    fRetrievePass.pack(fill="both", expand=1)
    my_notebook.add(fRetrievePass, text="Retrieve Passwords")

    # Creating labels for save passwords page
    sAcc_label = Label(fSavePass, text="Username")
    sAcc_label.grid(row=0, column=0, pady=20, padx=20)
    sPass_label = Label(fSavePass, text="Password")
    sPass_label.grid(row=1, column=0, padx=20)
    # Creating text boxes for save passwords Page
    sAcc_entry = Entry(fSavePass, width=43)
    sAcc_entry.grid(row=0, column=1, pady=20, columnspan=2)
    sPass_entry = Entry(fSavePass, width=20)
    sPass_entry.grid(row=1, column=1)
    # Generate Passwords button
    genPass_btn = Button(
        fSavePass, text="Generate Password", command=placeholder)
    genPass_btn.grid(row=1, column=2, padx=5, pady=20, ipadx=10)
    # Create a Save Password Button to Save the password
    save_btn = Button(fSavePass, text="Save Password", command=placeholder)
    save_btn.grid(row=3, column=0, columnspan=3,
                  pady=20, padx=10, ipadx=100)

    # Creating labels for retrieve passwords page
    rAcc_label = Label(fRetrievePass, text="Username")
    rAcc_label.grid(row=0, column=0, pady=20, padx=20)
    # Creating text boxes for retrieve passwords page
    rAcc_entry = Entry(fRetrievePass, width=43)
    rAcc_entry.grid(row=0, column=1, pady=20, columnspan=2)
    # Create a retrieve a single password button
    singleRetr_btn = Button(
        fRetrievePass, text="Retrieve Password", command=placeholder)
    singleRetr_btn.grid(row=3, column=0, columnspan=3,
                        pady=20, padx=10, ipadx=100)
   # Create a retrieve all passwords button
    allRetr_btn = Button(
        fRetrievePass, text="Retrieve all passwords", command=placeholder)
    allRetr_btn.grid(row=4, column=0, columnspan=3, padx=10, ipadx=90)
    # Create show retrieve pass labels
    PHText = "Placeholder: 1234jfsoi\ngoogle: google123\nfacebook: 202908hu\nTwitter: ejh0h87re7"
    rPass_label = Label(fRetrievePass, text="{}".format(PHText))
    rPass_label.grid(row=5, column=0, columnspan=3, pady=20)

    fStart.mainloop()


# Commit changes
conn.commit()
# Close connection
conn.close()

raise_frame(fmPassLogin)
root.mainloop()
