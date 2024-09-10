class Solution(object):
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        ROW,COL= len(board), len(board[0])
        visit=set()
        def dfs(r,c):
            if (r<0
            or c<0
            or r==ROW
            or c==COL
            or (r,c) in visit
            or board[r][c]=='X'):
                return
            visit.add((r,c))
            dfs(r+1,c)
            dfs(r-1,c)
            dfs(r,c+1)
            dfs(r,c-1)
        for r in range(ROW):
            dfs(r, 0)
            dfs(r, COL-1)
        for c in range(COL):
            dfs(0, c)
            dfs(ROW-1, c)

        for r in range(1, ROW-1):
            for c in range(1,COL-1):
                if board[r][c]=='O' and (r,c) not in visit:
                    board[r][c]='X'
