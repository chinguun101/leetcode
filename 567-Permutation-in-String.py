class Solution(object):
    def checkInclusion(self, s1, s2):
        \\\
        :type s1: str
        :type s2: str
        :rtype: bool
        \\\         
        if len(s1)>len(s2): return False

        c1,c2=[0]*26, [0]*26

        for i in range(len(s1)):
            c1[ord(s1[i])-ord(\a\)]+=1
            c2[ord(s2[i])-ord(\a\)]+=1

        l=0
        for r in range(len(s1),len(s2)):
            if c1==c2: return True
            c2[ord(s2[r])-ord(\a\)]+=1
            c2[ord(s2[l])-ord(\a\)]-=1
            l+=1
        return c1==c2
        