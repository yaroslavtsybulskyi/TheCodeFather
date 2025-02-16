"""
Regex module
Testing created regex
"""


import re

date_pattern = r'\d{1,2}[-/]\d{1,2}[-/]\d{2,4}'
hashtag_pattern = r'#\w+'
ten_letters_pattern = r'\b\w{10}\b'
second_a_pattern = r'\b\wa\w+\b'
words_with_numbers = r'\b\w*\d+\w*\b'
capital_words = r'\b[A-Z][a-z]+\b'
email = r"^[a-z0-9._%+-]+@[a-z0-9.-]+\.[a-z]{2,}$"
ten_letter_word_with_third_o = r'^..[o].{6}$'

if __name__ == '__main__':
    date_data = ["2/2/2024", "12-01-2023", "01/1/23", "2024-12-2"]
    print("date_pattern:")
    for data in date_data:
        print(f"'{data}': {bool(re.match(date_pattern, data))}")

    hashtag_data = ["#hashtag", "#programming123", "no hashtag", "#", " #test"]
    print("\nhashtag_pattern:")
    for data in hashtag_data:
        print(f"'{data}': {bool(re.search(hashtag_pattern, data))}")

    ten_letters_data = ["tenletters", "exactlyten", "short", "verylongword", "1234567890"]
    print("\nten_letters_pattern:")
    for data in ten_letters_data:
        print(f"'{data}': {bool(re.match(ten_letters_pattern, data))}")

    second_a_data = ["banana", "alphabet", "car", "data", "aapple"]
    print("\nsecond_a_pattern:")
    for data in second_a_data:
        print(f"'{data}': {bool(re.match(second_a_pattern, data))}")

    words_with_numbers_data = ["word123", "123word", "word123word", "word", "123"]
    print("\nwords_with_numbers:")
    for data in words_with_numbers_data:
        print(f"'{data}': {bool(re.match(words_with_numbers, data))}")

    capital_words_data = ["Word", "AnotherWord", "word", "WORD", "Word123"]
    print("\ncapital_words:")
    for data in capital_words_data:
        print(f"'{data}': {bool(re.match(capital_words, data))}")

    email_data = ["test@example.com", "invalid-email", "test@example", "test@example.verylongdomain",
                  "test@example.co.uk"]
    print("\nemail:")
    for data in email_data:
        print(f"'{data}': {bool(re.match(email, data))}")

    ten_letter_word_with_third_o_data = ["..oxxxxxx", "aboxxxxxx", "hellooooo", "oxxxxxxxx", "abcdefghij"]
    print("\nten_letter_word_with_third_o:")
    for data in ten_letter_word_with_third_o_data:
        print(f"'{data}': {bool(re.match(ten_letter_word_with_third_o, data))}")
