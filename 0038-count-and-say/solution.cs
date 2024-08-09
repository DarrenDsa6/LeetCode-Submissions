public class Solution {
    public string CountAndSay(int n) {
        if (n == 1) return "1";
        StringBuilder answer = new StringBuilder("1");
        for (int count = 1; count < n; count++) {
            StringBuilder nextSequence = new StringBuilder();
            char currentChar = answer[0];
            int currentCount = 0;
            foreach (char ch in answer.ToString()) {
                if (ch == currentChar) {
                    currentCount++;
                } else {
                    nextSequence.Append(currentCount).Append(currentChar);
                    currentChar = ch;
                    currentCount = 1;
                }
            }
            nextSequence.Append(currentCount).Append(currentChar);
            answer = nextSequence;
        }
        return answer.ToString();
    }
}

