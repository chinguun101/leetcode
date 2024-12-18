class Solution(object):
    def twoSum(self, nums, target):
        has={}
        for i in range(len(nums)):
            diff = target-nums[i]
            if diff in has:
                return [has[diff], i]
            else:
                has[nums[i]]=i