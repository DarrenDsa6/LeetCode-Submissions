public class Solution {
    public int[] ProductExceptSelf(int[] nums) {
        int[] ans = new int[nums.Length];
        int prefix = 1;
        int suffix = 1;
        int length = nums.Length;
        for(int i=0;i<length;i++){
            ans[i] = prefix;
            prefix *= nums[i];
        }
        for(int i =length-1;i>=0;i--){
            ans[i] *= suffix;
            suffix *= nums[i];
        }
        return ans;
    }
}
