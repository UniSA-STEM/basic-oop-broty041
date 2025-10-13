"""
File: Asset.py
Description: <This module contains all the code for assets.>
Author: <Thomas Brown>
ID: <110454503>
Username: <broty041>
This is my own work as defined by the University's Academic Misconduct Policy.
"""


class Asset:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.__encryption = False

    def __str__(self):
        if not self.__encryption:
            return f"{self.name}: {self.description}"
        else:
            return f"{self.name}: {self.description}[Encrypted]"

