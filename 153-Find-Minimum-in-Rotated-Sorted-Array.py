class Solution(object):
    def findMin(self, nums):
        \\\
        :type nums: List[int]
        :rtype: int
        \\\
        res=nums[-1]
        if nums[0]<nums[-1]:
            return nums[0]
        l, r= 0, len(nums)-1
        while l<r:
            mid=(l+r)//2
            if nums[mid]>nums[-1]:
                l=mid+1
            if nums[mid]<nums[-1]:
                res=nums[mid]
                r=mid
        return res