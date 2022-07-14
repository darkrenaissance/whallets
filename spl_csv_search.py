# Program to search through Solscan
# TODO:
# 1) Program donwloading history of solscan into csv according given parameters
# 2) Program exploring the alle, txhash, amont, time etc
# 3) API remote controllng program

import csv
from datetime import datetime
from tabulate import tabulate

def get_info():
    """Functiong extractiong info from the downloaded csv file"""
    filename = 'data/export_transfer_undefined_1654954858887.csv'
    with open(filename) as f:
        reader = csv.reader(f)
        header_row = next(reader)
        # This passes the next line (1st = header)

        # for index, column_header in enumerate(header_row):
        #     print(index, column_header)

        times, txhashes, amounts, source_owners, dest_owners = [], [], [], [], [],


        for row in reader:
            time_index = header_row.index('BlockTime')
            txhash_index = header_row.index('TxHash')
            amount_index = header_row.index('Amount')
            source_own_index = header_row.index('Source Owner Account')
            dest_own_index = header_row.index('Dest Owner Account')

            try:
                txhash = str(row[txhash_index])
                amount = float(row[amount_index])
                src_own = str(row[source_own_index])
                dst_own = str(row[dest_own_index])
                date_time = f"{row[time_index]}"
                # hover_date_time = \
                #     datetime.strptime(date_time, '%Y-%m-%d, %H%M')

            except IndexError:
                print(f"Missing data")

            else:
                times.append(date_time)
                txhashes.append(txhash)
                amounts.append(amount)
                source_owners.append(src_own)
                dest_owners.append(dst_own)

        return times, txhashes, amounts, source_owners, dest_owners




def display_csv_txs_usdt(min=100000,max=10000000):
    """Prints all tx's within the range of entered amount"""


    headers = _headers_txs_usdt(min,max)

    times, txhashes, amounts, source_owners, dest_owners = get_info()

    table = [
        headers[0],
        headers[1],
        headers[2]
    ]


    for index,amount in enumerate(amounts):
        usdt = amount/1000000
        i = index
        txhash = txhashes[i]
        src_own = source_owners[i]
        dst_own = dest_owners[i]
        time = times[i]
        if usdt > min and usdt < max:
            item =(f"{time} - ",
                   f"{txhash} - ",
                   f"{src_own} - ",
                   f"{dst_own} - ",
                   f"{usdt}"
            )
            table.append(item)

    print(tabulate(table))

def _headers_txs_usdt(min,max):
    """Support function to print the header for tx's in usdt"""
    header_0 = (f"\nTRANSACTIONS BETWEEN {min} and {max} USDT",)
    header_1 = ("=======================================",)
    header_2 = (
        "TIME",
        "TXHASH",
        "SOURCE OWNER",
        "DESTINATION OWNER",
        "AMOUNT (USDT)"
    )
    headers = [header_0,header_1,header_2]
    return headers


display_csv_txs_usdt(5000,5550)