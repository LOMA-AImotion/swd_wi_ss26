def lese_von_datei(dateiname):
    with open(dateiname, "r", encoding="utf-8") as datei:
        inhalt = datei.read().splitlines()
    return inhalt
