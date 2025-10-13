"""
File: Hacker.py
Description: <This module contains all the code for hackers.>
Author: <Thomas Brown>
ID: <110454503>
Username: <broty041>
This is my own work as defined by the University's Academic Misconduct Policy.
"""

from Asset import Asset
from Rig import Rig


class Hacker:

    def __init__(self, name):
        self.name = name
        self.__inventory = [Asset("CryptoToken", "Used to acquire or repair rigs.")]
        self.__equipped_rig = None
        self.__trace_level = 0

    # --- Getters and Setters ---
    def get_inventory(self):
        if not self.__inventory:
            print("Inventory is empty.")
        else:
            print(f"Contents of {self.name}'s inventory:")
            for i in self.__inventory:
                print(i)

    def get_rig(self):
        return self.__equipped_rig

    def get_trace(self):
        return self.__trace_level

    def set_trace(self, trace_change):
        self.__trace_level += trace_change

    # --- Property Attributes ---
    trace = property(get_trace, set_trace)


    # --- General Methods ---
    def search_inventory(self, item):
        for idx, i in enumerate(self.__inventory):
            if item == i.name:
                return idx
        return None

    def add_asset(self, item):
        self.__inventory.append(item)

    def start_journey(self, rig_name):
        if self.search_inventory("CryptoToken") is None:
            print("No CryptoToken's in inventory, cannot equip rig.")
        else:
            self.__equipped_rig = Rig(rig_name, self)
            self.__inventory.remove(self.__inventory[self.search_inventory("CryptoToken")])
            print(f"Welcome to {self.name}'s H.E.V. Mark IV protective system.")

    def __str__(self):
        return f"{self.name}"
