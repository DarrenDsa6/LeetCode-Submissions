class Solution:
    def hIndex(self, citations: List[int]) -> int:
        start, end = 0, len(citations) - 1
        ans = 0
        while start <= end:
            mid = (start + end) // 2
            papers = len(citations) - mid
            if citations[mid] >= papers:
                ans = papers 
                end = mid - 1  # try for larger h by moving left
            else:
                start = mid + 1
        return ans

