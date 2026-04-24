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


#Third function changes a mentee's cohort by id
def update_mentee(mentee_id=None, new_cohort=None):
    if mentee_id is None:
        mentee_id = input("Enter mentee id: ")
    if new_cohort is None:
        new_cohort = input("Enter the new cohort: ")

    cursor.execute(
        'UPDATE mentees SET cohort = ? WHERE id = ?',
        (new_cohort, mentee_id)
    )

    if cursor.rowcount == 0:
        print(f"No mentee found with id {mentee_id}.")
    else:
        db.commit()
        print(f"Mentee {mentee_id} cohort updated to {new_cohort}.")

update_mentee()