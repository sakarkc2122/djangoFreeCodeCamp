import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    user = "sakar",
    password = "sakar"
)

mycursor = mydb.cursor()

mycursor.execute("CREATE DATABASE mydatabase")
