#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul 29 22:16:21 2018

@author: bud-guy
"""
'''
Problem 20 Factorial digit sums

n! means n × (n − 1) × ... × 3 × 2 × 1

For example, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800,
and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.

Find the sum of the digits in the number 100!
'''
num = 1

for i in range(1,101):
    num = num * i

print(num)
num = str(num)
final = 0
for let in num:
    final += int(let)
    
print(final)