# List of Interesting Wallets to Follow

## Introduction

Compiling a list (dictionary) of wallets and an automatized tool to follow monitor them, can generate solid Alpha.

Feedback and cooperation/guidance is welcome.

## Programs

There are few programs to store and develope functions for wallet scannign.
* wallets.py - has function to display wallets in a quick overview, based on parameters for the given chain.
  * TODO: 
    * function to quickly insert a wallet into the dictionary json file
    * function to display wallets in a table form
* spl_scv_search.py - contains function to get transactions within a chosen price range
  * TODO:
    * cli program to interact with solscan API to download the data directly
* evm_scn.py - planned program to interact with etherscan and all the EVM forks APIs, monitoring, downloading and displaying the data according given parameters.

## Dictionaries

The wallet dictionary is used to store all the information according to this template:

**Template**

This is a simple template to make a database dictionary. Fill all \<*strings*\> with real data.

```python
#defi wallets:
{
	'@<name>':{
		'twitter':'<full_twitter_address>',
		'note':'<key info about the wallet owner>',  
		'ens':'<name.eth>',
		'wallets':{
			'erc':'<eth_wallet_address>',
			'<any_other_chain>':'<corresponding_address>'
	
		},
	},
}
```


### Unified syntax

To be able to automatize the data research later, particularly the on chain movement, some arbitrary variables must follow the same syntax expression.
Different whales have wallets on different chains, and to be able to pull form the scans, the chain keys for particular wallets must be noted, and unified across the whales.

**Use these ticks for different chains**


| **Syntax** | **Chain**            | **Explorer**                      |
| ------------ | ---------------------- | --------------------------------- |
| 'btc'      | Bitcoin              |                                   |
| 'erc'      | Erc 20 (Etherum)     | [Etherscan](https://etherscan.io) |
| 'ens'      | Etherum Name service |                                   |
| 'bsc'      | Binance Smart Chain  |                                   |
| 'spl'      | Solana               |   [Solscan](https://solscan.io)    |
| 'poly'     | Polygon (Matic)      |                                   |
| 'heco'     | Huobi                |                                   |
| 'ftm'      | Fantom               |                                   |
| 'avax'     | Avalanche            |                                   |
| 'arb'      | Arbitrum             |                                   |
| 'optm'     | Optimism             |                                   |
| 'gns'      | Gnosis               |                                   |
| 'aur'      | Aurora               |                                   |


