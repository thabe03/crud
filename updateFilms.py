import sqlite3
import time
conn = sqlite3.connect('filmflix.db')
cursor = conn.cursor()

def updateFilm():
    keyField = input("Enter the ID of the film to be updated: ")
    returnId = cursor.execute(
        'SELECT * FROM tblFilms' + ' WHERE filmID' + "=" + keyField)
    userChoice = returnId.fetchone()
    if userChoice == None:
        print("Sorry, we do not have a film for that record. Please try again.")
        updateFilm()
    else:
        print(userChoice)
        try:
          field = input(
              "Which field requires updating? (title, yearReleased, rating, duration, genre): ").lower()
          if field not in ("title", "yearreleased", "rating", "duration", "genre"):
              print("Sorry, we couldn't process that instruction.")
              updateFilm()
          else:
            newUpdatedFieldValue = input(
                  "Enter the new value for the field you are updating: ")
            cursor.execute("UPDATE tblFilms SET " + field + "= '" +
                           newUpdatedFieldValue + "' WHERE filmID" + "=" + keyField)
            conn.commit()
            returnAllRecords = cursor.execute('SELECT * FROM tblFilms')
            row = returnAllRecords.fetchall()
            for record in row:
                print(record)
        except ValueError as error:
            print(error)
            updateFilm()
