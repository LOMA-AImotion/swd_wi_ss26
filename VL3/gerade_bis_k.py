# Dieses Programm gibt alle Zahlen von 1 bis k aus, wobei k eine vom Benutzer eingegebene Zahl ist.
# Das Programm gibt nur gerade Zahlen aus.

k = int(input("Gib eine Zahl k ein: "))
for i in range(1, k + 1):
    if i % 2 == 0:
        print(i)