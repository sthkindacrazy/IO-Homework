"""
This module corresponds to functionality documented
at https://blockchain.info/api/blockchain_api
"""

#referenced from blockchain data API - Python
from . import util
import json


def get_block(block_id, api_code=None):
    """Get a single block based on a block index or hash.
    
    :param str block_id: block hash or index to look up
    :param str api_code: Blockchain.info API code (optional)
    :return: an instance of :class:`Block` class
    """
    
    resource = 'rawblock/' + block_id
    if api_code is not None:
        resource += '?api_code=' + api_code
    response = util.call_api(resource)
    json_response = json.loads(response)
    return Block(json_response)




class UnspentOutput:
    def __init__(self, o):
        self.tx_hash = o['tx_hash']
        self.tx_index = o['tx_index']
        self.tx_output_n = o['tx_output_n']
        self.script = o['script']
        self.value = o['value']
        self.value_hex = o['value_hex']
        self.confirmations = o['confirmations']


class Address:
    def __init__(self, a):
        self.hash160 = a['hash160']
        self.address = a['address']
        self.n_tx = a['n_tx']
        self.total_received = a['total_received']
        self.total_sent = a['total_sent']
        self.final_balance = a['final_balance']
        self.transactions = [Transaction(tx) for tx in a['txs']]


class Input:
    def __init__(self, i):
        obj = i.get('prev_out')
        if obj is not None:
            # regular TX
            self.n = obj['n']
            self.value = obj['value']
            self.address = obj['addr']
            self.tx_index = obj['tx_index']
            self.type = obj['type']
            self.script = obj['script']
            self.script_sig = i['script']
            self.sequence = i['sequence']
        else:
            # coinbase TX
            self.script_sig = i['script']
            self.sequence = i['sequence']


class Output:
    def __init__(self, o):
        self.n = o['n']
        self.value = o['value']
        self.address = o.get('addr')
        self.tx_index = o['tx_index']
        self.script = o['script']
        self.spent = o['spent']


class Transaction:
    def __init__(self, t):
        self.double_spend = t.get('double_spend', False)
        self.block_height = t.get('block_height')
        self.time = t['time']
        self.relayed_by = t['relayed_by']
        self.hash = t['hash']
        self.tx_index = t['tx_index']
        self.version = t['ver']
        self.size = t['size']
        self.inputs = [Input(i) for i in t['inputs']]
        self.outputs = [Output(o) for o in t['out']]
        
        if self.block_height is None:
            self.block_height = -1


class Block:
    def __init__(self, b):
        self.hash = b['hash']
        self.version = b['ver']
        self.previous_block = b['prev_block']
        self.merkle_root = b['mrkl_root']
        self.time = b['time']
        self.bits = b['bits']
        self.fee = b['fee']
        self.nonce = b['nonce']
        self.n_tx = b['n_tx']
        self.size = b['size']
        self.block_index = b['block_index']
        self.main_chain = b['main_chain']
        self.height = b['height']
        self.received_time = b.get('received_time', b['time'])
        self.relayed_by = b.get('relayed_by')
        self.transactions = [Transaction(t) for t in b['tx']]
        for tx in self.transactions:
            tx.block_height = self.height
