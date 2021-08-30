import mysql.connector as connector
from prettytable import PrettyTable
from prettytable import from_db_cursor
import time
db = connector.connect(host = "localhost", user = "root", passwd = "Anurag2004!", database = 'assignments')
if(db):
    print("SQL Connectivity Successful")

else: print("SQL Conncectivity Failed")


curs = db.cursor(buffered = True)
curs.execute("drop table if exists SPORTS")

print("1. Create Table SPORTS")


curs.execute('''create table SPORTS(
GCode int primary key,
GameName varchar(70),
No_Players int,
PrizeMoney int
);''')
curs.execute("desc SPORTS;")
print("Table: \n")
table = from_db_cursor(curs)

print(table)



print("\n \n")
print("2. Insert Values Into table SPORTS")


curs.execute('''insert into SPORTS values
(101, 'Carrom Board', 2, 5000),
(102, 'Table Tennis', 2, 12000),
(103, 'Lawn Tennis', 4, 8000),
(105, 'Chess', 2, 9000),
(108, 'Table Tennis', 4, 25000);
''')





inserted_table = from_db_cursor(curs)
curs.execute("select * from SPORTS;")

inserted_table = from_db_cursor(curs)

print(inserted_table)



print("\n \n")
print("3. Display count of players enrolled for each game")

curs.execute("select sum(No_Players) from SPORTS where GameName = 'Carrom Board';")
carrom_sum = (curs.fetchone())
carrom_sum = int(carrom_sum[0])



curs.execute("select sum(No_Players) from SPORTS where GameName = 'Table Tennis';")
table_tennis_sum = (curs.fetchone())
table_tennis_sum = int(table_tennis_sum[0])


curs.execute("select sum(No_Players) from SPORTS where GameName = 'Lawn Tennis';")
lawn_tennis_sum = (curs.fetchone())
lawn_tennis_sum = int(lawn_tennis_sum[0])


curs.execute("select sum(No_Players) from SPORTS where GameName = 'Chess';")
chess_sum = (curs.fetchone())
chess_sum = int(chess_sum[0])

inserted_table.clear()
inserted_table.field_names = ["Game", "Number Of Players"]
table_list = {("Carrom Board", carrom_sum), ("Table Tennis", table_tennis_sum), ("Lawn Tennis", lawn_tennis_sum), ("Chess", chess_sum) }
for i in table_list:
    inserted_table.add_row(i)
    
    
print(inserted_table)


print("\n \n")


print("4. Alter table to add column Date")

curs.execute("alter table SPORTS add Date date;")     

curs.execute('''update SPORTS set Date = "2020-03-14" where GCode = 101;''')
curs.execute('''update SPORTS set Date = "2021-12-03" where GCode = 102;''')
curs.execute('''update SPORTS set Date = "2020-03-05" where GCode = 103;''')
curs.execute('''update SPORTS set Date = "2020-09-03" where GCode = 105;''')
curs.execute('''update SPORTS set Date = "2020-08-12" where GCode = 108;''')
curs.execute('select * from SPORTS')
inserted_table = from_db_cursor(curs)

print(inserted_table)


print("\n \n")



print("5. Display total count, sum of PrizeMoney of players of Table Tennis")


curs.execute('''select GameName, sum(No_Players) as Total_No_Player, sum(PrizeMoney) as Total_Prize_Money from SPORTS where GameName = "Table Tennis"''')
inserted_table = from_db_cursor(curs)
print(inserted_table)
print("\n\n")



print("6. Display records in descending order based on PrizeMoney")
curs.execute("Select * from SPORTS order by PrizeMoney desc")
inserted_table = from_db_cursor(curs)
print(inserted_table)
print("\n\n")




print("###     Assignment Completed     ###")
