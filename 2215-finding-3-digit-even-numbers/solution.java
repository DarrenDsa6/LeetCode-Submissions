public class Solution {
    public int[] findEvenNumbers(int[] digits) {
        Set<Integer> uniqueNumbers = new TreeSet<>();  
        for (int i = 0; i < digits.length; i++) {
            if (digits[i] == 0) continue;  
            for (int j = 0; j < digits.length; j++) {
                if (i == j) continue;  
                for (int k = 0; k < digits.length; k++) {
                    if (i == k || j == k) continue;  
                    if (digits[k] % 2 == 0) { 
                        int num = digits[i] * 100 + digits[j] * 10 + digits[k];
                        uniqueNumbers.add(num);
                    }
                }
            }
        }
        return uniqueNumbers.stream().mapToInt(Integer::intValue).toArray();
    }
}

