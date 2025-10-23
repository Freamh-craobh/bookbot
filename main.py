import sys
from stats import get_num_char, list_dict_chars, get_num_words

if len(sys.argv) < 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()
    
def main():
    text = get_book_text(sys.argv[1])
    return text


wordcount = get_num_words(main())
book_char_count = get_num_char(main())

print("============ BOOKBOT ============\n"
    'Analyzing book found at books/frankenstein.txt...\n'
    '----------- Word Count ----------\n'
    f'Found {wordcount} total words\n'
    "--------- Character Count -------")
for dict in list_dict_chars(book_char_count):
    if dict["key"].isalpha():
        print(dict["key"]+": "+str(dict["num"]))
print("============= END ===============")
