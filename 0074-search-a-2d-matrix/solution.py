class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        a=len(matrix)
        b=len(matrix[0])
        
        for i in range(0,a):
            if(target<matrix[i][b-1] or target==matrix[i][b-1]):
                for j in range(0,b):
                    if(target==matrix[i][j]):
                        return 1
                return 0
        
