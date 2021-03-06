import csv
import os.path

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
    with open(database, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Username", "Password", "URL"])
    print("The database has been created!")
    return database

# vorhandene datenbank laden
def loadDatabase():
    correctInput = False
    while not correctInput:
        dbName = input("Type in the database you want to use: ")
        database = dbName + ".csv"
        if os.path.isfile(database):
            print("The database has been loaded!")
            correctInput == True
            return database
        else:
            print("This database doesn't exist!")

# passwörter der entsprechenden datenbank anzeigen
def showPasswords(database):
    with open(database, "r") as file:
        reader = csv.reader(file)
        for row in reader:
            print("{0:<20} {1:<20} {2:<20}".format(row[0], row[1], row[2]))

# neues passwort hinzufügen
def addPassword(database):
    username = input("Type in your username: ")
    password = input("Type in your password: ")
    url = input("Type in your URL: ")
    with open(database, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([username, password, url])

# passwort löschen
def deletePassword(database, list):
    with open(database, "r") as file:
        reader = csv.reader(file)
        for row in reader:
            list += [row]
    passwordToDelete = input("Type in the password you want to delete: ")
    if passwordToDelete != "Password":
        z = 0
        while z in range(len(list)):
            if passwordToDelete == list[z][1]:
                list.pop(z)
            z += 1
    else:
        print("Not deletable!")
    with open(database, "w", newline="") as file:
        writer = csv.writer(file)
        for row in list:
            writer.writerow(row)

# passwort ändern
def updatePassword(database, list):
    with open(database, "r") as file:
        reader = csv.reader(file)
        for row in reader:
            list += [row]
    passwordToUpdate = input("Type in the password you want to update: ")
    password = input("Type in the new password: ")
    if passwordToUpdate != "Password":
        z = 0
        while z in range(len(list)):
            if passwordToUpdate == list[z][1]:
                list[z][1] = password
            z += 1
    else:
        print("Not deletable!")
    with open(database, "w", newline="") as file:
        writer = csv.writer(file)
        for row in list:
            writer.writerow(row)

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
            database = createNewDatabase()
            run_menue_1 = False
            run_menue_2 = True
        # mit bestehender datenbank starten
        elif option == 2:
            database = loadDatabase()
            run_menue_1 = False
            run_menue_2 = True
        # abbrechen
        elif option == 3:
            exit()

    while run_menue_2:
        # ausgabemenü 2
        trennlinie()
        print("        Password manager (", database, ")")
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
            showPasswords(database)
        # passwort hinzufügen
        elif option == 2:
            addPassword(database)
        # passwort löschen
        elif option == 3:
            deletePassword(database, passwordList)
        # passwort ändern
        elif option == 4:
            updatePassword(database, passwordList)
        # abbrechen
        elif option == 5:
            exit()