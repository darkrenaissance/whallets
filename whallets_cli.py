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

print(tc._welcome_message())

def cli_main():
    """Main program for the cli"""


    print(tabulate(tc._main_menu()))
    main_menu_choice()

def main_menu_choice():
    """main cli operations choice"""
    choice = input(tc._menu_choice())
    if choice == '1':
        add_wallet()

    elif choice == '2':
        print(tc._missing_operation())
        _new_choice()
    elif choice == '3':
        display_all_wallets()
    elif choice == '4':
        print(tc._missing_operation())
        _new_choice()
    elif choice == '5':
        print(tc._missing_operation())
        _new_choice()
    elif choice.lower() == "q":
        quit()
    else:
        _new_choice()

    _new_choice()

def _new_choice():
    """Offer user a new choice"""

    x = 1
    while x < 3:
        chc = input(tc._ask_new_choice())
        if chc == '1':
            cli_main()
        elif chc == '2':
            quit()
        else:
            x += 1
    else:
        quit()

def add_wallet():
    """A function to add wallet to the wallets_dict.json"""
    ntw_i, name, addr, inf, twtr, ens = _get_inputs()
    wlt = check_wallet(ntw_i, name, addr, twtr, ens)
    print(wlt)





def _correct_item(y):
    """Allows user to rewrite an exisitng item in the wallet"""
    z = (input(tc._display_wallet_check_result(y)[0]))
    if z =='1':
        print(tc._display_wallet_check_result(y)[1])
        return True

    elif z == '2':
        new_item = input(tc._enter_new_info(y))
        return new_item

def remove_wallet():
    """Removes wallet from the wallet dictionary"""
    # This function needs to be developped

def _get_inputs():
    """Get infor to add a new wallet"""
    ntw_i = _check_network()
    name = input(tc._prompt_name())
    addr = input(tc._prompt_address())
    inf = input(tc._prompt_info())
    twtr = input(tc._prompt_twitter())
    ens = input(tc._prompt_ens())
    return ntw_i, name, addr, inf, twtr, ens

def _check_network():
    """Check if the existing network"""
    print(tabulate(tc._choose_network()))
    ntw = int(input(tc._menu_choice()))
    i = ntw - 1
    if i != 0:
        print(tc._missing_operation())
        _new_choice()
    else:
        return i

def check_wallet(ntw_i,name, addr, twtr, ens):
    """
    Scans through wallets to check if a new wallet is not already in the
    database
    """
    i = ntw_i

    dict = get_wallets()[i]
    for key, value in dict.items():
        user = key
        wallets = value['wallets']
        info = value['info']
        twitter = value['twitter']
        ens_saved = value['ens']
        if user == name:
            x = [1,'name']
        elif addr in wallets.values():
            x = [2, 'address']
        elif twtr == twitter:
            x = [3, 'twitter']
        elif ens == ens_saved:
            x = [4, 'ENS']
        else:
            x = [5,]

    x = x[0]
    y = x[1]

    if x != 5:
        new_item = _correct_item(y)
    else:
        print(tc._display_wallet_check_result(y)[1])
        new_item = True

    wlt = [ntw_i, name, addr, twtr, ens]

    if new_item != True:
        wlt[x] = new_item

    return wlt



def get_wallets():
    """ Gets the info from the dictionary """
    filename = 'wallets_dict.json'
    with open(filename) as f:
        all_wallets = json.load(f)
    evm_wallets = all_wallets['evm_wallets']
    spl_wallets = all_wallets['spl_wallets']

    return evm_wallets, spl_wallets,


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


# Run the program
cli_main()