"""
File: main.py
Description: <This module contains all the code for using and testing
rig, asset and hacker modules.>
Author: <Thomas Brown>
ID: <110454503>
Username: <broty041>
This is my own work as defined by the University's Academic Misconduct
Policy.
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
    """Perform testing of battle related methods and repairing."""
    print(f"--- EXECUTING battle testing ---")
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
    print(hk2.get_rig().broken)
    hk1.deal_damage(hk2)
    hk2.add_asset(get_asset("CryptoToken"))
    hk2.perform_repair()
    print(hk2.get_rig().broken)

    print(f"\n--- Test attacking without rig ---")
    hk3 = Hacker("Mr No Rig")
    hk3.deal_damage(hk1)

    print(f"\n--- Test attacking a hacker without rig ---")
    hk1.deal_damage(hk3)

    print(f"\n--- Test attacking a rig itself ---")
    hk1.deal_damage(hk2.get_rig())

    print(f"\n--- Test attacking when exposed ---")
    hk1.trace = 5
    hk1.encryption_flag = False
    hk1.get_rig().add_asset(get_asset("Data Spike"))
    hk1.deal_damage(hk2)

    print(f"\n--- CONCLUDED battle testing ---")


def extract_rig_storage_test():
    """Test extracting assets from an enemy rig."""
    print(f"--- EXECUTING EXTRACTION TESTING ---")
    hk1, hk2 = starting_procedure_test()

    print(f"\n--- Test extracting from not broken rig ---")
    hk1.extract_rig_storage(hk2.get_rig())

    print(f"\n--- Test extracting without Removable Drive ---")
    hk2.get_rig().broken = True
    hk1.get_rig().remove_asset("Removable Drive")
    hk1.extract_rig_storage(hk2.get_rig())

    print(f"\n--- Test extracting with encrypted Removable Drive ---")
    hk1.get_rig().add_asset(get_asset("Removable Drive"))
    hk1.add_asset(get_asset("Security Chip"))
    hk1.change_encryption(hk1.get_rig(), "Removable Drive", "encrypt")
    hk1.extract_rig_storage(hk2.get_rig())

    print(f"\n--- Test extracting ---")
    hk1.add_asset(get_asset("Security Chip"))
    hk1.change_encryption(hk1.get_rig(), "Removable Drive", "decrypt")
    hk2.get_rig().list_assets()
    hk1.list_assets()
    hk1.extract_rig_storage(hk2.get_rig())
    hk1.list_assets()

    print(f"\n--- Test extraction from an empty rig ---")
    hk1.get_rig().add_asset(get_asset("Removable Drive"))
    hk1.extract_rig_storage(hk2.get_rig())

    print(f"--- CONCLUDED EXTRACTION TESTING ---\n")


def change_encryption_test():
    """Test encrypting and decrypting assets"""
    print(f"--- EXECUTING ENCRYPTION TESTING ---")

    print(f"\n--- Test without Security Chip ---")
    hk1, hk2 = starting_procedure_test()
    hk1.change_encryption(hk1.get_rig(), "Security Chip",
                          "encrypt")

    print(f"\n--- Test with invalid mode ---")
    hk1.get_rig().add_asset(get_asset("Security Chip"))
    hk1.change_encryption(hk1.get_rig(), "Security Chip",
                          "asdfencrypt")

    print(f"\n--- Test actual encryption ---")
    hk1.add_asset(get_asset("Security Chip"))
    hk1.change_encryption(hk1.get_rig(), "Security Chip",
                          "encrypt")
    hk1.get_rig().list_assets()

    print(f"\n--- Test encrypting already encrypted  ---")
    hk1.add_asset(get_asset("Security Chip"))
    hk1.change_encryption(hk1.get_rig(), "Security Chip",
                          "encrypt")

    print(f"\n--- Test actual decryption ---")
    hk1.add_asset(get_asset("Security Chip"))
    hk1.change_encryption(hk1.get_rig(), get_asset("Security Chip"),
                          "decrypt")
    hk1.get_rig().list_assets()

    print(f"\n--- Test decrypt when nothing to decrypt ---")
    hk1.change_encryption(hk1.get_rig(), get_asset("Security Chip"),
                          "decrypt")

    print(f"\n--- Test encrypt in inventory Security Chip with <2"
          f" Security Chips---")
    hk1.change_encryption(hk1, get_asset("Security Chip"), "encrypt")

    print(f"\n--- Test encrypt in inventory on Security Chip ---")
    hk1.add_asset(get_asset("Security Chip"))
    hk1.change_encryption(hk1, get_asset("Security Chip"), "encrypt")
    hk1.list_assets()

    print(f"\n--- Test encrypt when exposed  ---")
    hk1.trace = 5
    hk1.encryption_flag = False
    hk1.add_asset(get_asset("Security Chip"))
    hk1.change_encryption(hk1, get_asset("Security Chip"), "encrypt")

    print(f"\n--- Test encrypting enemy asset ---")
    hk1.trace = 0
    hk1.encryption_flag = True
    hk1.add_asset(get_asset("Security Chip"))
    hk2.change_encryption(hk1, get_asset("Security Chip"), "encrypt")

    print(f"\n--- CONCLUDED ENCRYPTION TESTING ---")


def upgrade_rig_level_test():
    """Test upgrading hackers rig."""

    print(f"--- EXECUTING UPGRADE LEVEL TESTING ---")

    print(f"\n--- Test upgrading with no rig ---")
    hk3 = Hacker("Mr No Rig")
    hk3.upgrade_rig()

    print(f"\n--- Test with no hardware patch ---")
    hk1 = Hacker("Godfree Norman")
    hk1.start_journey("Orange HEV")
    hk1.upgrade_rig()

    print(f"\n--- Test upgrading ---")
    hk1.add_asset(get_asset("Hardware Patch"))
    hk1.upgrade_rig()

    print(f"\n--- CONCLUDED UPGRADE LEVEL TESTING ---")


def chop_shop_test():
    """Test the chop shop text adventure."""
    hk1, hk2 = starting_procedure_test()
    print(f"--- EXECUTING CHOP SHOP TEST ---")

    print(f"\n--- Test chopshop without cryptotokens ---")
    hk1.chop_shop()

    print(f"\n--- Test chop shop no trace ---")
    hk1.add_asset(get_asset("CryptoToken"))
    hk1.add_asset(get_asset("CryptoToken"))
    hk1.chop_shop()

    print(f"\n--- Test chopshop ---")
    hk1.trace = 3
    hk1.chop_shop()

    print(f"\n--- Test chopshop when exposed ---")
    hk1.add_asset(get_asset("CryptoToken"))
    hk1.add_asset(get_asset("CryptoToken"))
    hk1.trace = 3
    hk1.encryption_flag = False
    hk1.chop_shop()

    print(f"\n--- CONCLUDED CHOP SHOP TEST ---")


def perform_transfer_test():
    """Perform testing of transferring a single asset"""

    print(f"--- EXECUTING PERFORM TRANSFER TEST ---")

    print(f"\n--- Test transfer inventory to rig  ---")
    hk1, hk2 = starting_procedure_test()
    hk1.add_asset(get_asset("Hardware Patch"))
    hk1.list_assets()
    hk1.get_rig().list_assets()
    hk1.perform_transfer(hk1, hk1.get_rig(), get_asset("Hardware Patch"))
    hk1.list_assets()
    hk1.get_rig().list_assets()

    print(f"\n--- Test rig to inventory  ---")
    hk1.perform_transfer(hk1.get_rig(), hk1, get_asset("Hardware Patch"))
    hk1.list_assets()
    hk1.get_rig().list_assets()

    print(f"\n--- Test transfer asset not there ---")
    hk1.perform_transfer(hk1.get_rig(), hk1, get_asset("CryptoToken"))
    hk1.perform_transfer(hk1, hk1.get_rig(), get_asset("CryptoToken"))

    print(f"\n--- Test transfer to full rig  ---")
    fill_inv_stor(hk1)
    fill_inv_stor(hk1.get_rig())
    hk1.perform_transfer(hk1, hk1.get_rig(), get_asset("CryptoToken"))

    print(f"\n--- Test transfer encrypted asset ---")
    hk1.change_encryption(hk1.get_rig(), "CryptoToken",
                          "encrypt")
    hk1.perform_transfer(hk1.get_rig(), hk1, get_asset("CryptoToken"))

    print(f"\n--- Test transfer to enemy ---")
    hk1.perform_transfer(hk1.get_rig(), hk2, get_asset("CryptoToken"))

    print(f"\n--- CONCLUDED PERFORM TRANSFER TESTING ---")


def perform_multi_transfer_test():
    """Test transferring multiple assets."""
    print(f"--- EXECUTING MULTI TRANSFER TEST ---")

    print(f"\n--- Testing multi transfer inventory to rig  ---")
    hk1, hk2 = starting_procedure_test()
    fill_inv_stor(hk1)
    hk1.list_assets()
    hk1.perform_multi_transfer(hk1, hk1.get_rig())
    hk1.list_assets()
    hk1.get_rig().list_assets()

    print(f"\n--- Testing multi transfer rig to inventory  ---")
    hk1.list_assets()
    hk1.get_rig().list_assets()
    hk1.perform_multi_transfer(hk1.get_rig(), hk1)
    hk1.list_assets()
    hk1.get_rig().list_assets()

    print(f"\n--- Testing multi transfer from empty source  ---")
    hk1.perform_multi_transfer(hk1.get_rig(), hk1)

    print(f"\n--- CONCLUDED MULTI TRANSFER TEST ---")



def scan_and_remove_test():
    """Testing the scan and remove method."""
    print(f"--- EXECUTING SCAN AND REMOVE TEST ---")

    print(f"\n--- Test scan and remove  ---")
    hk1, hk2 = starting_procedure_test()
    hk1.get_rig().add_asset(get_asset("Hardware Patch"))
    hk1.get_rig().list_assets()
    hk1.get_rig().scan_and_remove("Hardware Patch")
    hk1.get_rig().list_assets()

    print(f"\n--- CONCLUDED SCAN AND REMOVE TEST ---")


def repair_rig_test():
    """Testing repairing rig."""
    print(f"--- EXECUTING REPAIR TESTING ---")

    print(f"\n--- Test repair undamaged rig ---")
    hk1, hk2 = starting_procedure_test()
    hk1.perform_repair()

    print(f"\n--- Test repair no rig ---")
    hk3 = Hacker("Mr No Rig")
    hk3.perform_repair()

    print(f"\n--- Test repair without CryptoToken ---")
    hk1.get_rig().damage = 2
    hk1.get_rig().broken = True
    print(hk1.get_rig().rig_condition())
    hk1.perform_repair()

    print(f"\n--- Test a repair ---")
    hk1.add_asset(get_asset("CryptoToken"))
    print(hk1.get_rig().broken)
    hk1.perform_repair()
    print(hk1.get_rig().rig_condition())
    print(hk1.get_rig().broken)

    print(f"\n--- CONCLUDED REPAIR TESTING ---")


def check_str_outputs():
    """Checking __str__'s are outputting correctly."""
    hk1, hk2 = starting_procedure_test()
    print(hk2.get_rig())
    print(hk2)

# --- Main Testing Sequence ---
# starting_procedure_test()
# battle_test()
# extract_rig_storage_test()
# change_encryption_test()
# upgrade_rig_level_test()
# chop_shop_test()
# perform_transfer_test()
# perform_multi_transfer_test()
# scan_and_remove_test()
# repair_rig_test()
# check_str_outputs()
