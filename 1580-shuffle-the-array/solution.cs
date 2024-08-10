public class Solution {
    public int[] Shuffle(int[] nums, int n) {
        int i = 0;
        int j = n;
        int index = 0;
        int[] newarr = new int[nums.Length];
        while (i<n){
            newarr[index++] = nums[i];
            newarr[index++] = nums[j];
            j+=1;
            i+=1;
        }
        return newarr;
    }
}
