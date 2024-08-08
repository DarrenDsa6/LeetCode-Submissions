using System;
using System.Collections.Generic;

public class Solution {
    public IList<IList<int>> PermuteUnique(int[] nums) {
        var result = new List<IList<int>>();
        var current = new List<int>();
        Array.Sort(nums);
        PermuteHelper(nums, current, new bool[nums.Length], result);
        return result;
    }
    private void PermuteHelper(int[] nums, List<int> current, bool[] used, IList<IList<int>> result) {
        if (current.Count == nums.Length) {
            result.Add(new List<int>(current)); 
            return;
        }

        for (int i = 0; i < nums.Length; i++) {
            if (used[i] || (i > 0 && nums[i] == nums[i - 1] && !used[i - 1])) {
                continue; 
            }
            current.Add(nums[i]);
            used[i] = true;
            PermuteHelper(nums, current, used, result);
            used[i] = false;
            current.RemoveAt(current.Count - 1);
        }
    }
}

