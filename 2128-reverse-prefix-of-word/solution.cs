public class Solution {
    public string ReversePrefix(string word, char ch) {
        int index = word.IndexOf(ch);
        if (index == -1)
        {
            return word;
        }
        char[] segment = word.Substring(0, index + 1).ToCharArray();
        Array.Reverse(segment);
        string reversedWord = new string(segment) + word.Substring(index + 1);
        return reversedWord;
    }
}
