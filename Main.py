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

asset_dict = {
    "CryptoToken": "Used to acquire or repair rigs.",
    "Data Spike": "Used in battles.",
    "Removable Drive": "Found in rigs and used for extraction.",
    "Security Chip": "Used to encrypt or decrypt assets.",
    "Hardware Patch": "Used to upgrade rigs."
}

def get_asset(name):

    assets = asset_dict
    return Asset(name, assets[name])


# Load char and rig with items for testing
def fill_inv_stor(char_rig):
    char_rig.set_display_add_print(False)
    print(f"{char_rig} filled with items.")
    char_rig.add_asset(get_asset("CryptoToken"))
    char_rig.add_asset(get_asset("CryptoToken"))
    char_rig.add_asset(get_asset("Data Spike"))
    char_rig.add_asset(get_asset("Data Spike"))
    char_rig.add_asset(get_asset("Removable Drive"))
    char_rig.add_asset(get_asset("Removable Drive"))
    char_rig.add_asset(get_asset("Security Chip"))
    char_rig.add_asset(get_asset("Security Chip"))
    char_rig.add_asset(get_asset("Hardware Patch"))
    char_rig.add_asset(get_asset("Hardware Patch"))
    char_rig.set_display_add_print(True)




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

    fill_inv_stor(hk1.get_rig())
    fill_inv_stor(hk2.get_rig())


    hk1.deal_damage(hk2)
    hk1.get_rig().remove_asset(get_asset("Data Spike"))
    hk1.deal_damage(hk2)
    print(hk2.rig_condition())
    hk2.get_rig().damage = -2
    print(hk2.rig_condition())
    hk2.add_asset(get_asset("Hardware Patch"))
    hk2.upgrade_rig()
    hk2.add_asset(get_asset("Hardware Patch"))
    hk2.upgrade_rig()
    print(hk2.rig_condition())
    hk2.get_rig().broken = False
    print(hk2.get_rig().broken)
    hk1.deal_damage(hk2)
    print(hk2.rig_condition())
    hk1.deal_damage(hk2)
    print(hk2.rig_condition())
    hk1.deal_damage(hk2)
    print(hk2.rig_condition())
    hk1.deal_damage(hk2)
    print(hk2.rig_condition())


    # hk1.get_rig().add_asset(get_asset("Data Spike"))
    # hk1.get_rig().list_storage()
    # hk1.deal_damage(hk2)
    # hk1.deal_damage(hk2)
    print(f"--- Concluded battle testing ---\n")



def single_asset_transfer():
    hk1, hk2 = starting_procedure_test()
    hk2.get_rig().add_asset(get_asset("CryptoToken"))
    hk1.asset_transfer(hk2.get_rig(), hk1, get_asset("CryptoToken"))
    hk2.get_rig().list_storage()
    hk1.list_inventory()

def extract_rig_storage_test():
    print(f"--- Executing rig storage extraction testing ---")
    hk1, hk2 = starting_procedure_test()
    fill_inv_stor(hk2.get_rig())
    hk2.get_rig().broken = True
    hk1.extract_rigs_storage(hk2.get_rig(), hk1)

    hk1.add_asset(get_asset("Removable Drive"))
    hk1.extract_rigs_storage(hk2.get_rig(), hk1)

    # hk2.get_rig().list_storage()
    print(f"--- Concluded rig storage extraction testing ---\n")

def consume_item_test():
    hk1, hk2 = starting_procedure_test()
    hk1.add_asset(get_asset("Removable Drive"))
    hk1.list_inventory()
    hk1.consume_item(get_asset("Removable Drive"))
    hk1.list_inventory()

def encrypt_asset_test():
    hk1, hk2 = starting_procedure_test()
    hk1.add_asset(get_asset("Security Chip"))
    hk1.add_asset(get_asset("Security Chip"))
    hk1.list_inventory()
    hk1.encrypt_asset(get_asset("Security Chip"), True)
    hk1.list_inventory()

def upgrade_rig_level_test():
    hk1, hk2 = starting_procedure_test()
    hk1.upgrade_rig()
    hk1.add_asset(get_asset("Hardware Patch"))
    hk1.upgrade_rig()
    hk1.add_asset(get_asset("Hardware Patch"))
    hk1.upgrade_rig()
    hk1.add_asset(get_asset("Hardware Patch"))
    hk1.remove_rig()
    hk1.upgrade_rig()





# --- Main Testing Sequence ---
# starting_procedure_test()
battle_test()
# single_asset_transfer()
# extract_rig_storage_test()
# consume_item_test()
# encrypt_asset_test()
#upgrade_rig_level_test()

