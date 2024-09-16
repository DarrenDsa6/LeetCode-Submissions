public class Solution {
    public int Trap(int[] height) {
        int trapped = 0;
        int l = 0;
        int r = height.Length -1;
        int lmax = height[l];
        int rmax = height[r];
        while(l<r){
            if (lmax < rmax){
                l +=1;
                lmax = Math.Max(lmax, height[l]);
                trapped += lmax - height[l];
            }
            else{
                r -=1;
                rmax = Math.Max(rmax, height[r]);
                trapped += rmax - height[r];
            }
        }
        return trapped;
    }
}
