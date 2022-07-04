"""A module with all the display info for whallets-cli."""
from tabulate import tabulate


def _welcome_message():
    """welcoming message to the cli"""
    msg = \
        "\n=========================================\n"\
        "WELCOME TO WHALLETS CLI"\
        "\n========================================="
    return msg

def _main_menu():
    """Displays the CLI main menu"""
    line_0 = ("**","Chose an operation from the menu:")
    line = ("---","---------------------------------",)
    line_1 = ("1 -","Add a wallet to the your list")
    line_2 = ("2 -","Remove a wallet from your list")
    line_3 = ("3 -","Display your wallet list")
    line_4 = ("4 -","Display recent whale TXs on your EVM list")
    line_5 = ("5 -","Display recent whale TXs on your SPL list")
    line_q = ("q -","Quit!")

    table = [
        line_0,
        line,
        line_1,
        line_2,
        line_3,
        line_4,
        line_5,
        line_q
    ]
    return table

def _menu_choice():
    """Sentence asking user for the next step"""
    msg = "\nEnter number and press Enter: "
    return msg

def _missing_operation():
    """Inform about non-existing users choice"""
    msg = "Sorry, but you had either choosen an unexisting option, "\
    "or this operation has not been developped yet."
    return msg

def _ask_new_choice():
    """Message offering a new choice or quit"""
    msg = \
        "\n\n=========================================\n"\
        "Do you have another choice?\n1 - YES\n2 - NO (quit)\n"
    return msg



def _choose_network():
    """Gives a choice of networks to work with"""
    line_0 = ("**","Please chose the network for the wallet address:")
    line = ("---", "---------------------------------",)
    line_1 = ("1 -","EVM; Etherum main net and any forks (BSC, Poly..)")
    line_2 = ("2 -","SPL; Solana Program Platform")
    line_3 = ("3 -","BTC; Bitcoin")
    table = [ line_0, line, line_1, line_2, line_3]
    return table

def _prompt_address():
    """Ask or the wallet address"""
    msg = "\nEnter the wallet address:\n"
    return msg

def _prompt_twitter():
    """Ask or the wallet address"""
    msg = "\nEnter the twitter link (full address):\n"
    return msg

def _prompt_info():
    """Ask or the wallet address"""
    msg = "\nEnter short info about the user:\n"
    return msg

def _prompt_name():
    """Ask or the wallet address"""
    msg = "\nEnter user/wallet name/tag:\n"
    return msg

def _prompt_ens():
    """Ask or the wallet address"""
    msg = "\nEnter user's ENS:\n"
    return msg


def _display_wallet_check_result(y):
    """displays answer based on added data"""
    msg_0 = \
        f"{y.title()} already exists in your wallet dictionary."\
        f"\nDo you want to continue?\n1 - YES\n2 - NO (change the item)"\
        f"{_menu_choice()}"
    msg_1 = \
        f"The new wallet will be saved with already existing info:\n"
    return msg_0, msg_1

def _enter_new_info(y):
    """Asks user for a correct information"""
    msg = f"\nPlease write a correct {y}:\n\n"
    return msg
