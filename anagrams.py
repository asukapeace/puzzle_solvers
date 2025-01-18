import random
import string
import requests
import itertools

def generate_random_string():
    """
    Generate a random 11 character string with at least 2 vowels
    """
    vowels = 'aeiou'
    all_chars = list((string.ascii_lowercase))
    random_string = ''
    while len(random_string) < 11:
        if len(random_string) < 2:
            random_string += random.choice(vowels)
        else:
            random_string += random.choice(all_chars)
    return ''.join(random.sample(random_string, len(random_string)))

def load_dictionary():
    url = 'https://raw.githubusercontent.com/dwyl/english-words/master/words_alpha.txt'
    response = requests.get(url)
    return set(response.text.splitlines())

def find_permutations(string, length):
    if length == 0:
        return []
    elif length == 1:
        return [char for char in string]
    else:
        permutations = []
        for i in range(len(string)):
            prefix = string[i]
            suffix = string[:i] + string[i+1:]
            for perm in find_permutations(suffix, length - 1):
                permutations.append(prefix + perm)
        return permutations
    
def generate_words(random_string, word_length, dictionary):
    """Generate all valid dictionary words of word_length from the 11 char string"""
    return {w for w in find_permutations(random_string, word_length) if w in dictionary}

def main():
    random_string = generate_random_string()
    print("Random string:", random_string)
    word_length = int(input("Enter word length: "))
    dictionary = load_dictionary()
    words = generate_words(random_string, word_length, dictionary)
    print("Valid words of length", word_length, ":", words)

if __name__ == "__main__":
    main()