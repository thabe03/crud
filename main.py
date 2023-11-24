import readFilms
import createFilms
import updateFilms
import deleteFilms

def menuOptions():
    options = 0
    while options not in ["1", "2", "3", "4", "5"]:
        print("\nWelcome to FilmFlix Main Menu:")
        print("\n1. Search Existing Films")
        print("\n2. Create a New Film Record")
        print("\n3. Update an Existing Film Record")
        print("\n4. Delete a Film Record")
        print("\n5. Exit")
        options = input("\nEnter one of the numbered options above: ")
        if options not in ["1", "2", "3", "4", "5"]:
            print("\nInput was not in the list of options. Please try again.")
            menuOptions()
    return options


mainProgram = True
while mainProgram == True: #mainMenu peut devenir un int
    mainMenu = menuOptions()
    if mainMenu == "1":
        readFilms.readFilmsFunc()
    elif mainMenu == "2":
        createFilms.addNewFilm()
    elif mainMenu == "3":
        updateFilms.updateFilm()
    elif mainMenu == "4":
        deleteFilms.delFilm()
    else:
        mainProgram = False
        quit()
