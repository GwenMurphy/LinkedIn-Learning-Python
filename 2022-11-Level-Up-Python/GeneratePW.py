"""
Note:           Look up Diceware

Challenge:      Write a Python function to generate passphrases

Input:          Number of words in passphrase

Output:         String of random words, separated by spaces

"""

##### ##### ##### ##### ##### Instructor's Solution

import secrets

def generate_passphrase(num_words, wordlist_path='diceware.wordlist.asc'):
    with open(wordlist_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()[2:7778]
        word_list = [line.split()[1] for line in lines]

    words = [secrets.choice(word_list) for i in range(num_words)]
    return ' '.join(words)