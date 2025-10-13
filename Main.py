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
    hk2 = Hacker("Gee Man")
    hk2.start_journey("Red HEV")
    return hk1, hk2


def battle_test():
    print(f"--- Executing battle testing ---")
    hk1, hk2 = starting_procedure_test()

    # Inventory and storage fill
    fill_inv_stor(hk1)
    fill_inv_stor(hk2)
    fill_inv_stor(hk1.get_rig())
    fill_inv_stor(hk2.get_rig())

    hk1.get_rig().deal_damage(hk2)
    hk1.get_rig().remove_asset("Data Spike")
    hk1.get_rig().deal_damage(hk2)
    hk1.get_rig().add_asset(Asset("Data Spike", "Used in battles."))
    hk1.get_rig().deal_damage(hk2)
    hk1.get_rig().deal_damage(hk2)
    print(f"--- Concluded battle testing ---\n")


def extract_rig_storage_test():
    print(f"--- Executing rig storage extraction testing ---")
    hk1, hk2 = starting_procedure_test()
    fill_inv_stor(hk2.get_rig())
    hk2.get_rig().broken = True
    hk1.get_rig().extract_rig_assets(hk2)
    hk1.get_inventory()
    hk2.get_rig().get_storage()
    print(f"--- Concluded rig storage extraction testing ---\n")


# --- Main Testing Sequence ---
starting_procedure_test()

battle_test()

extract_rig_storage_test()
