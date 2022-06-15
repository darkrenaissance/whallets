"""CLI for users to manage the wallet database and run research functions"""
#TODO:
# 1) Interacting with APIs
# 2) easy adding data to the wallets_dict.json
# 3) Scanning through APIs based on given parameters
# 4) Prints options for the user (-h)

import json

def get_wallets():
    ''' Gets the info from the dictionary '''
    filename = 'wallets_dict.json'
    with open(filename) as f:
        all_wallets = json.load(f)
    evm_wallets = all_wallets['evm_wallets']
    spl_wallets = all_wallets['spl_wallets']
    return evm_wallets, spl_wallets