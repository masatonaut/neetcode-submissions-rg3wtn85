class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        n = len(s)
        dp = [False] * n
        dp[0] = True
        window = 0

        for j in range(1, n):
            if j - minJump >= 0 and dp[j - minJump]:
                window += 1
            if j - maxJump - 1 >= 0 and dp[j - maxJump - 1]:
                window -= 1
            if s[j] == '0' and window > 0:
                dp[j] = True

        return dp[n - 1]