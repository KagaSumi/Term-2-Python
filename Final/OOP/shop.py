class Shop:
    """This class represents a generic shop in the "BCIT Sports" franchise
    """    
    
    def __init__(self,location):
        self.location = location
        self.inventory = {}
    
    def __len__(self):
        """Return the number of items in the shop
        """        
        return len(self.inventory)
    
    def __str__(self):
        return f"<Store: {self.location} ({len(self.inventory)} products)>"
    
    def add_product(self,product_name,product_quantity):
        """Adds a product to the inventory

        Args:
            product_name (str): product name
            product_quantity (int): product quantity
        """        
        self.inventory[product_name] = product_quantity

    def get_inventory(self):
        return self.inventory