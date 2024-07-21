class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        merged = nums1 + nums2
        merged.sort()
        length = len(merged)
        if length % 2 == 1:
            return float(merged[length // 2])
        else:
            return (merged[length // 2 - 1] + merged[length // 2]) / 2.0
