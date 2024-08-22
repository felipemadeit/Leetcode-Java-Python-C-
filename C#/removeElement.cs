class Solution {

    int RemoveElement(int[] nums, int val) {

        int pointer;

        for (int i = 0; i < pointer.Length(); i++){
            if(nums[i] != val) {
                nums[pointer] = nums[i];
                pointer ++;
            }
        }    
    }
}