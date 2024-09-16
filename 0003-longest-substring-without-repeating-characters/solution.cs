using System;
using System.Collections.Generic;

public class Solution {
    public int LengthOfLongestSubstring(string s) {
        if (s.Length == 0) return 0;

        HashSet<char> set = new HashSet<char>();  // To track unique characters
        int left = 0, right = 0, maxLen = 0;
        while (right < s.Length) {
            if (!set.Contains(s[right])) {
                set.Add(s[right]);
                right++;
                maxLen = Math.Max(maxLen, right - left);
            } else {
                set.Remove(s[left]);
                left++;
            }
        }

        return maxLen;
    }
}

