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
    class_type = "hacker"

    def __init__(self, name):
        self.name = name
        self.__inventory = [Asset("CryptoToken", "Used to acquire or repair rigs.")]
        self.__equipped_rig = None
        self.__trace_level = 0
        self.__display_add_print = True

    # --- Getters and Setters ---
    def list_inventory(self):
        if not self.__inventory:
            print(f"{self.name}'s inventory is empty.")
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

    def set_display_add_print(self, flag):
        self.__display_add_print = flag

    def remove_rig(self):
        self.__equipped_rig = None

    # --- Property Attributes ---
    trace = property(get_trace, set_trace)

    # --- Storage Related Methods ---
    def add_asset(self, item):
        if self.__display_add_print:
            print(f"Added {item.name} to {self.name}'s inventory.")
        self.__inventory.append(item)

    def remove_asset(self, item):
        if self.search_inventory(item) is None:
            print(f"No {item.name}'s in {self.name}'s inventory.")
        else:
            print(f"{item.name} removed from {self.owner}'s inventory.")
            self.__inventory.remove(self.__inventory[self.search_inventory(item)])

    def search_inventory(self, item):
        for idx, i in enumerate(self.__inventory):
            if item == i:
                return idx
        return None

    def extract_rig_check(self, from_object, to_object):
        storage_copy = from_object.get_storage().copy()
        if from_object.broken is False:
            print(f"{from_object.owner}'s rig must be broken before extracting assets.")
            return False

        if len(storage_copy) == 0:
            print(f"{from_object.name}'s storage is empty. Nothing to extract.")
            return False

        if to_object.search_inventory(Asset("Removable Drive", "Found in rigs and used for extraction.")) is None:
            print("No Removable Drive in rig storage.\n"
                  "A Removable Drive is required to extract another broken rig's assets.")
            return False

        return True

    def extract_rigs_storage(self, from_object, to_object):

        if self.extract_rig_check(from_object, to_object):

            print("Starting rig extraction.")

            to_object.set_display_add_print(False)
            loop_storage = from_object.get_storage().copy()
            unsecure_count = 0
            secure_count = 0

            for i in loop_storage:
                if i.get_encryption() is False:
                    self.asset_transfer(from_object, to_object, i)
                    unsecure_count += 1
                else:
                    secure_count += 1

            print(f"{unsecure_count} unsecured assets transferred from {from_object} to {to_object}."
                  f"\n{secure_count} secure assets not transferred.")

            to_object.set_display_add_print(True)

            print("Completed rig extraction.")

    def asset_transfer(self, from_object, to_object, item):

        idx = from_object.search_storage(item)
        transfer_item = from_object.get_storage()[idx]

        if isinstance(to_object, Rig):
            to_object.add_asset(transfer_item)
        elif isinstance(to_object, Hacker):
            to_object.add_asset(transfer_item)
        else:
            print("Invalid to_object.")

    def consume_item(self, item):
        idx = self.search_inventory(item)
        if idx is None:
            print(f"No {item}s in storage.")
            return None
        spent_item = self.__inventory.remove(self.__inventory[idx])
        print(f"{self.name} used a {item.name}")
        return spent_item

    def encrypt_asset(self, item, status):
        sec_chip = Asset("Security Chip", "Used to encrypt or decrypt assets.")
        if self.search_inventory(sec_chip) is None:
            print(f"No Security Chip in inventory, cannot encrypt {item.name}.")
        else:
            self.consume_item(sec_chip)
            item.set_encryption(status)
            print(f"{item.name} encrypted.")

    # --- General Methods ---

    def upgrade_rig(self):

        hware_patch = Asset("Hardware Patch", "Used to upgrade rigs.")
        if self.search_inventory(hware_patch) is None:
            print(f"No Hardware Patch in inventory, cannot upgrade {self.name}'s rig level.")
        elif self.__equipped_rig is None:
            print(f"Please equip a rig to upgrade.")
        else:
            self.consume_item(hware_patch)
            self.get_rig().upgrade = 1
            self.get_rig().storage = 1
            print(f"{self.name}'s rig upgraded to level {self.get_rig().upgrade}."
                  f"\nRig now has {self.get_rig().storage} inventory slots.")

    def start_journey(self, rig_name):
        cryp_tok = Asset("CryptoToken", "Used to acquire or repair rigs.")
        if self.search_inventory(cryp_tok) is None:
            print("No CryptoToken in inventory, cannot equip rig.")
        else:
            self.__equipped_rig = Rig(rig_name, self)
            self.__inventory.remove(self.__inventory[self.search_inventory(cryp_tok)])
            print(f"Welcome to {self.name}'s H.E.V. Mark IV protective system.")

    def __str__(self):
        return f"{self.name}"
