class Solution:
    def numDecodings(self, s: str) -> int:
        MOD = 10**9 + 7

        # dp[i] means the number of ways to decode s[:i]
        n = len(s)
        dp = [0] * (n + 1)
        dp[0] = 1  # Base case: an empty string has one way to be decoded

        if s[0] == '*':
            dp[1] = 9  # '*' can be any digit from '1' to '9'
        elif s[0] != '0':
            dp[1] = 1  # Single character that's not '0'

        for i in range(1, n):
            if s[i] == '*':
                dp[i + 1] = 9 * dp[i]  # '*' can be '1' to '9'
                if s[i - 1] == '1':
                    dp[i + 1] = (dp[i + 1] + 9 * dp[i - 1]) % MOD
                elif s[i - 1] == '2':
                    dp[i + 1] = (dp[i + 1] + 6 * dp[i - 1]) % MOD
                elif s[i - 1] == '*':
                    dp[i + 1] = (dp[i + 1] + 15 * dp[i - 1]) % MOD  # 11-19 and 21-26
            else:
                if s[i] != '0':
                    dp[i + 1] = dp[i]
                if s[i - 1] == '1':
                    dp[i + 1] = (dp[i + 1] + dp[i - 1]) % MOD
                elif s[i - 1] == '2' and s[i] <= '6':
                    dp[i + 1] = (dp[i + 1] + dp[i - 1]) % MOD
                elif s[i - 1] == '*':
                    if s[i] <= '6':
                        dp[i + 1] = (dp[i + 1] + 2 * dp[i - 1]) % MOD
                    else:
                        dp[i + 1] = (dp[i + 1] + dp[i - 1]) % MOD

        return dp[n]

# Example usage
solution = Solution()
print(solution.numDecodings("*"))  # Output: 9
print(solution.numDecodings("1*"))  # Output: 18
