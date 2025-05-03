class Solution {
    public int findDuplicate(int[] nums) {
        int i = 0;
        int len = nums.length;
        while(i<len){
            if(nums[i]!= i+1){
                if(nums[i] == nums[nums[i]-1]){
                    return nums[i];
                }
                int temp = nums[i];
                nums[i] = nums[temp - 1];
                nums[temp - 1] = temp;
            }
            else{
                i++;
            }
        }
        return -1;
    }
}
