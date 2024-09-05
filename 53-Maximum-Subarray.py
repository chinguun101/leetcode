class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        curSum=0
        maxSum=nums[0]
        for n in nums:
            curSum=max(n,curSum+n)
            maxSum=max(maxSum, curSum)
        return maxSum