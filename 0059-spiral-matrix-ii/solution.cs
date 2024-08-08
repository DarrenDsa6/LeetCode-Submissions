public class Solution {
    public int[][] GenerateMatrix(int n) {
        int number = 1;
        int[,] spiral_mat = new int[n, n];
        int top = 0; 
        int bottom = n - 1;
        int left = 0; 
        int right = n - 1;
        while (top <= bottom && left <= right) {
            for (int i = left; i <= right; i++) {
                spiral_mat[top, i] = number++;
            }
            top++;
            for (int i = top; i <= bottom; i++) {
                spiral_mat[i, right] = number++;
            }
            right--; 
            if (top <= bottom) {
                for (int i = right; i >= left; i--) {
                    spiral_mat[bottom, i] = number++;
                }
                bottom--; 
            }
            if (left <= right) {
                for (int i = bottom; i >= top; i--) {
                    spiral_mat[i, left] = number++;
                }
                left++;
            }
        }
        int[][] jaggedArray = new int[n][];
        for (int i = 0; i < n; i++) {
            jaggedArray[i] = new int[n];
            for (int j = 0; j < n; j++) {
                jaggedArray[i][j] = spiral_mat[i, j];
            }
        }
        return jaggedArray;
    }
}

