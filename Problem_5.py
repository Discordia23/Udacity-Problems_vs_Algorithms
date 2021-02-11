import hashlib
from datetime import datetime

class Block:

    def __init__(self, timestamp, data, previous_hash):
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.calc_hash()

    def calc_hash(self):
        sha = hashlib.sha256()

        # hash of new block consists in timestamp in str format + data + hash of previous block
        timestamp_str = self.timestamp.strftime("%d-%m-%Y (%H:%M:%S.%f)")
        data_str = str(self.data)
        previous_hash_str = str(self.previous_hash)
        hash_str = (timestamp_str + data_str + previous_hash_str).encode('utf-8')

        sha.update(hash_str)

        return sha.hexdigest()

class Blockchain:

    def __init__(self):
        self.tail = None
        self.head = None

    def append(self, data):
        if self.head == None:
            block = Block(datetime.now(), data, None)
            self.head = block
            self.tail = self.head
            return
        block = Block(datetime.now(), data, self.tail.hash)
        self.tail = block
        return

# Test 1: Blockchain with 4 blocks, check if data of first and last block are correct
first_chain = Blockchain()
first_chain.append('first_block')
first_chain.append('second_block')
first_chain.append('third_block')
first_chain.append('last_block')

print('Test 1:\n', 'Pass' if (first_chain.tail.data == 'last_block') and
     (first_chain.head.data == 'first_block') else 'Fail')

# Test 2: previous hash == hash of previous block
second_chain = Blockchain()
second_chain.append('first_block')
second_chain.append('last_block')

print('Test 2:\n', 'Pass' if (second_chain.head.hash == second_chain.tail.previous_hash) else 'Fail')

# Test 3 - edge case: Blockchain is empty
third_chain = Blockchain()

print('Test 3:\n', 'Pass' if (third_chain.head == None) else 'Fail')
