class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        
        ROW=len(grid)
        COL=len(grid[0])
        visit=set()
        def dfs(r,c):
            if r<0 or c<0 or r==ROW or c==COL or (r,c) in visit or grid[r][c]=="0":
                return
            visit.add((r,c))
            dfs(r-1,c)
            dfs(r+1,c)
            dfs(r,c+1)
            dfs(r,c-1)
        count=0
        for r in range(ROW):
            for c in range(COL):
                if (r,c) not in visit and grid[r][c]=="1":
                    count+=1
                    dfs(r,c)
        return count
