# 1, 5, 10, 20, 100
denominations = [100, 20, 10, 5, 1]

n = int(input())
total = 0
index_den = 0
rest = 0
while index_den < len(denominations):
    
    if denominations[index_den] <= n:
        total += int(n/denominations[index_den]) 
        rest =  n -int(n / denominations[index_den])*denominations[index_den]
        n = rest
        index_den += 1
    else: 
        index_den += 1
    
print(total)







   
