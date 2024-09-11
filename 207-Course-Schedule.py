class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        has={i:[] for i in range(numCourses)}
        visit=set()
        for crs,pre in prerequisites:
            has[crs].append(pre)

        def dfs(crs):
            if crs in visit:
                return False
            if has[crs]==[]:
                return True

            visit.add(crs)
            for pre in has[crs]:
                if not dfs(pre):
                    return False
            visit.remove(crs)
            has[crs]=[]
            return True
        
        for c in range(numCourses):
            if not dfs(c):
                return False
        return True 