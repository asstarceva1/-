import heapq
from collections import Counter
class Node:
    def __init__(self, symbol=None, freq=0):
        self.symbol = symbol
        self.freq = freq
        self.left = None
        self.right = None

    def __lt__(self, other):
        return self.freq < other.freq

def build_huffman_tree(text):
    freq_counter = Counter(text)
    heap = [Node(symbol, freq) for symbol, freq in freq_counter.items()]
    heapq.heapify(heap)

    while len(heap) > 1:
        left = heapq.heappop(heap)
        right = heapq.heappop(heap)
        merged = Node(freq=left.freq + right.freq)
        merged.left = left
        merged.right = right
        heapq.heappush(heap, merged)

    return heap[0]
def build_huffman_code_table(root):
    code_table = {}

    def traverse(node, code):
        if node.symbol is not None:
            code_table[node.symbol] = code
        else:
            traverse(node.left, code + '0')
            traverse(node.right, code + '1')

    traverse(root, '')
    return code_table
def encode(text, code_table):
    encoded_text = ''
    for symbol in text:
        encoded_text += code_table[symbol]
    return encoded_text
def decode(encoded_text, root):
    decoded_text = ''
    node = root
    for bit in encoded_text:
        if bit == '0':
            node = node.left
        else:
            node = node.right

        if node.symbol is not None:
            decoded_text += node.symbol
            node = root

    return decoded_text
def huffman_coding(text):
    root = build_huffman_tree(text)
    code_table = build_huffman_code_table(root)
    encoded_text = encode(text, code_table)
    return encoded_text, root

text = input('Введите текст: ')
encoded_text, root = huffman_coding(text)
print("Encoded text:", encoded_text)
decoded_text = decode(encoded_text, root)
print("Decoded text:", decoded_text)
