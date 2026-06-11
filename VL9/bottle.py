class Bottle:
  def __init__(self, content, type, amount):
    self.content = content
    self.type = type
    self.amount = amount
  
  def get_sugar(self):
    sugar_per_100ml = 0    
    if self.content == "coke":
        sugar_per_100ml = 10 
    elif self.content == "wine":
        sugar_per_100ml = 6
    return sugar_per_100ml * self.amount

b1 = Bottle("Water", "PET", 500)
b2 = Bottle("coke", "PET", 500)

print(b1.get_sugar())
print(b2.get_sugar())