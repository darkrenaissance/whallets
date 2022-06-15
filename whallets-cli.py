"""CLI for users to manage the wallet database and run research functions"""
#TODO:
# 1) Interacting with APIs
# 2) easy adding data to the wallets_dict.json
# 3) Scanning through APIs based on given parameters
# 4) Prints options for the user (-h)

import json
import texts_cli as tc

def cli():
    """Main program for the cli"""
    print(tc.welcome_message())

def main_menu():
    """main cli options"""

def add_wallet():
    """A function to add wallet to the wallets_dict.json"""




def get_wallets():
    ''' Gets the info from the dictionary '''
    filename = 'wallets_dict.json'
    with open(filename) as f:
        all_wallets = json.load(f)
    evm_wallets = all_wallets['evm_wallets']
    spl_wallets = all_wallets['spl_wallets']
    return evm_wallets, spl_wallets


def display_wallets(chain):
    """Displays the wallets according the given chain"""
    # Chains available 'evm','spl'
    # evm shows all the forks
    i = _chain_index(chain)
    dict = get_wallets()[i]
    print(f"\n\n{chain.upper()} WALLETS:")

def _chain_index(chain):
    '''Asigns an index based on given parameter of the chain'''
    if chain.lower() == 'evm':
        i = 0
    elif chain.lower() == 'spl':
        i = 1
    return i

def display_all_wallets():
    display_wallets('evm')
    display_wallets('spl')