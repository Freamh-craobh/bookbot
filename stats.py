def get_num_words(book):
    wordlist = book.split()
    num_words = len(wordlist)
    return num_words

def get_num_char(book):
    num_char = {}
    for char in book:
        num_char.setdefault(char.lower(), 0)
        num_char[char.lower()] += 1
    return num_char

def sort_on(item):
    return item["num"]

def list_dict_chars(dict):
    chars_list = []
    for key, value in dict.items():
        chars_list.append({"key":key, "num":value })
    chars_list.sort(key=sort_on, reverse=True)
    return chars_list

