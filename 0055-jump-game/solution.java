class Solution {
    public boolean canJump(int[] nums) {
        int n = nums.length;
        boolean[] ans = new boolean[n];
        ans[n - 1] = true;

        for (int i = n - 2; i >= 0; i--) {
            int maxJump = Math.min(i + nums[i], n - 1);
            for (int j = i + 1; j <= maxJump; j++) {
                if (ans[j]) {
                    ans[i] = true;
                    break;
                }
            }
        }

        return ans[0];
    }
}

