class Solution(object):
    def partitionLabels(self, s):
        """
        :type s: str
        :rtype: List[int]
        """
        count={}
        for j in range(len(s)):
            count[s[j]]=j
        length=goal=i=0
        res=[]
        while i<len(s):
            goal=max(goal, count[s[i]])
            length+=1
            if i==goal:
                res.append(length)
                length=0
            i+=1
        return res