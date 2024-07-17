class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        rows = len(matrix)
        columns = len(matrix[0])
        transpose = [[0] * rows for _ in range(columns)]
        for i in range(rows):
            for j in range(columns):
                    transpose[j][i] = matrix[i][j] 
        return transpose
