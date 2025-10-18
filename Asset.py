"""
File: Asset.py
Description: <This module contains all the code for assets.>
Author: <Thomas Brown>
ID: <110454503>
Username: <broty041>
This is my own work as defined by the University's Academic Misconduct
Policy.
"""



class Asset:
    # Class Docstring
    """
    Assets are like items, they are used by Hackers and Rigs to
    perform actions.

    Attributes
    ----------
    name: str
        Name of the asset.
    description: str
        Describes what the asset does.
    __encryption: bool
        True means asset is encryption, False means unencrypted.
    """
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

    # Matches asset names only.
    def __eq__(self, other):
        if isinstance(other, Asset):
            return self.name == other.name
        return False

    def __str__(self):
        if not self.__encryption:
            return f"{self.name}: {self.description}"
        else:
            return f"{self.name}: {self.description} [Encrypted]"

