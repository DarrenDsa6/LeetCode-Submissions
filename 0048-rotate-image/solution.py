class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        rows = len(matrix)
        for i in range(rows):
            for j in range(i+1, rows):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        for i in range(rows):
            j, k = 0, rows-1
            while j<k:
                matrix[i][j], matrix[i][k] = matrix[i][k], matrix[i][j]
                j+=1
                k-=1
        return matrix
        
