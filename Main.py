"""
File: main.py
Description: <This module contains all the code for using and testing rig, asset and hacker modules.>
Author: <Thomas Brown>
ID: <110454503>
Username: <broty041>
This is my own work as defined by the University's Academic Misconduct Policy.
"""
from Hacker import Hacker
from Asset import Asset

# Starting procedure
hk1 = Hacker("Godfree Norman")
hk1.get_inventory()
hk1.start_journey()
hk1.get_inventory()


# Load Godfree with items for testing
def load_em_up():
    hk1.add_asset(Asset("CryptoToken", "Used to acquire or repair rigs."))
    hk1.add_asset(Asset("CryptoToken", "Used to acquire or repair rigs."))
    hk1.add_asset(Asset("Data Spike", "Used in battles."))
    hk1.add_asset(Asset("Data Spike", "Used in battles."))
    hk1.add_asset(Asset("Removable Drive", "Found in rigs and used for extraction."))
    hk1.add_asset(Asset("Removable Drive", "Found in rigs and used for extraction."))
    hk1.add_asset(Asset("Security Chip", "Used to encrypt or decrypt assets."))
    hk1.add_asset(Asset("Security Chip", "Used to encrypt or decrypt assets."))
    hk1.add_asset(Asset("Hardware Patch", "Used to upgrade rigs."))
    hk1.add_asset(Asset("Hardware Patch", "Used to upgrade rigs."))


# Battles
def enemy_character():
    hk2 = Hacker("Gee Man")



load_em_up()
hk1.get_inventory()