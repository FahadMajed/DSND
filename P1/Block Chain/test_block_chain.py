from block_chain import BlockChain, Block


def test_add_block():
    block_chain = BlockChain()
    assert (block_chain.size == 1)


def test_add_another_block():
    block_chain = BlockChain()
    block = Block("hello", block_chain.head.hash)
    block_chain.add_block(block)
    assert (block_chain.size == 2)
    assert (block_chain.head.hash == block.hash)


def test_add_empty_block():
    block_chain = BlockChain()
    block = Block("", block_chain.head.hash)

    block_chain.add_block(block)

    assert (block_chain.size == 1)
