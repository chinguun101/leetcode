class Solution(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        comb,res=[],[]
        def dfs(i):
            if i>=len(s):
                res.append(list(comb))
                return
            for j in range(i,len(s)):
                if self.pal(s[i:j+1]):
                    comb.append(s[i:j+1])
                    dfs(j+1)
                    comb.pop()
        dfs(0)
        return res

    def pal(self,s):
        l,r=0,len(s)-1
        while r>l:
            if s[l]!=s[r]:
                return False
            l+=1
            r-=1
        return True