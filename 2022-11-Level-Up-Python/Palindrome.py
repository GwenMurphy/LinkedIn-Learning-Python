"""
Challenge:      Write a Python function to determine if a given string is a palindrome.

Input:          string to evaluate
Output:         Boolean value

"""

##### ##### My Attempt

# stringToEvaluate = input()

## I have no idea how I'd go from here.
## Literally no eexperience whatsoever.
## I can do random generators and Twitter bots, but not this.
## I'll have to learn by watching it and adding commenting all over it for what I think the thing does.


##### ##### Instructor's Solution

## Imports re
import re

## Function to check if it is a palindrome.
def is_palindrome(phrase):
    ## Takes the phrase and converts it to lowercase. Ignored non-alphabetical characters.
    forwards = ''.join(re.findall(r'[a-z]+', phrase.lower()))
    backwards = forwards[::-1]
    
    ## Returns whether it's true or false
    return forwards == backwards


#############################
phrase = input()
print(is_palindrome(phrase))