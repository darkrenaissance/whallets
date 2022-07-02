"""A module with all the display info for whallets-cli."""
from tabulate import tabulate

import whallets_cli as cli

def welcome_message():
    """welcoming message to the cli"""
    msg = \
        "WELCOME TO WHALLETS CLI"\
        "\n ========================================= \n"
    return msg

def _main_menu():
    """Displays the CLI main menu"""
    line_0 = ("**","Enter a number from the menu:")
    line = ("---","------------------------------",)
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


def _choose_chain():
    msg = \
        "\nPlease chose the network for the wallet address:"\
        "\n1 - EVM; Etherum main net and any forks (BSC, Poly..)"\
        "\n2 - SPL; Solana Program Platform"\
        "\n3 - BTC; Bitcoin"
    return msg

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

def _check_wallet_result(chain, name, addr, twtr, ens):
    """Messages informing about existing wallet"""
    ix = cli.check_wallet(chain, name, addr, twtr, ens)
    if ix < 4:
        items = ['name','address','twitter','ens']
        item = items[ix]
        msg = f"This {item} is already saved in the databse."
    else:
        msg = "New wallet was saved."
    return msg
