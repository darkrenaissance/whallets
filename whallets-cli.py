"""CLI for users to manage the wallet database and run research functions"""
#TODO:
# 1) Interacting with APIs
# 2) easy adding data to the wallets_dict.json
# 3) Scanning through APIs based on given parameters
# 4) Prints options for the user (-h)

import json
import texts_cli as tc

def cli_main():
    """Main program for the cli"""
    print(tc.welcome_message())

def main_menu():
    """main cli options"""

def add_wallet():
    """A function to add wallet to the wallets_dict.json"""
    chain = input(tc._choose_chain())
    name = input(tc._prompt_name())
    addr = input(tc._prompt_address())
    inf = input(tc._prompt_info())
    twtr = input(tc._prompt_twitter())
    ens = input(tc._prompt_ens())
    check_wallet(chain, name, addr, inf, twtr, ens)



def check_wallet(chain, name, addr, twtr, ens):
    """
    Scans through wallets to check if a new wallet is not already in the
    database"
    """
    i = _chain_index(chain)
    dict = get_wallets()[i]
    for key, value in dict.items():
        user = key
        wallets = value['wallets']
        for key
        info = value['info']
        twitter = value['twitter']
        if user == name:
            return 0
        elif addr in wallets.values():
            return 1
        elif



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

    for key, value in dict.items():
        user = key
        wallets = value['wallets']
        info = value['info']
        twitter = value['twitter']
        chains = []
        for key, value in wallets.items():
            chains.append(key)
        print(f"\nUser: {user}")
        print(f"Info: {info}")
        print(f"Twitter: {twitter}")
        print(f"Wallet address: {value}")
        print(f"Active networks: {chains}")

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

display_all_wallets()