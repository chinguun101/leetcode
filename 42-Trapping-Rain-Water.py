class Solution(object):
    def trap(self, height):
        total=0
        def counter(height, total):
            l1=0
            while l1<len(height)-1:
                if height[l1]<= height[l1+1]:
                    l1+=1
                    continue
                if len(height)==3:
                    print(height[2])
                    total+= height[2]-height[1]
                    print(total)
                    break
                else: #elif height[l1]>height[l1+1] and l1+1<len(height)-1:
                    mx= height[l1]
                    l2=l1+1
                    block=0
                    #print(\outside\)
                    while l2<=len(height)-1:
                        #print(\inside\)
                        if mx<=height[l2]:
                            total+= mx* (l2-l1-1)-block
                            l1=l2
                            break
                        if l2==len(height)-1:
                            l1+=1
                            counter(height[l1:l2],total)  

                        if mx>height[l2]:
                            block+= height[l2]  
                            l2+=1          
            return total 
        return counter(height,total)

        \\\
        :type height: List[int]
        :rtype: int
        \\\
        