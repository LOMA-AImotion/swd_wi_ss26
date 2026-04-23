"""
a2_task1_solution.py
Prints triangles made from characters.
L.L. 
"""

height = int(input("Please input the triangle's height: "))

for h in range(1, height, 1):
    print(h * '#')

# We can also choose a negative stepsize!
for h in range(height, 0, -1):
    print(h * '#')