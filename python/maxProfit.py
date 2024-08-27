class Solution:
    def maxProfit(prices: list[int]):
        
        to_buy = prices[0]
        best_profit = 0
        
        for i in prices[1:]:
            
            if i < to_buy:
                to_buy = i
            elif best_profit < i - to_buy:
                best_profit = i - to_buy
        
        print(best_profit)
            
                
            
                
                
        
        
        
        
        
      
        
solve = Solution.maxProfit([2,4,1])
            
        
       
                
        
        
        