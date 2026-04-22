"""
a5_task2.py
Transforms a parts list into a dictionary.
"""

parts = [(1, '500-1', 'Hammer', 2, 'Pieces'), (10, '500-1', 'Hammer', 3, 'Pieces'),(2, '503', 'Screwdriver', 3, 'Pieces'), (3, '555', 'Nail', 10, 'Pieces'), (4, '009', 'Motoroil', 10, 'Litres')]

inventory = dict()

for _, article_number, _, quantity, unit in parts:
    # Returns None if article_number is not yet in the dictionary 
    existing_stock = inventory.get(article_number, None)
   
    # We need to be careful if we have multiple entries for the same part!
    if existing_stock is None:
        inventory[article_number] = (quantity, unit)
    else:
        existing_quantity, existing_unit = existing_stock
        existing_quantity = existing_quantity + quantity
        
        inventory[article_number] = (existing_quantity, existing_unit)

print(inventory)