from typing import Dict, Union, Optional

class ResaleShop:
    # This class defines the resale shop in which computers are being sold

    #attributes required: inventory'

    def __init__(self, inventory:Dict[int, Dict[str, Union[str, int, bool]]]):
        self.inventory = inventory
        self.itemID=0

    # the following method records that a new computer has been bought
    def buy(self, computer: Dict[str, Union[str, int, bool]]):
        self.itemID += 1 # increment itemID
        self.inventory[self.itemID] = computer
        return self.itemID

    #the following method records that a computer has been sold out of the inventory
    def sell(self, item_id: int):
        if item_id in self.inventory:
            del self.inventory[item_id]
            print("Item", item_id, "sold!")
        else: 
            print("Item", item_id, "not found. Please select another item to sell.")
    
    # the following method displays the content of the inventory to the user
    def print_inventory(self):
        # If the inventory is not empty
        if self.inventory:
            # For each item
            for key, value in self.inventory.items():
                #repeat loop to print computer dictionaries
                print(key,
                 ' : ', vars(value))
        else:
            print("No inventory to display.")

    def refurbish(self, item_id: int, new_os: Optional[str] = None):
        if item_id in self.inventory:
            computer = self.inventory[item_id] # locate the computer
            if int(computer.year_made) < 2000:
                computer.price = 0 # too old to sell, donation only
            elif int(computer.year_made) < 2012:
                computer.price = 250 # heavily-discounted price on machines 10+ years old
            elif int(computer.year_made) < 2018:
                computer.price = 550 # discounted price on machines 4-to-10 year old machines
            else:
                computer.price = 1000 # recent stuff

            if new_os is not None:
                computer.operating_system = new_os # update details after installing new OS
        else:
            print("Item", item_id, "not found. Please select another item to refurbish.")
