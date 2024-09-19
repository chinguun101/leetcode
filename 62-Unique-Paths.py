class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        prevRow=n*[0]
        for i in range(m-1,-1,-1):
            curRow=n*[0]
            curRow[-1]=1
            for c in range(n-2,-1,-1):
                curRow[c]=curRow[c+1]+prevRow[c]
            prevRow=curRow
        return prevRow[0]