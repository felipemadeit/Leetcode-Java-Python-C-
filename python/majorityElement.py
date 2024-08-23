class Solution:
    
    def majorityElement(nums: list[int]):
        
        n = len(nums) /2
        non_repeat_nums = {}
        
        for i in nums:
            if i not in non_repeat_nums:
                non_repeat_nums[i] = 1
            else:
                non_repeat_nums[i] += 1
        
        for i in non_repeat_nums:
            if non_repeat_nums[i] > n:
                return i
        
        
        
      
        
            
            
solve = Solution.majorityElement([2,2,1,1,1,2,2])