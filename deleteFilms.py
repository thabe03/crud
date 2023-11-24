import sqlite3
import time
conn = sqlite3.connect('filmflix.db')
cursor = conn.cursor()

def delFilm():
    KeyField = input("Enter ID of film to be deleted: ")
    cursor.execute('SELECT * FROM tblFilms' + ' WHERE filmID' + "=" + KeyField)
    userChoice = cursor.fetchone()
    if userChoice == None:
        print("Sorry, we do not have a film for that record. Please try again.")
        delFilm()
    else:
        for record in userChoice:
            print(record)   
        try:
            cursor.execute("DELETE FROM tblFilms WHERE filmID=" + KeyField)
            conn.commit()
            cursor.execute('SELECT * FROM tblFilms')
            row = cursor.fetchall()
            for record in row:
                print(record)
        except Exception as error:
            print(error)