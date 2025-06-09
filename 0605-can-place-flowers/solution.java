class Solution {
    public boolean canPlaceFlowers(int[] flowerbed, int n) {
        int count = 0;
        for (int i = 0; i < flowerbed.length; i++) {
            if (flowerbed[i] == 0 && 
                (i == 0 || flowerbed[i - 1] == 0) && 
                (i == flowerbed.length - 1 || flowerbed[i + 1] == 0)) {
                
                flowerbed[i] = 1;  // Plant the flower
                count++;           // Increase the count
                
                if (count >= n) return true;  // If enough flowers planted, return true
            }
        }
        return count >= n;
    }
}

