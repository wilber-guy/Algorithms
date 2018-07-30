import math
import time

'''
the key to solving this is understanding what makes a pythagorean triplet
            a = n**2 - m**2
            b = 2*n*m
            c = n**2 + m**2
            where n > m

'''


def pythagorean_search(max_n, sum_of_nums):
    t = time.process_time()
    for i in range(max_n):
        for j in range(max_n):
            
            m = 1+i
            n = 2+j
            
            a = n**2 - m**2
            b = 2*n*m
            c = n**2 + m**2
            
            
            if a + b + c == sum_of_nums and a**2 + b**2 == c**2:
                print('found!', a,b,c,a*b*c)
                print('computed in ', time.process_time() - t)
                break

            
    print('finished running; ')


pythagorean_search(30, 1000)

