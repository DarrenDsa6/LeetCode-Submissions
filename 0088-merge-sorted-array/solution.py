class Solution(object):
    def merge(self, nums1, m, nums2, n):
        j=0
        for i in range(m,m+n):
            nums1[i]=nums2[j]
            j+=1
        n=len(nums1)
        if n<=1:
            return nums1
        for i in range(1,n):
            key=nums1[i]
            j=i-1
            while j>=0 and key<nums1[j]:
                nums1[j+1]=nums1[j]
                j-=1
            nums1[j+1]=key
        return nums1
            
