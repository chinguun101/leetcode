class Solution(object):
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        visit=set()
        ROW, COL= len(grid), len(grid[0])
        def dfs(r,c):
            if min(r,c)<0 or r==ROW or c==COL or (r,c) in visit or grid[r][c]==0:
                return 0
            visit.add((r,c))
            return 1+dfs(r+1, c)+dfs(r-1, c)+dfs(r, c+1)+dfs(r, c-1)
        area=0
        for r in range(ROW):
            for c in range(COL):
                area=max(area,dfs(r,c))
        return area
            
