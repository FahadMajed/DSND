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

    def __str__(self) -> str:
        self.print_time()
        print("Data: " + str(self.data))
        print("SHA256 Hash: " + str(self.hash))
        print("Previous Hash: " + str(self.previous_hash))
        print("---------------------------------------------")
        return ""

    def print_time(self):
        time = self.timestamp[0]
        print("Timestamp: " + str(time.tm_year) + "-" +
              str(time.tm_mon) + "-" + str(time.tm_mday) + " " + str(time.tm_hour) + ":" +
              str(time.tm_min) + ":" + str(time.tm_sec))
