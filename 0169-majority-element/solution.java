class Solution {
    public int majorityElement(int[] nums) {
        Map<Integer, Integer> myMap = new HashMap<>();
        for(int num: nums){
            myMap.put(num, myMap.getOrDefault(num, 0) + 1);
        }
        for (Map.Entry<Integer, Integer> entry : myMap.entrySet()) {
            if (entry.getValue() > nums.length/2) {
                return entry.getKey();
            }
        }
        return -1;
    }
}
