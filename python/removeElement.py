class Solution:
    def removeElement(nums: list[int], val:int):
        
        pointerR = 0

        for i in range(len(nums)):
            if nums[i] != val:
                nums[pointerR] = nums[i]
                pointerR +=1
        
        print(nums)
        return pointerR
            
        
        
        
solve = Solution.removeElement([0,1,2,2,3,0,4,2], 2)
        
        