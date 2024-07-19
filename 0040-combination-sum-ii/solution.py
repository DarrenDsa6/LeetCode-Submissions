class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        def backtracking(start, path, target):
            if target == 0:
                ans.append(path)
                return
            if target < 0:
                return
            for i in range(start, length):
                if i > start and candidates[i] == candidates[i - 1]:
                    continue
                backtracking(i+1, path + [candidates[i]], target - candidates[i])
        ans = []
        candidates.sort()
        length = len(candidates)
        backtracking(0 , [], target)
        return ans
