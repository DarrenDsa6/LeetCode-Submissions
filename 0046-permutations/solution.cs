public class Solution {
    public IList<IList<int>> Permute(int[] nums) {
        var result = new List<IList<int>>();
        var current = new List<int>();
        PermuteHelper(nums, current, result);
        return result;
    }
    private void PermuteHelper(int[] nums, List<int> current, IList<IList<int>> result) {
        if (current.Count == nums.Length) {
            result.Add(new List<int>(current));
            return;
        }
        foreach (var num in nums) {
            if (current.Contains(num)) continue; 
            current.Add(num);
            PermuteHelper(nums, current, result);
            current.RemoveAt(current.Count - 1); 
        }
    }
}

