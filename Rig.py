"""
File: Rig.py
Description: <This module contains all the code for the rig.>
Author: <Thomas Brown>
ID: <110454503>
Username: <broty041>
This is my own work as defined by the University's Academic Misconduct Policy.
"""


class Rig:
    class_type = "rig"

    def __init__(self, name, owner):
        self.name = name
        self.owner = owner
        self.__storage = []
        self.__damage = 0
        self.__max_damage = 2
        self.__broken = False
        self.__upgrade_level = 0
        self.__display_add_print = True
        self.__storage_size = 5

    # --- Getters and Setters ---
    def list_storage(self):
        if not self.__storage:
            print(f"{self.owner}'s rig storage is empty.")
        else:
            print(f"Contents of {self.name}'s storage:")
            for i in self.__storage:
                print(i)

    def get_storage(self):
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

    def set_display_add_print(self, flag):
        self.__display_add_print = flag

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
    storage = property(get_storage_size, set_storage_size)

    # --- Storage Related Methods ---
    def add_asset(self, item):
        if self.__display_add_print:
            print(f"{item.name} added to {self.owner}'s rig storage.")
        self.__storage.append(item)

    def remove_asset(self, item):
        if self.search_storage(item) is None:
            print(f"No {item.name}'s in inventory.")
        else:
            print(f"{item.name} removed from {self.owner}'s rig storage.")
            self.__storage.remove(self.__storage[self.search_storage(item)])

    def consume_item(self, item):
        idx = self.search_storage(item)
        if idx is None:
            print(f"No {item}s in storage.")
            return None
        spent_item = self.__storage.remove(self.__storage[idx])
        return spent_item

    def search_storage(self, item):
        for idx, i in enumerate(self.__storage):
            if item == i:
                return idx
        return None

    def __str__(self):
        return self.name
