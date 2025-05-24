class Solution {
    public boolean isAnagram(String s, String t) {
        if (s.length() != t.length()) return false;

        int[] count = new int[26]; // Only 26 lowercase letters

        for (char c : s.toCharArray()) {
            count[c - 'a']++; // Increment count for s
        }

        for (char c : t.toCharArray()) {
            count[c - 'a']--; 
            if (count[c - 'a'] < 0) return false; 
        }

        return true;
    }
}

