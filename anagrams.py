import random
import string
import requests

def generate_random_string():
    """
    Generate a random 11 character string with at least 2 vowels
    """
    vowels = 'aeiou'
    consonants = ''.join(set(string.ascii_lowercase) - set(vowels))
    random_string = ''
    while len(random_string) < 11:
        if len(random_string) < 2:
            random_string += random.choice(vowels)
        else:
            if random.random() < 0.5:
                random_string += random.choice(vowels)
            else:
                random_string += random.choice(consonants)
    return ''.join(random.sample(random_string, len(random_string)))

def load_dictionary():
    url = 'https://raw.githubusercontent.com/dwyl/english-words/master/words_alpha.txt'
    response = requests.get(url)
    return set(response.text.splitlines())

def generate_words(random_string, word_length, dictionary):
    """Generate all valid dictionary words of word_length from the 11 char string"""
    words = set()
    for i in range(len(random_string)):
        for j in range(i + word_length, len(random_string) + 1):
            word = ''.join(sorted(random_string[i:j]))
            if word in dictionary and len(word) == word_length:
                words.add(word)
    return words

def main():
    random_string = generate_random_string()
    print("Random string:", random_string)
    word_length = int(input("Enter word length: "))
    dictionary = load_dictionary()
    words = generate_words(random_string, word_length, dictionary)
    print("Valid words of length", word_length, ":", words)

if __name__ == "__main__":
    main()