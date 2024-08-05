public class Solution {
    public string KthDistinct(string[] arr, int k) {
        Dictionary<string, int> countMap = new Dictionary<string,int>();
        foreach(string str in arr){
            if (countMap.ContainsKey(str)){
                countMap[str]++;
            }
            else{
                countMap[str] = 1;
            }
        }
        List<string> distinctString = new List<string>();
        foreach (string str in arr) {
            if (countMap[str] == 1){
                distinctString.Add(str);
            }
        }
        if (k<=distinctString.Count && k>0){
            return distinctString[k-1];
        }
        else{
            return "";
        }
    }
}
