class Solution:
    
    def merge(nums1: list[int], m: int, nums2: list[int], n:int):
        
        """
            This function merge two non-decreasing orders arrays
            Don´t return anything modify nums1 in-place instead
        """
        
        
        # First delete the zeroes
        
        nums1 = [i for i in nums1 if i != 0]
        nums2 = [i for i in nums2 if i != 0]
        
        
        # Find ocurrencies of each number in the arrays
        numbers = {}
        
        for i in nums1:
            if i in numbers:
                numbers[i] +=1
            else:
                numbers[i] = 1
                
        for i in nums2:
            if i in numbers:
                numbers[i] += 1
            else:
                numbers[i] = 1
                
        # Trash all
        
        nums1 = []
        
        # Add the numbers in nums1 in decreasing order
        for key, value in numbers.items():
            nums1.extend([key]*value)
            
    
    def mergeWithPointers(nums1: list[int], m: int, nums2: list[int], n:int):
        
        last = m + n - 1
         
        while m > 0 and n > 0:
            if nums1[m-1] > nums2[n-1]:
                nums1[last] = nums1[m-1]
                m -= 1
            else:
                nums1[last] = nums2[n-1]
                n -= 1
            last -= 1

        while n > 0 :
            nums1[last] = nums2[n-1]
            n -=1
            last -=1
        
        print(nums1)
        
        
    
        
        
        
        
        
                
                    
            
    
    
    
        
        
        
    
solve = Solution.mergeWithPointers([1,2,3,0,0,0], 3, [2,5,6], 3)


