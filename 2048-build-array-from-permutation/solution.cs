public class Solution {
    public int[] BuildArray(int[] nums) {
        int[] answer = new int[nums.Length];
        for (int i = 0 ; i<nums.Length; i++){
            answer[i] = nums[nums[i]];
        }
        return answer;
    }
}
