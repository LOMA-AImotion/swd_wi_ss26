"""
a1_task2_solution.py
Converts dog years in human years.
L.L.
"""

dog_age = int(input("How old is your dog?"))

if dog_age == 0:
    print(f"{dog_age} dog years are equivalent to 0 human years.")
elif dog_age == 1:
    # The f-string can be assigned to a variable
    output = f"{dog_age} dog years are equivalent to 14 human years."
    print(output)
elif dog_age == 2:
    # This section is not strictly necessary since this case can be solved in else as well
    print(f"{dog_age} dog years are equivalent to 22 human years.")
else:
    human_age = 22 + ((dog_age-2) * 5) # For every year above 2, add 5 human years
    print(f"{dog_age} dog years are equivalent to {human_age} human years.")
