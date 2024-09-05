class Solution(object):
    def canJump(self, nums):
        curMax=1
        for i in range(len(nums)-1):
            curMax-=1
            curMax=max(curMax, nums[i])
            if curMax-1<0:
                return False
        return True
        