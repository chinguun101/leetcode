class Solution(object):
    def mergeTriplets(self, triplets, target):
        """
        :type triplets: List[List[int]]
        :type target: List[int]
        :rtype: bool
        """
        curr=[0,0,0]
        for t in triplets:
            if t[0]<=target[0] and t[1]<=target[1] and t[2]<=target[2]:
                curr=[max(t[0], curr[0]),
                max(t[1], curr[1]),
                max(t[2], curr[2])]
        return curr==target
            
        