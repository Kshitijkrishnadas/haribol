import mysql.connector as sql
conn=sql.connect(host='localhost',user='root',passwd='HareKrishna',database='electronic_shop')
cur=conn.cursor()
if conn.is_connected:
    print('                                             ELECTRONIC SHOP SYSTEM')
    print('                                             1.Admin')
    print('                                             2.Customers')
choice=int(input('                                             Enter the choice: '))
if choice == 1:
    pw = 'GaurNitai'
    passwrd = input('Enter the password: ')
    if passwrd == pw:
        print('                                             1.Enter data for Items')
        print('                                             2.Enter data for Labour')
        print('                                             3.Enter data for Customers')
        choose = int(input('Enter the choice for adding data: '))
        if choose == 1:
            item = input('Enter the name of item: ')
            availability = int(input('Availability of the item: '))
            price = int(input('Enter the price of item in rupees: '))
            cur.execute("INSERT INTO ITEMS VALUES('" + item + "'," + str(availability) + "," + str(price) + ")")
            print('ENTRY SUCCESSFUL.')
            conn.commit()
        elif choose == 2:
            name = input('Enter the name of labour: ')
            age = int(input('Enter the age: '))
            place = input('Enter the place of the labour: ')
            dept = input('Enter the name of the department: ')
            cur.execute("INSERT INTO LABOURS VALUES('" + name + "','" + str(age) + "','" + place + "','" + dept + "')")
            print('ENTRY SUCCESSFUL.')
            conn.commit()
        elif choose == 3:
            name = input('Enter the name of the customer: ')
            age = int(input('Enter the age: '))
            place = input('Enter the place of the customer: ')
            item = input('Enter the item bought: ')
            cur.execute("INSERT INTO CUSTOMER VALUES('" + name + "','" + str(age) + "','" + place + "','" + item + "')")
            print('ENTRY SUCCESSFUL.')
            conn.commit()
    else:
        print('Invalid Login!')
elif choice == 2:
    print('                                             1.Display the list of Items.')
    print('                                             2.Display the list of Labours.')
    print('                                             3.Display the list of Customers.')
    ch = int(input('Enter the choice: '))
    if ch == 1:
           print()
           cur.execute('SELECT * FROM ITEMS')
           dataa = cur.fetchall()
           print('List of items: ')
           for row in dataa:
               print()
               print('Item: ',row[0])
               print('Availablity: ',row[1])
               print('Price: ',row[2])
    elif ch == 2:
        print()
        cur.execute('SELECT * FROM LABOURS')
        data = cur.fetchall()
        print('List of Labours:')
        for row in data:
            print()
            print('Name: ',row[0])
            print('Age: ',row[1])
            print('Place: ',row[2])
            print('Department: ',row[3])
    elif ch == 3:
        print()
        cur.execute('SELECT * FROM CUSTOMER')
        datas = cur.fetchall()
        print('List of customers:')
        for row in datas:
            print()
            print('Name: ',row[0])
            print('Age: ',row[1])
            print('Place: ',row[2])
            print('Item bought: ',row[3])
