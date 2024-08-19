class Solution(object):
    def lengthOfLongestSubstring(self, s):
        # lst=[]
        # for i in range(len(s)-1):
        #     maxdistance=len(s)-1
        #     for j in range(i+1,len(s)-1,-1):
        #         if s[i]==s[j] and 
        #         if s[i]==s[j] and (j-i)<maxdistance:
        #             maxdistance=j-i
        #             lst.append(maxdistance)
        #             break
        # return lst
        window=set()
        l=0
        length=0
        for r in range(len(s)):
            while s[r] in window:
                window.remove(s[l])
                l=l+1
            length=max(length,r-l+1)
            window.add(s[r])
        return length
