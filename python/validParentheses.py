class Solution():
    def isValid(s: str):
        
        stack = []
        opening_chars = ['{', '[', '(']
        closing_chars = ['}', ']', ')']
        
        
        for i in s:
            if i in opening_chars:
                stack.append(i)
            else:
                if closing_chars.index(i)            
       
       
       
       

solution = Solution.isValid(input())