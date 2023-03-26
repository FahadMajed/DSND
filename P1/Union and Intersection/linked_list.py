class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return str(self.value)


class LinkedList:
    def __init__(self):
        self.head = None
        self.nodes = []

    def __str__(self):
        cur_head = self.head
        out_string = ""
        while cur_head:
            out_string += str(cur_head.value) + " -> "
            cur_head = cur_head.next
        return out_string

    def append(self, value):
        self.nodes.append(value)
        if self.head is None:
            self.head = Node(value)
            return

        node = self.head
        while node.next:
            node = node.next

        node.next = Node(value)

    def size(self):
        size = 0
        node = self.head
        while node:
            size += 1
            node = node.next

        return size

    def add_all(self, values: set):
        for value in values:
            self.append(value)

    def is_empty(self):
        return self.head == None


def union(llist_1: LinkedList, llist_2: LinkedList):

    if (llist_1.is_empty() or llist_2.is_empty()):
        return "Please Provice non empty list"

    union = LinkedList()
    union_set = set()

    current = llist_1.head

    while current:
        union_set.add(current.value)
        current = current.next

    current = llist_2.head

    while current:
        if current.value not in union_set:
            union_set.add(current.value)
        current = current.next

    union.add_all(union_set)

    return union


def intersection(llist_1, llist_2):
    if (llist_1.is_empty() or llist_2.is_empty()):
        return "Please Provice non empty list"
    intersection = LinkedList()

    for node in llist_1.nodes:

        if node in llist_2.nodes:
            intersection.append(node)

    return intersection
