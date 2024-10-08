def lzw_compress(data):
    dictionary = {chr(i): i for i in range(256)}
    current_string = ""
    code = 256
    result = []
    
    for symbol in data:
        combined_string = current_string + symbol
        if combined_string in dictionary:
            current_string = combined_string
        else:
            result.append(dictionary[current_string])
            dictionary[combined_string] = code
            code += 1
            current_string = symbol

    if current_string:
        result.append(dictionary[current_string])

    return result

# Example Usage
data = "ABABABA"
compressed_data = lzw_compress(data)
print(f"Compressed Data: {compressed_data}")
