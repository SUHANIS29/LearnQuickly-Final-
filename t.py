import mysql.connector


# try:
    
#     mydb = mysql.connector.connect(
#         host="localhost",
#         user="root",
#         password="1234",
#         database="lquick"
#         )
#     cursor=mydb.cursor()
    
#     print("sucess")
#     # query ="insert into logiInfo(name,email,password)values(%s,%s,%s)"
#     # data =("ayush","ayush@123","122345")
#     # cursor.execute(query,data)
#     mydb.commit()
#     cursor.close()
#     mydb.close()
# except mysql.connector.Error as e:
#     print("no",e)

try:
    mydb = mysql.connector.connect(
        host="127.0.0.1",
        user="root",
        password="root",
        database="lquick"
        )
    paswd1=567
    userid="ayushsolanki"
    cursor=mydb.cursor()
    query ="update logiInfo set password = %s where name = %s"
    data = (paswd1,userid)
    cursor.execute(query,data)
    mydb.commit()
    cursor.close()

    mydb.close()
    

    print("success")

except mysql.connector.Error as e:
    print("no",e)