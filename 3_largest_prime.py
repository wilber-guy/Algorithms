# largest prime factors
import math

num = 600851475143
largest_prime = 0
for i in range(1, int((math.sqrt(num)+1))):
    if num % i == 0:
        #print('//',i)
        for p in range(2, int(math.sqrt(i)+2)):
            #print(int(math.sqrt(i)+1))
            if i % p != 0:
                #print('---',p)
                if (p) > math.sqrt(i):
                    largest_prime = i
            else:
                #print('????')
                break
            
print('largest prime is: ',largest_prime)
