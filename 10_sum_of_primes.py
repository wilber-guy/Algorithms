# Project Euler # 10
# find the sum of all primes under 2 million
import  time
start_time = time.time()

def find_primes(num):
    """ Takes an argument and returns the sum of all primes under that number"""
    sum_primes = 0
    # count by 2 because all primes are odd other than 2
    for i in range(3, num +1, 2):
        #print('/// I ', i)
        for n in range(2, int((i**.5)+1)):
            #print('\\\\ N ',n)
            if i % n == 0 and i != n:
                #print(n,' is not prime')
                break
        else:
            #print(i,' is prime')
            sum_primes += i
            #prime_counter = i
    # here we add 2 because we counted only odd numbers to save time 
    # and 2 is the only even prime           
    print(sum_primes+2)
        
find_primes(2000000)

# rewritten utilizing Sieve of Eratosthenes algorithm from 276 BC
''' This algorithm uses a principle of primes, so it only has to check
numbers that are not divisible by numbers already calulated.
This is NOT my code, but I have it here to later come back to and recall
Here is a URL explaining Sieve of Eratosthenes
https://www.khanacademy.org/computing/computer-science/cryptography/comp-number-theory/v/sieve-of-eratosthenes-prime-adventure-part-4'''
# this code is about 10000 times faster than my method
maxval = 2000000
max_fac_base = int(round(maxval ** 0.5))
possible_factors = range(5, max_fac_base + 1, 2)
sieve = [True, True, False] * (maxval // 6)
for i, n in enumerate(possible_factors):
    print(i)
    print(n)
    if sieve[i]:
        print(i)
        sieve[n + i::n] = [False] * ((maxval // 6 * 3 - 1 - i) // n)

numbers = range(5, maxval + 1, 2)
primes = [2, 3] + [n for i, n in enumerate(numbers) if sieve[i]]
print(sum(primes))

stop_time = time.time()
total_time = stop_time - start_time
print(total_time)