# List of Interesting Wallets to Follow

## Introduction

Compiling a list (dictionary) of wallets and an automatized tool to follow monitor them, can generate solid Alpha.

Feedback and cooperation/guidance is welcome.

## Installation

## Programs

* **whallets_cli.py** - the main CLI to interact with the wallet database
* spl_scv_search.py - contains function to get transactions within a chosen price range
 

## Dictionaries

The wallet dictionary is used to store all the information according to this template:

**Template**

This is a simple template to make a database dictionary. Fill all \<*strings*\> with real data.

```python

{
        "<template_name_wallet>": {
            "twitter": "<https://twitter.com/full_address>",
            "info": "<info>",
            "ens": "<...> ",
            "wallets": {
                "wallet_0": {
                    "address": "<paste 0x... address>",
                    "networks": [
                        "erc",
                        "<paste all the networks separated by a comma>"

                    ]
                },
                "<wallet_1: in case another wallet of the same user>": {
                    "address": "<0x...>",
                    "networks": [
                        "<...>",
                        "<...>"
                    ]
                },
                "<wallet_2: in case of another wallet of the same user>": {
                    "address": "<0x...>",
                    "networks": [
                        "<..>"
                    ]
                }
            }
        }
}

```


### Unified syntax

To be able to automatize the data research later, particularly the on chain movement, some arbitrary variables must follow the same syntax expression.
Different whales have wallets on different chains, and to be able to pull form the scans, the chain keys for particular wallets must be noted, and unified across the whales.

**Use these ticks for different chains**


| **Syntax** | **Chain**            | **Explorer**                      |
|------------|----------------------| --------------------------------- |
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
| 'one'      | Harmony              |                                   |
| 'fuse'     | Fuse                 |                                   |


