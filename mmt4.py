def lz77_compress(data, window_size=10):
    i = 0
    compressed_data = []
    
    while i < len(data):
        match_offset, match_length = 0, 0
        for j in range(max(0, i - window_size), i):
            length = 0
            while i + length < len(data) and data[j + length] == data[i + length]:
                length += 1
                if length > match_length:
                    match_offset = i - j
                    match_length = length

        if match_length > 0:
            next_char = data[i + match_length] if i + match_length < len(data) else ''
            compressed_data.append((match_offset, match_length, next_char))
            i += match_length + 1
        else:
            compressed_data.append((0, 0, data[i]))
            i += 1

    return compressed_data

# Example usage:
data = "abracadabra"
compressed_data = lz77_compress(data)
print(f"Original data: {data}")
print(f"Compressed data: {compressed_data}")
