public class Solution {
    public int MinEatingSpeed(int[] piles, int h) {
        int l = 1, r = piles.Max();
        int minK = l;
        while(l <= r){
            int m = l + (r - l) / 2;
            long currTime = 0;
            foreach(int p in piles){
                currTime += (int)Math.Ceiling((double)p / m);
            }
            if(currTime <= h){
                minK = m;
                r = --m;
            }
            else{
                l = ++m; 
            }
        }
        
        return minK;
    }
}
