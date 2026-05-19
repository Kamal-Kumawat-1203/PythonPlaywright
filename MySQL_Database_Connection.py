import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="kamalroot",
    database="pydb"
)

# # I want to print only a single tuple in the result
# mycursor = mydb.cursor()
# mycursor.execute("SELECT emp_name FROM employee where emp_id=1024")
# myresult = mycursor.fetchone()
# print(myresult[0])

# # If, I want to print single row
# mycursor = mydb.cursor()
# mycursor.execute("SELECT * FROM employee where emp_id=1023")
# myresult = mycursor.fetchmany(1)
# print(myresult)

# # If, I want to print many rows
# mycursor = mydb.cursor()
# mycursor.execute("SELECT * FROM employee order by emp_id asc limit 4")
# myresult = mycursor.fetchmany(4)
# for x in myresult:
#     print(x)

# If, I want to print all table data
mycursor = mydb.cursor()
mycursor.execute("SELECT * FROM employee")
myresult = mycursor.fetchall()
for x in myresult:
    print(x)
