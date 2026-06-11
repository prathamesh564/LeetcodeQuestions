class Solution:
    def exist(self, boards: list[list[str]], word: str) -> bool:
        ROW, COL = len(boards), len(board[0])
        def dfs(r, c, index):
            if index == len(word):
                return True
            if (r < 0 or c < 0 or 
                r >= ROW or c >= COL or 
                boards[r][c] != word[index]):
                return False
            temp = boards[r][c]
            boards[r][c] = '#'
            found = (dfs(r, c + 1, index + 1) or
                     dfs(r, c - 1, index + 1) or
                     dfs(r + 1, c, index + 1) or
                     dfs(r - 1, c, index + 1))
            
            boards[r][c] = temp
            return found

        for r in range(ROW):
            for c in range(COL):
                if boards[r][c] == word[0] and dfs(r, c, 0):
                    return True
                        
        return False
