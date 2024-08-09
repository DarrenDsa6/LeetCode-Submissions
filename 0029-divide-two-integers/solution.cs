public class Solution {
    public int Divide(int dividend, int divisor) {
        if (divisor == 0) {
            throw new DivideByZeroException("Divisor cannot be zero.");
        }
        if (dividend == int.MinValue && divisor == -1) {
            return int.MaxValue;
        }
        bool isNegative = (dividend < 0) ^ (divisor < 0);
        long absDividend = Math.Abs((long)dividend);
        long absDivisor = Math.Abs((long)divisor);
        int quotient = 0;
        while (absDividend >= absDivisor) {
            long tempDivisor = absDivisor, multiple = 1;
            while (absDividend >= (tempDivisor << 1)) {
                tempDivisor <<= 1;
                multiple <<= 1;
            }
            absDividend -= tempDivisor;
            quotient += (int)multiple;
        }

        return isNegative ? -quotient : quotient;
    }
}

