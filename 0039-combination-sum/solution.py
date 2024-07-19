class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        def backtracking(start, path, target):
            if target == 0:
                ans.append(path)
                return
            if target < 0:
                return
            for i in range(start, length):
                backtracking(i, path +[candidates[i]], target - candidates[i])
        ans = []
        length = len(candidates)
        backtracking(0, [], target)
        return ans


