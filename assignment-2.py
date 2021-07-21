import mysql.connector as connector
from prettytable import PrettyTable
from prettytable import from_db_cursor
import time
db = connector.connect(host = "localhost", user = "root", passwd = "Anurag2004!", database = 'assignments')
if(db):
    print("SQL Connectivity Successful")

else: print("SQL Conncectivity Failed")


curs = db.cursor(buffered = True)
curs.execute("drop table if exists lab")

print("Creating table")
for i in range(5):
    print('.', end = '')



print()

curs.execute('''create table lab (
No int primary key,
ItemName varchar(70),
CostPerItem int,
Quantity int,
Warranty int,
Operational int
);''')
print("Table Created")
curs.execute("desc lab;")
print("Table: \n")
table = PrettyTable()
table.field_names = ["Field", "Type", "Null", "Key", "Default", "Extra"]
for i in curs:
    table.add_row(i)

print(table)



print("\n \n")
print("Inserting Values...")


curs.execute('''insert into lab values
(1, 'Computer', 60000, 9, 2, 7),
(2, 'Printer', 15000, 3, 4, 2),
(3, 'Scanner', 18000, 1, 3, 1),
(4, 'Camera', 21000, 2, 1, 1),
(5, 'Switch', 8000, 1, 2, 1);
''')


print("Values inserted")
print("\n \n")

inserted_table = PrettyTable()
inserted_table.field_names = ["No", "ItemName", "CostPerItem", "Quantity", "Warranty", "Operational"]
curs.execute("select * from lab;")

for i in curs:
    inserted_table.add_row(i)
print(inserted_table)



print("\n \n")
print("Updating Quantity...")

curs.execute("update lab set Quantity = 10 where ItemName = 'Printer';")
curs.execute("select * from lab where ItemName = 'Printer';")
print("\n \n")
print("Quantity updated")
print("\n \n")
inserted_table.clear_rows()


for i in curs:
    inserted_table.add_row(i)

print(inserted_table)

print("\n \n")

print("Arranging table in the descending order of ItemNames...")

print("\n \n")

print("Table arranged")

print("\n \n")

inserted_table.clear_rows()
curs.execute("select * from lab order by ItemName desc;")

for i in curs:
    inserted_table.add_row(i)

print(inserted_table)


print("\n \n")





print("Calculating CostPerItem > 20000...")
print("Calculated")
print("\n \n")
curs.execute('select ItemName from lab where CostPerItem > 20000;')

inserted_table.clear()
inserted_table.field_names = ["ItemName"]
for i in curs:
    inserted_table.add_row(i)
print("Items with CostPerItem > 20000:")
print(inserted_table)


print("\n \n")

print("Calculating Warranty = 2 years...")
curs.execute('select ItemName from lab where Warranty = 2')

inserted_table.clear_rows()
for i in curs:
    inserted_table.add_row(i)
print("Items with warranty of 2 years:")

print(inserted_table)


print("\n \n")

print("###     Assignment Completed     ###")
