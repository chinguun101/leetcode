class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        nums=candidates
        comb=[]
        res=[]
        #nums=sorted(nums)
        def dfs(i):
            if sum(comb)==target:
                res.append(list(comb))
                return
            elif sum(comb)>target:
                return

            for j in range(i,len(nums)):
                comb.append(nums[j])
                dfs(j)
                comb.pop()

        dfs(0)
        return res