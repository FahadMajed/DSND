from block_chain import BlockChain, Block


block_chain = BlockChain()
print(block_chain.size)
# 1


block_chain = BlockChain()
block = Block("hello", block_chain.head.hash)
block_chain.add_block(block)
print(block_chain.size)
# 2
print(block_chain.head.hash == block.hash)
# TRUE


block_chain = BlockChain()
block = Block("", block_chain.head.hash)

block_chain.add_block(block)

print(block_chain.size)
# 1 (Not Added)
