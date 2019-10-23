import sqlite3
import time
import datetime
import random

connection=sqlite3.connect('testDatabase.db')
c=connection.cursor()


def create_table():
    c.execute("CREATE TABLE IF NOT EXISTS student(rollno INTEGER,name TEXT)")

def insert_records():
    c.execute("INSERT INTO student VALUES(1112,'Steve')")
    connection.commit()
    c.close()
    connection.close()

create_table()
insert_records()

