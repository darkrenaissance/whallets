# getting info from Etherscan API

Resources: 
- https://github.com/pcko1/etherscan-python/blob/master/README.md
- https://www.youtube.com/watch?v=pIOg-f0GBBk
- https://rattibha.com/thread/1512983745988419588, 


- register a free account on etherscan
- install etherscan-python with: pip install etherscan-python
- https://github.com/pcko1/etherscan-python/blob/master/README.md

The github gives info on how to access the data in categories:
- accounts:(examples)
get_normal_txs_by_address(address, startblock, endblock, sort)
eth.get_erc20_token_transfer_events_by_address(address, startblock, endblock, sort)

You will get these columns from normal txs:
['blockHash', 'blockNumber', 'confirmations', 'contractAddress', 'cumulativeGasUsed', 'from', 'gas', 'gasPrice', 'gasUsed', 'hash', 'input', 'isError', 'nonce', 'timeStamp', 'to', 'transactionIndex', 'txreceipt_status', 'value']

- On the github there are example of responses returned.

- contacts
- transactions
- blocks
- GETH/Parity Proxy
- Tokens
- Gas tracker
- Stats
- Pro (PRO API key needed) for:
	- get_hist_eth_balance_for_address_by_block_no
	- get_daily_average_block_size
    	- get_daily_block_count_and_rewards
    	- get_daily_block_rewards
    	- get_daily_average_block_time
    	- get_daily_uncle_block_count_and_rewards
    	- get_hist_erc20_token_total_supply_by_contract_address_and_block_no
    	- get_hist_erc20_token_account_balance_for_token_contract_address_by_block_no
    	- get_token_info_by_contract_address
    	- get_daily_average_gas_limit
    	- get_eth_daily_total_gas_used
    	- get_eth_daily_average_gas_price
    	- get_eth_daily_network_tx_fee
    	- get_daily_new_address_count
    	- get_daily_network_utilization
    	- get_daily_average_network_hash_rate
    	- get_daily_tx_count
    	- get_daily_average_network_difficulty
    	- get_eth_hist_daily_market_cap
    	- get_eth_hist_price


Other resources than Etherscan:
- Coingecko --> we can create an api and request info
- Infura: https://infura.io/ --> they have free tier with up to 100 k requests/day
To use Infura with python, this is an example of code to use in python:

from web3 import Web3

w3 = Web3(Web3.HTTPProvider(projectID))
receipt=w3.eth.get_transaction_receipt(trHash)

-- Once you get the receipt, you need to get the DEX smart contract ABI --
-- ABI basically tells you how does which function look like when you see it in logs --

