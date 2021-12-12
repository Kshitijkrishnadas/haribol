import mysql.connector as sql
link=sql.connect(host="localhost",user="root",passwd="HareKrishna",database="mydb")
if link.is_connected():
    cur=link.cursor()
    cur.execute("select * from student;")
    record=cur.fetchall()
    print("Table contains following records:")
    for i in record:
        print(i)
    link.close()
else:
    print("Error connecting to MySQL.")
