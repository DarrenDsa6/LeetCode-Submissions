class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        n = len(matrix)
        low, high = matrix[0][0], matrix[n-1][n-1]

        while low <= high:
            mid = (low + high) // 2
            count = self.fun(matrix, mid)
            if count < k:
                low = mid + 1
            else:
                high = mid - 1
        return low

    def fun(self, matrix: List[List[int]], val: int) -> int:
        row, col = len(matrix)-1, 0
        count = 0
        while(row>=0 and col<=len(matrix[0])-1):
            if(matrix[row][col]<=val):
                count += row+1
                col+=1
            else:
                row-=1
        return count



