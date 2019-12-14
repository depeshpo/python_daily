import re


def swap_string(text):
    result = ''
    for i in text:
        if i.islower():
            result += i.upper()
        else:
            result += i.lower()
    # using list comprehension
    # result = ''.join([i.lower() if i.isupper() else i.upper() for i in text])
    return result

if __name__ == '__main__':
    inp = input('Give some input: ')
    result = swap_string(inp)
    print(result)
