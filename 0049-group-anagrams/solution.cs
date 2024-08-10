public class Solution {
    public IList<IList<string>> GroupAnagrams(string[] strs) {
        var anagrams = new Dictionary<string, List<string>>();
        foreach (var str in strs) {
            var count = new int[26];
            foreach (var ch in str) {
                count[ch - 'a']++;
            }
            var key = string.Join('#', count);
            if (!anagrams.ContainsKey(key)) {
                anagrams[key] = new List<string>();
            }
            anagrams[key].Add(str);
        }
        return anagrams.Values.Cast<IList<string>>().ToList();
    }
}

