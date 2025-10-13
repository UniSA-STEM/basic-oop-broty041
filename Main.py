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


# Load char and rig with items for testing
def fill_inv_stor(char_rig):
    char_rig.add_asset(Asset("CryptoToken", "Used to acquire or repair rigs."))
    char_rig.add_asset(Asset("CryptoToken", "Used to acquire or repair rigs."))
    char_rig.add_asset(Asset("Data Spike", "Used in battles."))
    char_rig.add_asset(Asset("Data Spike", "Used in battles."))
    char_rig.add_asset(Asset("Removable Drive", "Found in rigs and used for extraction."))
    char_rig.add_asset(Asset("Removable Drive", "Found in rigs and used for extraction."))
    char_rig.add_asset(Asset("Security Chip", "Used to encrypt or decrypt assets."))
    char_rig.add_asset(Asset("Security Chip", "Used to encrypt or decrypt assets."))
    char_rig.add_asset(Asset("Hardware Patch", "Used to upgrade rigs."))
    char_rig.add_asset(Asset("Hardware Patch", "Used to upgrade rigs."))


def starting_procedure_test():
    # Starting procedure
    hk1 = Hacker("Godfree Norman")
    hk1.start_journey("Orange HEV")

def battle_test

# Battles
fill_inv_stor(hk1)

hk2 = Hacker("Gee Man")
hk2.start_journey("Red HEV")
fill_inv_stor(hk2)

hk1.get_rig().deal_damage(hk2)


# hk1.get_inventory()


# Main testing sequence
starting_procedure_test()