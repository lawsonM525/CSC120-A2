from typing import Dict, Union, Optional

class ResaleShop:
    # This class defines the resale shop in which computers are being sold

    #attributes required: inventory, itemID

    def __init__(self, inventory:Dict[int, Dict[str, Union[str, int, bool]]]):
        self.inventory = inventory
        #self.inventory = {}

    def buy(self, computer: Dict[str, Union[str, int, bool]]):
        itemID += 1 # increment itemID
        self.inventory[itemID] = computer
        return itemID


    def sell(self, item_id: int):
        if item_id in self.inventory:
            del self.inventory[item_id]
            print("Item", item_id, "sold!")
        else: 
            print("Item", item_id, "not found. Please select another item to sell.")
    
    def print_inventory(self):
        # If the inventory is not empty
        if self.inventory:
            # For each item
            for item_id in self.inventory:
                # Print its details
                print(f'Item ID: {item_id} : {self.inventory[item_id]}')
        else:
            print("No inventory to display.")
