class Solution:
    def merge(self, arr: List[List[int]]) -> List[List[int]]:
        arr.sort()
        res = []
        start = arr[0][0]
        end = arr[0][1]
        for i in range(1, len(arr)):
            if end < arr[i][0]:
                res.append([start, end])
                start = arr[i][0]
                end = arr[i][1]
            end = max(end, arr[i][1])
        res.append([start,end])
        return res
