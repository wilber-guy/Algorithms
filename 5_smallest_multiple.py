import sys

solved = 0
num = 20

while solved == 0:
    count = 0
    
    for i in range(1,21):
        if num % i == 0:
            count += 1
            if count == 20:
                print(num)
                solved = 1
        else:
            break
        
              
    num += 2
