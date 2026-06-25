class Product:
    def __init__(self, name, price):
        self.name = name          
        self.price = price       
        self.is_manufactured = False
    
    def manufacture(self):
        # better:
        # raise NotImplementedError("Each product must implement its own manufacturing process")
        # but for simplicity:
        print("Each product must implement its own manufacturing process")
    
    def get_info(self):
        if self.is_manufactured: 
            status = "manufactured"  
        else: 
            status = "not manufactured"

        return f"{self.name} ({self.price}€) - {status}"
    
    def get_price(self):
        return self.price


class Electronics(Product):
    def __init__(self, name, price, warranty_months):
        super().__init__(name, price)
        self.warranty_months = warranty_months
    
    def manufacture(self):
        print(f"Installing systems of {self.name}")
        self.is_manufactured = True


class Furniture(Product):
    def __init__(self, name, price, material):
        super().__init__(name, price)
        self.material = material
    
    def manufacture(self):
        print(f"Cutting {self.material} pieces for {self.name}")
        print("Assembling furniture")
        self.is_manufactured = True


class Factory:
    def __init__(self):
        self.inventory = []    
    
    def add_product(self, product):
        if not isinstance(product, Product):
            # better:
            # raise TypeError("Only products can be added to the factory")
            # but for simplicity:
            print("Only objects of type can be added to the factory")
        else:
            self.inventory.append(product)
    
    def manufacture_all(self):
        for product in self.inventory:
            product.manufacture()
    
    def get_inventory(self):
        # we want to give the caller a copy of the inventory, not the inventory itself
        return self.inventory.copy()


if __name__ == "__main__":
    factory = Factory()
    
    laptop = Electronics("Laptop", 800, warranty_months=12)

    phone = Electronics("Phone", 500, warranty_months=24)
    chair = Furniture("Chair", 100, material="wood")
     
    for product in [laptop, phone, chair]:
        factory.add_product(product)
    
    print("Starting production line...")
    factory.manufacture_all()

    print("Current inventory:")
    for product in factory.get_inventory():
        print(product.get_info())
