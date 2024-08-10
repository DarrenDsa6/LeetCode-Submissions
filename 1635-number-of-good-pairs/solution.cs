public class Solution {
    public int NumIdenticalPairs(int[] nums) {
        int count = 0;
        for(int i = 0; i<nums.Length; i++){
            for (int j=0; j<i;j++){
                if (nums[i] == nums[j]){
                    count += 1;
                }
            }
        }
        return count;
    }
}
