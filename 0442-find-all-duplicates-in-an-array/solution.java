import java.util.ArrayList;
import java.util.List;

class Solution {
    public List<Integer> findDuplicates(int[] nums) {
        int i = 0;
        List<Integer> answer = new ArrayList<>();

        while (i < nums.length) {
            if (nums[i] != nums[nums[i] - 1]) {
                swap(nums, i, nums[i] - 1);
            } else {
                i++;
            }
        }

        // Collect duplicates after sorting
        for (i = 0; i < nums.length; i++) {
            if (nums[i] != i + 1 && !answer.contains(nums[i])) {
                answer.add(nums[i]);
            }
        }

        return answer;
    }

    private void swap(int[] nums, int i, int correctIndex) {
        int temp = nums[i];
        nums[i] = nums[correctIndex];
        nums[correctIndex] = temp;
    }
}

