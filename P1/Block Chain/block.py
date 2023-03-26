import hashlib
import time


class Block:

    def __init__(self, data, previous_hash):
        self.timestamp = time.gmtime(),
        self.data = data
        self.previous_hash = previous_hash
        self.prev_block = None
        self.hash = self.calc_hash()

    def calc_hash(self):
        sha = hashlib.sha256()

        hash_str = "We are going to encode this string of data!".encode(
            'utf-8')

        sha.update(hash_str)

        return sha.hexdigest()

    def data_is_empty(self):
        return self.data == "" or self.data == None
