public class Solution {
    public int numberOfSteps(int num) {
        return rec(num, 0);
    }

    static int rec(int num, int count) {
        if(num == 0) {
            return count; 
        }

        if(num % 2 == 0) {
            return rec(num / 2, count + 1); 
        } else {
            return rec(num - 1, count + 1);  
        }
    }
}
