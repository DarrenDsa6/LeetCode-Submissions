import java.util.*;

class Solution {
    public boolean containsDuplicate(int[] nums) {
        Set<Integer> checkDuplicates = new HashSet<>();

        for (int num : nums) {
            if (!checkDuplicates.add(num)) { 
                return true;
            }
        }
        return false;
    }
}

