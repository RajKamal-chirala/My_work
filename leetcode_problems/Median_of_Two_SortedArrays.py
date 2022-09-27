class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums=nums1+nums2
        n=len(nums)
        nums.sort()
        half=n//2
        if n%2 == 0:
            sum=(nums[half-1] + nums[half])
            median=sum/2
        else: 
            median=nums[half]
        return median
        
