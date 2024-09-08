class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res=[]
        comb=[]
        nums=sorted(nums)
        def dfs(i):
            if i>=len(nums):
                res.append(list(comb))
                return

            comb.append(nums[i])
            dfs(i+1)
            comb.pop()

            while i<len(nums)-1 and nums[i]==nums[i+1]:
                i+=1
            dfs(i+1)
        dfs(0)
        return res

        