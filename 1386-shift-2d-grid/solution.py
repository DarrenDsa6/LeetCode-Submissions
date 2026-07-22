from typing import List

class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m, n = len(grid), len(grid[0])
        total = m * n
        
        # Flatten grid
        flat = [grid[i][j] for i in range(m) for j in range(n)]
        
        # Shift using modulo
        k %= total
        flat = flat[-k:] + flat[:-k]
        
        # Reshape back to 2D
        ans = []
        for i in range(m):
            ans.append(flat[i*n:(i+1)*n])
        return ans

