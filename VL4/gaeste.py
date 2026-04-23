guests = []

guest_name = input("Geben Sie den Namen des Gastes ein (oder 'ende' zum Beenden): ")
while guest_name != 'ende':
    guests.append(guest_name)
    guest_name = input("Geben Sie den Namen des Gastes ein (oder 'ende' zum Beenden): ")

print(f"Die eingegebenen {len(guests)} Gäste sind:")
print(guests)
