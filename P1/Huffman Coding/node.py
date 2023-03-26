class Node:
    def __init__(self, char, frequency, left=None, right=None) -> None:
        self.character = char
        self.left = left
        self.right = right
        self.frequency = frequency
        pass

    def __str__(self) -> str:

        return self.character + str(self.frequency)

    def set_left(self, node):

        self.left = node

    def set_right(self, node):
        self.right = node

    def in_order_traversal(self, root):
        result = []
        if root:
            result = self.in_order_traversal(root.left)
            result.append((root.character, root.frequency))
            result = result + self.in_order_traversal(root.right)
        return result

    def __lt__(self, other):

        self.frequency < other.frequency

    def __le__(self, other):

        self.frequency <= other.frequency
