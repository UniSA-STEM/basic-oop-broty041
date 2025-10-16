"""
File: Rig.py
Description: <This module contains all the code for the rig.>
Author: <Thomas Brown>
ID: <110454503>
Username: <broty041>
This is my own work as defined by the University's Academic Misconduct Policy.
"""
from Asset import Asset

class Rig:
    class_type = "rig"

    def __init__(self, name, owner):
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
        if not self.__storage:
            print(f"{self.owner}'s rig's storage is empty.")
        else:
            print(f"{self.name} contains {len(self.get_asset())} items::")
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

    def get_container_term(self):
        return "rig's storage"

    # --- Property Attributes ---
    damage = property(get_damage, set_damage)
    max_damage = property(get_max_damage, set_max_damage)
    broken = property(get_broken, set_broken)
    upgrade = property(get_upgrade_level, set_upgrade_level)
    storage_size = property(get_storage_size, set_storage_size)

    # --- Storage Related Methods ---
    def add_asset(self, asset):
        if len(self.get_asset()) >= self.get_storage_size():
            print("Storage is full.")
            return False
        self.__storage.append(asset)
        return True

    def remove_asset(self, asset):
        found = self.find_asset(asset)
        if found:
            self.__storage.remove(found)
        return found

    def find_asset(self, asset: "Takes asset as object or string"):
        find_ref = asset.name if isinstance(asset, Asset) else asset
        for i in self.__storage:
            if i.name == find_ref:
                return i
        return None

    def find_asset_index(self, asset):
        for idx, i in enumerate(self.__storage):
            if asset == i:
                return idx
        return None

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

    def scan_and_remove(self, asset):
        for i in self.__storage:
            if asset == i.name:

                self.__storage.remove(i)

                return i
        return None


    def __str__(self):
        return self.name
