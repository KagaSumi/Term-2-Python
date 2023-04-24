from shop import Shop
import requests, csv

class OutdoorShop(Shop):
    """ This is a class that inherits from Shop class handles loading through API Requests
    """    
    def __init__(self,location):
        super().__init__(location)

    def load(self):
        """Updates the store inventory based on store location if end point returns 200 status (OK)

        Raises:
            UserWarning: Raises warning to notify user that the inventory didn't update
        """        
        URL = f"https://bcitoutdoor.ca/api/store/{self.location}"
        request = requests.get(URL)
        if request.status_code == 200:
            self.inventory = request.json()["products"]
        else:
            raise UserWarning

class EastCoastShop(Shop):
    """ This is a class that inherits from Shop class handles loading through local csv files
    """    
    def __init__(self,location):
        super().__init__(location)
    
    def load(self):
        """Loads local csv file and updates inventory based on store location
        if file is not found warn user about not updating inventory

        Raises:
            UserWarning: Warning User if inventory does not update
        """        
        try:
            temp_dict = {}
            with open(f"./stores/{self.location}.txt", "r") as CSV:
                File = csv.reader(CSV)
                next(File)
                for key,val in File:
                    temp_dict[key] = int(val)
            self.inventory = temp_dict
        except FileNotFoundError:
            raise UserWarning

class BCITSports():
    """This class represents the whole "BCIT Sports" franchise, and not a single shop. Its goal is to store a "global
    inventory" of products across all stores. 
    - From instructions
    """    
    def __init__(self):
        self.stores= []

    def register_store(self,location:str) -> bool:
        """Registter stores to local list, it will try to see if it it is an OutdoorStore first
        If it isn't it will catch the userwarning and try again with EastCoastShop, 
        if that failes it will return False

        Args:
            location (str): location of the store

        Returns:
            bool: Returns True if store is registered False if it isn't
        """        
        store = OutdoorShop(location)
        try:
            store.load()
            self.stores.append(store)
            return True
        except UserWarning:
            store = EastCoastShop(location)
        try:
            store.load()
            self.stores.append(store)
            return True
        except UserWarning:
            return False

    def products(self) -> list[str]:
        """Returns a list of the products available at a store

        Returns:
            list[*str]: List of product names
        """
        products = []
        for store in self.stores:
            for key in store.get_inventory().keys():
                products.append(key)
        return list(set(products))

    def where(self,product_name:str) -> list[str]:
        """Returns a list of stores where the product is available
        Args:
            product_name (str): name of the product
        Returns:
            List[*str]: List of store locations that hold the product
        """                
        return [store.location for store in self.stores\
                if product_name in store.get_inventory().keys()]

    def available(self,product_name:str) -> int:
        """Returns Total of how many products are available in the store

        Args:
            product_name (str): name of the product

        Returns:
            int: Total of how many products are in our shops
        """        
        return sum([int(store.get_inventory().get(product_name))\
            for store in self.stores\
                if store.get_inventory().get(product_name)])
