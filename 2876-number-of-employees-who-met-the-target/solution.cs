public class Solution {
    public int NumberOfEmployeesWhoMetTarget(int[] hours, int target) {
        int count = 0;
        foreach(int i in hours){
            if (i>=target){
                count+=1;
            }
        }
        return count;
    }
}
