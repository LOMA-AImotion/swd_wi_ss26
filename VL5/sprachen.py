en = {"Hallo_Code": "Hello", "Bye_Code": "Bye"}
de = {"Hallo_Code": "Hallo", "Bye_Code": "Tschüss"}
bv = {"Hallo_Code": "Servus", "Bye_Code": "Servus"}

choice = input("Select language (1 for English, 2 for German, 3 for Bavarian): ")

languages = {"1": en, "2": de, "3": bv}
selected = languages.get(choice, en) # sichere Option en

print(f"Hallo: {selected['Hallo_Code']}")
print(f"Bye: {selected['Bye_Code']}")
