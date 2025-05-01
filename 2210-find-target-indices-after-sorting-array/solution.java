import java.util.List;
import java.util.ArrayList;

class Solution {
    public List<Integer> targetIndices(int[] nums, int target) {
        int smallerCount = 0;
        boolean targetExists = false;
        int largerCount = 0;

        for (int num : nums) {
            if (num < target) {
                smallerCount++;
            } else if (num > target) {
                largerCount++;
            }
            if (num == target) {
                targetExists = true;
            }
        }

        List<Integer> result = new ArrayList<>();
        if (targetExists) {
            while (smallerCount + largerCount <= nums.length - 1) {
                result.add(smallerCount++);
            }
        }
        return result;
    }
}

