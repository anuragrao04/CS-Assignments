import mysql.connector as connector
from prettytable import PrettyTable
from prettytable import from_db_cursor
import time
db = connector.connect(host = "localhost", user = "root", passwd = "Anurag2004!")
if(db):
    print("SQL Connectivity Successful")

else: print("SQL Conncectivity Failed")

curs = db.cursor(buffered = True)
curs.execute("drop database if exists assignments")
curs.execute("create database assignments")
print("database created")
print('\n \n')


print("Creating table")
for i in range(5):
    print('.', end = '')



print()
curs.execute("use assignments")
curs.execute('''create table students (
Sno int primary key,
Sname varchar(70),
Gender varchar(1),
Age int,
Fees int
);''')
print("Table Created")
curs.execute("desc students;")
print("Table: \n")
table = PrettyTable()
table.field_names = ["Field", "Type", "Null", "Key", "Default", "Extra"]
for i in curs:
    table.add_row(i)

print(table)



print("\n \n")
print("Inserting Values...")

curs.execute('use assignments')
curs.execute('''insert into students values
(1, 'Ashish', 'M', 17, 6550),
(2, 'Madhulika', 'F', 20, 7124),
(3, 'Niti Singh', 'F', 21, 18000),
(4, 'Pratyush', 'M', 18, 1200),
(5, 'Anand Seth', 'M', 16, 19500);
''')


print("Values inserted")
print("\n \n")

inserted_table = PrettyTable()
inserted_table.field_names = ["Sno", "Sname", "Gender", "Age", "Fees"]
curs.execute("select * from students;")

for i in curs:
    inserted_table.add_row(i)
    print(inserted_table)



print("\n \n")
print("Updating age...")

curs.execute("update students set age = 20 where Sno = 4;")
curs.execute("select * from students where Sno = 4;")
print("\n \n")
print("Age updated")
print("\n \n")
inserted_table.clear_rows()


for i in curs:
    inserted_table.add_row(i)

print(inserted_table)

print("\n \n")

print("Arranging table in the order of names...")

print("\n \n")

print("Table arranged")

print("\n \n")

inserted_table.clear_rows()
curs.execute("select * from students order by Sname desc;")

for i in curs:
    inserted_table.add_row(i)

print(inserted_table)


print("\n \n")



print("Adding column 'course'...")

print("\n \n")

curs.execute("alter table students add Course varchar(70);")     #NOT 50


curs.execute('''update students set course = "C" where Sno = 1;''')
curs.execute('''update students set course = "C--" where Sno = 2;''')
curs.execute('''update students set course = "Python" where Sno = 3;''')
curs.execute('''update students set course = "Java" where Sno = 4;''')
curs.execute('''update students set course = "JavaScript" where Sno = 5;''')


print("Column was added.")
print("\n \n")


curs.execute("select * from students")
inserted_table.clear()
inserted_table.field_names = ["Sno", "Sname", "Gender", "Age", "Fees", "Course"]



for i in curs:
    inserted_table.add_row(i)

print(inserted_table)

print("\n \n")

print("Calculating lowest and highest fees")
print("Calculated")
print("\n \n")
curs.execute('select * from students order by Fees;')

inserted_table.clear_rows()
inserted_table.add_row(curs.fetchone())
print("Lowest: ")
print(inserted_table)


print("\n \n")

curs.execute('select * from students order by Fees desc;')

inserted_table.clear_rows()
inserted_table.add_row(curs.fetchone())
print("Highest: ")
print(inserted_table)


print("\n \n")

print("###     Assignment Completed     ###")
