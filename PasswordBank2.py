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

# Windows #


# root window
root = Tk()
root.geometry("350x200")  # size of the window width: 350, height: 200
root.resizable(0, 0)  # this prevents from resizing the window
root.title("Password Manager")  # title

# Frames #

# For root window
fmPassLogin = Frame(root)
fStart = Frame(root)
fSavePass = Frame(root)
fRetrievePass = Frame(root)
fShowReplacedPass = Frame(root)
fShowSavedPass = Frame(root)

for frame in (fmPassLogin, fStart, fSavePass, fRetrievePass, fShowSavedPass):
    frame.grid(row=0, column=0, sticky="news")

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
    c.execute("SELECT * FROM MasterPassword")
    records = c.fetchall()

    # Loop through the results
    mpassFound = False
    for record in records:
        if record[0] == pass_id:
            mpassFound = True
            mpassword.delete(0, END)
            raise_frame(fStart)
    if not mpassFound:
        mpassword.delete(0, END)
        mpass_error_label.config(text="Wrong password, try again.")

    conn.commit()

    conn.close()


# Create a Function to Check if the password exists for a username

def checkSPass():

    # Connect to a database
    conn = mysql.connector.connect(host="localhost", user="root", passwd="1234",
                                   database="PasswordManager", auth_plugin='mysql_native_password')
    # Create cursor
    c = conn.cursor()

    # Getting information from text box
    user_id = aAccName.get()

    # Query the database
    c.execute("SELECT * FROM sPasswords")
    records = c.fetchall()

    # Loop through the results
    userFound = False
    for record in records:
        if record[0] == user_id:
            userFound = True
            # If the username is found then ask if you want to replace the password
            openReplacePass()

    if not userFound:
        # PLACEHOLDER: function that generates a new password and saves it to database like replacePassYes
        raise_frame(fShowSavedPass)

    conn.commit()

    conn.close()

# Create Function to open a replace password window


def openReplacePass():  # The window is not opening

    # Saved password replace window
    # Toplevel object which will be treated as a new window
    sReplace = Toplevel(root)
    sReplace.title("Replace Password")
    sReplace.geometry("200x150")
    sReplace.resizable(0, 0)

    # Creating Labels for Replace Saved Passwords Page
    sPass_error_label = Label(
        sReplace, text="That account already has a Saved password. Do you want to replace it?")
    sPass_error_label.grid(row=0, column=0)
    # Creating a yes button
    sReplace_yes_btn = Button(sReplace, text="Yes",
                              command=replacePassYes(sReplace))
    sReplace_yes_btn.grid(row=1, column=0)
    # Creating a no Button
    sReplace_no_btn = Button(sReplace, text="No", command=close(sReplace))
    sReplace_no_btn.grid(row=1, column=1)


replacedPass = ['']


def replacePassYes(window):

    # Closing the replace window
    close(window)

    # Generate a new password
    # Now how do you access replacedPass outside this function so you can show this in fShowReplacedPass?
    global replacedPass
    replacedPass[0] = genPass()

    '''replacedPass can only be used if replacePassYes is called but we need it to be there without that for fShowReplacedPass
    I'll try declaring rP as a list (so it is mutable and then try making it global in the function)
    '''

    # Then save it to database

    # Connect to a database
    conn = mysql.connector.connect(host="localhost", user="root", passwd="1234",
                                   database="PasswordManager", auth_plugin='mysql_native_password')

    # Create cursor
    c = conn.cursor()

    # Query the database
    c.execute('INSERT INTO sPasswords VALUES("{}", "{}")'.format(
        aAccName_text, replacedPass[0]))

    # Raising replacedPassword window
    raise_frame(fShowReplacedPass)

    conn.commit()

    conn.close()


def genPass():

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

    return passw


# GUI #

# Master Password Login Page

# Create labels for login page
mpassword_label = Label(fmPassLogin, text="Master password")
mpassword_label.grid(row=0, column=0)
mpass_error_label = Label(fmPassLogin, text="")
mpass_error_label.grid(row=1, column=0, columnspan=2)
# Create text boxes for login page
mpassword = Entry(fmPassLogin, width=30)
mpassword.grid(row=0, column=1, padx=20)
# Create a login button
login_btn = Button(fmPassLogin, text="Login", command=login)
login_btn.grid(row=3, column=1)

# Starting Page

# Create Retrieve passwords button
retrievePass_btn = Button(
    fStart, text="Retrieve Passwords")
retrievePass_btn.grid(row=0, column=0)
# Create Save a password button
savedPass_btn = Button(fStart, text="Save a Password",
                       command=lambda: raise_frame(fSavePass))
savedPass_btn.grid(row=0, column=1)

# Saving a password page

# Creating Back Button
savedPass_back_btn = Button(fSavePass, text="Back",
                            command=lambda: raise_frame(fStart))
savedPass_back_btn.grid(row=0, column=0)
# Creating Labels for Saved Passwords Page
aAccName_label = Label(fSavePass, text="Enter Account Name: ")
aAccName_label.grid(row=1, column=0)
# Creating text boxes for Saved Passwords Page
aAccName = Entry(fSavePass, width=30)
aAccName.grid(row=1, column=1)
aAccName_text = aAccName.get()
# Creating Enter button
sEnter_btn = Button(fSavePass, text="Enter", command=checkSPass)
sEnter_btn.grid(row=2, column=1)

# Showing Replaced Pass Page

# Creating Back Button
replacedPass_back_btn = Button(
    fShowReplacedPass, text="Back", command=lambda: raise_frame(fSavePass))
replacedPass_back_btn.grid(row=0, column=0)
# Creating Labels for Replaced Pass page
replacedPassText = Label(fShowReplacedPass, text="The saved password for {} is {}".format(
    aAccName.get(), replacedPass[0]))
replacedPassText.grid(row=1, column=0)
# Creating "Go back to start" Button
replacedPass_start_btn = Button(
    fShowReplacedPass, text="Go back to start", command=lambda: raise_frame(fStart))
replacedPass_start_btn.grid(row=2, column=0)

# Commit changes
conn.commit()
# Close connection
conn.close()

raise_frame(fmPassLogin)
root.mainloop()
