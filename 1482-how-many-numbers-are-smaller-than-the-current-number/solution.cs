public class Solution {
    public int[] SmallerNumbersThanCurrent(int[] nums) {
        int[] answer = new int[nums.Length];
        for(int i=0;i<nums.Length;i++){
            int count = 0;
            for(int j=0;j<nums.Length;j++){
                if (i!= j){
                    if (nums[i]>nums[j]){
                        count+=1;
                    }
                }
            }
            answer[i] = count;
        }
        return answer;
    }
}
