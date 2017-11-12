import time
"""Memoization uses already computed values to prevent doing the same
calculations many times. It stores these values in a dictionary, named cache here.
This reduces any need to do a calulation already preformed, try removing the
single line comments in the while loop to notice the imporved preformence.
 DOCUMENTATION FOR MEMOIZATOIN:
https://www.python-course.eu/python3_memoization.php """

t1 = time.time()

cache = {}

def collatz(n):
   count = 0
   start = n
   while n!=1:
      #if n in cache:
         #count += cache[n]
         #break
      if n%2==0: n/=2
      else: n = 3*n+1
      count += 1

   cache[start] = count
   return count


answer = max(((collatz(i),i) for i in range(1,1000001)))
print("The number generating the longest sequence is {} with a sequence of {} iterations".format(answer[1], answer[0]))
print(len(cache))
t2 = time.time()

total_time = t2 - t1
print(total_time)
