import mysql.connector as connector
from prettytable import PrettyTable
from prettytable import from_db_cursor
import time
db = connector.connect(host = "localhost", user = "root", passwd = "Anurag2004!", database = 'assignments')
if(db):
    print("SQL Connectivity Successful")

else: print("SQL Conncectivity Failed")


curs = db.cursor(buffered = True)
curs.execute("drop table if exists EMP")

print("1. Create Table EMP")


curs.execute('''create table EMP (
W_ID int primary key,
FIRSTNAME varchar(70),
LASTNAME varchar(70),
CITY varchar(70),
SALARY int
);''')
curs.execute("desc EMP;")
print("Table: \n")
table = PrettyTable()
table.field_names = ["Field", "Type", "Null", "Key", "Default", "Extra"]
for i in curs:
    table.add_row(i)

print(table)



print("\n \n")
print("2. Insert Values Into table EMP")


curs.execute('''insert into EMP values
(102, 'SAM', 'TONES', 'PARIS', 75000),
(105, 'SARAH', 'ACKERMAN', 'NEW YORK', 85000),
(144, 'MANILA', 'SENGUPTA', 'NEW DELHI', 70000),
(210, 'GEORGE', 'SMITH', 'PARIS', 75000),
(255, 'MARY', 'JONES', 'HUSTON', 50000);
''')





inserted_table = PrettyTable()
inserted_table.field_names = ["W_ID", "FIRSTNAME", "LASTNAME", "CITY", "SALARY"]
curs.execute("select * from EMP;")

for i in curs:
    inserted_table.add_row(i)
print(inserted_table)



print("\n \n")
print("3. Display details of employees from Paris")

curs.execute("select * from EMP where CITY = 'PARIS';")

inserted_table.clear_rows()


for i in curs:
    inserted_table.add_row(i)

print(inserted_table)


print("\n \n")


print("4. Alter table to add column department")

curs.execute("alter table EMP add DEPARTMENT varchar(20);")     

curs.execute('''update EMP set DEPARTMENT = "HR" where W_ID = 102;''')
curs.execute('''update EMP set DEPARTMENT = "SALES" where W_ID = 105;''')
curs.execute('''update EMP set DEPARTMENT = "HR" where W_ID = 144;''')
curs.execute('''update EMP set DEPARTMENT = "ADMIN" where W_ID = 210;''')
curs.execute('''update EMP set DEPARTMENT = "SALES" where W_ID = 255;''')
curs.execute('select * from EMP')
inserted_table.clear()
inserted_table.field_names = ["W_ID", "FIRSTNAME", "LASTNAME", "CITY", "SALARY", "DEPARTMENT"]


for i in curs: 
    inserted_table.add_row(i)
print(inserted_table)


print("\n \n")



print("5. Show highest and lowest salary department wise")


curs.execute('''select * from EMP where DEPARTMENT = "HR" order by SALARY desc''')
sal = curs.fetchall()
sal = list(sal)
inserted_table.clear_rows()
inserted_table.add_row(sal[0])
print("Highest salary in HR: ")
print(inserted_table)
print("\n\n")

curs.execute('''select * from EMP where DEPARTMENT = "HR" order by SALARY''')
sal = curs.fetchall()
sal = list(sal)
inserted_table.clear_rows()
inserted_table.add_row(sal[0])
print("Lowest salary in HR: ")
print(inserted_table)
print("\n\n")


curs.execute('''select * from EMP where DEPARTMENT = "SALES" order by SALARY desc''')
sal = curs.fetchall()
sal = list(sal)
inserted_table.clear_rows()
inserted_table.add_row(sal[0])
print("Highest salary in SALES: ")
print(inserted_table)
print("\n\n")

curs.execute('''select * from EMP where DEPARTMENT = "SALES" order by SALARY''')
sal = curs.fetchall()
sal = list(sal)
inserted_table.clear_rows()
inserted_table.add_row(sal[0])
print("Lowest salary in SALES: ")
print(inserted_table)
print("\n\n")







curs.execute('''select * from EMP where DEPARTMENT = "ADMIN"''')
sal = curs.fetchall()
sal = list(sal)
inserted_table.clear_rows()
inserted_table.add_row(sal[0])
print("Admin Salary: ")
print(inserted_table)
print("\n\n")















print("###     Assignment Completed     ###")
