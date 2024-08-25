public class Solution {
    public int[] MinOperations(string boxes) {
        int i = 0;
        int length = boxes.Length;
        if (length==0){
            return [];
        }
        int[] answer = new int[length];
        int j = 1;
        int count = 0;
        while (i<length){
            if (j==length){
                j = 0;
                answer[i] = count;
                i += 1;
                count = 0;
            }
            else{
                if (boxes[j] == '1'){
                    count += Math.Abs(i - j);
                }
                j += 1;
            }
        }
        return answer;
    }
}
