class Solution(object):
    def eraseOverlapIntervals(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        intervals.sort()
        res=0
        lastend= intervals[0][1]
        for s,e in intervals[1:]:
            if s>=lastend:
                lastend=e
            else:
                res+=1
                lastend=min(lastend,e)
        return res