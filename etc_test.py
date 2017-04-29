from blockchain import blockexplorer

block = blockexplorer.get_block("00000000000000000035d467f3e31a04bd9814bc0aec04b7e5877530b41b4450")


#to check whether n_tx includes unconfirmed transactions
def tx_test():
    print(block.n_tx)
    print(len(block.transactions))
    
    count = 0
    for i in range(len(block.transactions)):
        if (block.transactions[i].block_height != -1): #-1 means unconfirmed
            count += 1
    print(count)

#to discern relationship between total_value, output_values sum, input_values sum
def values_test():
    val = 0
    for i in range (1,len(block.transactions)):
        for j in range(len(block.transactions[i].inputs)):
            val += block.transactions[i].inputs[j].value
        for k in range(len(block.transactions[i].outputs)):
            val += block.transactions[i].outputs[k].value
    print(val)
    
def tot_tx_val(block_hash):
    block = blockexplorer.get_block(block_hash)
    val = 0
    for i in range (1,len(block.transactions)):
        for j in range(len(block.transactions[i].inputs)):
            val += block.transactions[i].inputs[j].value
        for k in range(len(block.transactions[i].outputs)):
            val += block.transactions[i].outputs[k].value
    return val

def tot_tx_size(block_hash):
    block = blockexplorer.get_block(block_hash)
    tot_size = 0
    for i in range(block.n_tx):
        tot_size += block.transactions[i].size
    return tot_size
