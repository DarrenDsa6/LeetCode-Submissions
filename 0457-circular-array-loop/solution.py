class Solution:
    def circularArrayLoop(self, nums: List[int]) -> bool:
        length = len(nums)

        def nextIndex(currIndex, isPos):
            nextIndex = (currIndex + nums[currIndex])%length
            if (isPos and nums[nextIndex]<0) or (not isPos and nums[nextIndex] >0) or nums[nextIndex] == 0:
                return -1

            return nextIndex

        for i in range(length):
            slow, fast = i, i
            if nums[i] == 0:
                continue
            isPos = True if nums[i]>0 else False
            while(True):
                slow = nextIndex(slow, isPos)
                fast = nextIndex(fast, isPos)
                if slow==-1 or fast==-1:
                    break
                fast = nextIndex(fast, isPos)
                if fast==-1:
                    break
                if slow == fast:
                    if slow == nextIndex(slow, isPos):
                        break
                    return True
        return False
        
        
