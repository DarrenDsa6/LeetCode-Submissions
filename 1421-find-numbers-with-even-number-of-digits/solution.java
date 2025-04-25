class Solution {
    public int findNumbers(int[] nums) {
        int num = 0;
        for(int i=0; i< nums.length; i++){
            int count=0;
            while(nums[i] > 0){
                count +=1;
                nums[i]/=10;
            }
            if(count%2==0){
                num +=1;
            }
        }
        return num;
    }
}
