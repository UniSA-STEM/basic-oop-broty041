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
    # Class Docstring
    """
    Hacker is a character that interacts with the game world. It can
    perform actions, interact with rigs, other hackers and assets.

    Attributes
    ----------
    name: str
        Name of the hacker.
    __inventory: list
        Lists the hackers assets.
    __equipped_rig: bool
        Shows if hacker currently has a instantiated rig equipped.
    __trace_level: int
        Tracks a hackers exposure.
    __attack_state: int

    """
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

    def scan_and_remove(self, asset):
        for i in self.__inventory:
            if asset == i.name:
                self.__inventory.remove(i)

                return i
        return None

    def __transfer_asset(self, from_object, to_object, asset):
        """Private method that is the base for transferring of assets.
            Should only be called after validation."""
        found = from_object.find_asset(asset)

        if found:
            to_object.add_asset(found)
            from_object.remove_asset(found)
            return True
        return False

    def perform_transfer(self, from_object, to_object, asset):
        """
        Validates and performs transfers only on storage and
        inventory the Hacker owns. An object transfers FROM
        somewhere, TO somewhere.

            Parameters:
            from_object: object
                The source of the object being transferred.
            to_object: object
                The destination for the object being transferred.
            asset: str or object
                Reference to the object being transferred.

            Returns:
                bool: True for a successful transfer, otherwise False.
        """

        # Using asset object as safer than using the string parameter
        found_asset = from_object.find_asset(asset)

        allow_transfer = True

        # Checks for transfers rig to hacker
        if allow_transfer and isinstance(from_object, Rig) and isinstance(to_object, Hacker):
            if from_object.owner != to_object:
                print("You must perform extraction to transfer "
                      "assets from an opponents rig.")
                allow_transfer = False

        # Checks for transfers hacker to rig
        if allow_transfer and isinstance(from_object, Hacker) and isinstance(to_object, Rig):
            if to_object.owner != from_object:
                print("You must perform extraction to transfer "
                      "assets from an opponents rig.")
                allow_transfer = False

        # Check that the from_object exists at the origin.
        if allow_transfer and not from_object.find_asset(asset):
            if isinstance(from_object, Rig) and isinstance(to_object, Hacker):
                print(f"{asset} not found in {from_object.owner.name}'s rig.")
                allow_transfer = False
            elif isinstance(from_object, Hacker) and isinstance(to_object, Rig):
                print(f"{asset} not found in {from_object.name}'s inventory.")
                allow_transfer = False

        # Check the rigs storage level.
        if isinstance(to_object, Rig):
            if len(to_object.get_asset()) >= to_object.storage_size:
                print(f"{to_object.owner.name}'s rig is full."
                      f" Unable to transfer asset.")
                allow_transfer = False

        # Check if asset is encrypted
        if allow_transfer and found_asset.encrypt:
            print(f"{found_asset.name} encrypted, please decrypt before transferring.")
            allow_transfer = False

        # Perform the transfer after validation
        if allow_transfer:

            self.__transfer_asset(from_object, to_object, asset)

            # Different print output based on the combination of objects.
            if isinstance(from_object, Rig) and isinstance(to_object, Rig):
                print(f"{found_asset.name} transferred from {from_object.owner}"
                      f"'s rig to {to_object.owner}'s rig.")
            elif isinstance(to_object, Rig):
                print(f"{found_asset.name} transferred from {from_object.name}"
                      f" inventory to rig.")
            elif isinstance(from_object, Rig):
                print(f"{found_asset.name} transferred from {to_object.name}"
                      f"'s rig to inventory.")
            else:
                # In case the game is expanded with more assets
                print("Invalid destination for asset.")

            return True
        return False

    def perform_multi_transfer(self, from_object, to_object):
        if not from_object.get_asset().copy():
            for i in from_object.get_asset().copy():
                self.perform_transfer(from_object, to_object, i)

    def extract_rig_storage(self, enemy):
        """ Validates and performs transfers only on opponent
            hackers broken rig."""
        allow_extraction = True

        # Check enemy rigs storage level.
        if not enemy.broken:
            print(f"{enemy.owner.name}'s rig must be broken before extracting assets.")
            allow_extraction = False

        # Check that enemy rig has assets in storage.
        if allow_extraction and len(enemy.get_asset()) == 0:
            print(f"{enemy.name}'s storage is empty. Nothing to extract.")
            allow_extraction = False

        if allow_extraction and not self.get_rig().find_asset("Removable Drive"):
            print("No Removable Drive in rig storage. It's required for extraction.")
            allow_extraction = False

        if allow_extraction:
            loop_storage = enemy.get_asset().copy()
            unsecure_count = 0
            secure_count = 0

            for i in loop_storage:
                if not i.encrypt:
                    self.__transfer_asset(enemy, self, i)
                    unsecure_count += 1
                else:
                    secure_count += 1

            self.get_rig().remove_asset("Removable Drive")

            # Trace increments +1 per extraction
            self.adjust_trace(enemy)

            # Chose to use (s) to increase readability of code...
            # slightly.
            print(f"{unsecure_count} unsecured asset(s) transferred "
                  f"from {enemy.owner.name}'s rig to {self.name}'s "
                  f"inventory."
                  f"\n{secure_count} secure asset(s) remain.")
            return True
        return False

    # --- Encryption methods---

    def verify_encryption(self, target, asset, mode):
        """Validation to allow encryption to occur."""
        allow_encryption = True

        # Using asset object as safer than using the string parameter
        found_asset = target.find_asset(asset)

        # Check if the asset exists
        if allow_encryption and target.find_asset(asset) is None:
            location = "rig" if isinstance(target, Rig) else "inventory"
            name = asset.name if isinstance(asset, Asset) else asset
            print(f"{name} not found in {self.name}'s {location}.")

            allow_encryption = False

        # Prevent decryption of enemy's encrypted assets
        if isinstance(target, Rig):
            if target.owner != self:
                print("Cannot encrypt or decrypt assets in an "
                      "enemy hacker's rig.")
                allow_encryption = False

        if allow_encryption and isinstance(target, Hacker):
            if target != self:
                print("Cannot encrypt or decrypt assets in a "
                      "hacker's inventory.")
                allow_encryption = False

        # Check if mode is invalid
        if allow_encryption and (mode != "encrypt" and mode != "decrypt"):
            print(f"Please enter 'encrypt' or 'decrypt', '{mode}' is not valid. .")
            allow_encryption = False

        # Check if the hacker is exposed
        if allow_encryption and mode == "encrypt" and not self.set_encryption_flag:
            self.change_attack_state(1)
            allow_encryption = False

        # Check if the hacker has a security chip
        if allow_encryption and self.find_asset("Security Chip") is None:
            print(f"No Security Chip in inventory, cannot {mode} "
                  f"{found_asset.name}.")
            allow_encryption = False

        # Check if asset already encrypted
        if allow_encryption and mode == "encrypt":
            asset_found = target.find_encryption_target(target, asset, mode)
            if asset_found is None:
                print(f"{found_asset.name} is already encrypted.")
                allow_encryption = False

        # Check if asset already decrypted
        if allow_encryption and mode == "decrypt":
            asset_found = target.find_encryption_target(target, asset, mode)
            if not asset_found:
                if isinstance(target, Rig):
                    print(f"{found_asset.name} in {self.name}'s rig isn't encrypted.")
                else:
                    print(f"{found_asset.name} in {self.name}'s inventory isn't encrypted.")
                allow_encryption = False

        return allow_encryption

    def find_encryption_target(self, target, asset, mode):
        """Find if inventory contains an asset thats not encrypted,
            or an asset with encryption set that can be decrypted"""
        find_ref = asset.name if isinstance(asset, Asset) else asset
        for i in target.get_asset():
            if i.name == find_ref:
                if mode == 'encrypt':
                    if not i.encrypt:
                        return i
                elif mode == 'decrypt':
                    if i.encrypt:
                        return i
        return None

    def change_encryption(self, target, asset, mode):
        found_encryption_target = target.find_encryption_target(target, asset, mode)

        # Validating if encryption can be performed
        if not self.verify_encryption(target, asset, mode):
            return False

        self.remove_asset("Security Chip")

        if mode == "encrypt":
            found_encryption_target.encrypt = True
            location = "rig" if isinstance(target, Rig) else "inventory"
            print(f"{self.name} used a Security Chip to encrypt a {found_encryption_target.name} in their {location}.")

        elif mode == "decrypt":
            found_encryption_target.encrypt = False
            location = "rig" if isinstance(target, Rig) else "inventory"
            print(f"{self.name} used a Security Chip to decrypt a {found_encryption_target.name} in their {location}.")

    # --- General Methods ---
    def adjust_trace(self, target):
        """Increases trace only for the player and prints messages
            displaying changes."""
        allow_trace_increment = True

        # Check if a rig is the players
        if isinstance(target, Rig):
            if target.owner is self:
                allow_trace_increment = False

        # Check if it's the player
        if target.name is self.name:
            allow_trace_increment = False

        # Check if already at trace level 5 exposed
        if self.trace == 5:
            self.change_attack_state(1)
            allow_trace_increment = False

        if allow_trace_increment:
            self.trace = 1
            print(f"ALERT! RISKY ACTION DETECTED!")
            if self.trace < 5:
                print(f"Trace level now: {self.trace}")
            if self.trace == 5:
                self.change_attack_state(1)
                self.encryption_flag = False
            allow_trace_increment = True

        return allow_trace_increment

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

    def repair_rig(self):
        minus_damage = self.get_rig().damage - (self.get_rig().damage * 2)
        self.get_rig().damage = minus_damage

    def perform_repair(self):

        allow_repair = True

        if self.get_rig().damage == 0:
            print("Rig is in perfect condition. Nothing to repair.")
            allow_repair = False

        if allow_repair and not self.find_asset("CryptoToken"):
            print("CryptoToken is needed in your inventory "
                  "to perform repair.")
            allow_repair = False

        if allow_repair:
            self.repair_rig()
            self.get_rig().broken = False
            self.remove_asset("CryptoToken")
            print(f"Used CryptoToken to fully repair rig.")

        return True

    def start_journey(self, rig_name):
        if self.find_asset("CryptoToken") is None:
            print("No CryptoToken in inventory, cannot equip rig.")
        else:
            self.start_rig(rig_name)
            self.scan_and_remove("CryptoToken")
            print(f"Welcome to {self.name}'s H.E.V. Mark IV protective system.")

    def chop_shop(self):
        """Provides a way for the player to reduce their trace and
            remove exposure."""

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


    # --- Battle methods ---
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

        self.adjust_trace(enemy)

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



    def __str__(self):
        return (f"Hacker: {self.name} | Rig: {self.get_rig().name} | Trace level: {self.trace}\n"
                f"Inventory: \n" +
                f"\n".join(str(i) for i in self.get_asset()))
