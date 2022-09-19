
from typing import Dict, Union, Optional
from oo_resale_shop import ResaleShop

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
    description: str, # computer description (eg model and type)
    processor_type: str, # computer processor's type (eg Intel)
    hard_drive_capacity: int, # amount of storage capacity in hard drive
    memory: int, # amount of computer memory available
    operating_system: str, # OS currently installed
    year_made: int,# year the computer was made
    price: int): # price of computer
        self.description = description
        self.processor_type = processor_type
        self.hard_drive_capacity = hard_drive_capacity
        self.memory = memory
        self.operating_system = operating_system
        self.year_made = year_made
        self.price = price

    def update_price(self, shop: ResaleShop, item_id: int, new_price: int):
        if item_id in shop.inventory: 
            shop.inventory[item_id]["price"] = new_price
        else:
            print("Item", item_id, "not found. Cannot update price.")
        
