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

if __name__ == '__main__':
    passwordList = [] # liste zum lesen und schreiben der passwörter
    ## ausgabemenüs
    # ausgabemenü 1
    trennlinie()
    print("     Password manager     ")
    trennlinie()
    text = ""
    text1 = "{:>3} Create new password database\n".format("1)")
    text2 = "{:>3} Start with an existing database\n".format("2)")
    text3 = "{:>3} Cancel\n".format("3)")
    print(text, text1, text2, text3)
    trennlinie()

    # ausgabemenü 2
    trennlinie()
    print("     Password manager     ")
    trennlinie()
    text = ""
    text1 = "{:>3} Show existing passwords\n".format("1)")
    text2 = "{:>3} Add new passwords\n".format("2)")
    text3 = "{:>3} Delete an existing password\n".format("3)")
    text4 = "{:>3} Update password\n".format("4)")
    text5 = "{:>3} Exit\n".format("5)")
    print(text, text1, text2, text3, text4, text5)