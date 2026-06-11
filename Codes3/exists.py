class Solution:
    def exist(self, board: list[list[str]], word: str) -> bool:
        ROW, COL = len(board), len(board[0])
        def dfs(r, c, index):
            if index == len(word):
                return True
            if (r < 0 or c < 0 or 
                r >= ROW or c >= COL or 
                board[r][c] != word[index]):
                return False
            temp = board[r][c]
            board[r][c] = '#'
            found = (dfs(r, c + 1, index + 1) or
                     dfs(r, c - 1, index + 1) or
                     dfs(r + 1, c, index + 1) or
                     dfs(r - 1, c, index + 1))
            
            board[r][c] = temp
            return found

        for r in range(ROW):
            for c in range(COL):
                if board[r][c] == word[0] and dfs(r, c, 0):
                    return True
                        
        return False
