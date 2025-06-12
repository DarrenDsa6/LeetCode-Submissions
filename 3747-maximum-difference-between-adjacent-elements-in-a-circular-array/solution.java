class Solution {
    public int maxAdjacentDistance(int[] nums) {
        int length = nums.length;
        int max = Math.abs(nums[length-1] - nums[0]);
        for(int i = 1; i<length; i++){
            if(Math.abs(nums[i]-nums[i-1]) > max){
                max = Math.abs(nums[i]-nums[i-1]);
            }
        }
        return max;
    }
}
