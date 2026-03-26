regen = input("Regnet es? (ja/nein): ").strip().lower() == "ja"

if regen:   
    print("Schränke")
    print("Keller")
    print("Fahrrad")
else: 
    print("Sonne")
    print("Strand")
    print("Eis")
