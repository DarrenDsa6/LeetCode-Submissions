import java.util.List;

class Solution {
    public int countMatches(List<List<String>> items, String ruleKey, String ruleValue) {
        int count = 0;
        for (List<String> item : items) {
            if (("type".equals(ruleKey) && item.get(0).equals(ruleValue)) ||
                ("color".equals(ruleKey) && item.get(1).equals(ruleValue)) ||
                ("name".equals(ruleKey) && item.get(2).equals(ruleValue))) {
                count++;
            }
        }
        return count;
    }
}

