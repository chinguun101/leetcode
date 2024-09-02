class Solution(object):
    def merge(self, intervals):
        \\\
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        \\\
        intervals.sort(key= lambda i:i[0])
        res=[intervals[0]]

        for s,e in intervals:
            lastend= res[-1][1]
            if s <= lastend:
                res[-1][1]=max(e,lastend)
            else:
                res.append([s,e])
        return res
        