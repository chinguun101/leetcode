class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        res=[]
        comb=[]
        candidates.sort()
        def helper(i):
            if sum(comb)==target:
                res.append(list(comb))
                return
            if i == len(candidates) or sum(comb)>target:
                return
            
            comb.append(candidates[i])
            helper(i+1)
            comb.pop()
            while i<len(candidates)-1 and candidates[i]==candidates[i+1]:
                i+=1
            helper(i+1)

        helper(0)
        return res
