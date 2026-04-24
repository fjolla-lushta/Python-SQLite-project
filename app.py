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

#Second function prints all mentees, one per line, sorted by full_name
def list_mentees():
    cursor.execute('SELECT full_name FROM mentees ORDER BY full_name')
    mentees=cursor.fetchall()
    for mentee in mentees:
        print(mentee[0])

list_mentees()


