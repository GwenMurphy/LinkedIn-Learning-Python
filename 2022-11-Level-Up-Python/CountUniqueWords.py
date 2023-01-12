"""
Challenge:      Write a Python function to count the number of unique words and how often each occurs.

Input:          Path to text file.

Output:         Print message with:
                    > total number of words
                    > top 20 most frequent words

                Ignore case

                Words contain:
                    > Letters
                    > Numbers
                    > Apostraphes
"""

##### ##### ##### ##### ##### Instructor's Solution
import re
import collections

def count_words(path):
    with open(path, 'r', encoding='utf-8') as file:
        all_words = re.findall(r"[0-9a-zA-Z-']+", file.read())
        all_words = [word.upper() for word in all_words]
        print(f'\nTotal Words: {len(all_words)}')

        word_counts = collections.Counter(all_words)
        
        print('\Top 20 Words:')
        for word in word_counts.most_common(20):
            print(f'{word[0]}\t{word[1]}')