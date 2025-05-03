import java.util.Arrays;

class Solution {
    public void merge(int[] nums1, int m, int[] nums2, int n) {
        int i = m - 1; // Pointer for nums1 (last valid element)
        int j = n - 1; // Pointer for nums2 (last element)
        int k = m + n - 1; // Pointer for merged array (last position)

        // Merge from the back to avoid extra space
        while (i >= 0 && j >= 0) {
            if (nums1[i] > nums2[j]) {
                nums1[k--] = nums1[i--];
            } else {
                nums1[k--] = nums2[j--];
            }
        }

        // If nums2 still has elements left, add them
        while (j >= 0) {
            nums1[k--] = nums2[j--];
        }
    }
}

