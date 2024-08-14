class Solution:
    def romanToInt(s: str):
        
        values = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }
        
        final_value = 0
        prev_value = 0
        
        for i in range(len(s)-1, -1, -1):
            current_value = values[s[i]]
            if current_value < prev_value:
                final_value -= values[s[i]]
            else:
                final_value += current_value
            prev_value = current_value
        
        print(final_value)
                
            
        
    
solve = Solution.romanToInt(input())