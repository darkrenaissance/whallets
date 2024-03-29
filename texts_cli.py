"""A module with all the display info for whallets-cli."""

def _welcome_message():
    """welcoming message to the cli"""
    msg = \
        "\n=========================================\n"\
        "WELCOME TO WHALLETS CLI"\
        "\n========================================="
    return msg


def _main_menu():
    """Displays the CLI main menu"""
    line_0 = ("**","MAIN MENU:")
    line = ("---","------------------------")
    line_1 = ("1 -","Add a wallet")
    # line_2 = ("2 -","Remove a wallet")
    line_3 = ("2 -","Display wallet database")
    line_4 = ("3 -","Display whale TXs on your EVM list (option not active yet)")
    # line_5 = ("5 -","Display whale TXs on your SPL list")
    line_6 = ("4 -","Export wallet database to csv")
    line_q = ("Q -","Quit!")

    table = [
        line_0,
        line,
        line_1,
        #line_2,
        line_3,
        line_4,
        line_6,
        line_q
    ]
    return table


def _menu_choice():
    """Sentence asking user for the next step"""
    msg = "\nEnter number and press Enter: "
    return msg


def _missing_operation():
    """Inform about non-existing users choice"""
    msg = "\nSorry, but you had either choosen an unexisting option, "\
    "or this operation has not been developped yet."
    return msg


def _ask_new_choice():
    """Message offering a new choice or quit"""
    msg = \
        "\n\n=========================================\n"\
        "Do you have another choice?\n1 - YES\n2 - NO (quit)\n"
    return msg

# Commentig out, simplified to ETH only
# def _choose_network():
#     """Gives a choice of networks to work with"""
#     line_0 = ("**","Please chose the network for the wallet address:")
#     line = ("---", "---------------------------------",)
#     line_1 = ("1 -","EVM; Etherum main net and any forks (BSC, Poly..)")
#     line_2 = ("2 -","SPL; Solana Program Platform")
#     line_3 = ("3 -","BTC; Bitcoin")
#     table = [ line_0, line, line_1, line_2, line_3]
#     return table


def _prompt_new_info(item):
    """Ask or the wallet address"""
    msg = f"\nEnter the wallet {item}:\n(if unknown press Enter)\n"
    return msg


def _ask_more_wallets():
    """ask user if an account has more wallet addresses"""
    msg_0 = \
        "\nDo you want to add another address to this username?" \
        "\n1 - YES (add more wallets)\n2 - NO (continue)\n"
    msg_1 = "\nEnter another wallet address:\n"

    return msg_0, msg_1


def _display_wallet_check_result(key):
    """displays answer based on added data"""
    msg_0 = \
        f"\nThis {key} already exists in your wallet dictionary."\
        f"\nDo you want to continue?\n1 - YES (keep it duplicate)"\
        f"\n2 - NO (change the item)"\
        f"{_menu_choice()}"

    msg_1 = \
        f"This is your the wallet info:\n(Press Enter to save, 'q' to cancell)"
    return (msg_0, msg_1)


def _enter_new_info(key):
    """Asks user for a correct information"""
    msg = f"\nPlease write a correct {key}:\n\n"
    return msg

def _save_wallet_confirm(addresses, new_wallet):
    """print wallet and ask user if to save it"""
    network = new_wallet["Network"]
    username = new_wallet["username"]
    twtr = new_wallet["twitter address"]
    ens = new_wallet["ENS"]
    info = new_wallet["info/note"]
    # addr = list(addresses)

    line_0 = ("****","Wallet to be saved:")
    line = ("-----","--------------------")
    line_1 = (f"Network:",f"{network}")
    line_2 = (f"Name:",f"{username}")
    line_3 = (f"Twitter:",f"{twtr}")
    line_4 = (f"ENS:",f"{ens}")
    line_5 = (f"Info:", f"{info}")


    table = [
        line_0,
        line,
        line_1,
        line_2,
        line_3,
        line_4,
        line_5,
        ]

    for i, address in enumerate(addresses):
        line = (f"Address_{i}:", f"{address}")
        table.append(line)
    return table

def _confirm_entry():
    """Asks user to confirm the wallet saving or repeat"""
    msg_0 = \
        "\nDo you want to save the wallet to the database?"\
        "\n1 - YES\n2 - NO\n"
    msg_1 = "\nThe wallet was saved to your database."
    msg_2 = \
        "\nDo you want to add another wallet?"\
        "\n1 - YES\n2 - NO\n"

    return msg_0, msg_1, msg_2


def _table_headers():
    """Text template for table of wallet display function"""
    line_0 = [
        "#", "USER", "ENS", "TWITTER", "INFO", "ADDRESSES", "NETWORKS"]
    line_ = ["==", "=========", "===========", "===========",
             "===========", "===========", "==========="]
    return line_0, line_

def _csv_exported():
    """displays information about csv stored"""
    msg = "\nThe wallet database was exported to ~/whallets/data/whallets.csv."
    return msg

def _return_network(ntw_i):
    """Return network based on index"""
    if ntw_i == 0:
        ntw = "EVM; ETH and forks (BSC, Poly..)"
    elif ntw_i == 1:
        ntw = "Solana Program Library"
    elif ntw_i == 2:
        ntw = "Bitcoin"
    else:
        ntw = None

    return ntw
