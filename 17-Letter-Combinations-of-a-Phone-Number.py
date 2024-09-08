class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        nums={
            '2':["a","b","c"],
            '3':["d","e","f"],
            '4':["g","h","i"],
            '5':["j","k","l"],
            '6':["m","n","o"],
            '7':["p","q","r","s"],
            '8':["t","u","v"],
            '9':["w","x","y","z"]
        }
        comb=[]
        res=[]
        def helper(i):
            if len(comb)==len(digits):
                res.append("".join(comb))
                return

            for j in range(len(nums[digits[i]])):
                comb.append(nums[digits[i]][j])
                helper(i+1)
                comb.pop()
        if digits: helper(0)
        return res
