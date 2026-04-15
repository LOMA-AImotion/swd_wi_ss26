"""
task2_solution.py
While loops
L.L.
"""

integer_list = []
user_input = input("Enter an integer: ")

while user_input != "stop":
    user_input = int(user_input)
    integer_list.append(user_input)
    user_input = input("Enter an integer: ")

print(integer_list)

# This ensures that the first element of the list is set as min and max in the first iteration 
min = float('inf') # Value is larger than any int by guarantee
max = -float('inf') # Value is smaller than any int by guarantee

# Equivalent: 
# min = integer_list[0]
# max = integer_list[0]

sum = 0

for i in integer_list:
    
    print(f"Current min: {min}")
    print(f"Current max {max}")
    print(f"i: {i}")
    print("-------")
    
    if i < min:
        min = i
    
    if i > max:
        max = i

    sum = sum + i

mean = sum / len(integer_list)

print(f"Minimum: {min}, Maximum: {max} and Mean: {mean}.")
