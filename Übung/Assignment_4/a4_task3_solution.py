"""
a5_task3.py
Transforms two lists of names into a single list of tuples.
"""

# This is not optimal:
#   - Easy to loose the connection between first and last names
#   - Information belongs together -> tuple is the better data structure (see slides)
# Neutral: Names can be changed afterwards -> either positive or negative

first_names = ['Jane', 'Max', 'Giannis', 'Juan']
last_names = ['Doe', 'Mustermann', 'Karamitros', 'Perez', "Max"]

names = list(zip(first_names, last_names))
# also possible: names = [name for name in zip(first_names, last_names)]

print(names)