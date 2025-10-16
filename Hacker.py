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
        self.__attack_state = 0
        # Encryption flag True means hacker can encrypt.
        self.__encryption_flag = True

    # --- Getters and Setters ---
    def list_assets(self):
        if not self.__inventory:
            print(f"{self.name}'s inventory is empty.")
        else:
            print(f"{self.name}'s inventory contains "
                  f"{len(self.get_asset())} items:")
            for i in self.__inventory:
                print(i)

    def get_rig(self):
        return self.__equipped_rig

    def start_rig(self, rig_name):
        self.__equipped_rig = Rig(rig_name, self)

    def get_trace(self):
        return self.__trace_level

    def set_trace(self, trace_change):
        self.__trace_level += trace_change

    def edit_trace(self, trace_change):
        self.__trace_level = trace_change

    def remove_rig(self):
        self.__equipped_rig = None

    def get_attack_state(self):
        return self.__attack_state

    def set_attack_state(self, state):
        self.__attack_state = state

    def get_encryption_flag(self):
        return self.__encryption_flag

    def set_encryption_flag(self, state):
        self.__encryption_flag = state

    def get_equipped_status(self):
        return self.__equipped_rig

    def get_container_term(self):
        return "inventory"


    # --- Property Attributes ---
    trace = property(get_trace, set_trace)
    attack_state = property(get_attack_state, set_attack_state)
    encryption_flag = property(get_encryption_flag, set_encryption_flag)

    # --- Storage Related Methods ---
    def get_asset(self):
        return self.__inventory

    def add_asset(self, asset):
        self.__inventory.append(asset)

    def remove_asset(self, asset):
        found = self.find_asset(asset)
        if found:
            self.__inventory.remove(found)
        return found

    def find_asset(self, asset: "Takes asset as object or string"):
        find_ref = asset.name if isinstance(asset, Asset) else asset
        for i in self.__inventory:
            if i.name == find_ref:
                return i
        return None

    def count_asset(self, asset):
        count = 0
        for i in self.get_asset():
            if asset == i.name:
                count += 1
        return count

    def find_asset_index(self, asset):
        for idx, i in enumerate(self.__inventory):
            if asset == i:
                return idx
        return None

    def scan_and_remove(self, asset):
        for i in self.__inventory:
            if asset == i.name:

                self.__inventory.remove(i)

                return i
        return None


    # def extract_rig_check(self, from_object, to_object):
    #     storage_copy = from_object.get_asset().copy()
    #     if from_object.broken is False:
    #         print(f"{from_object.owner}'s rig must be broken before extracting assets.")
    #         return False
    #
    #     if len(storage_copy) == 0:
    #         print(f"{from_object.name}'s storage is empty. Nothing to extract.")
    #         return False
    #
    #     if to_object.find_asset_index(Asset("Removable Drive", "Found in rigs and used for extraction.")) is None:
    #         print("No Removable Drive in rig storage.\n"
    #               "A Removable Drive is required to extract another broken rig's assets.")
    #         return False
    #
    #     return True
    #
    # def extract_rigs_storage(self, from_object, to_object):
    #
    #     if self.extract_rig_check(from_object, to_object):
    #
    #         print("Starting rig extraction.")
    #
    #
    #         loop_storage = from_object.get_asset().copy()
    #         unsecure_count = 0
    #         secure_count = 0
    #
    #         for i in loop_storage:
    #             if i.get_encryption() is False:
    #                 self.asset_transfer(from_object, to_object, i)
    #                 unsecure_count += 1
    #             else:
    #                 secure_count += 1
    #
    #         print(f"{unsecure_count} unsecured assets transferred from {from_object} to {to_object}."
    #               f"\n{secure_count} secure assets not transferred.")
    #
    #
    #
    #         print("Completed rig extraction.")

    def asset_transfer_check(self, from_object, to_object, asset):

        if isinstance(to_object, Rig):
            if len(to_object.get_asset()) >= to_object.get_storage_size():

                print(f"{to_object.name}'s storage is full."
                      f" Unable to transfer asset.")
                return False

        if not from_object.find_asset(asset):
            print(f"{asset.name} not found on {from_object.name}")
            return False

        if isinstance(from_object, Rig) and isinstance(to_object, Hacker):
            if from_object.find_asset(asset):
                if not from_object.broken:
                    if from_object.owner !=  to_object:
                        print("To transfer assets from an opponents rig, "
                              "it must be broken and your rig must hold "
                              "a 'Removable Drive'.")
                        return False

        if isinstance(from_object, Hacker) and isinstance(to_object, Rig):
            if not to_object.broken:
                if to_object.owner !=  from_object:
                    print("To transfer assets from an opponents rig, "
                          "it must be broken and your rig must hold "
                          "a 'Removable Drive'.")
                    return False


        return True


    def asset_transfer(self, from_object, to_object, asset):
        if not self.asset_transfer_check(from_object, to_object, asset):
            return
        transfer_asset = from_object.find_asset(asset)

        if isinstance(from_object, Rig) and isinstance(to_object, Rig):
            to_object.add_asset(transfer_asset)
            from_object.remove_asset(asset)
            print(f"{asset.name} transferred from {from_object.owner}"
                  f"'s rig to {to_object.owner}'s rig.")
        elif isinstance(to_object, Rig):
            to_object.add_asset(transfer_asset)
            from_object.remove_asset(asset)
            print(f"{asset.name} transferred from {from_object.name}'s"
                  f" inventory to {to_object.owner}'s rig.")
        elif isinstance(from_object, Rig):
            to_object.add_asset(transfer_asset)
            from_object.remove_asset(asset)
            print(f"{asset.name} transferred from {from_object.owner}"
                  f"'s rig to {to_object.name}.")


        else:
            print("Invalid destination for asset.")



    def multi_asset_transfer(self, from_object, to_object):
        if not from_object.get_asset().copy():
            print(f"{from_object}'s {from_object.get_container_term()} contains no assets.")
        else:
            for i in from_object.get_asset().copy():
                from_object.asset_transfer(from_object, to_object, i)


    # --- Encryption, decryption and trace methods ---
    def trace_check(self, target):

        if isinstance(target, Rig):
            if target.owner is self:
                return True

        if target.name is self.name:
            return True

        if self.trace == 5:
            self.change_attack_state(1)
            return False

        self.trace = 1
        print(f"ALERT! RISKY ACTION DETECTED!")
        if self.trace < 5:
              print(f"Trace level now: {self.trace}")
        if self.trace == 5:
            self.change_attack_state(1)
            self.encryption_flag = False
        return True

    def verify_encryption(self, target, asset, mode):
        if isinstance(target, Rig):
            if target.owner !=  self:
                print("Cannot encrypt or decrypt assets in a "
                      "hacker's rig.")
                return False

        if isinstance(target, Hacker):
            if target !=  self:
                print("Cannot encrypt or decrypt assets in a "
                      "hacker's inventory.")
                return False

        if mode == "encrypt" and not self.set_encryption_flag:
            self.change_attack_state(1)
            return False

        if self.find_asset("Security Chip") is None:
            print(f"No Security Chip in inventory, cannot {mode} {asset.name}.")
            return False

        if target.find_asset_index(asset) is None:
            print(f"Can't find a {asset.name}.")
            return False



        if mode == "encrypt":
            asset_found = target.find_unencrypted(target, asset)
            if asset_found is None:
                print(f"{asset.name} is already encrypted.")
                return False

        elif mode == "decrypt":
            asset_found = target.find_encrypted(target, asset)
            if asset_found is None:
                print(f"The {asset.name} in {self.name}'s {target.get_container_term()} is not encrypted.")
                return False

        else:
            print(f"{mode} is not valid. Please enter 'encrypt' or 'decrypt'.")
            return False

        return True

    def find_unencrypted(self, target, asset):
        for i in target.get_asset():
            if i.name == asset.name:
                if not i.encrypt:
                    return i
        return None

    def find_encrypted(self, target, asset):
        for i in target.get_asset():
            if i.name == asset.name:
                if i.encrypt:
                    return i
        return None

    def change_encryption(self, target, asset, mode):
        found_unencrypted = target.find_unencrypted(target, asset)
        found_encrypted = target.find_encrypted(target, asset)



        if not self.verify_encryption(target, asset, mode):
            return

        if mode == "encrypt" and not self.trace_check(target):
            return

        self.remove_asset("Security Chip")

        if mode == "encrypt":
            found_unencrypted.encrypt = True
            print(f"{self.name} used a Security Chip to encrypt "
                  f"a {asset.name} in "
                  f"their {target.get_container_term()}.")
        elif mode == "decrypt":
            found_encrypted.encrypt = False
            print(f"{self.name} used a Security Chip to decrypt "
                  f"a {asset.name} in "
                  f"their {target.get_container_term()}.")



    # --- General Methods ---

    def upgrade_rig(self):
        if self.get_rig() is None:
            print(f"Please equip a rig to upgrade.")
        elif self.find_asset("Hardware Patch") is None:
            print(f"No Hardware Patch in inventory, cannot upgrade {self.name}'s rig level.")
        else:
            self.remove_asset("Hardware Patch")
            self.get_rig().upgrade = 1
            self.get_rig().storage_size = 1
            self.get_rig().max_damage = 1
            print(f"Hardware Patch used. {self.name}'s rig upgraded to level {self.get_rig().upgrade}."
                  f"\nRig now has {self.get_rig().storage_size} inventory slots."
                  f"\n{self.get_rig()} can now take {self.get_rig().max_damage} max damage when fully repaired.")

    def start_journey(self, rig_name):
        if self.find_asset("CryptoToken") is None:
            print("No CryptoToken in inventory, cannot equip rig.")
        else:
            self.start_rig(rig_name)
            self.scan_and_remove("CryptoToken")
            print(f"Welcome to {self.name}'s H.E.V. Mark IV protective system.")

    def chop_shop(self):
        if self.count_asset("CryptoToken") < 2:
            print("You need at least 2 CryptoTokens for "
                  "the chop shop. Better go scrounge under the "
                  "couch.")
            return None

        if self.trace < 1:
            print(f"Your trace level is {self.trace}, no need for the "
                  f"chop shop.")
            return None

        print("You travel to the metropolis outskirts in hopes of "
              "finding somewhere to decrease your trace level.\n"
              "You enter a chop shop and a dark shadowy figure with"
              " long finger nails asks, 'You have the tokens?'")
        while True:
            give_tokens = input("Give man 2 tokens (Y/N): ")

            if self.trace == 5:
                print("You're really testing my patience coming in"
                      " here with that much exposure.")
            if give_tokens in ["Y", "y"]:
                self.remove_asset("CryptoToken")
                self.remove_asset("CryptoToken")
                self.trace = -1
                self.attack_state = 0
                self.encryption_flag = False
                print(f"{self.name} gives shadowy figure 2 "
                      f"CryptoTokens")
                print("'A fine trade.' The shadowy figure taps on"
                      " his keyboard, a moment later your HUD shows your "
                      f"trace level is now {self.trace}."
                      f"\n.You say thanks and leave the chop shop.")
                if self.trace == 4:
                    print("No longer exposed.")
                return False
            elif give_tokens in ["N", "n"]:
                print("You come in here for no reason?! Be gone!"
                      "\nThe shadowy figure throws you out of the "
                      "shop.")
                return False
            else:
                print("Invalid input. Enter Y or N.")




    # --- Battle Related Methods ---

    def change_attack_state(self, state):
        if state == 1:
            self.attack_state = 1
            print(f"EXPOSED! Trace level: {self.trace}"
                  f"\nAttacks and encrypting are disabled until trace "
                  f"level is decreased.")

        elif state == 2:
            self.attack_state = 2
            print("A rig needs to be equipped in order to attack.")

    def pre_attack_check(self, enemy):

        if self.get_attack_state() > 0:
            print("Cannot attack.")
            self.change_attack_state(1)
            return False

        if enemy.get_rig().broken is True:
            print(f"Unable to attack a broken rig.")
            return False

        elif self.get_rig().find_asset("Data Spike") is None:
            print("No Data Spike in storage, cannot deal damage.")
            return False

        self.trace_check(enemy)

        return True

    def deal_damage(self, enemy):
        if self.pre_attack_check(enemy):
            self.get_rig().remove_asset("Data Spike")
            enemy.get_rig().damage = 1
            print(f"{self.name} launched Data Spike"
                  f"\n{enemy.name} took 1 damage."
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
        return (f"{self.name} {self.__equipped_rig} {self.__trace_level}\n"
                f"Inventory: \n" +
                f"\n".join(str(i) for i in self.__inventory))
