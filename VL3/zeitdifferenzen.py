zeiten = [0, 1, 4, 5, 7, 8]
# gesucht: die aufeinander folgenden Differenzen der Zeiten
differenzen = [ zeiten[i+1] - zeiten[i] for i in range(0, len(zeiten)-1)]
print(differenzen)