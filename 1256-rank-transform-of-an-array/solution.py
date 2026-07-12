class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        # Step 1: Get all unique numbers and sort them
        unique_sorted = sorted(set(arr))
        
        # Step 2: Assign ranks starting from 1
        # Example: [10, 20, 30] → {10:1, 20:2, 30:3}
        rank_map = {}
        for i, num in enumerate(unique_sorted):
            rank_map[num] = i + 1
        
        # Step 3: Replace each number in arr with its rank
        result = []
        for num in arr:
            result.append(rank_map[num])
        
        return result

