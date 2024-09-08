class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        def helper(i):
            if i==len(nums):
                return [[]]
            res=[]
            per=helper(i+1)
            for p in per:
                for j in range(1+len(p)):
                    pcopy=list(p)
                    pcopy.insert(j,nums[i])
                    res.append(pcopy)
            return res
        return helper(0)

        