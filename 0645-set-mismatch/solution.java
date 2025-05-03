class Solution {
    public int[] findErrorNums(int[] nums) {
        int i = 0;
        while(i<nums.length){
            if(nums[i] != nums[nums[i]-1]){
                swap(nums, i, nums[i]-1);
            }
            else{
                i++;
            }
        }
        int[] ans= {0,0};
        for( i = 0; i<nums.length;i++){
            if(nums[i] != i+1){
                ans[0] = nums[i];
                ans[1] = i+1;
            }
        }
        return ans;

    }

    static void swap(int[] nums,int i,int correct){
        int temp = nums[i];
        nums[i] = nums[correct];
        nums[correct] = temp;
    }
}
