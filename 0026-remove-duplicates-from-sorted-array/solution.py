class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        seen = set()
        unique = []
        for num in nums:
            if num not in seen:
                unique.append(num)
                seen.add(num)
        # Update the original list
        nums[:len(unique)] = unique
        # Return the length of the unique elements
        return len(unique)
