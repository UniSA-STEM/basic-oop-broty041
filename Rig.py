"""
File: Rig.py
Description: <This module contains all the code for the rig.>
Author: <Thomas Brown>
ID: <110454503>
Username: <broty041>
This is my own work as defined by the University's Academic Misconduct Policy.
"""


class Rig:
    def __init__(self, name):
        self.name = name
        self.__storage = []
        self.__damage = 0
        self.__broken = False
        self.__damage_reduction = 1
        self.__level = 1

    # --- Getters and Setters ---
    def get_storage(self):
        for i in self.__storage:
            print(i)

    def get_damage(self):
        return self.__damage

    def set_damage(self, damage):
        self.__damage += damage

    # --- Property Attributes ---
    damage = property(get_damage, set_damage)

    # --- General Methods ---
    def add_asset(self, item):
        self.__storage.append(item)

    def deal_damage(self, enemy):
        enemy.get_rig().damage = 1


    def __str__(self):
        return f"{self.name}\n{[i for i in self.__storage]}"
