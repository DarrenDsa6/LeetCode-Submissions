public class Solution {
    public int MostWordsFound(string[] sentences) {
        int max = 0;
        foreach(string sentence in sentences){
            string[] count = sentence.Split(" ");
            max = (max > count.Length)? max : count.Length;
        }
        return max;
    }
}
