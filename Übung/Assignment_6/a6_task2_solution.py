"""
Implements several variants of the max function
"""

def max2(x, y):
    if x >= y:
        return x
    else:
        return y

def max3a(x, y, z): 
    if x >= y:
        if x >= z:
            return x
        else: 
            return z
    else:
        if y >= z:
            return y
        else: 
            return z

def max3b(x, y, z):
    return max2(x, max2(y, z))

x = 3
y = 5
z = 7

print(f"Maximum of {x} and {y}: {max2(x, y)}")
print(f"Maximum of {x}, {y} and {z}: {max3a(x, y, z)}")
print(f"Maximum of {x}, {y} and {z}: {max3b(x, y, z)}")
    