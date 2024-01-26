import mysql.connector 

mydb = mysql.connector.connect(    
    host = "localhost",
    user = "root",
    password = "47Billion@123",
    database="office")

print(mydb)

cursor=mydb.cursor()

cursor.execute("show tables")
for x in cursor:
    print(x)

cursor.execute("select * from employees")
for x in cursor:
    print(x)
