"""CLI for users to manage the wallet database and run research functions"""
#TODO:
# 1) Learn operating Blockscan APIs
# 2) Program functions pulling APIs data based on users interaction
# 3) CLI function to easy add new wallets and other data to the wallets_dict.json
# - loop through each info separately
# - ask to re-add info if matches
# - ask for additional wallets for the same user
# - add and print all the added wallets
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
    new_wallet, addresses = get_inputs()

    print(tabulate(tc._save_wallet_confirm(addresses, new_wallet)))
    confirm_entry(addresses, new_wallet)


def confirm_entry(addresses, new_wallet):
    """Preview the new wallet and confirm saving it"""
    x = input(tc._confirm_entry()[0])
    if x == '1':
        # new_wallet_dict = refactor_wallet(addresses, **new_wallet)
        # save_wallet(**new_wallet_dict)
        print(tc._confirm_entry()[1])

        refactor_wallet(addresses, new_wallet)

    x = input(tc._confirm_entry()[2])
    if x == '1':
        add_wallet()




def save_wallet(**new_wallet_dict):
    """Saves the wallet into the database/dictionary and informs the user"""

def refactor_wallet(addresses, new_wallet):
    """Refactor the wallet items to the wallet_dict format"""
    username = new_wallet["username"]
    twtr = new_wallet["twitter address"]
    ens = new_wallet["ENS"]
    info = new_wallet["info/note"]

    new_wallet_dictionary = {username: {
        "twitter": twtr,
        "info": info,
        "ens":ens,
        "wallets": {}
            }
        }

    for idx, addr in enumerate(addresses):
        wallet = {f"wallet_{idx}":{
            "address":f"{addr}",
            "networks":[
                "erc"
                # need to add a code how to add networks
                ]
            }
        }
        new_wallet_dictionary[username]["wallets"].append(wallet)

    print(f"\n\n\n{new_wallet_dictionary}")




    # This is the result aiming for:
    # {
    #     "evm_wallets": {
    #         "@vitalik.eth": {
    #             "twitter": "https://twitter.com/VitalikButerin",
    #             "info": "ETH foundation, influencer, researcher, cult",
    #             "ens": "vitalik.eth",
    #             "wallets": {
    #                 "wallet_0": {
    #                     "address": "0xd8da6bf26964af9d7eed9e03e53415d37aa96045",
    #                     "networks": [
    #                         "erc",
    #                         "bsc",
    #                         "poly",
    #                         "heco",
    #                         "ftm",
    #                         "avax",
    #                         "optm",
    #                         "arb"
    #                     ]
    #                 },






def remove_wallet():
    """Removes wallet from the wallet dictionary"""
    # This function needs to be developed

def get_inputs():
    """Get infor to add a new wallet"""
    ntw_i = _check_network()
    network = tc._return_network(ntw_i)
    addresses = []
    new_wallet = {
            "username":" ",
            "twitter address":" ",
            "ENS":" ",
            "info/note":" ",
            "address": addresses
    }

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
        new_wallet[item] = new_item

    new_wallet["Network"] = network

    return new_wallet, addresses

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

def _correct_item(x,z):
    """Allows user to rewrite an exisitng item in the wallet"""
    a = '2'
    while a == '2':
        a = (input(tc._display_wallet_check_result(z)[0]))

        if a == '1':
            new_item = x

        elif a == '2':
            new_item = input(tc._enter_new_info(z))
            if new_item == x:
                a = '2'
            else:
                new_item = x
        break
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