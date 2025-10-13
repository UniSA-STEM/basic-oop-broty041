"""
File: Rig.py
Description: <This module contains all the code for the rig.>
Author: <Thomas Brown>
ID: <110454503>
Username: <broty041>
This is my own work as defined by the University's Academic Misconduct Policy.
"""


class Rig:
    def __init__(self, name, owner):
        self.name = name
        self.owner = owner
        self.__storage = []
        self.__damage = 0
        self.__max_damage = 2
        self.__broken = False
        self.__damage_reduction = 1
        self.__level = 1

    # --- Getters and Setters ---
    def get_storage(self):
        if not self.__storage:
            print("Inventory is empty.")
        else:
            print(f"Contents of {self.name}'s storage:")
            for i in self.__storage:
                print(i)

    def getter_storage(self):
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

    # --- Property Attributes ---
    damage = property(get_damage, set_damage)
    max_damage = property(get_max_damage, set_max_damage)
    broken = property(get_broken, set_broken)

    # --- Storage Related Methods ---
    def add_asset(self, item):
        self.__storage.append(item)

    def remove_asset(self, item):
        if self.search_storage(item) is None:
            print(f"No {item.name}'s in inventory.")
        else:
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
            if item == i.name:
                return idx
        return None

    def extract_rig_assets(self, target):
        owner = self.owner
        storage_copy = target.get_rig().getter_storage().copy()
        unsecure_count = 0
        secure_count = 0
        if target.get_rig().broken is True and len(storage_copy) > 0:
            for i in storage_copy:
                if i.get_encryption() is False:
                    print(i)
                    owner.add_asset(i)
                    target.get_rig().remove_asset(i.name)
                    unsecure_count += 1
                else:
                    secure_count += 1
            print(f"{unsecure_count} unsecured assets transferred from {self.owner} to {target.get_rig().owner}."
                  f"\n{secure_count} secure assets not transferred.")
        else:
            print("This rig has no items.")


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
        return f"{self.name}\n{[i for i in self.__storage]}"

