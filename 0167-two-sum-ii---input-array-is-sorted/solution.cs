public class Solution {
    public int[] TwoSum(int[] numbers, int target) {
        Dictionary<int, int> numIndex = new Dictionary<int, int>();
        for(int i=0; i<numbers.Length; i++){
            if (numIndex.ContainsKey(target-numbers[i])){
                return [numIndex[target-numbers[i]]+1, i+1];
            }
            else{
                numIndex[numbers[i]] = i;
            }
        }
        return [];
    }
}
