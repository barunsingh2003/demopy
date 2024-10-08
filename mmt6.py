def lz78_compress(data):
    dictionary = {}
    current_string = ""
    result = []
    code = 1

    for symbol in data:
        combined_string = current_string + symbol
        if combined_string not in dictionary:
            if current_string:
                result.append((dictionary.get(current_string, 0), symbol))
            else:
                result.append((0, symbol))
            dictionary[combined_string] = code
            code += 1
            current_string = ""
        else:
            current_string = combined_string

    if current_string:
        result.append((dictionary.get(current_string, 0), ""))

    return result

# Example Usage
data = "ABABABA"
compressed_data = lz78_compress(data)
print(f"Compressed Data: {compressed_data}")
