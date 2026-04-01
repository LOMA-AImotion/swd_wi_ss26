"""
a1_task3_solution.py
Checks if a given year is a leap year.
L.L. 
"""

year = int(input("Which year do you want to check?"))
leap_year = False

# Note the correct levels of intendation!
if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            leap_year = True
        else:
            leap_year = False
    else:
        leap_year = True
else:
    leap_year = False

if leap_year:
    print(f"Year {year} is a leap year.")
else:
     print(f"Year {year} is not a leap year.")
