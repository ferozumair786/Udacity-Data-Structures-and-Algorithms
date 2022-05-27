class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return str(self.value)


class LinkedList:
    def __init__(self):
        self.head = None

    def __str__(self):
        cur_head = self.head
        out_string = ""
        while cur_head:
            out_string += str(cur_head.value) + " -> "
            cur_head = cur_head.next
        return out_string


    def append(self, value):

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

def union(llist_1, llist_2):
    # Your Solution Here
    node1 = llist_1.head
    node2 = llist_2.head
    unlist = LinkedList()
    slist_1 = set()
    slist_2 = set()
    while node1:
        slist_1.add(node1.value)
        node1 = node1.next

    while node2:
        slist_2.add(node2.value)
        node2 = node2.next

    unset = slist_1 | slist_2

    for i in unset:
        unlist.append(i)

    return unlist

def intersection(llist_1, llist_2):
    # Your Solution Here

    node1 = llist_1.head
    node2 = llist_2.head
    inlist = LinkedList()
    slist_1 = set()
    slist_2 = set()
    while node1:
        slist_1.add(node1.value)
        node1 = node1.next

    while node2:
        slist_2.add(node2.value)
        node2 = node2.next

    inset = slist_1.intersection(slist_2)

    for i in inset:
        inlist.append(i)

    return inlist


# Test case 1

linked_list_1 = LinkedList()
linked_list_2 = LinkedList()

element_1 = [3,2,4,35,6,65,6,4,3,21]
element_2 = [6,32,4,9,6,1,11,21,1]

for i in element_1:
    linked_list_1.append(i)

for i in element_2:
    linked_list_2.append(i)

print (union(linked_list_1,linked_list_2))
print (intersection(linked_list_1,linked_list_2))

# Test case 2

linked_list_3 = LinkedList()
linked_list_4 = LinkedList()

element_1 = [3,2,4,35,6,65,6,4,3,23]
element_2 = [1,7,8,9,11,21,1]

for i in element_1:
    linked_list_3.append(i)

for i in element_2:
    linked_list_4.append(i)

print (union(linked_list_3,linked_list_4))
print (intersection(linked_list_3,linked_list_4))

# Add your own test cases: include at least three test cases
# and two of them must include edge cases, such as null, empty or very large values

# Test Case 1
#one of the lists is empty
print("Test Case 1: Union with an Empty Linked List")
empty_list = LinkedList()

#union should return a distinct linkedlist
print(union(linked_list_1, empty_list))

# Test Case 2

print("Test Case 2: Intersection with Empty Linked List")
#intersection should return nothing
print(intersection(linked_list_1, empty_list))


# Test Case 3
#word bubble
print("Test Case 3: Intersection of Two Words")
word1 = "gemeinshaft"
word2 = "shaghufta"

linked_list_5 = LinkedList()
for letter in word1:
    linked_list_5.append(letter)

linked_list_6 = LinkedList()
for letter in word2:
    linked_list_6.append(letter)

print(intersection(linked_list_5, linked_list_6))
