"""
File: Asset.py
Description: <This module contains all the code for assets.>
Author: <Thomas Brown>
ID: <110454503>
Username: <broty041>
This is my own work as defined by the University's Academic Misconduct Policy.
"""


class Asset:
    class_type = "asset"
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.__encryption = False

    # --- Getters and Setters ---
    def get_encryption(self):
        return self.__encryption

    def set_encryption(self, status):
        self.__encryption = status

    # --- Property Attributes ---
    encrypt = property(get_encryption, set_encryption)


    def __eq__(self, other):
        if isinstance(other, Asset):
            return self.name == other.name
        return False

    def __str__(self):
        if not self.__encryption:
            return f"{self.name}: {self.description}"
        else:
            return f"{self.name}: {self.description} [Encrypted]"

