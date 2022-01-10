import csv

# trennlinie in der ausgabe
def trennlinie():
    anzahlTrennzeichen = 40
    for x in range(anzahlTrennzeichen):
        print("=", end="")
    print("\n")

## datenbank starten und erstellen
# neue datenbank erstellen
def createNewDatabase():
    dbName = input("Name your database: ")
    database = dbName + ".csv"
    with open(database, "w") as file:
        writer = csv.writer(file)
        firstRow = "Username {:>15} {:>10}".format("Password", "URL")
        writer.writerow(firstRow)
    print("The database has been created!")
    return database

# vorhandene datenbank laden
def loadDatabase():
    dbName = input("Type in the database you want to use: ")
    database = dbName + ".csv"
    with open(database, "a") as file:
        writer = csv.writer(file)
    print("The database has been loaded!")
    return database

def showPasswords():
    with open() as file:
        reader = csv.reader(file)
        print(file)

def addPassword():
    None

def deletePassword():
    None

def updatePassword():
    None

if __name__ == '__main__':
    passwordList = [] # liste zum lesen und schreiben der passwörter
    run_menue_1 = True
    run_menue_2 = False

    ## ausgabemenüs
    while run_menue_1:
        # ausgabemenü 1
        trennlinie()
        print("          Password manager")
        trennlinie()
        text = ""
        text1 = "{:>3} Create new password database\n".format("1)")
        text2 = "{:>3} Start with an existing database\n".format("2)")
        text3 = "{:>3} Cancel\n".format("3)")
        print(text, text1, text2, text3)
        trennlinie()

        option = int(input("Choose an option: "))
        # neue datenbank erstellen
        if option == 1:
            createNewDatabase()
            run_menue_1 = False
            run_menue_2 = True
        # mit bestehender datenbank starten
        elif option == 2:
            loadDatabase()
            run_menue_1 = False
            run_menue_2 = True
        # abbrechen
        elif option == 3:
            exit()

    while run_menue_2:
        # ausgabemenü 2
        trennlinie()
        print("          Password manager")
        trennlinie()
        text = ""
        text1 = "{:>3} Show existing passwords\n".format("1)")
        text2 = "{:>3} Add new passwords\n".format("2)")
        text3 = "{:>3} Delete an existing password\n".format("3)")
        text4 = "{:>3} Update password\n".format("4)")
        text5 = "{:>3} Exit\n".format("5)")
        print(text, text1, text2, text3, text4, text5)

        option = int(input("Choose an option: "))
        # passwörter anzeigen
        if option == 1:
            showPasswords()
        # passwort hinzufügen
        elif option == 2:
            addPassword()
        # passwort löschen
        elif option == 3:
            deletePassword()
        # passwort ändern
        elif option == 4:
            updatePassword()
        # abbrechen
        elif option == 5:
            exit()