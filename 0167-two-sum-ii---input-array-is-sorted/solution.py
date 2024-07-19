class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        k = len(numbers) - 1
        j = 0
        if k==-1:
            return k
        while j<k:
            sum = numbers[j] + numbers[k]
            if sum==target:
                return [j+1, k+1]
            elif sum>target:
                k -= 1
            else:
                j+=1
        return -1
