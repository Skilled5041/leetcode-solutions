class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        dp = [[0 for _ in range(len(text2))] for _ in range(len(text1))]
        longest = 0
        for x, char1 in enumerate(text1):
            for y, char2 in enumerate(text2):
                dp[x][y] = (dp[x - 1][y - 1] if x >= 1 and y >= 1 else 0) + 1 if char1 == char2 else max(dp[x - 1][y] if x >= 1 else 0, dp[x][y - 1] if y >= 1 else 0)
                longest = max(longest, dp[x][y])

        return longest
