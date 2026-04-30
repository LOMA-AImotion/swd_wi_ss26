with open("adjektive.txt", "r", encoding="utf-8") as datei:
    adjektive = datei.read().splitlines()
# Nach dem Ende des with-Blocks wird die Datei automatisch geschlossen, daher ist kein explizites Schließen erforderlich.

#datei = open("adjektive.txt", "r", encoding="utf-8")
#adjektive = datei.read().splitlines()

print(adjektive)