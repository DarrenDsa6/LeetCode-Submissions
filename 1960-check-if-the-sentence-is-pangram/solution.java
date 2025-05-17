class Solution {
    public boolean checkIfPangram(String sentence) {
        int[] count = new int[26];
        for(int i=0; i<sentence.length(); i++){
            int ascii = (int)sentence.charAt(i);
            count[ascii - 97] += 1;
        }
        for(int i=0; i<26;i++){
            if(count[i]==0){
                return false;
            }
        }
        return true;
    }
}
