class Solution(object):
    def generateParenthesis(self, n):
        \\\
        :type n: int
        :rtype: List[str]
        \\\
        res=[]
        stack=[]
        def bt(a,b):
            if a== b ==n:
                res.append(\\.join(stack))
                return
            
            if a < n:
                stack.append(\(\)
                bt(a+1, b)
                stack.pop()

            if b <a:
                stack.append(\)\)
                bt(a,b+1)
                stack.pop()
        bt(0,0)
        return res
