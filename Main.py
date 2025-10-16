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

    print(f"{char_rig.name} filled with items.")
    char_rig.add_asset(get_asset("CryptoToken"))
    char_rig.add_asset(get_asset("Data Spike"))
    char_rig.add_asset(get_asset("Removable Drive"))
    char_rig.add_asset(get_asset("Security Chip"))
    char_rig.add_asset(get_asset("Hardware Patch"))
    char_rig.add_asset(get_asset("CryptoToken"))
    char_rig.add_asset(get_asset("Data Spike"))
    char_rig.add_asset(get_asset("Removable Drive"))
    char_rig.add_asset(get_asset("Security Chip"))
    char_rig.add_asset(get_asset("Hardware Patch"))



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

    hk1.get_rig().remove_asset()
    hk1.deal_damage(hk2)
    hk1.deal_damage(hk2)
    hk1.deal_damage(hk2)


    # hk1.get_rig().remove_asset(get_asset("Data Spike"))
    # hk1.deal_damage(hk2)
    # print(hk2.rig_condition())
    # hk2.get_rig().damage = -2
    # print(hk2.rig_condition())
    # hk2.add_asset(get_asset("Hardware Patch"))
    # hk2.upgrade_rig()
    # hk2.add_asset(get_asset("Hardware Patch"))
    # hk2.upgrade_rig()
    # print(hk2.rig_condition())
    # hk2.get_rig().broken = False
    # print(hk2.get_rig().broken)
    # hk1.deal_damage(hk2)
    # print(hk2.rig_condition())
    # hk1.deal_damage(hk2)
    # print(hk2.rig_condition())
    # hk1.deal_damage(hk2)
    # print(hk2.rig_condition())
    # hk1.deal_damage(hk2)
    # print(hk2.rig_condition())

    # hk1.get_rig().add_asset(get_asset("Data Spike"))
    # hk1.get_rig().list_assets()
    # hk1.deal_damage(hk2)
    # hk1.deal_damage(hk2)
    print(f"--- Concluded battle testing ---\n")


def single_asset_transfer():
    hk1, hk2 = starting_procedure_test()
    hk2.get_rig().add_asset(get_asset("CryptoToken"))
    hk1.asset_transfer(hk2.get_rig(), hk1, get_asset("CryptoToken"))
    hk2.get_rig().list_assets()
    hk1.list_assets()


def extract_rig_storage_test():
    print(f"--- Executing rig storage extraction testing ---")
    hk1, hk2 = starting_procedure_test()
    fill_inv_stor(hk2.get_rig())
    hk2.get_rig().broken = True
    hk1.extract_rigs_storage(hk2.get_rig(), hk1)

    hk1.add_asset(get_asset("Removable Drive"))
    hk1.extract_rigs_storage(hk2.get_rig(), hk1)

    # hk2.get_rig().list_assets()
    print(f"--- Concluded rig storage extraction testing ---\n")


def consume_item_test():
    hk1, hk2 = starting_procedure_test()
    hk1.add_asset(get_asset("Removable Drive"))
    hk1.list_assets()
    hk1.consume_asset(get_asset("Removable Drive"))
    hk1.list_assets()


def change_encryption_test():
    hk1, hk2 = starting_procedure_test()
    #hk1.add_asset(get_asset("Security Chip"))
    # hk1.add_asset(get_asset("Security Chip"))
    hk1.get_rig().add_asset(get_asset("Security Chip"))
    # hk2.add_asset(get_asset("Security Chip"))
    # hk2.get_rig().add_asset(get_asset("Security Chip"))
    # # hk2.add_asset(get_asset("Security Chip"))
    # # hk2.add_asset(get_asset("Security Chip"))
    hk1.change_encryption(hk1.get_rig(), get_asset("Security Chip"), "encrypt")
    # # hk1.change_encryption(hk2, get_asset("Security Chip"), "encrypt")
    # # #
    # # hk2.list_assets()
    # # #
    # # hk1.change_encryption(hk2, get_asset("Security Chip"), "decrypt")
    # # #
    # # hk2.list_assets()
    # hk1.get_rig().add_asset(get_asset("Data Spike"))
    # hk1.deal_damage(hk2)
    # hk1.add_asset(get_asset("CryptoToken"))
    # hk1.add_asset(get_asset("CryptoToken"))
    # hk1.add_asset(get_asset("CryptoToken"))
    # hk1.add_asset(get_asset("CryptoToken"))
    # hk1.add_asset(get_asset("CryptoToken"))
    # hk1.add_asset(get_asset("CryptoToken"))
    # hk1.add_asset(get_asset("CryptoToken"))

    # hk1.chop_shop()
    #
    # hk1.deal_damage(hk2)
    # hk1.deal_damage(hk2)
    # hk1.chop_shop()
    # hk1.get_rig().list_assets()
    #
    # hk1.change_encryption(hk2, get_asset("Security Chip"), "encrypt")
    #
    # hk1.get_rig().list_assets()


def upgrade_rig_level_test():
    hk1 = Hacker("Godfree Norman")
    hk1.upgrade_rig()
    hk1.start_journey("Orange HEV")
    hk1.upgrade_rig()
    hk1.add_asset(get_asset("Hardware Patch"))
    hk1.upgrade_rig()
    hk1.add_asset(get_asset("Hardware Patch"))
    hk1.upgrade_rig()
    hk1.add_asset(get_asset("Hardware Patch"))
    hk1.remove_rig()
    hk1.upgrade_rig()


def chop_shop_test():
    hk1, hk2 = starting_procedure_test()

    # Inventory and storage fill
    fill_inv_stor(hk1)
    hk1.list_assets()
    hk1.chop_shop()
    hk1.edit_trace(5)
    hk1.chop_shop()
    # hk1.chop_shop()


def asset_transfer_test():
    hk1, hk2 = starting_procedure_test()
    hk1.add_asset(get_asset("Hardware Patch"))
    hk1.add_asset(get_asset("Hardware Patch"))
    hk1.add_asset(get_asset("Hardware Patch"))

    hk1.get_rig().add_asset(get_asset("Security Chip"))
    hk1.get_rig().add_asset(get_asset("Hardware Patch"))
    hk1.get_rig().add_asset(get_asset("Hardware Patch"))

    hk1.get_rig().add_asset(get_asset("Hardware Patch"))

    hk2.add_asset(get_asset("Hardware Patch"))
    hk1.list_assets()
    hk2.get_rig().broken = True

    hk1.asset_transfer(hk1, hk2.get_rig(), get_asset("Hardware Patch"))
    hk1.list_assets()

    print(hk1.get_rig().find_asset("Security Chip"))

    # Does from_object asset exist?

    # If its a rig, is it full?

    # What if the class was different?


def multi_asset_transfer_test():
    hk1, hk2 = starting_procedure_test()
    hk1.add_asset(get_asset("Hardware Patch"))
    hk1.add_asset(get_asset("Hardware Patch"))
    hk1.add_asset(get_asset("Hardware Patch"))
    hk1.add_asset(get_asset("Hardware Patch"))
    hk1.add_asset(get_asset("Hardware Patch"))
    hk1.add_asset(get_asset("Hardware Patch"))
    hk1.add_asset(get_asset("Hardware Patch"))
    hk2.add_asset(get_asset("Hardware Patch"))

    hk1.list_assets()

    hk1.get_rig().list_assets()

    hk1.multi_asset_transfer(hk1,hk2.get_rig())
    #hk1.get_rig().list_assets()
    #hk1.list_assets()

def scan_and_remove_test():
    hk1, hk2 = starting_procedure_test()
    hk1.list_assets()
    hk1.add_asset(get_asset("Hardware Patch"))
    hk1.add_asset(get_asset("Hardware Patch"))
    hk1.add_asset(get_asset("Hardware Patch"))


    hk1.get_rig().add_asset(get_asset("Hardware Patch"))
    hk1.get_rig().list_assets()

    print(hk1.get_rig().scan_and_remove("Hardware Patch"))
    hk1.get_rig().list_assets()
    print(hk1)

# --- Main Testing Sequence ---
# starting_procedure_test()
battle_test()
# single_asset_transfer()
# extract_rig_storage_test()
# consume_item_test()
# change_encryption_test()
# upgrade_rig_level_test()
# chop_shop_test()
# asset_transfer_test()
# multi_asset_transfer_test()
# scan_and_remove_test()
