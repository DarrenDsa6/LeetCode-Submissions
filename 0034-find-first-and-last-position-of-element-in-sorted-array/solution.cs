public class Solution {
    public int[] SearchRange(int[] nums, int target) {
        if (nums.Length==0){
            return [-1,-1];
        }
        int count = 0;
        int index = -1;
        int[] answer = new int[]{-1,-1};
        for (int i=0;i<nums.Length;i++){
            if (nums[i]==target){
                count +=1;
                index = i;
                if(count==1){
                    answer[0] = i;
                }
            }
        }
        if (count==0){
            return [-1,-1];
        }
        if (count>1){
            answer[1] = index;
        }
        else{
            answer[1] = answer[0];
        }
        return answer;
    }
}
