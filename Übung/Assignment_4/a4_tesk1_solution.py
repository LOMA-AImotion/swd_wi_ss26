"""
task1_solution.py
List comprehensions part 2
L.L.
"""

mixed_strings = ['H', 'P', 'E', 'E', 'L', 'T', 'L', 'E', 'O', 'R']

hello = [character for i, character in enumerate(mixed_strings) if i%2 == 0]
peter = [character for i, character in enumerate(mixed_strings) if i%2 == 1]

print(hello)
print(peter)

parts = [(1, "500-1", "Hammer", 2, "Pieces"), (2, "503", "Screwdriver", 3, "Pieces"), (3, "222", "Oil", 1, "Liters")]

# the underscore _ is a convention for unused "throw away" variables
all_names = [name for (_, _, name, _, _) in parts]
print(all_names)
