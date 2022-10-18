class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        length = len(nums1) + len(nums2)
        
        a = nums1+nums2
        if len(a)<=10:
            a.sort()
        elif nums1[len(nums1)-1] > nums2[0]:
            a.sort()
        if length % 2 == 0:
            ans = length // 2
            i1 = ans - 1
            c = a[ans]+a[i1]
            return c / 2

        return a[length//2]/1