class Solution {
    public int findPeakElement(int[] nums) {
        int start = 0;
        int end = nums.length - 1;
        while(end >= start){
            int mid = (start + end) / 2;
            if(mid+1 < nums.length && nums[mid+1] > nums[mid]){
                start = mid + 1;
            }
            else if(mid-1 >= 0 && nums[mid-1] > nums[mid]){
                end = mid - 1;
            }
            else{
                return mid;
            }
        }
        return 1;
    }
}
