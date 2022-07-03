"""CLI for users to manage the wallet database and run research functions"""
#TODO:
# 1) Learn operating Blockscan APIs
# 2) Program functions pulling APIs data based on users interaction
# 3) CLI function to easy add new wallets and other data to the wallets_dict.json
# - loop through each info separately
# - ask to re-add info if matches
# 4) Prints options for the user (-h)

import json
from tabulate import tabulate

import texts_cli as tc

print(tc.welcome_message())

def cli_main():
    """Main program for the cli"""

    while True:
        print(tabulate(tc._main_menu()))
        main_menu_choice()

def main_menu_choice():
    """main cli operations choice"""
    choice = input(tc._main_menu())
    if choice == 1:
        add_wallet()
    elif choice == 2:
        remove_wallet()
    elif choice == 3:
        display_all_wallets()
    elif choice == 4:
        print(tc._missing_operation())
        _new_choice()
    elif choice == 5:
        print(tc._missing_operation())
        _new_choice()
    elif choice.lower() == "q":
        quit()
    else:
        _new_choice()

def _new_choice():
    """Offer user a new choice"""

    x = 1
    if x < 3:
        choice = input(tc._ask_new_choice())
        if choice == 1:
            cli_main()
        elif choice == 2:
            quit()
        else:
            x += 1
    else:
        quit()

def add_wallet():
    """A function to add wallet to the wallets_dict.json"""
    chain, name, addr, inf, twtr, ens = _get_inputs()
    msg = tc._check_wallet_result(chain, name, addr, twtr, ens)
    print(msg)

def remove_wallet():
    """Removes wallet from the wallet dictionary"""
    # This function needs to be developped

def _get_inputs():
    """Get infor to add a new wallet"""
    chain = int(input(tc._choose_chain()))
    name = input(tc._prompt_name())
    addr = input(tc._prompt_address())
    inf = input(tc._prompt_info())
    twtr = input(tc._prompt_twitter())
    ens = input(tc._prompt_ens())
    return chain, name, addr, inf, twtr, ens


def check_wallet(chain, name, addr, twtr, ens):
    """
    Scans through wallets to check if a new wallet is not already in the
    database
    """

    i = chain - 1
    dict = get_wallets()[i]
    for key, value in dict.items():
        user = key
        wallets = value['wallets']
        info = value['info']
        twitter = value['twitter']
        ens_saved = value['ens']
        if user == name:
            return 0
        elif addr in wallets.values():
            return 1
        elif twtr == twitter:
            return 2
        elif ens == ens_saved:
            return 3
        else:
            return 4



def get_wallets():
    """ Gets the info from the dictionary """
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
        info = value['info']
        twitter = value['twitter']
        wallets = {}
        wlts = value['wallets']
        for x, y in wlts.items():
            wallets[x] = y


        print(f"\nUser: {user}")
        print(f"Info: {info}")
        print(f"Twitter: {twitter}")
        for wlt,inf in wallets.items():
            print(f"Wallets: {wlt}")
            print(f"Address: {inf['address']}")
            print(f"Active networks:")
            networks = inf['networks']
            networks_str = ', '.join(networks)
            print(networks_str)

def _chain_index(chain):
    """Asigns an index based on given parameter of the chain"""
    if chain.lower() == 'evm':
        i = 0
    elif chain.lower() == 'spl':
        i = 1
    return i

def display_all_wallets():
    display_wallets('evm')
    display_wallets('spl')

