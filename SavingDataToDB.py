# -*- coding: utf-8 -*-

#This part saving data from file to sql database. This is 2nd part of application (last).

import mysql.connector as db

data = []

#Reading data from file "data.txt"
file = open("data.txt", "r")

for i in file:
    data.append(i[:-1])

file.close()

#Saving to database on localhost
mydb = db.connect(host="localhost", user="root", password="", database="cepik20")
mydbcursor = mydb.cursor()

for i in data:
    mydbcursor.execute(i)

print("Data was written")