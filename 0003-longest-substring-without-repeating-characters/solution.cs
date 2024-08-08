public class Solution {
    public int LengthOfLongestSubstring(string s) {
        int n = s.Length;
        if (n == 0) return 0;
        HashSet<char> charSet = new HashSet<char>();
        int left = 0;
        int maxLength = 0;
        for (int right = 0; right < n; right++) {
            while (charSet.Contains(s[right])) {
                charSet.Remove(s[left]);
                left++;
            }
            charSet.Add(s[right]);
            maxLength = Math.Max(maxLength, right - left + 1);
        }
        return maxLength;
    }
}

