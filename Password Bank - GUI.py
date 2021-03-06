# create a database called "PasswordManager"
# create a table called masterpassword (mpassword: admin)
# create a table called savedpasswords

"""
first you have to change the password and username of the conn variable then
you have to enter these commands:
CREATE DATABASE PasswordManager;
USE DATABASE PasswordManager;
CREATE TABLE mPassword(mPassword VARCHAR(50));
INSERT INTO mPassword VALUES("admin")
CREATE TABLE sPasswords(username VARCHAR(50), Password VARCHAR(50));
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
root.geometry("340x200")  # size of the window width: 350, height: 200
root.resizable(0, 0)  # this prevents from resizing the window
root.title("Password Manager")  # title

# Functions #


def login():

    # Connect to a database
    conn = mysql.connector.connect(host="localhost", user="root", passwd="1234",
                                   database="PasswordManager", auth_plugin='mysql_native_password')
    # Create cursor
    c = conn.cursor()

    # Getting information from text box
    mpass_id = mpassword.get()

    # Query the database
    c.execute("SELECT * FROM MPassword")
    records = c.fetchall()

    # Loop through the results
    mpassFound = False
    for record in records:
        if record[0] == mpass_id:
            mpassFound = True
            mpassword.delete(0, "end")
            openfStart()
    if not mpassFound:
        mpassword.delete(0, "end")
        mpass_error_label.config(text="Wrong password, try again.")

    conn.commit()
    conn.close()


def genPass(entry):

    letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    numbers = "1234567890"
    symbols = "!@#$%^&*()"

    passw = ""
    for _ in range(10):
        passw_letters = random.choice(letters)
        passw += passw_letters
    for _ in range(5):
        passw_num = random.choice(numbers)
        passw += passw_num
    for _ in range(5):
        passw_sym = random.choice(symbols)
        passw += passw_sym

    entry.delete(0, "end")
    entry.insert(0, passw)


def savePass(userEntry, passEntry, error, window):

    # Connect to a database
    conn = mysql.connector.connect(host="localhost", user="root", passwd="1234",
                                   database="PasswordManager", auth_plugin='mysql_native_password')
    # Create cursor
    c = conn.cursor()

    # Getting information from the textboxes
    sUser_id = userEntry.get()
    sPass_id = passEntry.get()

    sUserFound = False
    userOrPassEnpty = False

    c.execute("SELECT * from sPasswords")
    records = c.fetchall()

    if ((sUser_id == "") or (sPass_id == "")):
        userEntry.delete(0, "end")
        passEntry.delete(0, "end")
        error.config(
            text="Username or password is empty. Please try again.")
        userOrPassEmpty = True
    else:
        # Loop through the results
        for record in records:
            if record[0] == sUser_id:
                sUserFound = True
                break

    if sUserFound:
        openRepWindow(window, error, userEntry, passEntry)

    elif not userOrPassEmpty:
        error.config(text="")
        saveTodb(sUser_id, sPass_id, error)
        userEntry.delete(0, "end")
        passEntry.delete(0, "end")

    conn.commit()
    conn.close


def openRepWindow(window, error, userEntry, passEntry):

    RepWindow = Toplevel(window)

    RepWindow.title("Replace Password")
    RepWindow.geometry("380x200")

    error.config(text="")

    # Create message Labels
    RepPass_label = Label(
        RepWindow, text="That username already exists. Do you want to replace it?")
    RepPass_label.grid(row=0, column=0, columnspan=2, padx=40, pady=50)
    # Create yes/no buttons
    yes_btn = Button(RepWindow, text="Yes", command=lambda: repPass(
        RepWindow, error, userEntry, passEntry))
    yes_btn.grid(row=1, column=0)
    no_btn = Button(RepWindow, text="No", command=lambda: close(RepWindow))
    no_btn.grid(row=1, column=1)


def saveTodb(user, passw, error):

    # Connect to a database
    conn = mysql.connector.connect(host="localhost", user="root", passwd="1234",
                                   database="PasswordManager", auth_plugin='mysql_native_password')
    # Create cursor
    c = conn.cursor()

    # Query the database
    c.execute('INSERT INTO sPasswords VALUES("{}", "{}")'.format(user, passw))
    error.config(text="Saved to database.")

    conn.commit()
    conn.close()


def repPass(window, error, userEntry, passEntry):

    replaceTodb(userEntry.get(), passEntry.get(), error)
    userEntry.delete(0, "end")
    passEntry.delete(0, "end")
    error.config(text="Password is replaced.")

    close(window)


def replaceTodb(user, passw, error):

    # Connect to a database
    conn = mysql.connector.connect(host="localhost", user="root", passwd="1234",
                                   database="PasswordManager", auth_plugin='mysql_native_password')
    # Create cursor
    c = conn.cursor()

    # Query the database
    c.execute('UPDATE sPasswords SET Password = "{}" WHERE username = "{}"'.format(
        passw, user))
    error.config(text="Saved to database.")

    conn.commit()
    conn.close()


def retrSinglePass(userEntry, error):

    # Connect to a database
    conn = mysql.connector.connect(host="localhost", user="root", passwd="1234",
                                   database="PasswordManager", auth_plugin='mysql_native_password')
    # Create cursor
    c = conn.cursor()

    user_id = userEntry.get()
    userFound = False

    c.execute("SELECT * FROM sPasswords")
    records = c.fetchall()

    if user_id == "":
        error.config(text="The entry fields are empty. Please try again")
    else:
        for record in records:
            if record[0] == user_id:
                username = record[0]
                password = record[1]
                userFound = True

    if userFound:
        error.config(text="{}: {}".format(username, password))
    else:
        error.config(text="The username doesn't exist in the database.")

    conn.commit()
    conn.close()


def retrAllPass(error):

    # Connect to a database
    conn = mysql.connector.connect(host="localhost", user="root", passwd="1234",
                                   database="PasswordManager", auth_plugin='mysql_native_password')
    # Create cursor
    c = conn.cursor()

    c.execute("SELECT * FROM sPasswords")
    records = c.fetchall()

    allPass = ""

    for record in records:
        username = record[0]
        password = record[1]
        allPass += "{}: {}\n".format(username, password)

    error.config(text=allPass)

    conn.commit()
    conn.close()

# GUI #

# Master Password Login Page


fmPassLogin = Frame(root)
fmPassLogin.pack()

# Create labels for login page
mpassword_label = Label(fmPassLogin, text="Master password")
mpassword_label.grid(row=0, column=0, pady=50, padx=10)
mpass_error_label = Label(fmPassLogin, text="")
mpass_error_label.grid(row=1, column=0, columnspan=3)
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
    sAcc_text = StringVar()
    sAcc_entry = Entry(fSavePass, width=45, text=sAcc_text)
    sAcc_entry.grid(row=0, column=1, pady=20, columnspan=2)
    sPass_text = StringVar()
    sPass_entry = Entry(fSavePass, width=25, text=sPass_text)
    sPass_entry.grid(row=1, column=1)
    # Generate Passwords button
    genPass_btn = Button(
        fSavePass, text="Generate Password", command=lambda: genPass(sPass_entry))
    genPass_btn.grid(row=1, column=2, padx=5, pady=20)
    # Error message
    error_label = Label(fSavePass, text="")
    error_label.grid(row=2, column=0, columnspan=3)
    # Create a Save Password Button to Save the password
    save_btn = Button(fSavePass, text="Save Password",
                      command=lambda: savePass(sAcc_entry, sPass_entry, error_label, fSavePass))
    save_btn.grid(row=3, column=0, columnspan=3,
                  pady=20, padx=10, ipadx=100)

    # Creating labels for retrieve passwords page
    rAcc_label = Label(fRetrievePass, text="Username")
    rAcc_label.grid(row=0, column=0, pady=20, padx=20)
    # Creating text boxes for retrieve passwords page
    rAcc_entry = Entry(fRetrievePass, width=45)
    rAcc_entry.grid(row=0, column=1, pady=20, columnspan=2)
    # Create a retrieve a single password button
    singleRetr_btn = Button(
        fRetrievePass, text="Retrieve Password", command=lambda: retrSinglePass(rAcc_entry, rPass_label))
    singleRetr_btn.grid(row=3, column=0, columnspan=3,
                        pady=20, padx=10, ipadx=100)
   # Create a retrieve all passwords button
    allRetr_btn = Button(
        fRetrievePass, text="Retrieve all passwords", command=lambda: retrAllPass(rPass_label))
    allRetr_btn.grid(row=4, column=0, columnspan=3, padx=10, ipadx=90)
    # Create show retrieve pass labels
    rPass_label = Label(fRetrievePass, text="")
    rPass_label.grid(row=5, column=0, columnspan=3, pady=20)

    fStart.mainloop()


# Commit changes
conn.commit()
# Close connection
conn.close()

raise_frame(fmPassLogin)
root.mainloop()
