class Solution(object):
    def isValidSudoku(self, board):
        \\\
        :type board: List[List[str]]
        :rtype: bool
        \\\
        row_seen = defaultdict(set)
        col_seen= defaultdict(set)
        box_seen= defaultdict(set)
        
        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j]!=\.\ and (board[i][j] in row_seen[i] or
                board[i][j] in col_seen[j] or
                board[i][j] in box_seen[str(i//3)+ str(j//3)]):
                    return False
                row_seen[i].add(board[i][j])
                col_seen[j].add(board[i][j])
                box_seen[str(i//3)+ str(j//3)].add(board[i][j])

        return True