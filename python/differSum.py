import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

n = int(input())
for i in range(n):
    x = int(input())
    str(x)
    total_x = 0 
    for i in str(x):
        total_x += int(i)
    
    searched = True
    nums = {}
    total_x = str(total_x)
    for i in total_x:
        if i not in nums:
            nums[i] = 1
        else:
            searched = False
    
    print(searched)
    
    
    

        
    
            
    



