"""CLI for users to manage the wallet database and run research functions"""
#TODO:
# 1) Learn operating Blockscan APIs
# 2) Program functions pulling APIs data based on users interaction
# 3) CLI function to easy add new wallets and other data to the wallets_dict.json
# - loop through each info separately
# - ask to re-add info if matches
# - ask for additional wallets for the same user
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
    new_wallet = get_inputs()

    print(tabulate(tc._save_wallet_confirm(**new_wallet)))





def remove_wallet():
    """Removes wallet from the wallet dictionary"""
    # This function needs to be developped

def get_inputs():
    """Get infor to add a new wallet"""
    ntw_i = _check_network()
    network = tc._return_network(ntw_i)
    new_wallet = {
            "username":" ",
            "twitter address":" ",
            "ENS":" ",
            "info/note":" ",
            "address": []
    }

    addresses = []

    for item, value in new_wallet.items():
        x = input(tc._prompt_new_info(item))
        new_item = check_wallet_item(ntw_i,x)
        if item == 'address':
            addresses.append(new_item)
            y = input(tc._ask_more_wallets()[0])
            while y == '1':
                new_item = input(tc._ask_more_wallets()[1])
                addresses.append(new_item)
                y = input(tc._ask_more_wallets()[0])
            new_wallet[item] = addresses
        new_wallet[item] = new_item

    new_wallet["Network"] = network

    return new_wallet

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

def check_wallet_item(ntw_i,x):
    """
    Scans through wallets to check if a new wallet is not already in the
    database
    """
    dict = get_wallets()[ntw_i]
    for key, value in dict.items():
        username = key
        wallets = value['wallets']
        info = value['info']
        twitter = value['twitter']
        ens_saved = value['ens']

        if x == username:
            new_item = _correct_item(x,'username')
        elif x in wallets.values():
            new_item = _correct_item(x,'wallet address')
        elif x == twitter:
            new_item = _correct_item(x,'twitter address')
        elif x == ens_saved:
            new_item = _correct_item(x, 'ENS')
        else:
            new_item = x

    return new_item

    # else:
    #     print(tc._display_wallet_check_result(y)[1])
    #     new_item = True
    #
    # wlt = [ntw_i, name, addr, twtr, ens, inf]
    #
    # if new_item != True:
    #     wlt[x] = new_item
    #
    # return wlt

def _correct_item(x,z):
    """Allows user to rewrite an exisitng item in the wallet"""
    a = (input(tc._display_wallet_check_result(z)[0]))

    if a == '1':
        new_item = x

    elif a == '2':
        new_item = input(tc._enter_new_info(z))
        return new_item


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