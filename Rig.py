"""
File: Rig.py
Description: <This module contains all the code for the rig.>
Author: <Thomas Brown>
ID: <110454503>
Username: <broty041>
This is my own work as defined by the University's Academic Misconduct Policy.
"""
from Asset import Asset
import random


class Rig:
    # Class Docstring
    """
    The rig class simulates a computer that is equipped to a hacker.

    Attributes
    ----------
    name: str
        Name of the rig.
    owner: object(Hacker)
        Reference to object Hacker owner of rig.
    __storage: list
        List of assets in rig storage.
    __damage: int
        Current damage the rig has taken.
    __max_damage: int
        Max damage rig can take before becoming broken.
    __broken: bool
        Shows if Rig is broken or not.
    __upgrade_level: int
        Rigs current level.
    __storage_size: int
        Rigs current max storage slots.


    Methods
    -------
    generate_asset():
        Uses import random to generate a random asset, 1 at a time
        and add to the rigs storage if not full.
    rig_condition():
        Returns a string showing the rigs current category of
        condition.
    find_asset():
        Find an asset in rigs storage and accept either a string
        or object as a parameter.
    find_encryption_target():
        Find if rig storage contains an asset that's not encrypted,
        or an asset with encryption set that can be decrypted
    scan_and_remove():
        Scans for a specific asset by name, returning and removing
        it if found.
    """

    def __init__(self, name: str, owner):
        self.name = name
        self.owner = owner
        self.__storage = [Asset("Data Spike",
                                "Used in battles."),
                          Asset("Data Spike",
                                "Used in battles."),
                          Asset("Removable Drive",
                                "Found in rigs and "
                                "used for extraction.")
                          ]
        self.__damage = 0
        self.__max_damage = 2
        self.__broken = False
        self.__upgrade_level = 0
        self.__storage_size = 5

    # --- Getters and Setters ---
    def list_assets(self):
        """Prints a list of assets in storage or if its empty."""
        if not self.__storage:
            print(f"{self.owner.name}'s rig's storage is empty.")
        else:
            print(f"{self.owner.name}'s rig contains {len(self.get_asset())} items:")
            for i in self.__storage:
                print(i)



    def get_asset(self):
        return self.__storage

    def get_damage(self):
        return self.__damage

    def set_damage(self, damage):
        self.__damage += damage

    def get_max_damage(self):
        return self.__max_damage

    def set_max_damage(self, damage):
        self.__max_damage += damage

    def get_broken(self):
        return self.__broken

    def set_broken(self, status):
        self.__broken = status

    def get_upgrade_level(self):
        return self.__upgrade_level

    def set_upgrade_level(self, level):
        self.__upgrade_level += level

    def get_storage_size(self):
        return self.__storage_size

    def set_storage_size(self, level):
        self.__storage_size += level

    # --- Property Attributes ---
    damage = property(get_damage, set_damage)
    max_damage = property(get_max_damage, set_max_damage)
    broken = property(get_broken, set_broken)
    upgrade = property(get_upgrade_level, set_upgrade_level)
    storage_size = property(get_storage_size, set_storage_size)

    # --- Storage Related Methods ---
    def add_asset(self, asset):
        """Add an asset to rigs storage. Print if storage full."""
        if len(self.get_asset()) >= self.get_storage_size():
            print("Storage is full.")
            return False
        self.__storage.append(asset)
        return True

    def remove_asset(self, asset):
        """Remove an asset from rigs storage."""
        found = self.find_asset(asset)
        if found:
            self.__storage.remove(found)
        return found

    def find_asset(self, asset: "Takes asset as object or string"):
        """
        Find an asset in rigs storage and accept either a string
        or object as a parameter.
        """
        find_ref = asset.name if isinstance(asset, Asset) else asset
        for i in self.__storage:
            if i.name == find_ref:
                return i
        return None

    def find_encryption_target(self, target, asset, mode):
        """
        Find if rig storage contains an asset that's not encrypted,
        or an asset with encryption set that can be decrypted
        """
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

    def scan_and_remove(self, asset):
        """
        Scans for a specific asset by name, returning and removing
        it if found.
        """
        for i in self.__storage:
            if asset == i.name:
                self.__storage.remove(i)

                return i
        return None


    # --- General methods ---
    def generate_asset(self):
        """
        Uses import random to randomly generate an asset from a list
        and add it to rig's storage if not full.

        Returns:
            bool: True if asset generated otherwise false.
        """
        allow_creation = True

        if len(self.get_asset()) >= self.get_storage_size():
            print("Storage full, unable to generate an asset.")
            allow_creation = False

        if allow_creation:
            # Generate random asset from list of assets
            asset_list = [
                ["CryptoToken", "Used to acquire or repair rigs."],
                ["Data Spike", "Used in battles."],
                ["Removable Drive", "Found in rigs and used for extraction."],
                ["Security Chip", "Used to encrypt or decrypt assets."],
                ["Hardware Patch", "Used to upgrade rigs."]
            ]

            # Generate random number represents index in list.
            x = random.randint(0, 4)

            # Get assets name and desc
            assets_name = asset_list[x][0]
            assets_desc = asset_list[x][1]

            # Add the asset
            self.add_asset(Asset(assets_name, assets_desc))
            print(f"Generated a {assets_name}.")
            return True

        return False

    def rig_condition(self):
        """
        Determines and prints a category of condition for the rig
        based on its damage and upgrade level.

        Returns:
            str: Describes the rigs condition.
        """
        damage = self.damage
        level = self.upgrade

        # Used to determine 'Poor' and 'Usable' categories
        half = self.max_damage / 2

        # Logic to determine categories
        if damage == 0:
            return f"Pristine (Level {level})"
        elif damage == self.max_damage:
            return f"Broken (Level {level})"
        elif damage > half:
            return f"Poor (Level {level})"
        else:
            return f"Usable (Level {level})"

    def __str__(self):
        return (f"{self.name} | Condition: {self.rig_condition()}"
                f"\nInventory: \n" +
                f"\n".join(str(i) for i in self.get_asset()))
