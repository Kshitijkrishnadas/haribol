import mysql.connector as sql
link=sql.connect(host="localhost",user="root",passwd="HareKrishna",database="mydb")
if link.is_connected():
    cur=link.cursor()
    cur.execute('insert into student values(5,"Dinesh",39);')
    link.commit()
    link.close()
else:
    print("Error connecting to MySQL.")
