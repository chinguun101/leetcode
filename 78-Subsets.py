class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        subset=[]
        res=[]
        def helper(i):
            if i >= len(nums):
                res.append(list(subset))
                return

            subset.append(nums[i])
            helper(i+1)
            subset.pop()
            helper(i+1)

        helper(0)
        return res