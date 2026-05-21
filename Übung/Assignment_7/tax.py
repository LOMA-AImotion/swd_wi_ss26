"""
tax.py

module for several tax related calculations.
"""

def calc_net_price_of_property(area, price_per_sqm=10):
    # Not calling the area-function here to make this 
    # function independent from the area calculation
    
    net_price = area * price_per_sqm
    return net_price


def calc_gross_price(net_price, tax_percentage=0.01):
    # Not calling calc_net_price_of_property here 
    # to make this function independent from the
    # net price calculation
    
    gross_price = net_price + (net_price * tax_percentage)
    return gross_price