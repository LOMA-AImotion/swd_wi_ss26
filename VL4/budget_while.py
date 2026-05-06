budget = int(input("Budget?"))
quadrat_zahl = 1 
guthaben = 0

while budget - quadrat_zahl*quadrat_zahl >= 0:
    budget = budget - quadrat_zahl*quadrat_zahl
    guthaben = guthaben + quadrat_zahl*quadrat_zahl
    quadrat_zahl = quadrat_zahl+1

print("Die letzte Zahl, die gepasst hat, war: ", quadrat_zahl-1)
print("Mein Guthaben: ", guthaben)
print("Mein Budget: ", budget)