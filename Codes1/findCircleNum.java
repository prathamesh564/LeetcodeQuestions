class Solution:
    def findCircleNum(self, M: list[list[int]]) -> int:
        n = len(M)
        vis = [0] * n
        ans = 0
        for i in range(n):
            if not vis[i]:
                ans += 1
                st = [i]
                vis[i] = 1
                while st:
                    curr = st.pop()
                    for nxt in range(n):
                        if M[curr][nxt] == 1 and not vis[nxt]:
                            vis[nxt] = 1
                            st.append(nxt)
        return ans
