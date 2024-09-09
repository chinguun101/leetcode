class Solution(object):
    def orangesRotting(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        ROW,COL=len(grid), len(grid[0])
        q=deque()
        visit=set()
        def helper(r,c):
            if (r==ROW
            or c==COL
            or r<0
            or c<0
            or (r,c) in visit
            or grid[r][c]==0):
                return
            q.append([r,c])
            visit.add((r,c))
            
        for r in range(ROW):
            for c in range(COL):
                if grid[r][c]==2:
                    q.append([r,c])
                    visit.add((r,c))
                if grid[r][c]==0:
                    visit.add((r,c))
        move=[[0,1],[0,-1],[1,0],[-1,0]]
        time=0
        while len(visit)!=ROW*COL and q:
            for i in range(len(q)):
                r,c=q.popleft()
                for dr,dc in move:
                    helper(r+dr, c+dc)
            time+=1
        return time if len(visit)==ROW*COL else -1