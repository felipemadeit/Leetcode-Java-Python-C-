class Solution:
    
     def lengthOfLastWord(s: str):
         
        
        reversed_s = s[::-1].strip()
        
        counter = 0
        
        for letter in reversed_s:
            if letter != ' ':
                counter += 1
            else:
                break
        
        return counter
            
            
                
        
            
            

solve = Solution.lengthOfLastWord("luffy is still joyboy")
            
                
             
            