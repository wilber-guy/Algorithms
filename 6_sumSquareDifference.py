sumOfSquare = 0
Sum = 0

for i in range(0,101):
    sumOfSquare += i*i
    Sum += i

print(abs(sumOfSquare - (Sum*Sum)))


