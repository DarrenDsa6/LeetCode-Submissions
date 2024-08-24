public class Solution {
    public int CountMatches(IList<IList<string>> items, string ruleKey, string ruleValue) {
        int count = 0;
        int index = 0;
        if (ruleKey == "color"){
            index = 1;
        }
        else if(ruleKey == "type"){
            index = 0;
        }
        else{
            index = 2;
        }
        foreach(IList<string> list in items){
            if (list[index] == ruleValue){
                count +=1;
            }
        }
        return count;
    }
}
