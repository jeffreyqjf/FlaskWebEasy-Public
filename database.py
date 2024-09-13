import sqlite3

data = sqlite3.connect('data.db')
cursor = data.cursor()
try:
    cursor.execute('''create table user(
    name varchar(20)primary key,
    password int(20))
    ''')
    cursor.execute('''create table loading(
    name varchar(20)primary key)
    ''')
    cursor.execute('''create table leaveword(
    name varchar(20),
    value varchar(100))
    ''')
    data.commit()
except:
    print('error')

#cursor.execute('''insert into user values(1,1)''')
'''data.commit()
cursor.close()
data.close()
print('finish')'''
'''
cursor.execute("select*from leaveword")
result = cursor.fetchall()
print(result)
cursor.close()
data.close()
print('finish')
'''

cursor.execute('''insert into user values('吴',123456)''')
cursor.execute('''insert into user values('廖',1234567)''')
cursor.execute('''insert into user values('潘',12345678)''')
cursor.execute('''insert into user values('钱',1)''')
data.commit()
cursor.close()
data.close()
