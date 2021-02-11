import sys
import heapq

class Node():
    def __init__(self, value, frequency):
        self.value = value
        self.frequency = frequency
        self.left = None
        self.right = None
    def __lt__(self, other):
        return self.frequency < other.frequency

class Huffman_tree():
    def __init__(self, data):
        self.data = data

    def create_tree(self):
        # create a frequency dictionary
        self.freq_dict = dict()
        for char in self.data:
            if char in self.freq_dict:
                self.freq_dict[char] += 1
            else:
                self.freq_dict[char] = 1

        # create a priority queue to build the tree
        self.prio_q = []

        # push the leaves to the priority queue
        for char, freq in self.freq_dict.items():
            heapq.heappush(self.prio_q, Node(char, freq))

        # create the tree
        while len(self.prio_q) > 1:
            min_node = heapq.heappop(self.prio_q)
            next_min_node = heapq.heappop(self.prio_q)
            merged_node = Node((min_node.value + next_min_node.value), (min_node.frequency + next_min_node.frequency))
            merged_node.left = min_node
            merged_node.right = next_min_node
            heapq.heappush(self.prio_q, merged_node)
        return self.prio_q[0]

    # this function is needed for the encoding function to transform the characters of the string into '0' and '1'
    def codes(self, char):
        code = []
        root = self.prio_q[0]
        # edge case: data string consists in just in the same character
        if root.left is None:
            code.append('0'*len(char))
            return ''.join(code)
        # traverse the tree and create the code for the character
        def traverse(node):
            if node.left:
                if char in node.left.value:
                    code.append('0')
                    traverse(node.left)
                else:
                    code.append('1')
                    traverse(node.right)
        traverse(root)
        return ''.join(code)

def huffman_encoding(data):
    if data == "":
        return "", None

    # create the tree
    encode = Huffman_tree(data)
    tree = encode.create_tree()
    # hashmap to avoid repetitive encoding of the characters
    hashmap = dict()
    encoded_data = ""
    # loop through string and encode it
    for char in data:
        if char in hashmap:
            encoded_data += hashmap[char]
            continue
        code = encode.codes(char)
        encoded_data += code
        hashmap[char] = code
    return encoded_data, tree


def huffman_decoding(data,tree):
    root = tree
    decoded_data = ""

    if data == "":
        return decoded_data
    # edge case: data string consists in just in the same character
    if root.left is None:
        decoded_data = len(data)*root.value
        return decoded_data
    # loop through the encoded string, traverse the tree until a leaf is reached and decode the encoded string
    for char in data:
        if char == '0':
            root = root.left
            if root.left is None:
                decoded_data += root.value
                root = tree
        else:
            root = root.right
            if root.left is None:
                decoded_data += root.value
                root = tree
    return decoded_data

if __name__ == "__main__":
    codes = {}

    tests = ["The bird is the word", "ASDEWFsdfoer44", "AAAAAAAAA", ""]

    for i, a_great_sentence in enumerate(tests):
        if a_great_sentence:
            print ('Test: {}\n'.format(i+1))
            print ("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
            print ("The content of the data is: {}\n".format(a_great_sentence))

            encoded_data, tree = huffman_encoding(a_great_sentence)

            print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
            print ("The content of the encoded data is: {}\n".format(encoded_data))

            decoded_data = huffman_decoding(encoded_data, tree)

            print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
            print ("The content of the encoded data is: {}\n".format(decoded_data))
            print ("_______________________________________________________________________________________")
        else:
            print ('Test: {}\n'.format(i+1))
            print ("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
            print ("The content of the data is: {}\n".format(a_great_sentence))
            print ("No data available to encode")
            encoded_data, tree = huffman_encoding(a_great_sentence)
