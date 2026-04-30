import random
#random.seed(1)
for i in range(3):
    zufallszahl = random.randint(1, 100)
    print("Die Zufallszahl ist:", zufallszahl)

farben = ["rot", "grün", "blau", "gelb", "lila"]
zufallsfarbe = random.choice(farben)
print("Die Zufallsfarbe ist:", zufallsfarbe)
