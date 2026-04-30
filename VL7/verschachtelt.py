def brutto_liste(artikel_liste : list) -> list:
    def brutto(artikel: int) -> float:
        return artikel * 1.19
    
    bruttos = []
    for artikel in artikel_liste:
        bruttos.append(brutto(artikel))
    return bruttos

nettos = [10, 20, 30]
bruttos = brutto_liste(nettos)
print("Nettos:", nettos)
print("Bruttos:", bruttos)  
# not possible: print("Brutto von einem Wert:", brutto(10))