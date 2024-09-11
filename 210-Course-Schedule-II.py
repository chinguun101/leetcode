class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        has={i:[] for i in range(numCourses)}
        for crs,pre in prerequisites:
            has[crs].append(pre)
        cycle=set()
        visit=set()
        res=[]
        def dfs(crs):
            if crs in cycle:
                return False
            if crs in visit:
                return True
            cycle.add(crs)
            for pre in has[crs]:
                if not dfs(pre):
                    return False
            cycle.remove(crs) 
            visit.add(crs)
            res.append(crs)
            return True
        for c in range(numCourses):
            if not dfs(c):
                return []
        return res
