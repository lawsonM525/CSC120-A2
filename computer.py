import oo_resale_shop
from typing import Dict, Union, Optional
class Computer:

    # This  class defines the blueprint for individual computers within the shop
    # attributes required for the computer class: 
    # description of the computer, type of processor, hard drive capacity, memory, OS, year it was made, price
    # methods required:
    # updating price, refurbishing the computer (repricing & upgrading the OS)

    '''
    Pseudocode Steps:
    1. Initialize attributes within constructor
    2. Define method to update price
    3. Define method to refurbish computer
    '''

    def __init__(self, 
    description: str, 
    processor_type: str, 
    hard_drive_capacity: int, 
    memory: int, 
    operating_system: str, 
    year_made: int,
    price: int):
        self.description = description
        self.processor_type = processor_type
        self.hard_drive_capacity = hard_drive_capacity
        self.memory = memory
        self.operating_system = operating_system
        self.year_made = year_made
        self.price = price

    def update_price(self, item_id: int, new_price: int):
        if item_id in self.inventory: 
            self.inventory[item_id]["price"] = new_price
        else:
            print("Item", item_id, "not found. Cannot update price.")
        
    def refurbish(self, item_id: int, new_os: Optional[str] = None):
        if item_id in self.inventory:
            computer = self.inventory[item_id] # locate the computer
            if int(computer["year_made"]) < 2000:
                computer["price"] = 0 # too old to sell, donation only
            elif int(computer["year_made"]) < 2012:
                computer["price"] = 250 # heavily-discounted price on machines 10+ years old
            elif int(computer["year_made"]) < 2018:
                computer["price"] = 550 # discounted price on machines 4-to-10 year old machines
            else:
                computer["price"] = 1000 # recent stuff

            if new_os is not None:
                computer["operating_system"] = new_os # update details after installing new OS
        else:
            print("Item", item_id, "not found. Please select another item to refurbish.")