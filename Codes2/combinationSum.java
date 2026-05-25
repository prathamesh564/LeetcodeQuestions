class Solution:
    def combinationSum(self, c: list[int], t: int) -> list[list[int]]:
        st = []
        
        def dfs(rem, cur, idx):
            if rem == 0:
                st.append(list(cur))
                return
            for i in range(idx, len(c)):
                if c[i] <= rem:
                    cur.append(c[i])
                    dfs(rem - c[i], cur, i)
                    cur.pop()
                    
        dfs(t, [], 0)
        return st
