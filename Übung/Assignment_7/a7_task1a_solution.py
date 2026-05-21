"""
a7_task1a.py
Calculates the area of multiple rectangles and applies a tax calculation on them.
"""

import geometric_formulas as gf
from tax import calc_gross_price, calc_net_price_of_property


tax_percentage = 0.035
price_per_sqm = 50

# List contains properties: [(length, width)]
properties = [(3, 7), (15, 25), (10, 11)]

for length, width in properties:
    area = gf.area_of_rectangle(length, width)
    net_price = calc_net_price_of_property(area, price_per_sqm)
    gross_price = calc_gross_price(net_price, tax_percentage)
    
    print(f"Length: {length}, width: {width} -> Net price is {net_price}€, gross price is {gross_price}€.")
    

