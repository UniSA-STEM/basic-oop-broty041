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
    def get_asset(self):
        return self.__inventory

    def add_asset(self, item):
        if self.__display_add_print:
            print(f"Added {item.name} to {self.name}'s inventory.")
        self.__inventory.append(item)

    def remove_asset(self, item):
        if self.find_asset_index(item) is None:
            print(f"No {item.name}'s in {self.name}'s inventory.")
        else:
            print(f"{item.name} removed from {self.owner}'s inventory.")
            self.__inventory.remove(self.__inventory[self.find_asset_index(item)])

    def search_assets(self, item):
        for idx, i in enumerate(self.__inventory):
            if item == i:
                return i
        return None


    def find_asset_index(self, item):
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

        if to_object.find_asset_index(Asset("Removable Drive", "Found in rigs and used for extraction.")) is None:
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

        idx = from_object.find_asset_index(item)
        transfer_item = from_object.get_storage()[idx]

        if isinstance(to_object, Rig):
            to_object.add_asset(transfer_item)
        elif isinstance(to_object, Hacker):
            to_object.add_asset(transfer_item)
        else:
            print("Invalid to_object.")

    def consume_item(self, item):
        idx = self.find_asset_index(item)
        if idx is None:
            print(f"No {item}s in storage.")
            return None
        spent_item = self.__inventory.remove(self.__inventory[idx])
        print(f"{self.name} used a {item.name}")
        return spent_item


    # --- Encryption, decryption and trace methods ---
    def trace_check(self, target):
        print(f"current trace {self.trace} {self.name}")
        notorious_warning = "YOU ARE NOTORIOUS.\nYou cannot attack or encrypt when trace level is 5."

        if target.name is self.name:
            return True

        if self.trace == 5:
            print(notorious_warning)
            return False

        self.trace = 1
        print(f"ALERT! RISKY ACTION DETECTED!"
              f"\nTRACE LEVEL NOW: {self.trace}")
        if self.trace == 5:
            print(notorious_warning)
        return True

    def encrypt_decrypt_check(self, target, item):
        sec_chip = Asset("Security Chip", "Used to encrypt or decrypt assets.")
        asset_found = target.not_encrypted_search(target, item)
        if self.find_asset_index(sec_chip) is None:
            print(f"No Security Chip in inventory, cannot encrypt {item.name}.")
            return False

        elif target.find_asset_index(item) is None:
            print(f"Can't find a {item.name}.")
            return False

        elif asset_found is None:
            print(f"{item.name} is already encrypted.")
            return False

        elif asset_found.encrypt is True:
            print(f"{item.name} is already encrypted.")
            return False
        return True

    def not_encrypted_search(self, target, item):
        for i in target.get_asset():
            if i.name == item.name:
                if not i.encrypt:
                    return i
        return None

    def encrypt_asset(self, target, item):
        sec_chip = Asset("Security Chip", "Used to encrypt or decrypt assets.")
        asset_found = target.not_encrypted_search(target, item)
        if self.encrypt_decrypt_check(target, item):
            if self.trace_check(target):
                self.consume_item(sec_chip)
                asset_found.encrypt = True
                print(f"{asset_found.name} encrypted.")


    # --- General Methods ---

    def upgrade_rig(self):
        hware_patch = Asset("Hardware Patch", "Used to upgrade rigs.")
        if self.find_asset_index(hware_patch) is None:
            print(f"No Hardware Patch in inventory, cannot upgrade {self.name}'s rig level.")
        elif self.__equipped_rig is None:
            print(f"Please equip a rig to upgrade.")
        else:
            self.consume_item(hware_patch)
            self.get_rig().upgrade = 1
            self.get_rig().storage = 1
            self.get_rig().max_damage = 1
            print(f"{self.name}'s rig upgraded to level {self.get_rig().upgrade}."
                  f"\nRig now has {self.get_rig().storage} inventory slots."
                  f"\n{self.name} total HP is now {self.get_rig().max_damage}")

    def start_journey(self, rig_name):
        cryp_tok = Asset("CryptoToken", "Used to acquire or repair rigs.")
        if self.find_asset_index(cryp_tok) is None:
            print("No CryptoToken in inventory, cannot equip rig.")
        else:
            self.__equipped_rig = Rig(rig_name, self)
            self.__inventory.remove(self.__inventory[self.find_asset_index(cryp_tok)])
            print(f"Welcome to {self.name}'s H.E.V. Mark IV protective system.")


    # --- Battle Related Methods ---

    def pre_attack_check(self, enemy):
        d_spike = Asset("Data Spike", "Used in battles.")

        if enemy.get_rig().broken is True:
            print(f"Unable to attack a broken rig.")
            return False

        elif self.get_rig().find_asset_index(d_spike) is None:
            print("No Data Spike in storage, cannot deal damage.")
            return False

        return True

    def deal_damage(self, enemy):
        d_spike = Asset("Data Spike", "Used in battles.")

        if self.pre_attack_check(enemy):
            self.consume_item(d_spike)
            enemy.get_rig().damage = 1
            print(f"{self.name} attacked {enemy.name}"
                  f"\n{enemy.name} rig: {enemy.get_rig().damage}/{enemy.get_rig().max_damage} Damage")

        if enemy.get_rig().damage >= enemy.get_rig().max_damage:
            enemy.get_rig().broken = True

    def rig_condition(self):
        damage = self.get_rig().damage
        level = self.get_rig().upgrade
        half = self.get_rig().max_damage / 2

        if damage == 0:
            return f"Pristine (Level {level})"
        elif damage == self.get_rig().max_damage:
            return f"Broken (Level {level})"
        elif damage > half:
            return f"Poor (Level {level})"
        else:
            return f"Usable (Level {level})"



    def __str__(self):
        return f"{self.name}"
