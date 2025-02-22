class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        # set len of Row and Columns
        ROWS, COLS = len(board), len(board[0])

        # set iterated path
        path = set()

        # helper function
        def dfs(r, c, i):
            # if i iterate up to len of the word then return True
            if i == len(word):
                return True
            # condition for False (no match sequence)
            if (r < 0 or c < 0 or
                r >= ROWS or c >= COLS or
                ((r,c)) in path or
                board[r][c] != word[i]):
                return False
            # add the row,col into the path so no repeat
            path.add((r,c))
            # as long as 1 path is winning, the team is winning.
            res = (dfs(r + 1 , c, i + 1) or
                  dfs(r , c + 1, i + 1) or
                  dfs(r - 1, c, i + 1)  or
                  dfs(r , c - 1, i + 1))
            # remove just incase if we ever needs it later for a different start point
            path.remove((r,c))
            return res
        
        # iter thru Rows & Cols
        for r in range(ROWS):
            for c in range(COLS):
                # run the helper func and return True
                if dfs(r, c, 0): return True
        # if no match, return False
        return False
        
            