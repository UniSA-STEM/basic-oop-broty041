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
        self.__damage_reduction = 1
        self.__upgrade_level = 0
        self.__display_add_print = True

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

    def set_upgrade_level(self):
        self.__upgrade_level += 1

    # --- Property Attributes ---
    damage = property(get_damage, set_damage)
    max_damage = property(get_max_damage, set_max_damage)
    broken = property(get_broken, set_broken)
    upgrade = property(get_upgrade_level, set_upgrade_level)

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







    # --- Battle Related Methods ---
    def pre_attack_check(self, enemy):
        if enemy.get_rig().broken is True:
            print(f"Unable to attack a broken rig.")
            return False

        elif self.search_storage("Data Spike") is None:
            print("No Data Spike's in storage, cannot deal damage.")
            return False

        return True

    def deal_damage(self, enemy):
        if self.pre_attack_check(enemy):
            self.consume_item("Data Spike")
            enemy.get_rig().damage = 1
            print(f"{self.name} attacked {enemy.name}")

        if enemy.get_rig().damage >= enemy.get_rig().max_damage:
            enemy.get_rig().broken = True




    def __str__(self):
        return self.name



