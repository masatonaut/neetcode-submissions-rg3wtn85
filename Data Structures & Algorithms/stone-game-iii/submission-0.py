class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        n = len(stoneValue)
        dp = [0] * (n + 1)

        for i in range(n - 1, -1, -1):
            take = 0
            dp[i] = float('-inf')
            for x in range(3):
                if i + x < n:
                    take += stoneValue[i + x]
                    dp[i] = max(dp[i], take - dp[i + x + 1])

        if dp[0] > 0:
            return "Alice"
        elif dp[0] < 0:
            return "Bob"
        else:
            return "Tie"