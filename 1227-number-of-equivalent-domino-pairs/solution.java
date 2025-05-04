import java.util.HashMap;
import java.util.Arrays;

class Solution {
    public int numEquivDominoPairs(int[][] dominoes) {
        HashMap<String, Integer> dictArray = new HashMap<>();
        int count = 0;
        for (int[] domino : dominoes) {
            Arrays.sort(domino);
            String key = Arrays.toString(domino);
            count += dictArray.getOrDefault(key, 0);
            dictArray.put(key, dictArray.getOrDefault(key, 0) + 1);
        }

        return count;
    }
}

