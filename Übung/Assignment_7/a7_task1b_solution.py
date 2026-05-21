"""
a7_task1b.py

Implements countdowns using the datetime module
"""

import datetime
import time


def calculate_time_difference(date, name, print_difference=True):
    now = datetime.datetime.now()
    difference = date - now
    # The number of seconds is positive if the date is in the future, otherwise negative
    difference_in_seconds = difference.total_seconds()

    # print only if wanted and if the date is in the future.
    if print_difference and difference_in_seconds > 0:
        print(f"Till {name}: {difference}")

    return difference, difference_in_seconds

# Christmas Eve, 18:00
christmas_eve =  datetime.datetime(2026, 12, 24, 18)
new_year = datetime.datetime(2027, 1, 1)
easter= datetime.datetime(2027, 3, 28)

print(f"Now: {datetime.datetime.now()}")

while True:
    _, till_xmas_seconds = calculate_time_difference(christmas_eve, "Christmas eave")
    _, till_newyear_seconds = calculate_time_difference(new_year, "new year")
    _, till_easter_seconds = calculate_time_difference(easter, "easter")
    
    if till_xmas_seconds <= 0 and till_easter_seconds <= 0 and till_newyear_seconds <= 0:
        break
    
    print("---------------") # for better looks
    
    time.sleep(1) # lets the program pause for 1 second 
 