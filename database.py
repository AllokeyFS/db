import sqlite3 as sql
import random
from faker import Faker

conn = sql.connect('mydatabase.db')

cursor = conn.cursor()

cursor.execute("""CREATE TABLE IF NOT EXISTS users
                    (
                    id integer primary key,
                    first_name varchar(20),
                    last_name varchar(30),
                    phone_number varchar(30), 
                    age integer,
                    salary integer)""")

conn.commit()

cursor.execute('''
                CREATE TABLE IF NOT EXISTS children 
                (
                id integer primary key,
                name varchar(20),
                age integer
                )''')

conn.commit()

conn.execute("""
            INSERT INTO users (
            first_name,
            last_name,
            phone_number,
            age,
            salary
            ) VALUES ('elturan','test','+996555555555', 20, 124988)""")

conn.commit()
fake = Faker('ru_RU') 

for _ in range(1,20):
    first_name = f'{fake.first_name()}'
    last_name = f'{fake.last_name()}'
    phone = f'{fake.phone_number()}'
    age = random.randint(10,30)
    salary = random.randint(10000, 50000)


    cursor.execute('''
                    INSERT INTO users(
                    first_name,
                    last_name,
                    phone_number,
                    age,
                    salary                    
                    ) VALUES(?,?,?,?,?)''', (first_name, last_name,phone,age,salary))
conn.commit()

cursor.execute("SELECT first_name, age FROM users WHERE age < 20")
row = cursor.fetchall()
for name in row:
    user_name = name[0]
    user_age = name[1]
    cursor.execute('''
                    INSERT INTO children(
                    name,
                    age
                    ) VALUES (?,?)''', (user_name, user_age))

conn.commit()

# cursor.execute('DELETE FROM users WHERE salary < 15000')
# conn.commit()

# cursor.execute("SELECT phone_number, first_name FROM users")
# row = cursor.fetchall()
# for i in row:
#     print(i)

conn.close()