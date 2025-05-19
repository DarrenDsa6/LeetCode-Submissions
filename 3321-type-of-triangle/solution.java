class Solution {
    public String triangleType(int[] nums) {
        // First, check if the three sides can form a valid triangle
        if (nums[0] + nums[1] <= nums[2] || nums[1] + nums[2] <= nums[0] || nums[0] + nums[2] <= nums[1]) {
            return "none"; // Not a valid triangle
        }

        // Now, classify the triangle type
        if (nums[0] == nums[1] && nums[1] == nums[2]) {
            return "equilateral";
        }
        if (nums[0] == nums[1] || nums[1] == nums[2] || nums[0] == nums[2]) {
            return "isosceles";
        }
        return "scalene"; // If no sides are equal, it's scalene
    }
}

