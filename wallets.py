"""Functions automatizing the monitoring of whale wallets"""

#TODO:
# 1) A program automatizing the dictionary compiling with a given wallet or ens
# Using blockscan etc
# 2) A program scanning through the given block explorers and scraping useful
# data about the wallet actions based on the given parameters of time, amount etc
# 3) A program exporting the data from #2 into a spread sheet and plotting graph

import json



def display_wallets(chain):
    """Displays the wallets according the given chain"""
    # Chains available 'evm','spl'
    # evm shows all the forks
    i = _chain_index(chain)
    dict = _get_wallets()[i]
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

def _get_wallets():
    ''' Gets the info from the dictionary '''
    filename = 'wallets_dict.json'
    with open(filename) as f:
        all_wallets = json.load(f)
    evm_wallets = all_wallets['evm_wallets']
    spl_wallets = all_wallets['spl_wallets']
    return evm_wallets, spl_wallets

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