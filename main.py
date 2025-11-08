from stats import get_num_words
from stats import get_num_of_characters, sort_on ,dict_with_two_keys
import sys


def get_book_text(filepath):
    try:
        with open(filepath[1]) as f:
            file_contents = ""
            file_contents  = f.read()
    except Exception as e:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    return file_contents

text = get_book_text(sys.argv)

number_char = get_num_of_characters(text)
length = get_num_words(text)
two_key_number_char = []
for key in number_char:
    count = number_char[key]
    two_key_number_char.append(dict_with_two_keys(key, count))

two_key_number_char.sort(key=sort_on, reverse=True)
#print(two_key_number_char)


print("============ BOOKBOT ============")
print(f"Analyzing book found at {sys.argv[1]}")
print("----------- Word Count ----------")
print(f"Found {length} total words")
print("--------- Character Count -------")
for item in two_key_number_char:
    print(f"{item['key']}: {item['count']}")
print("============= END ===============")
