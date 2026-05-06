"""
Calculates the area of multiple rectangles and applies a tax calculation on them.
"""

# You can use comments to document your code  
def calc_net_price_of_property(length, width, price_per_sqm=10):
    """Calculates the net price of a single property

        Args:
            length: length of the property
            width: width of the property
            price_per_sqm: Price per square meter in €

        Returns:
            net_price: The net price of the property as integer
    """

    area = length * width
    net_price = area * price_per_sqm
    
    return net_price

def calc_gross_price(net_price, tax_percentage=0.01):
    """Calculates the gross price based on a net price

        Args:
            net_price: net price on which the tax is applied
            tax_percentage: percentage value for the tax applied on net_price

        Returns:
            gross_price: The gross price of the property
    """
    gross_price = net_price + (net_price * tax_percentage)
    return gross_price


tax_percentage = 0.035
price_per_sqm = 50

# List contains properties: [(length, width)]
properties = [(3, 7), (15, 25), (10, 11)]

for length, width in properties:
    net_price = calc_net_price_of_property(length=length, width=width, price_per_sqm=price_per_sqm)
    gross_price = calc_gross_price(net_price, tax_percentage)
    print(f"Length: {length}, width: {width} -> Net price is {net_price}€, gross price is {gross_price}€.")
