name = input("Wie heißt du?")
alter = input("Wie alt bist du?")
alter = int(alter)

wahl_alter = 18

if alter > wahl_alter:
	wahl_jahre = alter - wahl_alter
	print("Hallo", name, "Du darfst seit", wahl_jahre, "Jahren wählen.")
elif alter == wahl_alter:
	print("Hallo", name, "Du bist Erstwähler!")
else:
	jahre_bis_wahl = wahl_alter - alter
	print("Hallo", name, "Du darfst in", jahre_bis_wahl, "Jahren wählen.")