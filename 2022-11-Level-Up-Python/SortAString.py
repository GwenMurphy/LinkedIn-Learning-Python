### Doesn't make it easy, does he?
### Went straight for the deep end.

"""
Challenge:          Write a Python function to sort the words in a string.

Input:              String of words, separated by spaces
Output:             String of words, sorted alphabecitally.

"""

##### ##### My Attempt

## ?



##### ##### Instructor's Solution

def sort_words(input):
    ## Split method.
    words = input.split()
    words = [w.lower() + w for w in words]
    ## Sorts them.
    words.sort()
    ## Does something else.
    words = [w[len(w)//2:] for w in words]

    return ' '.join(words)

## Single line version of solution
def sortwords_singlelinever(words):
    return ' '.join(sorted(words.split(), key=str.casefold))