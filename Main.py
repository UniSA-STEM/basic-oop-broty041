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


def fill_inv_stor(char_rig):
    """Fill hacker up with items."""
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
    """Initialise 2 hackers."""

    # Create hackers
    hk1 = Hacker("Godfree Norman")
    hk2 = Hacker("Gee Man")

    # Start hackers journeys
    hk1.start_journey("Orange HEV")
    hk2.start_journey("Red HEV")

    print(hk1)
    print(hk2)

    return hk1, hk2


def battle_test():
    """Perform testing of battle related methods"""
    print(f"--- Executing battle testing ---")
    hk1, hk2 = starting_procedure_test()

    print(f"\n--- Test without dataspike ---")
    hk1.get_rig().remove_asset("Data Spike")
    hk1.get_rig().remove_asset("Data Spike")
    hk1.deal_damage(hk2)

    print(f"\n--- Test attacking ---")
    hk1.get_rig().add_asset(get_asset("Data Spike"))
    hk1.get_rig().add_asset(get_asset("Data Spike"))
    hk1.deal_damage(hk2)
    hk1.deal_damage(hk2)

    print(f"\n--- Test attacking broken rig ---")
    hk2.get_rig().broken = True
    print(hk2.get_rig().broken)
    hk1.deal_damage(hk2)
    hk2.get_rig().broken = False
    print(hk2.get_rig().broken)

    print(f"\n--- Test trace level interaction ---")
    hk1.deal_damage(hk2)
    hk1.deal_damage(hk2)
    hk1.deal_damage(hk2)

    # hk1.get_rig().remove_asset(get_asset("Data Spike"))
    # hk1.deal_damage(hk2)
    # print(hk2.get_rig().rig_condition())
    # hk2.get_rig().damage = -2
    # print(hk2.get_rig().rig_condition())
    # hk2.add_asset(get_asset("Hardware Patch"))
    # hk2.upgrade_rig()
    # hk2.add_asset(get_asset("Hardware Patch"))
    # hk2.upgrade_rig()
    # print(hk2.get_rig().rig_condition())
    # hk2.get_rig().broken = False
    # print(hk2.get_rig().broken)
    # hk1.deal_damage(hk2)
    # print(hk2.get_rig().rig_condition())
    # hk1.deal_damage(hk2)
    # print(hk2.get_rig().rig_condition())
    # hk1.deal_damage(hk2)
    # print(hk2.get_rig().rig_condition())
    # hk1.deal_damage(hk2)
    # print(hk2.get_rig().rig_condition())
    #
    # hk1.get_rig().add_asset(get_asset("Data Spike"))
    # hk1.get_rig().list_assets()
    # hk1.get_rig().add_asset(get_asset("Data Spike"))
    # hk1.get_rig().add_asset(get_asset("Data Spike"))
    # hk1.get_rig().add_asset(get_asset("Data Spike"))
    #
    # hk1.deal_damage(hk2)
    # hk1.deal_damage(hk2)
    # hk1.deal_damage(hk2)
    # hk1.deal_damage(hk2)
    print(f"--- Concluded battle testing ---\n")


def extract_rig_storage_test():
    """Test extracting assets from an enemy rig."""
    print(f"--- Executing rig storage extraction testing ---")
    hk1, hk2 = starting_procedure_test()
    hk2.get_rig().broken = False
    hk1.extract_rig_storage(hk2.get_rig())
    hk2.get_rig().broken = True
    hk1.get_rig().remove_asset("Removable Drive")
    hk1.extract_rig_storage(hk2.get_rig())
    hk1.get_rig().add_asset(get_asset("Removable Drive"))
    hk1.get_rig().list_assets()
    hk1.add_asset(get_asset("Security Chip"))
    hk1.change_encryption(hk1.get_rig(), "Removable Drive", "encrypt")
    hk1.extract_rig_storage(hk2.get_rig())
    hk1.add_asset(get_asset("Security Chip"))
    hk1.change_encryption(hk1.get_rig(), "Removable Drive", "decrypt")
    hk1.extract_rig_storage(hk2.get_rig())
    hk1.get_rig().list_assets()
    hk1.get_rig().add_asset(get_asset("Removable Drive"))
    hk1.extract_rig_storage(hk2.get_rig())
    hk2.get_rig().add_asset(get_asset("Removable Drive"))
    hk1.extract_rig_storage(hk2.get_rig())
    print(f"--- Concluded rig storage extraction testing ---\n")


def change_encryption_test():
    """Test encrypting and decrypting assets"""
    hk1, hk2 = starting_procedure_test()

    print(hk1.get_trace())
    hk1.add_asset(get_asset("Security Chip"))
    hk1.get_rig().add_asset(get_asset("Security Chip"))
    hk1.change_encryption(hk1.get_rig(), "Security Chip", "asdfencrypt")
    # hk1.get_rig().list_assets()
    hk1.perform_transfer(hk1.get_rig(), hk1, "Security Chip")
    # hk1.get_rig().list_assets()

    hk1.list_assets()
    hk1.add_asset(get_asset("Security Chip"))
    hk1.add_asset(get_asset("Security Chip"))
    hk1.get_rig().add_asset(get_asset("Security Chip"))
    hk1.get_rig().add_asset(get_asset("Security Chip"))

    hk1.change_encryption(hk1.get_rig(), get_asset("Security Chip"), "encrypt")
    hk1.get_rig().list_assets()
    hk1.change_encryption(hk1.get_rig(), get_asset("Security Chip"), "decrypt")
    hk1.get_rig().list_assets()
    hk1.trace = 5
    hk1.encryption_flag = False
    hk1.change_encryption(hk1, get_asset("Security Chip"), "encrypt")


def upgrade_rig_level_test():
    """Test upgrading hackers rig."""
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
    """Test the chop shop text adventure."""
    hk1, hk2 = starting_procedure_test()
    fill_inv_stor(hk1)
    hk1.list_assets()
    hk1.chop_shop()
    hk1.trace = 5
    hk1.chop_shop()


def perform_transfer_test():
    """Perform testing of transferring a single asset"""
    hk1, hk2 = starting_procedure_test()
    hk1.add_asset(get_asset("Hardware Patch"))
    hk1.get_rig().add_asset(get_asset("Hardware Patch"))
    hk2.get_rig().broken = True
    hk1.perform_transfer(hk2.get_rig(), hk1, get_asset("Hardware Patch"))
    hk1.perform_transfer(hk1, hk2.get_rig(), get_asset("Hardware Patch"))
    hk1.perform_transfer(hk1.get_rig(), hk1, "Security Chip")
    hk1.perform_transfer(hk1, hk1.get_rig(), "Security Chip")
    # Storage size check
    hk1.get_rig().storage_size = -4
    hk1.perform_transfer(hk1, hk1.get_rig(), "Hardware Patch")
    hk1.get_rig().list_assets()
    hk1.add_asset(get_asset("Security Chip"))
    hk1.change_encryption(hk1.get_rig(), "Hardware Patch", "encrypt")
    hk1.get_rig().list_assets()
    hk1.add_asset(get_asset("Security Chip"))
    hk1.change_encryption(hk1.get_rig(), "Hardware Patch", "decrypt")
    hk1.add_asset(get_asset("Security Chip"))
    hk1.change_encryption(hk1, "Hardware Patch", "encrypt")
    hk1.list_assets()
    hk1.perform_transfer(hk1, hk1.get_rig(), "Hardware Patch")
    hk1.get_rig().remove_asset("Data Spike")
    hk1.get_rig().remove_asset("Data Spike")
    hk1.perform_transfer(hk1, hk1.get_rig(), "Hardware Patch")
    hk1.get_rig().storage_size = 8
    hk1.perform_transfer(hk1, hk1.get_rig(), "Hardware Patch")
    hk1.change_encryption(hk1.get_rig(), "Hardware Patch", "asdfencrypt")
    hk1.add_asset(get_asset("Security Chip"))
    hk1.change_encryption(hk1.get_rig(), "Hardware Patch", "asdfencrypt")


def perform_multi_transfer_test():
    """Test transferring multiple assets."""
    hk1, hk2 = starting_procedure_test()
    hk1.list_assets()
    hk1.perform_multi_transfer(hk1, hk1.get_rig())


def scan_and_remove_test():
    """Testing the scan and remove method."""
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
    """Testing repairing rig."""
    hk1, hk2 = starting_procedure_test()

    hk1.perform_repair()
    hk1.get_rig().damage = 3
    hk1.perform_repair()
    hk1.add_asset(get_asset("CryptoToken"))
    hk1.perform_repair()
    print(hk1.get_rig().damage)


def check_str_outputs():
    """Checking __str__'s are outputting correctly."""
    hk1, hk2 = starting_procedure_test()
    print(hk2.get_rig())
    print(hk2)


# --- Main Testing Sequence ---
# starting_procedure_test()
battle_test()
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
