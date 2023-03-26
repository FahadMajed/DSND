from huffman_coding import HuffmanCipher
from node import Node


def test_init_pq():
    huffman = HuffmanCipher("BBFFFFFUUUUURJJJJJJJ")
    huffman._init_priority_queue()
    chars = []

    for node in huffman.nodes:
        chars.append(node[1].character)

    assert (chars == [
        "R", "B", "U", "F", "J", ])


def test_merge_nodes():
    pass
    huffman = HuffmanCipher("AABBB")
    huffman._init_priority_queue()
    huffman._merge_nodes()

    merged_node = Node('', 5)
    merged_node.set_left(Node("A", 2))
    merged_node.set_right(Node("B", 3))

    assert (huffman.nodes[0]
            [1].frequency == merged_node.frequency)


def test_merge_nodes_len_four():
    pass
    huffman = HuffmanCipher("AAAABBBBBCDD")
    huffman._init_priority_queue()

    chars = []

    for node in huffman.nodes:
        chars.append(node[1].character)

    assert (chars == [
        "C", "D", "A", "B"])

    huffman._merge_nodes()

    merged_node = Node('', 12, Node("B", 5), Node("", 7))

    assert (huffman.nodes[0]
            [1].frequency == merged_node.frequency)

    assert (huffman.nodes[0]
            [1].left.character == merged_node.left.character)

    assert (huffman.nodes[0]
            [1].right.character == merged_node.right.character)
    node = huffman._pop()[1]
    print(node.right.left.left)


def test_generate_encoded_data():
    huffman = HuffmanCipher("AAAAAAABBBCCCCCCCDDEEEEEE")
    huffman._init_priority_queue()
    huffman._merge_nodes()
    node = huffman._pop()[1]
    encoded = huffman._generate_binary_codes(node, '')

    assert (encoded["D"] == "000")
    pass


def test_encode():
    huffman = HuffmanCipher("AAAAAAABBBCCCCCCCDDEEEEEE")

    code = huffman.encode()

    assert (code == "1010101010101000100100111111111111111000000010101010101")


def test_decode():
    huffman = HuffmanCipher("AAAAAAABBBCCCCCCCDDEEEEEE")

    code = huffman.encode()

    assert (huffman.decode(code, huffman._pop()
            [1]) == "AAAAAAABBBCCCCCCCDDEEEEEE")
