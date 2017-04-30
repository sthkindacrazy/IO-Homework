"""
    should calculate 
    1. total number of transactions
    2. avg value of transactions
    3. avg fee of transactions
    4. avg size of transcations
    
    function input is block hash value
"""
#import given API
import blockexplorer
import re

#To make floating point as depicted in the chart
#Originally it returns int value 281XXX for example
#but Charted data represents 2.81XXX with 8 digits under the point
btcDigit = 100000000
#compensation BTC for transactions
compBTC = 125000000

def tot_tx(block):
    return block.n_tx

#total produced BTC-> values by transactions, divided by total transactions
def avg_tx_val(block):
    tot_val = 0
    for transaction in range(block.n_tx):
        n_output = len(block.transactions[transaction].outputs)
        for j in range(n_output):
            tot_val += block.transactions[transaction].outputs[j].value
    return (tot_val/block.n_tx)/btcDigit

#total fee divided by total transactions(tot_tx)
def avg_tx_fee(block):
    fee = (block.fee/block.n_tx)/btcDigit
    return fee

def avg_tx_size(block):
    tot_size = 0
    for i in range(block.n_tx):
        tot_size += block.transactions[i].size
    return (tot_size/block.n_tx)

def print_tx_parameters(block_hash):
    block = blockexplorer.get_block(block_hash)
    print("Total number of transactions : " + str(tot_tx(block)))
    print("Average value of transactions : " + str(avg_tx_val(block)))
    print("Average fee of transactions : " + str(avg_tx_fee(block)))
    print("Average size of transactions : " + str(avg_tx_size(block)))
    
#problem 2
#Here function input is hash_order which is block_hash (input/output) connected with space
#e.g [hash_value] input or [hash_value] output

def input_print(block_hash):
    block = blockexplorer.get_block(block_hash)
    for transaction in range(1,block.n_tx):
        n_input = len(block.transactions[transaction].inputs)
        for i in range(n_input):
            input_val_list = [block.transactions[transaction].inputs[i].n, 
                              block.transactions[transaction].inputs[i].value,
                              block.transactions[transaction].inputs[i].tx_index,
                              block.transactions[transaction].inputs[i].script ]
            print(input_val_list)

def output_print(block_hash):
    block = blockexplorer.get_block(block_hash)
    for transaction in range(1,block.n_tx):
        n_output = len(block.transactions[transaction].outputs)
        for j in range(n_output):
            output_val_list = [block.transactions[transaction].outputs[j].n,
                               block.transactions[transaction].outputs[j].value,
                               block.transactions[transaction].outputs[j].tx_index,
                               block.transactions[transaction].outputs[j].script ]
            print(output_val_list)

def in_out_valPrint(hash_order):
    args = hash_order.split()
    pattern = re.compile("[A-Za-z0-9]+")
    block_hash = pattern.search(args[0]).group()
    order = args[1]
    if (order == "input"):
        input_print(block_hash)
    else:
        output_print(block_hash)
