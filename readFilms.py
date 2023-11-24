import sqlite3
import time
conn = sqlite3.connect('filmflix.db')
cursor = conn.cursor()

def readFilmsFunc():
  cursor.execute('SELECT * FROM tblFilms')
  row = cursor.fetchall()
  for record in row:
      print(record)
  toSearchByIdOrNotToSearchByID = str(
      input("Would you like to search by film ID? (Y/N) ")).lower()
  try:
      if ((toSearchByIdOrNotToSearchByID == 'y') or (toSearchByIdOrNotToSearchByID == 'yes')):
          searchFilmById()
      elif ((toSearchByIdOrNotToSearchByID == 'n') or (toSearchByIdOrNotToSearchByID == 'no')):
          toSearchByTitleOrNotToSearchByTitle()
  except ValueError as error:
      print("Please enter valid inputs")
      print(error)
      readFilmsFunc()


def toSearchByTitleOrNotToSearchByTitle():
    searchByTitleOrNotToSearchByTitle = str(
        input("Would you like to search by film title? (Y/N) ")).lower()
    try:
        if ((searchByTitleOrNotToSearchByTitle == 'y') or (searchByTitleOrNotToSearchByTitle == 'yes')):
            searchByTitle()
        elif ((searchByTitleOrNotToSearchByTitle == 'n') or (searchByTitleOrNotToSearchByTitle == 'no')):
            print("You have exited the search menu. Returning to the main menu.")
        else:
            print("Please enter valid inputs")
            toSearchByTitleOrNotToSearchByTitle()
    except ValueError as error:
        print("Please enter valid inputs")
        print(error)
        toSearchByTitleOrNotToSearchByTitle()

def searchFilmById():
    filmID = input("Enter ID of film to search for: ")
    cursor.execute('SELECT * FROM tblFilms WHERE filmID=' + filmID)
    row = cursor.fetchall()
    if row == []:
        print("Sorry, we do not have a film for that record. Please try again.")
        searchFilmById()
    else:
        for record in row:
            print(record)
        toSearchByTitleOrNotToSearchByTitle()

def searchByTitle():
    searchByKeyword = input("Please enter part of the film title. ")
    tupleConvertedSearchByKeyword = ('%'+searchByKeyword+'%',)
    query = "SELECT * FROM tblFilms WHERE title like ?"
    try:
        cursor.execute('SELECT * FROM tblFilms')
        my_cursor = cursor.execute(query, tupleConvertedSearchByKeyword)
        row = my_cursor.fetchall()
        if row == []:
            print("No results found. Please try again.")
            searchByTitle()
        else:
            for record in row:
                print(record)
    except ValueError as error:
        print(error,
              "\nError: sorry, we couldn't find any film with that keyword. Please try a new keyword.")
        searchByTitle()
