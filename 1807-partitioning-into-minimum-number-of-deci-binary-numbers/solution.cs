public class Solution {
    public int MinPartitions(string n) {
        if(n.Contains('9')){
            return 9;
        }
        else if (n.Contains('8')){
            return 8;
        }
        else if (n.Contains('7')){
            return 7;
        }
        else if (n.Contains('6')){
            return 6;
        }
        else if (n.Contains('5')){
            return 5;
        }else if (n.Contains('4')){
            return 4;
        }else if (n.Contains('3')){
            return 3;
        }
        else if (n.Contains('2')){
            return 2;
        }
        else if (n.Contains('1')){
            return 1;
        }
        else{
            return 0;
        }
    }
}
