class Solution:
    def maximumSum(self, arr: List[int]) -> int:
        n = len(arr)
        noDel = arr[0]          # max sum ending here without deletion
        oneDel = float('-inf')  # max sum ending here with one deletion
        ans = arr[0]

        for i in range(1, n):
            oneDel = max(noDel, oneDel + arr[i])   # delete current OR extend oneDel
            noDel = max(arr[i], noDel + arr[i])    # extend or restart
            ans = max(ans, noDel, oneDel)

        return ans

