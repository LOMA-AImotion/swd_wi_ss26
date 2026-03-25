price = float(input("Wie teuer ist das Produkt? "))
money_given = float(input("Wie viel wurde gezahlt? "))

change = money_given - price 

# Both prints are equivalent, but I prefer the second one 
print("Das Rückgeld beträgt", change, "€")
print(f"Das Rückgeld beträgt {change}€")

if money_given < price:
    print(f"Sie haben {-1*change}€ zu wenig bezahlt :(")
else:
    print(f"Das Rückgeld beträgt {change}€")

