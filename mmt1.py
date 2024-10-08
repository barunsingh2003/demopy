class ShannonFanoNode:
    def __init__(self, symbol=None, frequency=0):
        self.symbol = symbol
        self.frequency = frequency
        self.left = None
        self.right = None

def build_tree(frequencies):
    sorted_symbols = sorted(frequencies.items(), key=lambda x: x[1], reverse=True)
    return shannon_fano(sorted_symbols)

def shannon_fano(sorted_symbols):
    if len(sorted_symbols) == 1:
        return ShannonFanoNode(symbol=sorted_symbols[0][0], frequency=sorted_symbols[0][1])
    
    half = sum(freq for sym, freq in sorted_symbols) / 2
    accumulated = 0
    i = 0
    for i, (sym, freq) in enumerate(sorted_symbols):
        accumulated += freq
        if accumulated >= half:
            break
    
    node = ShannonFanoNode()
    node.left = shannon_fano(sorted_symbols[:i+1])
    node.right = shannon_fano(sorted_symbols[i+1:])
    
    return node

def encode_tree(node, prefix='', codebook={}):
    if node.symbol is not None:
        codebook[node.symbol] = prefix
    else:
        if node.left:
            encode_tree(node.left, prefix + '0', codebook)
        if node.right:
            encode_tree(node.right, prefix + '1', codebook)
    return codebook

def shannon_fano_encoding(data):
    frequencies = {char: data.count(char) for char in set(data)}
    tree = build_tree(frequencies)
    codebook = encode_tree(tree)
    encoded_data = ''.join(codebook[char] for char in data)
    return encoded_data, codebook

# Example Usage
data = "hello world"
encoded_data, codebook = shannon_fano_encoding(data)
print(f"Encoded Data: {encoded_data}")
print(f"Codebook: {codebook}")
