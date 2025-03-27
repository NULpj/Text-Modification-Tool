import re
import random

def reverse_text(text):
    return text[::-1]

def to_uppercase(text):
    return text.upper()

def to_lowercase(text):
    return text.lower()

def replace_text(text, old, new):
    return text.replace(old, new)

def remove_spaces(text):
    return text.replace(" ", "")

def capitalize_each_word(text):
    return text.title()

def swap_case(text):
    return text.swapcase()

def count_characters(text):
    return len(text)

def remove_vowels(text):
    return re.sub(r'[aeiouAEIOU]', '', text)

def remove_consonants(text):
    return re.sub(r'[^aeiouAEIOU\s]', '', text)

def reverse_words(text):
    return ' '.join(text.split()[::-1])

def is_palindrome(text):
    cleaned_text = re.sub(r'[^a-zA-Z0-9]', '', text.lower())
    return "Yes" if cleaned_text == cleaned_text[::-1] else "No"

def count_words(text):
    return len(text.split())

def remove_punctuation(text):
    return re.sub(r'[^a-zA-Z0-9\s]', '', text)

def leetspeak(text):
    leet_dict = {'a': '4', 'e': '3', 'i': '1', 'o': '0', 's': '5', 't': '7'}
    return ''.join(leet_dict.get(c.lower(), c) for c in text)

def duplicate_text(text):
    return text * 2

def reverse_case(text):
    return ''.join(c.upper() if c.islower() else c.lower() for c in text)

def remove_digits(text):
    return re.sub(r'\d', '', text)

def keep_digits(text):
    return re.sub(r'\D', '', text)

def add_spaces_between_letters(text):
    return ' '.join(text)

def remove_duplicates(text):
    return ''.join(sorted(set(text), key=text.index))

def scramble_text(text):
    text_list = list(text)
    random.shuffle(text_list)
    return ''.join(text_list)

def count_vowels(text):
    return sum(1 for c in text if c.lower() in 'aeiou')

def count_consonants(text):
    return sum(1 for c in text if c.lower() in 'bcdfghjklmnpqrstvwxyz')

def count_sentences(text):
    return len(re.split(r'[.!?]', text)) - 1

def repeat_each_letter(text):
    return ''.join(c * 2 for c in text)

def reverse_each_word(text):
    return ' '.join(word[::-1] for word in text.split())

def add_line_numbers(text):
    return '\n'.join(f"{i+1}. {line}" for i, line in enumerate(text.split('\n')))

def remove_whitespace(text):
    return ''.join(text.split())

def replace_vowels_with_star(text):
    return re.sub(r'[aeiouAEIOU]', '*', text)

def replace_consonants_with_hash(text):
    return re.sub(r'[^aeiouAEIOU\s]', '#', text)

def camel_case(text):
    words = text.split()
    return words[0].lower() + ''.join(word.capitalize() for word in words[1:])

def snake_case(text):
    return text.lower().replace(" ", "_")

def kebab_case(text):
    return text.lower().replace(" ", "-")

def pascal_case(text):
    return ''.join(word.capitalize() for word in text.split())

def shift_letters_forward(text):
    return ''.join(chr(ord(c) + 1) if c.isalpha() else c for c in text)

def shift_letters_backward(text):
    return ''.join(chr(ord(c) - 1) if c.isalpha() else c for c in text)

def remove_first_letter(text):
    return text[1:] if text else text

def remove_last_letter(text):
    return text[:-1] if text else text

def add_prefix_suffix(text, prefix, suffix):
    return prefix + text + suffix

def mirror_text(text):
    return text + text[::-1]

def random_case(text):
    return ''.join(random.choice([c.upper(), c.lower()]) for c in text)

def double_words(text):
    return ' '.join([word * 2 for word in text.split()])

def reverse_sentence_order(text):
    return '. '.join(reversed(text.split('. ')))

def encode_rot13(text):
    return text.translate(str.maketrans("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz", "NOPQRSTUVWXYZABCDEFGHIJKLMnopqrstuvwxyzabcdefghijklm"))

def shuffle_words(text):
    words = text.split()
    random.shuffle(words)
    return ' '.join(words)

def reverse_only_letters(text):
    letters = [c for c in text if c.isalpha()]
    return ''.join(letters.pop() if c.isalpha() else c for c in text)

def count_unique_characters(text):
    return len(set(text))

def remove_special_characters(text):
    return re.sub(r'[^a-zA-Z0-9\s]', '', text)

def replace_spaces_with_underscore(text):
    return text.replace(" ", "_")

def main():
    print("Text Modifier Tool")
    functions = [reverse_text, to_uppercase, to_lowercase, replace_text, remove_spaces, capitalize_each_word, swap_case,
                 count_characters, remove_vowels, remove_consonants, reverse_words, is_palindrome, count_words,
                 remove_punctuation, leetspeak, duplicate_text, reverse_case, remove_digits, keep_digits,
                 add_spaces_between_letters, remove_duplicates, scramble_text, count_vowels, count_consonants,
                 count_sentences, repeat_each_letter, reverse_each_word, add_line_numbers, remove_whitespace,
                 replace_vowels_with_star, replace_consonants_with_hash, camel_case, snake_case, kebab_case,
                 pascal_case, shift_letters_forward, shift_letters_backward, remove_first_letter, remove_last_letter,
                 add_prefix_suffix, mirror_text, random_case, double_words, reverse_sentence_order, encode_rot13,
                 shuffle_words, reverse_only_letters, count_unique_characters, remove_special_characters,
                 replace_spaces_with_underscore]
    
    for i, func in enumerate(functions, 1):
        print(f"{i}. {func.__name__.replace('_', ' ').title()}")
    
    choice = int(input("Choose an option: "))
    text = input("Enter your text: ")
    
    if 1 <= choice <= len(functions):
        func = functions[choice - 1]
        if func == replace_text:
            old = input("Enter text to replace: ")
            new = input("Enter new text: ")
            print("Modified: ", func(text, old, new))
        elif func == add_prefix_suffix:
            prefix = input("Enter prefix: ")
            suffix = input("Enter suffix: ")
            print("Modified: ", func(text, prefix, suffix))
        else:
            print("Modified: ", func(text))
    else:
        print("Invalid choice")

if __name__ == "__main__":
    main()
