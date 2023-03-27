from block import Block
import time


class BlockChain:

    def __init__(self):
        genisis = Block("Genesis Block", previous_hash=None)
        self.head = None
        self.size = 0
        self.add_block(genisis)

    def __str__(self):
        current = self.head
        while current:
            print(current)
            current = current.prev_block
        return ""

    def add_block(self, block: Block):
        if (block.data_is_empty()):
            return "Please provide data"

        self.size += 1
        if (self.head == None):
            self.head = block
            return
        new_head = block
        new_head.prev_block = self.head
        self.head = new_head
