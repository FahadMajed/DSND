from block_chain import BlockChain, Block


block_chain = BlockChain()
print(block_chain.size)
# 1


block_chain = BlockChain()
block = Block("hello", block_chain.head.hash)
block_chain.add_block(block)
print(block_chain.size)
# 2

print(block_chain)
'''
Timestamp: 2023-3-27 17:4:56
Data: hello
SHA256 Hash: a20200a94c75010576e2d6a83e6fa69271901a9d805894b28bd91e6054fbfd10
Previous Hash: a20200a94c75010576e2d6a83e6fa69271901a9d805894b28bd91e6054fbfd10
---------------------------------------------

Timestamp: 2023-3-27 17:4:56
Data: Genesis Block
SHA256 Hash: a20200a94c75010576e2d6a83e6fa69271901a9d805894b28bd91e6054fbfd10
Previous Hash: None
---------------------------------------------
'''
print(block_chain.head.hash == block.hash)
# TRUE


block_chain = BlockChain()
block = Block("", block_chain.head.hash)

block_chain.add_block(block)

print(block_chain.size)
# 1 (Not Added)
