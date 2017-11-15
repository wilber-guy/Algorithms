largest_num = 0

for i in range(1,1000):
    num = i
    for p in range(1,1000):
        total = num * p
        if total > largest_num:
            if str(total) == str(total)[::-1]:
                largest_num = total
        
print(largest_num)
