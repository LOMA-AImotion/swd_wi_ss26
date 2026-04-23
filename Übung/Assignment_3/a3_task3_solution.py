"""
task3_solution.py
Transformations of loops. 
L.L.
"""


print(20*"-")    
print("Converting list comprehension to for loop.")

customers = [
    ["Max", "Mustermann", "01.01.83"],
    ["Martina", "Musterfrau", "02.02.84"],
    ["Gabi", "Meier", "03.03.85"]
]

# last_names = [person[1] for person in customers]

last_names = []
for c in customers: 
    last_names.append(c[1])
    
print(f"Last names: {last_names}")

# ---------------------------------
print(20*"-")    
print("Converting for to while.")

numbers = [1, 4, 2, 8, 5]
squared_numbers = []

i = 0 
while i < len(numbers):
    squared_numbers.append(numbers[i]**2)
    i += 1

print(f"Squared numbers: {squared_numbers}")

# ---------------------------------
print(20*"-")    
print("Converting while to for.")

print("Problem!")
# Doesn't work without advanced Python tricks! 
 