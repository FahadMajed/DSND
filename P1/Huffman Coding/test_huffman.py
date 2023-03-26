from huffman_coding import HuffmanCipher
from node import Node


huffman = HuffmanCipher("AAAAAAABBBCCCCCCCDDEEEEEE")

code = huffman.encode()

print(code)
# 1010101010101000100100111111111111111000000010101010101


huffman = HuffmanCipher("AAAAAAABBBCCCCCCCDDEEEEEE")

code = huffman.encode()

print(huffman.decode(code, huffman._pop()
                     [1]))
# AAAAAAABBBCCCCCCCDDEEEEEE

huffman = HuffmanCipher("")
try:
    code = huffman.encode()
except:
    print('Please Provide Test')
#
