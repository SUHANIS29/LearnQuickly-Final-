import mysql.connector
import socket


try:
    
    mydb = mysql.connector.connect(
        host="locahost",
        user="root",
        password="1234",
        database="lquick"
        )
    
    print("sucess")
except mysql.connector.Error as e:
    print("no",e)