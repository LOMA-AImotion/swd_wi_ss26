k = int(input("k = ?"))
#menge = {}
menge = set()

for i in range(1, k+1): 
    menge.add((i, "x"*i))

print(menge)
menge2 = {(i, "x"*i) for i in range(1, k+1)}
print(menge2)
menge_sortiert = list(menge)
menge_sortiert.sort()
print(menge_sortiert)