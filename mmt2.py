import heapq

class HuffmanNode:
    def __init__(self, symbol=None, frequency=0):
        self.symbol = symbol
        self.frequency = frequency
        self.left = None
        self.right = None
    
    def __lt__(self, other):
        return self.frequency < other.frequency

def huffman_encoding(data):
    if len(data) == 0:
        return "", {}

    frequencies = {char: data.count(char) for char in set(data)}
    priority_queue = [HuffmanNode(symbol=sym, frequency=freq) for sym, freq in frequencies.items()]
    heapq.heapify(priority_queue)

    while len(priority_queue) > 1:
        left = heapq.heappop(priority_queue)
        right = heapq.heappop(priority_queue)
        merged = HuffmanNode(frequency=left.frequency + right.frequency)
        merged.left = left
        merged.right = right
        heapq.heappush(priority_queue, merged)

    tree = priority_queue[0]
    codebook = encode_tree(tree)
    encoded_data = ''.join(codebook[char] for char in data)
    return encoded_data, codebook

def encode_tree(node, prefix='', codebook={}):
    if node.symbol is not None:
        codebook[node.symbol] = prefix
    else:
        if node.left:
            encode_tree(node.left, prefix + '0', codebook)
        if node.right:
            encode_tree(node.right, prefix + '1', codebook)
    return codebook

# Example Usage
data = "hello world"
encoded_data, codebook = huffman_encoding(data)
print(f"Encoded Data: {encoded_data}")
print(f"Codebook: {codebook}")
