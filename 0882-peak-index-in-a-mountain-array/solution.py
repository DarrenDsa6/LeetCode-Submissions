class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        start=0
        end = len(arr)-1
        while(start<=end):
            mid = (start+end)//2
            if(arr[mid-1]<arr[mid] and arr[mid]>arr[mid+1]):
                return mid
            elif(arr[mid-1]>arr[mid]):
                end=mid
            else:
                start=mid+1
        return start
        
