FILE_PATH = "books/frankenstein.txt"

with open(FILE_PATH) as f:
    file_contents = f.read()
file_contents = file_contents.lower().strip()

def word_count(file_string):
    words = file_string.split()
    return f"{len(words)} words found in the document"

def letter_count(file_contents):
    letter_dict = {}
    alphabet_list = "abcdefghijklmnopqrstuvwxyz"

    for letter in alphabet_list:
        letter_dict[letter] = 0

    for letter in file_contents:
        if letter in alphabet_list:
            letter_dict[letter] += 1
    return letter_dict

def print_report(letter_dict):
    print(f"--- Begin report of {FILE_PATH} ---")
    print(word_count(file_contents))
    print()
    sorted_letter_dict_by_value = sorted(letter_count(file_contents).items(), key=lambda x:x[1], reverse=True)
    for test in sorted_letter_dict_by_value:
        print(f"the '{test[0]}' character was found {test[1]} times")
    print(f"--- End report ---")
    print()



print_report(letter_count(file_contents))