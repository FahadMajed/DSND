
from linked_list import LinkedList, union, intersection, Node
# Test case 1


linked_list_1 = LinkedList()
linked_list_2 = LinkedList()
element_1 = [1, 2, 3]
element_2 = [4, 5, 6, 2]

for i in element_1:
    linked_list_1.append(i)
for i in element_2:
    linked_list_2.append(i)
print('union')
print(union(linked_list_1, linked_list_2))
# 1 -> 2 -> 3 -> 4 -> 5 -> 6 ->
print('intersection')
print(intersection(linked_list_1, linked_list_2))
# 2 ->

# Test case 2


linked_list_3 = LinkedList()
linked_list_4 = LinkedList()

element_1 = [3, 2, 4, 35, 6, 65, 6, 4, 3, 23]
element_2 = [1, 7, 8, 9, 11, 21, 1, 3, 2, 4]

for i in element_1:
    linked_list_3.append(i)

for i in element_2:
    linked_list_4.append(i)
print('union')
print(union(linked_list_3, linked_list_4))
# 65 -> 2 -> 35 -> 3 -> 4 -> 6 -> 1 -> 7 -> 8 -> 9 -> 11 -> 21 -> 23 ->
print('intersection')
print(intersection(linked_list_3, linked_list_4))
# 3 -> 2 -> 4 ->

linked_list_5 = LinkedList()
linked_list_6 = LinkedList()

element_1 = []
element_2 = []

for i in element_1:
    linked_list_5.append(i)

for i in element_2:
    linked_list_6.append(i)
print('union')
print(union(linked_list_5, linked_list_6))
# Please Provice non empty list
print('intersection')
print(intersection(linked_list_5, linked_list_6))
# Please Provice non empty list
