from node import Node

import heapq


class HuffmanCipher:

    def __init__(self, text) -> None:
        self.text: str = text
        self.nodes = []
        pass

    def encode(self):
        self._init_priority_queue()
        self._merge_nodes()
        root = self._pop()[1]
        codes = self._generate_binary_codes(root, "")
        self._push(root)
        return self._generate_encoded_data(codes)

    def _init_priority_queue(self):
        if self.text == "":
            raise Exception("Please Provide Text")

        characters = {}

        for char in self.text:
            if char in characters:
                characters[char] += 1
            else:
                characters[char] = 1

        for char in characters.keys():
            frequency = characters[char]
            node = Node(char, frequency)
            heapq.heappush(self.nodes, (frequency, node))

    def _merge_nodes(self):
        iterations = len(self.nodes) - 1

        while iterations > 0:
            highest_priority = self._pop()
            second_priority = self._pop()

            merged_node = self._get_node_from_tuples(
                highest_priority, second_priority)

            self._push(merged_node)
            iterations = iterations - 1

    def _pop(self):
        return heapq.heappop(self.nodes)

    def _get_node_from_tuples(self, first_tuple, second_tuple):
        return Node('', first_tuple[1].frequency +
                    second_tuple[1].frequency, first_tuple[1], second_tuple[1])

    def _push(self, node):
        heapq.heappush(self.nodes, (node.frequency, node))

    def _generate_binary_codes(self, root, current_code):
        generated_codes = {}

        if root is None:
            return {}

        if root.character != '':
            generated_codes[root.character] = current_code

        generated_codes.update(self._generate_binary_codes(
            root.left, current_code + "0"))
        generated_codes.update(self._generate_binary_codes(
            root.right, current_code + "1"))

        return generated_codes

    def _generate_encoded_data(self, codes):
        encoded_data = self.text
        for char in encoded_data:
            encoded_data = encoded_data.replace(char, codes[char])

        return encoded_data

    def decode(self, encoded_data: str, root: Node):

        decoded_data = ""
        current_node = root

        for bit in encoded_data:

            if bit == "0":

                current_node = current_node.left
            else:

                current_node = current_node.right
            if current_node.character != "":

                decoded_data += current_node.character
                # go back
                current_node = root

        return decoded_data
