"""CLI for users to manage the wallet database and run research functions"""
#TODO:
# 1) Learn operating Blockscan APIs
# 2) Program functions pulling APIs data based on users interaction
# 3) CLI function to easy add new wallets and other data to the wallets_dict.json
# DONE - loop through each info separately
# DONE - ask to re-add info if matches
# DONE - ask for additional wallets for the same user
# DONE - add and print all the added wallets
# DONE - csv export (get away the line row)
# - Network choice on expoer csv option
# 4) Prints options for the user (-h)
# 5) Remove wallet option
# 6) Edit wallet option

import json
from tabulate import tabulate
import texts_cli as tc
import csv


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
    elif choice == '6':
        csv_export()
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
    new_wallet, addresses, ntw_i = get_inputs()
    print(tabulate(tc._save_wallet_confirm(addresses, new_wallet)))
    confirm_entry(ntw_i, addresses, new_wallet)


def confirm_entry(ntw_i, addresses, new_wallet):
    """Preview the new wallet and confirm saving it"""
    x = input(tc._confirm_entry()[0])
    if x == '1':
        print(tc._confirm_entry()[1])
        new_wallet_dictionary = refactor_wallet(addresses, new_wallet)
        save_wallet(ntw_i, new_wallet_dictionary)

        refactor_wallet(addresses, new_wallet)

    x = input(tc._confirm_entry()[2])
    if x == '1':
        add_wallet()


def save_wallet(ntw_i, new_wallet_dictionary):
    """Saves the wallet into the database/dictionary and informs the user"""
    filename = 'wallets_dict.json'

    with open(filename) as f:
        all_wallets = json.load(f)


    dict_0 = all_wallets['evm_wallets']
    dict_1 = all_wallets['spl_wallets']
    dicts = [dict_0,dict_1]
    dict = dicts[ntw_i]

    dict.update(new_wallet_dictionary)
    with open(filename, 'w') as f:
        json.dump(all_wallets,f, indent=4)


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
                # need to add a code how to add networks automatically
                ]
            }
        }
        new_wallet_dictionary[username]["wallets"].update(wallet)

    return new_wallet_dictionary


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

    for key, value in new_wallet.items():
        x = input(tc._prompt_new_info(key))
        new_item = check_wallet_item(ntw_i, x, key)

        if key == 'address':
            addresses.append(new_item)
            y = input(tc._ask_more_wallets()[0])
            while y == '1':
                new_item = input(tc._ask_more_wallets()[1])
                addresses.append(new_item)
                y = input(tc._ask_more_wallets()[0])
        new_wallet[key] = new_item

    new_wallet["Network"] = network

    return new_wallet, addresses, ntw_i


def check_wallet_item(ntw_i,x,key,):
    """
    Scans through wallets to check if a new wallet is not already in the
    database
    """
    dict = get_wallets()[ntw_i]

    if x == "" or x == " ":
        new_item = x
    else:
        for a,b in dict.items():

            if x == a or x == b:
                # print("\n\na or b\n\n")
                new_item = _correct_item(x, key)

            for v in b.values():
                if x == v:
                    # print("\n\nv\n\n")
                    new_item = _correct_item(x, key)
                    return new_item
                else:
                    new_item = x

    return new_item


def _correct_item(x,key):
    """Allows user to rewrite an exisitng item in the wallet"""
    choice = input(tc._display_wallet_check_result(key)[0])

    if choice == '1':
        new_item = x

    elif choice == '2':
        new_item = input(tc._enter_new_info(key))

    return new_item


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


def get_wallets():
    """ Gets the info from the dictionary """
    filename = 'wallets_dict.json'
    with open(filename) as f:
        all_wallets = json.load(f)
    evm_wallets = all_wallets['evm_wallets']
    spl_wallets = all_wallets['spl_wallets']

    return evm_wallets, spl_wallets,


def table_format_wallets(chain):
    """Format wallets to table"""
    # Chains available 'evm','spl'
    # evm shows all the forks
    i = _chain_index(chain)
    dict = get_wallets()[i]
    print(f"\n\n{chain.upper()} WALLETS:")

    line_0, line_ = tc._table_headers()
    table = [line_0, line_,]

    for i, (key, value) in enumerate(dict.items()):
        index = i + 1
        user = key
        info = value['info']
        twitter = value['twitter']
        ens = value['ens']
        wallets = {}
        wlts = value['wallets']

        for x, y in wlts.items():
            wallets[x] = y

        line = [index, user, ens, twitter, info]

        x = 1
        for wlt,inf in wallets.items():
            address = inf['address']
            networks = inf['networks']
            networks_str = ', '.join(networks)
            if x == 1:
                line.append(address)
                line.append(networks_str)
                x += 1
            else:
                line = [' ',' ',' ',' ',' ',address,networks_str]
                x += 1
            table.append(line)

    return table


def csv_export():
    """Exports the wallets to csv files"""
    # Need to add SPL & BTC wallet option when relevant
    table = table_format_wallets('evm')
    del table[1]
    file = 'data/whallets.csv'
    with open(file, 'w') as output:
        new_writer = csv.writer(output)
        for row in table:
            new_writer.writerow(row)
    print(tc._csv_exported())


def _chain_index(chain):
    """Asigns an index based on given parameter of the chain"""
    if chain.lower() == 'evm':
        i = 0
    elif chain.lower() == 'spl':
        i = 1
    return i


def display_wallets(chain):
    """Displays the wallets according the given chain"""
    table = table_format_wallets(chain)
    print(tabulate(table))


def display_all_wallets():
    display_wallets('evm')
    display_wallets('spl')


# Run the program
if __name__ == '__main__':
    print(tc._welcome_message())
    cli_main()