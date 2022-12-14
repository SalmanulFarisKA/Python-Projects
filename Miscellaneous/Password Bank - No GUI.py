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
    host="localhost", user="root", passwd="tiger", database="PasswordManager", auth_plugin='mysql_native_password')
 
# Creating cursor
c = conn.cursor()
 
 
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
 
 
while 1:
    master_pass = input("Enter master password: ")
 
    # Query the database
    c.execute("SELECT * FROM mPassword")
    records = c.fetchall()
 
    mPassFound = False
    for record in records:
        if master_pass == record[0]:
            mPassFound = True
 
    if mPassFound:
        break
 
while 1:
 
    print("1. Save a password")
    print("2. Retrieve a password")
 
    choice = input("Enter choice: ")
 
    savePass = False
    if choice == "1":
        savePass = True
    retrievePass = False
    if choice == "2":
        retrievePass = True
 
    if savePass == True:
        break
    if retrievePass == True:
        break
 
sUserFound = False
 
# sAccNameList = ['']
sAccName = ""
 
if savePass == True:
    while 1:
 
        sAccName = "" + input("Enter account name: ")
 
        # Query the database
        c.execute("SELECT * FROM sPasswords")
        records = c.fetchall()
 
        # Loop through the results
        for record in records:
            if record[0] == sAccName:
                sUserFound = True
                # sAccNameList[0] = sAccName
                break
 
        break
 
if sUserFound:
 
    while True:
        print("That account already exists in the database. Do you want to replace the password?")
        print("")
        print("1. Yes")
        print("2. No")
 
        choice = input("Enter choice: ")
 
        if choice == "1":
            replacePass = True
        if choice == "2":
            break
 
        if replacePass:
            print('Generating a new password...')
 
            replacedPass = genPass()
 
            # Query the database
            c.execute('UPDATE sPasswords SET Password = "{}" WHERE Account = "{}"'.format(
                replacedPass, sAccName))
 
            print("The new password is {}".format(replacedPass))
 
            break
 
if not sUserFound:
 
    print("Generating a new password...")
 
    savedPass = genPass()
 
    # Query the database
    c.execute('INSERT INTO sPasswords VALUES("{}", "{}")'.format(
        sAccName, savedPass)) 
 
    print("The saved password is {}".format(savedPass))
 
RetrieveSinglePass = False
RetrieveAllPass = False
 
if retrievePass:
 
    while True:
 
        print("1. Retrieve a single password")
        print("2. Retrieve all passwords")
        print("")
 
        choice = input("Enter choice: ")
 
        if choice == "1":
            RetrieveSinglePass = True
            break
        if choice == "2":
            RetrieveAllPass = True
            break
 
rUserFound = False
 
if RetrieveSinglePass:
 
    while 1:
 
        rAccName = input("Enter account name: ")
 
        # Query the database
        c.execute("SELECT * FROM sPasswords")
        records = c.fetchall()
 
        # Loop through the results
        for record in records:
            if record[0] == rAccName:
                retrievedPass = record[1]
                rUserFound = True
                break
 
        if rUserFound:
            break
        else:
            print("That account doesn't exist in database. Please try again.")
 
if rUserFound:
    print("The password for {} is {}".format(rAccName, retrievedPass))
 
if RetrieveAllPass:
 
    # Query the database
    c.execute("SELECT * FROM sPasswords")
    records = c.fetchall()
 
    accList = []
 
    for record in records:
 
        accName = record[0]
        password = record[1]
 
        accList.append([accName, password])
 
    for i in accList:
        print(i)
 
conn.commit()
 
conn.close()
