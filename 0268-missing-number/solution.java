class Solution {
    public int missingNumber(int[] nums) {
        int numsLen = nums.length;
        int totalSum= numsLen*(numsLen+1)/2;
        int sum = 0;
        for(int num: nums){
            sum += num;
        }
        return (totalSum - sum);
    }
}
