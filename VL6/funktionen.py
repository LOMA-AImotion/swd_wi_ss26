def area(width, height):
    print("In der Funktion area")
    print(width*height)
    return width * height

def flaechen_daten(width : float, 
                   height : float) -> dict:
    return {"info": (width * height, width, height), "flaeche": width * height }

print("Hallo")
flaecheninhalt = area(5, 3)
print("Flächeninhalt:", flaecheninhalt)
preis = flaecheninhalt * 20
print("Der Preis für ein Rechteck mit Breite 5 und Höhe 3 ist:", preis)

daten = flaechen_daten()
print("Daten:", daten)