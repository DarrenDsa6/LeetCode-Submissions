class Solution {
    public int fib(int n) {
        if (n == 0) return 0;
        if (n == 1) return 1;

        int prev = 0, last = 1;
        for (int i = 2; i <= n; i++) {
            int temp = last;
            last = prev + last;
            prev = temp;
        }
        return last;
    }
}

