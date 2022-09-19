# Import a few useful containers from the typing module
from calendar import c
from typing import Dict, Union
from computer import Computer
from oo_resale_shop import ResaleShop

# Import the functions we wrote in procedural_resale_shop.py
from procedural_resale_shop import buy, update_price, sell, print_inventory, refurbish

""" This helper function takes in a bunch of information about a computer,
    and packages it up into a python dictionary to make it easier to store

    Note: because python is dynamically typed, you may not be used to seeing 
    explicit data types (str, int, etc.) listed in a python function. We're 
    going to go the extra step, because when we get to Java it'll be required!
"""
def create_computer(description: str,
                    processor_type: str,
                    hard_drive_capacity: int,
                    memory: int,
                    operating_system: str,
                    year_made: int,
                    price: int):
    return {Computer(description, processor_type, hard_drive_capacity, memory,operating_system, year_made, price)
    }

def main():
    
    store = ResaleShop({})

    # First, we make a computer by calling an instance of our class
    computer0 = Computer(
        "HP 27.2 Delicious Pro",
        "Intel 5.25 50 GHc 10-Core", 
        1024, 128,
        "Windows 11", 2012, 5200
    )

    # user is able to add their own computer
    '''
    Create variable computer2
    Take inpput from user for all parameters
    validate parameter types
    '''
    print("You can add a computer now.")
    computer1 = Computer(
        str(input("Describe computer model: ")),
        str(input("Describe processor type: ")),
        int(input("What is the capacity of the Hard drive? ")),
        int(input("How much memory can the computer store? ")),
        str(input("What operating system is currently running on the computer? ")),
        int(input("What year was this computer made? ")),
        int(input("What is the price of this computer? "))
    )

    # Print a banner of the store name
    print("-" * 21)
    print("COMPUTER RESALE STORE")
    print("-" * 21)

    # Add two computers to the resale store's inventory
    print("Buying", computer0.description)
    print("Adding to inventory...")
    print("Buying", computer1.description)
    print("Adding to inventory...")
    computer_0_id = store.buy(computer0)
    computer_1_id = store.buy(computer1)
    print("Done.\n")

    # Make sure it worked by checking inventory
    print("Checking inventory...")
    store.print_inventory()
    print("Done.\n")

    # Now, let's refurbish it
    new_OS = "MacOS Monterey"
    print("Refurbishing Item ID:", computer_0_id, ", updating OS to", new_OS)
    print("Updating inventory...")
    store.refurbish(computer_0_id, new_OS)
    print("Done.\n")

    # Make sure it worked by checking inventory
    print("Checking inventory...")
    store.print_inventory()
    print("Done.\n")
    
    # Now, let's sell it!
    print("Selling Item ID:", computer_0_id)
    store.sell(computer_0_id)
    
    # Make sure it worked by checking inventory
    print("Checking inventory...")
    store.print_inventory()
    print("Done.\n")

    '''# Check to see if price can be updated
    new_price = int(input("What is the new price for this computer?"))
    print("Updating price...")
    computer1.update_price(store, computer_1_id, new_price)
    print("Done.\n")

    # Make sure it worked by checking inventory
    print("Checking inventory...")
    store.print_inventory()
    print("Done.\n")'''

# Calls the main() function when this file is run
if __name__ == "__main__": main()
