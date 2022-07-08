# getting info from Etherscan API using etherscan-python or Etherscan api

## Resources: 

- https://github.com/pcko1/etherscan-python/blob/master/README.md
- https://www.youtube.com/watch?v=pIOg-f0GBBk
- https://rattibha.com/thread/1512983745988419588,
- See example of result of requests: https://github.com/pcko1/etherscan-python/tree/master/logs/standard 
- https://api.etherscan.io/apis (for .json)

## Free account on Etherscan

- register a free account on etherscan
- install etherscan-python with: pip install etherscan-python
- https://github.com/pcko1/etherscan-python/blob/master/README.md

## How to get the information
The github gives info on how to access the data in categories:
- accounts:(examples)
get_normal_txs_by_address(address, startblock, endblock, sort)
eth.get_erc20_token_transfer_events_by_address(address, startblock, endblock, sort)

You will get these columns from normal txs:
['blockHash', 'blockNumber', 'confirmations', 'contractAddress', 'cumulativeGasUsed', 'from', 'gas', 'gasPrice', 'gasUsed', 'hash', 'input', 'isError', 'nonce', 'timeStamp', 'to', 'transactionIndex', 'txreceipt_status', 'value']

### Balances from multiple addresses

https://api.etherscan.io/api?module=account&action=balancemulti&address=0xddbd2b932c763ba5b1b7ae3b362eac3e8d40121a,0x63a9975ba31b0b9626b34300f7f627147df1f526,0x198ef1ec325a96cc354c7266a038be8b5c558f67&tag=latest&apikey=YourApiKeyToken

## Get a list of "ERC20 - Token Transfer Events" by Address

https://api.etherscan.io/api?module=account&action=tokentx&address=0x4e83362442b8d1bec281594cea3050c8eb01311c&startblock=0&endblock=999999999&sort=asc&apikey=YourApiKeyToken

## Get Block Number by Timestamp

https://api.etherscan.io/api?module=block&action=getblocknobytime&timestamp=1578638524&closest=before&apikey=YourApiKeyToken

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

## On the question on decimals

- https://ethereum.stackexchange.com/questions/19673/decimals-on-erc20-tokens#19703


## Other resources than Etherscan:

- Coingecko --> we can create an api and request info
- Infura: https://infura.io/ --> they have free tier with up to 100 k requests/day
To use Infura with python, this is an example of code to use in python:

from web3 import Web3

w3 = Web3(Web3.HTTPProvider(projectID))
receipt=w3.eth.get_transaction_receipt(trHash)

-- Once you get the receipt, you need to get the DEX smart contract ABI --
-- ABI basically tells you how does which function look like when you see it in logs --

