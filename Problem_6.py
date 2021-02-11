class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return str(self.value)


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.count = 0
        self.llist = []

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
            self.tail = self.head
            self.count += 1
            self.llist.append(value)
            return

        self.tail.next = Node(value)
        self.tail = self.tail.next
        self.count += 1
        self.llist.append(value)

    def size(self):
        return self.count

def union(llist_1, llist_2):
    union_set = set(llist_1.llist + llist_2.llist)
    if len(union_set) == 0:
        return "Lists are empty"
    union = LinkedList()
    for item in union_set:
        union.append(item)
    return union

def intersection(llist_1, llist_2):
    intersection_set = set(llist_1.llist).intersection(set(llist_2.llist))
    if len(intersection_set) == 0:
        return 'No intersection'
    intersection = LinkedList()
    for item in intersection_set:
        intersection.append(item)
    return intersection


# Test 1 - normal case
linked_list_1 = LinkedList()
linked_list_2 = LinkedList()

element_1 = [1,1,2,200]
element_2 = [1,2,3,4,5,100]

for i in element_1:
    linked_list_1.append(i)

for i in element_2:
    linked_list_2.append(i)

print ('Test 1:\n','Union:', union(linked_list_1,linked_list_2)) # Should return "Union: 1 -> 2 -> 3 -> 4 -> 5 -> 100 -> 200 ->"
print ('Intersection: ', intersection(linked_list_1,linked_list_2),'\n') # should return "Intersection:  1 -> 2 ->"

# Test 2 - Edge case: Linked Lists are empty
linked_list_3 = LinkedList()
linked_list_4 = LinkedList()

element_1 = []
element_2 = []

for i in element_1:
    linked_list_3.append(i)

for i in element_2:
    linked_list_4.append(i)

print ('Test 2:\n','Union:', union(linked_list_3,linked_list_4)) # Should return "Union: Lists are empty"
print ('Intersection:', intersection(linked_list_3,linked_list_4), '\n') # Should return "Intersection: No intersection"

# Test 3 - Edge case: One Linked List is empty
linked_list_5 = LinkedList()
linked_list_6 = LinkedList()

element_1 = [1,1,2,3,4]
element_2 = []

for i in element_1:
    linked_list_5.append(i)

for i in element_2:
    linked_list_6.append(i)

print ('Test 3:\n','Union:', union(linked_list_5,linked_list_6)) # Should return "Union: 1 -> 2 -> 3 -> 4 -> "
print ('Intersection:', intersection(linked_list_5,linked_list_6),'\n') # Should return "Intersection: No intersection"
