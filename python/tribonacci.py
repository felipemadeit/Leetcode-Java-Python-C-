# 0, 1, 1, 2, 4, 7, 13, 24, 44, 81, 149,

n = int(input())

if n > 0 :

    first = [0,1,1]

    for i in range(n):
        
        first.append(sum(first[-3:]))

    print(first[n])
elif n < 0:
    print("Incorrect input")

elif n == 0:
    print(0)