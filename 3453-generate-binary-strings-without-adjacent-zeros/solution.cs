public class Solution 
{
    public IList<string> ValidStrings(int n) 
    {
        List<string> result = new List<string>();
        StringBuilder sb = new StringBuilder();
        void Backtrack(int index)
        {
            if (index == n) { result.Add(sb.ToString()); return; }
            char last = '1';
            if (sb.Length > 0) { last = sb[sb.Length - 1]; }
            sb.Append('1');
            Backtrack(index + 1);
            sb.Remove(index, 1);
            if (last == '1')
            {
                sb.Append('0');
                Backtrack(index + 1);
                sb.Remove(index, 1);
            }
        }
        Backtrack(0);
        return result;
    }
}
