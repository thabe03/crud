import sqlite3
import time
conn = sqlite3.connect('filmflix.db')
cursor = conn.cursor()

def addNewFilm():
    films = []
    title = input("Enter the title of the film: ")
    yearReleased = input("Enter the year the film was released: ")
    rating = input("Enter the rating of the film (PG, G, or R): ")
    duration = input("Enter the film duration: ")
    genre = input("Enter the genre of the film: ")

    films.append(title)
    films.append(yearReleased)
    films.append(rating)
    films.append(duration)
    films.append(genre)

    try:
        cursor.execute('INSERT INTO tblFilms VALUES (NULL,?,?,?,?,?)', films)
        conn.commit()
        print("Film Record Added")
        cursor.execute('SELECT * FROM tblFilms')
        row = cursor.fetchall()
        for record in row:
            print(record)
    except:
        print("film record not added")
