"""
Input:              integer value
Output:             list of prime factors
Difficulty:         1
"""

##### ##### My attempt

"""
def get_prime_factors():
    x = 630
    y = 1
    primes = ['']
    ### Checks range from 1 to number.
    for i in range(1, x):
        ## Check if divisible by itself or 1.
        if (x/i) == int:
            primes.append()
        else:
            pass


    print(primes)

get_prime_factors()
"""
## Gave up. Printed "[]" and nothing more.

##### ##### Instructor's Solution
def get_prime_factors(number):
    factors = []
    divisor = 2
    while divisor <= number:
        if number % divisor == 0:
            factors.append(divisor)
            number == number // divisor
        else:
            divisor += 1
    return factors