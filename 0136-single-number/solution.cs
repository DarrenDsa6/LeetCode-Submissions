public class Solution {
    public int SingleNumber(int[] nums) {
        Dictionary<int, int> myDictionary = new Dictionary<int, int>();
        foreach( int i in nums){
             if (myDictionary.ContainsKey(i)) {
                myDictionary[i]++;
            } else {
                myDictionary[i] = 1;
            }
         }
        foreach (var kvp in myDictionary)
        {
            if(kvp.Value == 1)
            {
                return kvp.Key;
            }
        }
        return 0;
    }
}
