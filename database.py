
import sqlite3

#creating table in database
def create_table():
    conn = sqlite3.connect('test.db')
    print ("Opened database successfully")
    c = conn.cursor()
    c.execute('''CREATE TABLE movies (
             NAME           TEXT    NOT NULL,
             ACTOR            TEXT     NOT NULL,
             ACTRESS        TEXT,
             DIRECTOR         TEXT,
             YEAR INT)''')

    print ("Table created successfully")

    conn.commit()
    conn.close()
    
# Retrive all data from table
def retrive_all():
    conn =  sqlite3.connect('test.db')
    c = conn.cursor()
    c.execute("SELECT * from movies")
    items = c.fetchall()
    for i in items:
        print(i)
    conn.commit()
    conn.close()

# create or insert data into database table
def create_many():
    conn =  sqlite3.connect('test.db')
    c = conn.cursor()
    movie_name = str(input("Enter movie name"))
    actor = str(input("Enter actor name"))
    actress = str(input("Enter actress name"))
    director = str(input("Enter director name"))
    year = str(input("Enter movie year"))
    c.execute("INSERT INTO movies VALUES (?,?,?,?,?)",(movie_name,actor,actress,director,year))
    conn.commit()
    conn.close()

#Retrive data by name
def retrive_by_name():
    conn =  sqlite3.connect('test.db')
    c = conn.cursor()
    c.execute("SELECT * from movies WHERE actor = ' Sidharth Malhotra' ")
    items = c.fetchall()
    for i in items:
        print(items)
    conn.commit()
    conn.close()
