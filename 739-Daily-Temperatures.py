class Solution(object):
    def dailyTemperatures(self, temperatures):
        \\\
        :type temperatures: List[int]
        :rtype: List[int]
        \\\
        res=len(temperatures)*[0]
        stack=[]
        for i,t in enumerate(temperatures):
            while stack and t> stack[-1][1]:
                index, temp = stack.pop()
                res[index]= i-index
            stack.append((i,t))
        return res
        