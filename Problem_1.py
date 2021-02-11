class DoubleNode:
    def __init__(self, key, value):
        self.value = value
        self.next = None
        self.previous = None
        self.key = key

class LRU_Cache(object):
    def __init__(self, capacity):
        self.head = None
        self.tail = None
        self.capacity = capacity
        self.value_dict = dict()

    def append(self, node):
        self.tail.next = node
        self.tail.next.previous = self.tail
        self.tail = self.tail.next

    def remove_head(self):
        self.head = self.head.next # there was an error here in the first review => self.head.next = self.head
        self.head.previous = None

    def remove_node(self, node):
        if node == self.head:
            self.remove_head()
            return
        node.previous.next = node.next
        node.next.previous = node.previous

    def get(self, key):
        if key not in self.value_dict:
            return -1
        # remove the retrieved node from the linked list and append it at the end of the list (newest item)
        node = self.value_dict[key]
        self.append(node)
        self.remove_node(node)

        # remove the entry from value_dict and "append" it back
        self.value_dict.pop(key)
        self.value_dict[key] = node
        return node.value


    def set(self, key, value):
        node = DoubleNode(key, value)
        # if key is in cache, actualize the node (remove the existant node from the linked list and append it as a new node) in
        # the linked list and actualize the entry in the cache
        if key in self.value_dict:
            self.append(node)
            self.value_dict.pop(key)
            self.value_dict[key] = node
            return

        # if cache capacity is reached, append new node, remove head and actualize the cache entries
        if len(self.value_dict) >= self.capacity:
            if self.capacity == 0:
                return -1
            self.append(node)
            self.value_dict[key] = node
            self.value_dict.pop(self.head.key)
            self.remove_head()
            return

        # if linked list is empty, put new node as head+tail and actualize the cache
        if self.head is None:
            self.head = node
            self.tail = self.head
            self.value_dict[key] = self.head
            return

        # append the new node as new tail in the linked list and actualize the cache
        self.append(node)
        self.value_dict[key] = node
        return

# Test 1
lru = LRU_Cache(5)
lru.set(1, 20)
lru.set(2, 40)
lru.set(3, 30)
lru.set(4, 40)
lru.set(5, 100)
lru.get(6)

print ("Test 1:\n", "Pass" if  (lru.get(6) == -1) else "Fail")

# Test 2 - Edge case: Capacity == 0
lru = LRU_Cache(0)
lru.set(1, 20)

print ("Test 2:\n", "Pass" if  (lru.set(1, 20) == -1) else "Fail")

# Test 3
lru = LRU_Cache(1)
lru.set(1, 20)
lru.set(1, 40)
lru.get(1)

print ("Test 3:\n", "Pass" if  (lru.get(1) == 40) else "Fail")

# Test 4 (from the first review)
our_cache=LRU_Cache(3)
our_cache.set(1,1)
our_cache.set(2,2)
our_cache.set(3,3)
our_cache.set(4,4)
our_cache.get(4)   # Expected Value = 4
our_cache.get(1)   # Expected Value = -1
our_cache.set(2,4)
our_cache.get(2)   # Expected Value = 4
our_cache.set(5,5)
