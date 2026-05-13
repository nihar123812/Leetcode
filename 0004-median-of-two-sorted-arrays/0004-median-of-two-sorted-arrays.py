class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums3= sorted(nums1+nums2)
        x = len(nums3)

        if x%2==1:
            return nums3[x//2]
        else:
            return (nums3[x//2-1]+nums3[x//2])/2