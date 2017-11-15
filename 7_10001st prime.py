import math
import sys

primes = []

def find_primes(x):
    """ Takes a number and calulates if that number is equal to 
    zero when divided by numbers up to the square root of this number, 
    since the sqrt is the highest number possible to be a"""
    global primes
    n = x // 2
    for i in range(2, n + 1):
        if x % i == 0:
            return False
    if primes.count(x) == 0:
        primes.append(x)
    if len(primes) > 10000:
        print('Calulation complete, number: ', primes[-1])
        sys.exit()

def display(X):
    for i in range(2, X):
        find_primes(i)

display(10000000)

