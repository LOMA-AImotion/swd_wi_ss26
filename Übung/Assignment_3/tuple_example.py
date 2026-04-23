customers = [
    ["Max", "Mustermann", "01.01.83"],
    ["Martina", "Musterfrau", "02.02.84"],
    ["Gabi", "Meier", "03.03.85"]
    ]

max_mustermann = ("Max", "Mustermann", "01.01.83")

first_name, last_name, birth_date = max_mustermann

customers = [
    ("Max", "Mustermann", "01.01.83"),
    ("Martina", "Musterfrau", "02.02.84"),
    ("Gabi", "Meier", "03.03.85")
]

for first_name, last_name, birth_date in customers:
    print(last_name)
