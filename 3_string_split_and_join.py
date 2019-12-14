def split_string(text):
    split_text = text.split(" ")
    join_text = "-".join(split_text)
    return join_text

if __name__ == '__main__':
    inp = input("Give some raw input: ")
    result = split_string(inp)
    print(result)
