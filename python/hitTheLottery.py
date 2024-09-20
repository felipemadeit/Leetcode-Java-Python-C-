# 1, 5, 10, 20, 100
denominations = [100, 20, 10, 5, 1]

n = int(input())

total = 0

position = 0

while total < n:
    if denominations[position] < n:
        position += denominations[position]
        if n % denominations[position] < denominations[position]:
            position += 1

print(total)        



   
