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

    def get_storage(self):
        for i in self.__storage:
            print(i)

    def __str__(self):
        return [i for i in self.__storage]