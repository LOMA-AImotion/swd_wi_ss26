"""
a1_task1_solution.py
Calculates the area of a rectangle and applies a tax calculation on it.
L.L. 
"""

naive_area = 4 * 3
print("Area calculated in a naive way:", naive_area)

length = 4
width = 3
area = length * width

# Using the 'f-print' here, another way to do prints without explicit type casting.
print(f"Area calculated using variables: {area}")

# This is equivalent:
print("Area caculated using variables:", area)

price_per_sqm = 50
tax_percentage = 0.035
net_price = area * price_per_sqm
gross_price = net_price + (net_price * tax_percentage)
print(f"The net price for the property is {net_price}€.")
print(f"The gross price is {gross_price}€, which includes {net_price*tax_percentage}€ tax.")
