"""
File: Hacker.py
Description: <This module contains all the code for hackers.>
Author: <Thomas Brown>
ID: <110454503>
Username: <broty041>
This is my own work as defined by the University's Academic Misconduct
Policy.
"""
from operator import truediv

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
        Shows if hacker currently has an instantiated rig equipped.
    __trace_level: int
        Tracks a hackers exposure.
    __encryption_flag: bool
        Determines if hacker can perform encryption.

    Methods
    -------
    list_assets():
        Prints contents of inventory.
    find_asset():
        Find an asset in inventory.
    count_asset():
        Count how many of an asset.
    scan_and_remove():
        Find an asset and remove it.
    __transfer_asset():
        Private method transfer an asset.
    perform_transfer():
        Performs a single asset transfer.
    perform_multi_transfer():
        Performs multiple asset transfers.
    extract_rig_storage():
        Extracts assets from an enemy rig's storage.
    __verify_encryption():
        Private method validates encryption.
    find_encryption_target():
        Finds encrypted or decrypted assets.
    change_encryption():
        Performs encryption or decryption on an asset.
    adjust_trace():
        Adjusts the trace level of hacker.
    upgrade_rig():
        Upgrades the hackers rigs level.
    __repair_rig():
        Private method repairs hackers rig.
    perform_repair():
        Validates then performs repair on hackers rig.
    start_journey():
        Initialises and equips hackers rig.
    chop_shop():
        Text adventure that reduces trace and can remove exposure.
    __validate_attack():
        Provides validation for damage dealing.
    deal_damage():
        Deals damage to enemy hacker.
    """

    def __init__(self, name):
        self.name = name
        self.__inventory = [Asset("CryptoToken",
                        "Used to acquire or repair rigs.")]
        self.__equipped_rig = None
        self.__trace_level = 0
        # True means hacker is allowed to encrypt/decrypt.
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

    def remove_rig(self):
        self.__equipped_rig = None

    def get_encryption_flag(self):
        return self.__encryption_flag

    def set_encryption_flag(self, state):
        self.__encryption_flag = state

    def get_equipped_status(self):
        return self.__equipped_rig

    # --- Property Attributes ---
    trace = property(get_trace, set_trace)
    encryption_flag = property(get_encryption_flag,
                               set_encryption_flag)

    # --- Storage Related Methods ---
    def get_asset(self):
        return self.__inventory

    def add_asset(self, asset):
        self.__inventory.append(asset)

    def remove_asset(self, asset):
        """Remove an asset from inventory  storage."""
        found = self.find_asset(asset)
        if found:
            self.__inventory.remove(found)
        return found

    def find_asset(self, asset: "Takes asset as object or string"):
        """
        Find an asset in inventory and accept either a string
        or object as a parameter.
        """
        find_ref = asset.name if isinstance(asset, Asset) else asset
        for i in self.__inventory:
            if i.name == find_ref:
                return i
        return None

    def count_asset(self, asset):
        """Provide a count of an object in inventory."""
        count = 0
        for i in self.get_asset():
            if asset == i.name:
                count += 1
        return count

    def scan_and_remove(self, asset):
        """
        Search for an asset and then remove it. This is its own
        method as per interpretation of assessment spec.
        """
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
        Validates and performs transfers on storage and
        inventory the Hacker owns. An object transfers FROM
        somewhere, TO somewhere.

            Parameters:
            from_object (object):   The source of the object being
                                    transferred.
            to_object (object):     The destination for the object
                                    being transferred.
            asset (str or object):  Reference to the object being
                                    transferred.

            Returns:
                bool: True for a successful transfer, otherwise False.
        """
        # Using asset object as safer than using the string parameter

        found_asset = from_object.find_asset(asset)

        allow_transfer = True

        # Checks for transfers rig to hacker
        if (allow_transfer and isinstance(from_object, Rig)
                and isinstance(to_object, Hacker)):
            if from_object.owner != to_object:
                print("You must perform extraction to transfer "
                      "assets from an opponents rig.")
                allow_transfer = False

        # Checks for transfers hacker to rig
        if (allow_transfer and isinstance(from_object, Hacker)
                and isinstance(to_object, Rig)):
            if to_object.owner != from_object:
                print("You must perform extraction to transfer "
                      "assets from an opponents rig.")
                allow_transfer = False

        # Check that the from_object exists at the origin.
        if allow_transfer and not from_object.find_asset(asset):
            if (isinstance(from_object, Rig) and
                    isinstance(to_object, Hacker)):
                print(f"'{asset}' not found in "
                      f"{from_object.owner.name}'s rig.")
                allow_transfer = False
            elif (isinstance(from_object, Hacker) and
                  isinstance(to_object, Rig)):
                print(f"'{asset}' not found in "
                      f"{from_object.name}'s inventory.")
                allow_transfer = False

        # Check the rigs storage level.
        if isinstance(to_object, Rig):
            if len(to_object.get_asset()) >= to_object.storage_size:
                print(f"{to_object.owner.name}'s rig is full."
                      f" Unable to transfer asset.")
                allow_transfer = False

        # Check if asset is encrypted
        if allow_transfer and found_asset.encrypt:
            print(f"{found_asset.name} encrypted, please decrypt "
                  f"before transferring.")
            allow_transfer = False

        # Perform the transfer after validation
        if allow_transfer:

            self.__transfer_asset(from_object, to_object, asset)

            # Different print output based on the combination of objects.
            if isinstance(from_object, Rig) and isinstance(to_object, Rig):
                print(f"{found_asset.name} transferred from "
                      f"{from_object.owner}"
                      f"'s rig to {to_object.owner}'s rig.")
            elif isinstance(to_object, Rig):
                print(f"{found_asset.name} transferred from "
                      f"{from_object.name}"
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
        """
        Builds on perform_transfer. Iterate over storage or
        inventory and transfers all assets.
        """
        if from_object.get_asset():
            print("Initiating transfer of multiple items:")
            for i in from_object.get_asset().copy():
                self.perform_transfer(from_object, to_object, i)
        else:
            print(f"{from_object.name} is empty.")

    def extract_rig_storage(self, enemy):
        """
        Validates and performs transfers only on opponent
        hackers broken rig. Requires an unencrypted removable drive.

            Parameters:
                enemy (object):     The source of transferring assets.

            Returns
                bool:           True if the extraction was successful.
        """
        allow_extraction = True

        # Check enemy rigs storage level
        if not enemy.broken:
            print(f"{enemy.owner.name}'s rig must be broken before "
                  f"extracting assets.")
            allow_extraction = False

        # Check that enemy rig has assets in storage
        if allow_extraction and len(enemy.get_asset()) == 0:
            print(f"{enemy.name}'s storage is empty. Nothing to extract.")
            allow_extraction = False

        # Check if hacker has a removable drive in inventory
        if allow_extraction and not self.get_rig().find_asset("Removable Drive"):
            print("No Removable Drive in rig storage. It's required for extraction.")
            allow_extraction = False

        # Check if that removable drive is encrypted
        if (allow_extraction and
                self.get_rig().find_asset("Removable Drive").encrypt):
            print("Cannot use an encrypted Removable Drive to perform "
                  "extraction.")
            allow_extraction = False

        # Keep a tally of unsecure/secure assets for print output
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
            print("[Extraction initiated.]")
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
    def __verify_encryption(self, target, asset, mode):
        """
        Validation to allow encryption to occur.

            Parameters:
                target (object):    Destination location of asset to
                                    encrypt/decrypt.
                asset (object):     Which asset to encrypt/decrypt.
                mode (str):         Is the encryption mode "encrypt"
                                    or "decrypt".

            Returns:
                bool:               True if encrypt/decrypt allowed.


        """
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
            print(f"Please enter 'encrypt' or 'decrypt', "
                  f"'{mode}' is not valid.")
            allow_encryption = False

        # Check if the hacker is exposed
        if (allow_encryption and mode == "encrypt" and
                not self.encryption_flag):
            print(f"EXPOSED! Trace level: {self.trace}"
                  f"\nAttacks and encrypting are disabled until trace "
                  f"level is decreased.")
            allow_encryption = False

        # Check if the hacker has a security chip
        if allow_encryption and self.find_asset("Security Chip") is None:
            print(f"No Security Chip in inventory, cannot {mode} "
                  f"{found_asset.name}.")
            allow_encryption = False

        # Check hacker has 2 security chips if encrypting a security chip
        if allow_encryption and mode == "encrypt":
            asset_name = asset.name if isinstance(asset, Asset) else asset
            if (asset_name == "Security Chip" and
                    self.count_asset("Security Chip") < 2):
                print("Need at least 2 security chips when encrypting a "
                      "security chip")
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
                location = "rig" if isinstance(target, Rig) else "inventory"
                print(f"{found_asset.name} in {self.name}'s {location} isn't "
                      f"encrypted.")
                allow_encryption = False

        return allow_encryption

    def find_encryption_target(self, target, asset, mode):
        """Find if inventory contains an asset not encrypted,
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
        """
        Performs encryption or decryption on an asset after
        validation.

            Parameters:
                target (object):    Destination location of asset to
                                    encrypt/decrypt.
                asset (object):     Which asset to encrypt/decrypt.
                mode (str):         Is the encryption mode "encrypt"
                                    or "decrypt".

            Returns:
                bool:               True if encrypt/decrypt performed.


        """
        success = True


        # Validating if encryption can be performed
        if not self.__verify_encryption(target, asset, mode):
            success = False


        # If still True then encrypt/decrypt
        if success:
            self.remove_asset("Security Chip")
            found_encryption_target = (
                target.find_encryption_target(target, asset, mode))

            # Encrypt or decrypt by changing the encryption flag of asset.
            if mode == "encrypt":
                found_encryption_target.encrypt = True
                location = "rig" if isinstance(target, Rig) else "inventory"
                print(f"{self.name} used a Security Chip to encrypt a "
                      f"{found_encryption_target.name} in their {location}.")

            elif mode == "decrypt":
                found_encryption_target.encrypt = False
                location = "rig" if isinstance(target, Rig) else "inventory"
                print(f"{self.name} used a Security Chip to decrypt a "
                      f"{found_encryption_target.name} in their {location}.")

        return success


    # --- General Methods ---
    def adjust_trace(self, target):
        """
        Validate then adjust trace level by 1 and print adjustment.

            Parameters:
                target (object):    Which hackers trace will be
                                    adjusted.

            Returns:
                bool:               True if trace validated and
                                    adjustment made.
        """
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
            print(f"EXPOSED! Trace level: {self.trace}"
                  f"\nAttacks and encrypting are disabled until trace "
                  f"level is decreased.")
            allow_trace_increment = False

        # Increment by 1 and show trace level if below 5. If == 5
        # print exposed and change flag to False.
        if allow_trace_increment:
            self.trace = 1
            print(f"ALERT! RISKY ACTION DETECTED!")
            if self.trace < 5:
                print(f"Trace level now: {self.trace}")
            elif self.trace == 5:
                print(f"Trace level now: {self.trace}"
                      f"\nYOU ARE EXPOSED! SEEK HELP!")
                self.encryption_flag = False
            allow_trace_increment = True

        return allow_trace_increment

    def upgrade_rig(self):
        """
        Upgrades rig incrementing its upgrade level, storage size and
        max damage.
        """

        # Validates if rig is equipped and whether hacker has hardware
        # patch in inventory.
        if self.get_rig() is None:
            print(f"Please equip a rig to upgrade.")
        elif self.find_asset("Hardware Patch") is None:
            print(f"No Hardware Patch in inventory, cannot upgrade "
                  f"{self.name}'s rig level.")
        else:
            self.remove_asset("Hardware Patch")
            self.get_rig().upgrade = 1
            self.get_rig().storage_size = 1
            self.get_rig().max_damage = 1
            # Print upgrade summary name, level, storage size, max damage
            print(f"Hardware Patch used. {self.name}'s rig upgraded to level "
                  f"{self.get_rig().upgrade}."
                  f"\nRig now has {self.get_rig().storage_size}"
                  f" inventory slots."
                  f"\n{self.name}'s {self.get_rig().name} can now take "
                  f"{self.get_rig().max_damage} max damage when fully "
                  f"repaired.")

    def __repair_rig(self):
        """
        Private method use in perform_repair. Repairs hackers rig
        resetting back to 0 damage. Changing broken state
        controlled by perform_repair.
        """
        self.get_rig().damage = -self.get_rig().damage

    def perform_repair(self):
        """Allows hacker to perform repair on rig. Provides feedback
            on repair process."""
        allow_repair = True

        if self.get_rig() is None:
            print(f"Please equip a rig.")
            allow_repair = False

        # Check if rig damaged
        if allow_repair and self.get_rig().damage == 0:
            print("Rig is in perfect condition. Nothing to repair.")
            allow_repair = False

        # Check if hacker has cryptotoken in inventory.
        if allow_repair and not self.find_asset("CryptoToken"):
            print("CryptoToken is needed in your inventory "
                  "to perform repair.")
            allow_repair = False

        if allow_repair:
            self.__repair_rig()
            self.get_rig().broken = False
            self.remove_asset("CryptoToken")
            print(f"Used CryptoToken to fully repair rig.")

        return allow_repair

    def start_journey(self, rig_name):
        """
        Initialise rig in hackers inventory and begin their
        adventure. Assuming a hacker initialises with a
        cryptotoken.
        """
        # Account for possible future cases where Hacker may not
        # start with cryptotoken in inventory.
        if self.find_asset("CryptoToken") is None:
            print("No CryptoToken in inventory, cannot equip rig.")
        else:
            self.start_rig(rig_name)
            self.scan_and_remove("CryptoToken")
            print(f"Welcome to {self.name}'s H.E.V. Mark IV "
                  f"protective system.")

    def chop_shop(self):
        """
        Provides a way for the player to reduce their trace and
        remove exposure. Features a user controlled loop adventure.

            Returns:
                bool: True if chop_shop visit was completed.
        """
        allowed = True

        # Check if hacker has 2 CryptoTokens
        if self.count_asset("CryptoToken") < 2:
            print("You need at least 2 CryptoTokens for "
                  "the chop shop. Better go scrounge under the "
                  "couch.")
            allowed = False

        # Check if hacker needs to adjust trace
        if allowed and self.trace < 1:
            print(f"Your trace level is {self.trace}, no need for the "
                  f"chop shop.")
            allowed = False

        # Begin chop_shop adventure
        if allowed:
            print(f"Your HUD alerts you that your current trace level is "
                  f"[{self.trace}].\n'This is no good.', you think out loud."
                  f" 'I must fix it.'"
                  "\nYou travel to the metropolis outskirts in hopes of "
                  "finding somewhere to decrease your trace level.\n"
                  "You enter a chop shop and a dark shadowy figure with"
                  " long finger nails asks, 'You have the tokens?'")

            # Loop adventure controlled by user input of Y/N
            while True:
                give_tokens = input("Give man 2 tokens (Y/N): ")
                if self.trace == 5:
                    print("You're really testing my patience coming in"
                          " here with that much exposure.")
                if give_tokens in ["Y", "y"]:
                    self.remove_asset("CryptoToken")
                    self.remove_asset("CryptoToken")
                    self.trace = -1
                    self.encryption_flag = False
                    print(f"{self.name} gives shadowy figure 2 "
                          f"CryptoTokens")
                    print("'A fine trade.' The shadowy figure taps on"
                          " his keyboard, a moment later your HUD shows your "
                          f"trace level is now {self.trace}."
                          f"\nYou say thanks and leave the chop shop.")
                    if self.trace == 4:
                        print("[No longer exposed.]")
                    return False
                elif give_tokens in ["N", "n"]:
                    print("You come in here for no reason?! Be gone!"
                          "\nThe shadowy figure throws you out of the "
                          "shop.")
                    return False
                else:
                    print("Invalid input. Enter Y or N.")

        return allowed


    # --- Battle methods ---

    def __validate_attack(self, enemy):
        """Validate if a hacker is allowed to deal damage.

            Parameters:
                enemy (object): The target being damaged.

            Returns:
                bool: True if allowed to deal damage.
        """

        allowed = True

        # Check trace level isn't already at 5
        if self.trace >= 5:
            print(f"EXPOSED! Trace level: {self.trace}"
                  f"\nAttacks and encrypting are disabled until trace "
                  f"level is decreased.")
            allowed = False

        # Check if attacking the Hackers rig and not the hacker
        if allowed and isinstance(enemy, Rig):
            print("Must attack a hacker directly.")
            allowed = False

        # Check is a rig equipped
        if allowed and self.get_rig() is None:
            print("A rig needs to be equipped in order to attack.")
            allowed = False

        # Check if enemy has a rig
        if allowed and enemy.get_equipped_status() is None:
            print(f"Unable to attack an enemy who doesnt have a "
                  f"rig equipped.")
            allowed = False

        # Check if enemy rig is broken
        if allowed and enemy.get_rig().broken is True:
            print(f"Unable to attack a broken rig.")
            allowed = False

        # Check if hacker has a data spike
        if allowed and self.get_rig().find_asset("Data Spike") is None:
            print("No Data Spike in storage, cannot deal damage.")
            allowed = False

        # If checks pass, adjust trace as damage can be dealt
        if allowed:
            self.adjust_trace(enemy)

        return allowed

    def deal_damage(self, enemy):
        """
        Deal damage to an enemy.

            Parameters:
                enemy (object): The target being damaged.
        """
        if self.__validate_attack(enemy):
            self.get_rig().remove_asset("Data Spike")
            enemy.get_rig().damage = 1
            print(f"{self.name} launched Data Spike"
                  f"\n{enemy.name} took 1 damage."
                  f"\n{enemy.name} rig: "
                  f"{enemy.get_rig().damage}/{enemy.get_rig().max_damage}"
                  f" Damage")

            # Set enemy rig to broken if damage = max damage
            if enemy.get_rig().damage >= enemy.get_rig().max_damage:
                enemy.get_rig().broken = True

    def __str__(self):
        return (f"Hacker: {self.name} | Rig: {self.get_rig().name}"
                f" | Trace level: {self.trace}\n"
                f"Inventory: \n" +
                f"\n".join(str(i) for i in self.get_asset()))
