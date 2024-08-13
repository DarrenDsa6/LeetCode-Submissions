public class Solution {
    public int[] LeftRightDifference(int[] nums) {
        int[] answer = new int[nums.Length];
        for(int i = 0;i<nums.Length;i++){
            int leftsum = 0;
            int rightsum = 0;
            for(int j=i-1; j>=0;j--){
                leftsum += nums[j];
            }
            for (int j=i+1;j<nums.Length;j++){
                rightsum += nums[j];
            }
            answer[i] = Math.Abs(leftsum-rightsum);
        }
        return answer;
    }
}
