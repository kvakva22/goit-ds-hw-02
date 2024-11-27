from faker import Faker
import sqlite3 as sql
import random

fake=Faker()

with sql.connect("D:\GoIt\sqlite\homewrk") as con:
    cur = con.cursor()

    con.execute("PRAGMA foreign_keys = ON;")
    con.commit()

    cur.execute("""CREATE TABLE IF NOT EXISTS status (
    id INTEGER PRIMARY KEY,
    name VARCHAR(50) UNIQUE
    );""")

    cur.execute("""INSERT OR REPLACE INTO status(id, name) VALUES ('1','new'), ('2', 'in progress'), ('3', 'completed');""")
    con.commit()

    def fake_users(records):
        cur.execute("DROP TABLE users")

        cur.execute("""CREATE TABLE users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        fullname VARCHAR(100),
        email VARCHAR(100) UNIQUE
        ); """)
        con.commit()

        for record in range(records):
            fakename = fake.name()
            email=fake.unique.email()
            cur.execute("INSERT INTO users(fullname, email)  VALUES (?,?)", (fakename, email))
        con.commit()

    
    def fake_tasks(n):
        cur.execute("DROP TABLE tasks")

        cur.execute("""CREATE TABLE tasks (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title VARCHAR(100),
        description TEXT,
        status_id INTEGER,
        user_id INTEGER,
        FOREIGN KEY (status_id) REFERENCES status (id),
        FOREIGN KEY (user_id) REFERENCES users (id) ON DELETE CASCADE
        );""")
        con.commit()

        cur.execute("SELECT id From users")
        fakeusers_id = [el[0] for el in cur.fetchall()]  #Fetchall повертає список кортежів (Наприклад: [(1, ), (2, )]), а нам просто потрбіне перший елемент цього кортежа.
        

        cur.execute("SELECT id FROM status")
        fakestatus_id = [el[0] for el in cur.fetchall()]
        
        for i in range(n):
            faketitle = fake.sentence(nb_words=8)
            fdescription = fake.text()

            cur.execute("INSERT INTO tasks(title, description, status_id, user_id) VALUES (?, ?, ?, ?)", (faketitle, fdescription, random.choice(fakestatus_id), random.choice(fakeusers_id)))
        con.commit()

    fake_users(10)
    fake_tasks(20)


