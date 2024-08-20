public class Solution
{
    public int MinOperations(int[] nums, int k)
    {
        Array.Sort(nums);
        int operations = 0;
        foreach (int num in nums)
        {
            if (num >= k)
            {
                break; 
            }
            operations++; 
        }

        return operations;
    }
}
