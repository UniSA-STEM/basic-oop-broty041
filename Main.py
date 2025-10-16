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

    hk1.remove_asset("Data Spike")
    hk1.deal_damage(hk2)
    hk1.deal_damage(hk2)
    hk1.deal_damage(hk2)


    hk1.get_rig().remove_asset(get_asset("Data Spike"))
    hk1.deal_damage(hk2)
    print(hk2.get_rig().rig_condition())
    hk2.get_rig().damage = -2
    print(hk2.get_rig().rig_condition())
    hk2.add_asset(get_asset("Hardware Patch"))
    hk2.upgrade_rig()
    hk2.add_asset(get_asset("Hardware Patch"))
    hk2.upgrade_rig()
    print(hk2.get_rig().rig_condition())
    hk2.get_rig().broken = False
    print(hk2.get_rig().broken)
    hk1.deal_damage(hk2)
    print(hk2.get_rig().rig_condition())
    hk1.deal_damage(hk2)
    print(hk2.get_rig().rig_condition())
    hk1.deal_damage(hk2)
    print(hk2.get_rig().rig_condition())
    hk1.deal_damage(hk2)
    print(hk2.get_rig().rig_condition())

    hk1.get_rig().add_asset(get_asset("Data Spike"))
    hk1.get_rig().list_assets()
    hk1.deal_damage(hk2)
    hk1.deal_damage(hk2)

    print(f"--- Concluded battle testing ---\n")


def single_asset_transfer():
    hk1, hk2 = starting_procedure_test()
    hk2.get_rig().add_asset(get_asset("CryptoToken"))
    hk1.perform_transfer(hk2.get_rig(), hk1, get_asset("CryptoToken"))
    hk2.get_rig().list_assets()
    hk1.list_assets()


def extract_rig_storage_test():
    print(f"--- Executing rig storage extraction testing ---")
    hk1, hk2 = starting_procedure_test()
    hk2.get_rig().broken = False
    hk1.extract_rig_storage(hk2.get_rig())
    hk2.get_rig().broken = True
    hk1.get_rig().remove_asset("Removable Drive")
    hk1.extract_rig_storage(hk2.get_rig())
    hk1.get_rig().add_asset(get_asset("Removable Drive"))
    hk1.get_rig().list_assets()

    hk1.extract_rig_storage(hk2.get_rig())
    hk1.get_rig().list_assets()
    hk1.get_rig().add_asset(get_asset("Removable Drive"))
    hk1.extract_rig_storage(hk2.get_rig())
    hk2.get_rig().add_asset(get_asset("Removable Drive"))
    hk1.extract_rig_storage(hk2.get_rig())



    print(f"--- Concluded rig storage extraction testing ---\n")




def change_encryption_test():
    hk1, hk2 = starting_procedure_test()
    hk1.add_asset(get_asset("Security Chip"))
    hk1.get_rig().add_asset(get_asset("Security Chip"))
    hk1.change_encryption(hk1.get_rig(), "Security Chip", "encrypt")
    hk1.get_rig().list_assets()
    hk1.perform_transfer(hk1.get_rig(), hk1,"Security Chip")
    hk1.get_rig().list_assets()

    hk1.list_assets()

    # hk1.change_encryption(hk1.get_rig(), get_asset("Security Chip"), "decrypt")
    #hk1.add_asset(get_asset("Security Chip"))
    # hk1.change_encryption(hk1.get_rig(), get_asset("Security Chip"), "decrypt")
    #hk1.get_rig().list_assets()


    # # hk1.change_encryption(hk2, get_asset("Security Chip"), "encrypt")
    # # #
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


def perform_transfer_test():
    hk1, hk2 = starting_procedure_test()
    hk1.add_asset(get_asset("Hardware Patch"))
    hk1.get_rig().add_asset(get_asset("Hardware Patch"))
    hk2.get_rig().broken = True
    hk1.perform_transfer(hk2.get_rig(), hk1, get_asset("Hardware Patch"))
    hk1.perform_transfer(hk1, hk2.get_rig(), get_asset("Hardware Patch"))
    hk1.perform_transfer(hk1.get_rig(), hk1, "Security Chip")
    hk1.perform_transfer(hk1, hk1.get_rig(), "Security Chip")
    hk1.get_rig().storage_size = -4
    hk1.perform_transfer(hk1, hk1.get_rig(), "Hardware Patch")
    hk1.get_rig().list_assets()
    hk1.add_asset(get_asset("Security Chip"))
    hk1.change_encryption(hk1.get_rig(),"Hardware Patch", "encrypt")
    hk1.get_rig().list_assets()
    hk1.add_asset(get_asset("Security Chip"))
    hk1.change_encryption(hk1.get_rig(),"Hardware Patch", "decrypt")
    hk1.add_asset(get_asset("Security Chip"))
    hk1.change_encryption(hk1,"Hardware Patch", "encrypt")
    hk1.list_assets()
    hk1.perform_transfer(hk1, hk1.get_rig(), "Hardware Patch")
    hk1.get_rig().remove_asset("Data Spike")
    hk1.get_rig().remove_asset("Data Spike")
    hk1.perform_transfer(hk1, hk1.get_rig(), "Hardware Patch")
    hk1.get_rig().storage_size = 8
    hk1.perform_transfer(hk1, hk1.get_rig(), "Hardware Patch")
    hk1.change_encryption(hk1.get_rig(),"Hardware Patch", "asdfencrypt")
    hk1.add_asset(get_asset("Security Chip"))
    hk1.change_encryption(hk1.get_rig(),"Hardware Patch", "asdfencrypt")




def perform_multi_transfer_test():
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
    hk1.perform_multi_transfer(hk1.get_rig(), hk1)
    hk1.perform_multi_transfer(hk1,hk1.get_rig())

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


def repair_rig_test():
    hk1, hk2 = starting_procedure_test()

    hk1.perform_repair()
    hk1.get_rig().damage = 3
    hk1.perform_repair()
    hk1.add_asset(get_asset("CryptoToken"))
    hk1.perform_repair()

def generate_asset_test():
    hk1, hk2 = starting_procedure_test()
    hk1.get_rig().generate_asset()
    hk1.get_rig().generate_asset()
    hk1.get_rig().generate_asset()
    hk1.get_rig().generate_asset()

def check_str_outputs():
    hk1, hk2 = starting_procedure_test()
    print(hk2.get_rig())
    print(hk2)

# --- Main Testing Sequence ---
# starting_procedure_test()
# battle_test()
# single_asset_transfer()
# extract_rig_storage_test()
# change_encryption_test()
# upgrade_rig_level_test()
# chop_shop_test()
# perform_transfer_test()
# perform_multi_transfer_test()
# scan_and_remove_test()
# repair_rig_test()
# generate_asset_test()
# check_str_outputs()

