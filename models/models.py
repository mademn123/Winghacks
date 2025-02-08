# creating a database containing links
import mysql.connector
data_base = mysql.connector.connect (
    host = "localhost",
    user = "user",
    password = "winghacks"
)

cursor_object = data_base.cursor()

cursor_object.execute("CREATE DATABASE winghacks")