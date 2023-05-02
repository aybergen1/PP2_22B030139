import psycopg2
import csv

con = psycopg2.connect(host="localhost", database="postgres", user="postgres", password="aybek777667")
current = con.cursor()
def search():
    n = input("Contact Name or Number: ")
    current.execute(f"""SELECT * FROM Phone_Book WHERE name LIKE '{n}' OR phone_number LIKE '{n}';""")
    print(current.fetchone())
create = """CREATE TABLE Phone_Book (
    name VARCHAR(255) NOT NULL,
    phone_number VARCHAR(255) NOT NULL
);
"""
insert = """
    INSERT INTO PhoneBook VALUES(%s,%s) returning *;
"""

update1 = """
    UPDATE PhoneBook SET name = %s WHERE phone_number = %s;
"""
update2 = """
    UPDATE PhoneBook SET phone_number = %s WHERE name = %s;
"""

select = """
    SELECT * FROM PhoneBook
"""
select1 = """
    SELECT * FROM PhoneBook WHERE name= %s ;
"""
select2 = """
   SELECT * FROM PhoneBook WHERE phone_number LIKE %s;

"""
delete = """
    DELETE FROM PhoneBook WHERE name = %s;
"""
delete1 = """
    DELETE FROM PhoneBook WHERE phone_number LIKE %s;
"""


while True:


    n = int(input("0 - create,\n1 - insert csv,\n2 - insert console,\n3 - update of name,\n "
                  "31 - update of phone,\n4 - select,\n 41 - select of name,\n 42 - select of number,\n5 - delete,"
                  "\n 51 - delete of number,\n6 - проверка,\n"))
    if n == 0:
        current.execute(create)
    if n == 1:
        with open("ca2.csv", 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                name, phoneNumber = row
                current.execute(insert, (name, phoneNumber))
        con.commit()
    if n == 2:
        name = input("name:")
        phoneNumber = input("Number:")
        current.execute(insert, (name, phoneNumber))
        con.commit()

    if n == 3:
        name = input("newName:")
        phone_number = input("number:")
        current.execute(update1, (name, phone_number))
        con.commit()
    if n == 31:
        name = input("Name:")
        phone_number = input("newnumber:")
        current.execute(update2, (phone_number,name))
        con.commit()
    if n == 4:
        current.execute(select)
        print(*current.fetchall(), sep='\n')
        con.commit()
    if n == 41:
        name = input("Name: ")
        current.execute(select1,[name])
        print(*current.fetchall(), sep='\n')
        con.commit()
    if n == 42:
        phone_number = input("Number: ")
        current.execute(select2, [phone_number])
        print(*current.fetchall(), sep='\n')
        con.commit()
    if n == 5:
        name = input("Name:")
        current.execute(delete, [name])
        con.commit()
    if n == 51:
        phone_number = input("Number:")
        current.execute(delete1, [phone_number])
        con.commit()
    if n == 6:
        search()

current.close()
con.commit()
con.close()