"""
    should calculate 
    1. total number of transactions
    2. avg value of transactions
    3. avg fee of transactions
    4. avg size of transcations
    
    function input is block hash value
"""
#import given API
from blockchain import blockexplorer

#To make floating point as depicted in the chart
#Originally it returns int value 281XXX for example
#but Charted data represents 2.81XXX with 8 digits under the point
btcDigit = 100000000
#compensation BTC for transactions
compBTC = 125000000

def tot_tx(block_hash):
    block = blockexplorer.get_block(block_hash)
    return block.n_tx

#total produced BTC-> values by transactions, divided by total transactions
def avg_tx_val(block_hash):
    block = blockexplorer.get_block(block_hash)
    tot_val = 0
    for transaction in range(block.n_tx):
        n_input = len(block.transactions[transaction].inputs)
        n_output = len(block.transactions[transaction].outputs)
        for i in range(n_input):
            tot_val += block.transactions[transaction].inputs[i].value
        for j in range(n_output):
            tot_val += block.transactions[transaction].outputs[j].value
    return (tot_val/block.n_tx)/btcDigit

#total fee divided by total transactions(tot_tx)
def avg_tx_fee(block_hash):
    block = blockexplorer.get_block(block_hash)
    fee = (block.fee/block.n_tx)/btcDigit
    return fee

def avg_tx_size(block_hash):
    block = blockexplorer.get_block(block_hash)
    tot_size = 0
    for i in range(block.n_tx):
        tot_size += block.transactions[i].size
    return (tot_size/block.n_tx)

