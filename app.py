import sqlite3

#Lidhja e databazes
db=sqlite3.connect('database.db')
cursor=db.cursor()

with open('schema.sql' ,'r') as f:
    cursor.executescript(f.read())

#First function create a mentee
def create_mentee():
    full_name = input("Enter your full name: ")
    email = input("Enter your full email: ")
    cohort = input("Enter your cohort: ")
    cursor.execute(
        'INSERT OR IGNORE INTO mentees(full_name,email,cohort) VALUES (?, ?, ?)',
        (full_name, email, cohort)
    )
    db.commit()

create_mentee()   