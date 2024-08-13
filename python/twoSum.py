def twoSum (nums: list[int], target:int):
    """This function search the index of the two values that their sum is equal to a target

    Args:
        nums (list[int]): Array of nums
        target (int): Target
    """

    for i in range(len(nums)-1):
        if nums[i] + nums[i+1] == target:
            return([i, i+1])
            


print(twoSum(nums = [int(x) for x in input().split()], target= int(input())))
    