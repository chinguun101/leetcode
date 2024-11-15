class Solution(object):
    def isHappy(self, n):
        \\\
        :type n: int
        :rtype: bool
        \\\

        visit=set()

        while n not in visit:
            visit.add(n)
            n=self.sumo(n)
            if n==1:
                return True
        return False


    def sumo(self,n):
        output=0

        while n:
            output+=(n%10)**2
            n=n//10
        return output
        
        