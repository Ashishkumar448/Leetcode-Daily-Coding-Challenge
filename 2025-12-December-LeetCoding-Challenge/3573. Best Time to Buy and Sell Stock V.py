from typing import List

class Solution:
    def maximumProfit(self, prices: List[int], k: int) -> int:
        INF = float('-inf')
        
        # dp[t][state]
        # state: 0 = flat, 1 = long, 2 = short
        dp = [[INF] * 3 for _ in range(k + 1)]
        dp[0][0] = 0

        for price in prices:
            new_dp = [row[:] for row in dp]
            
            for t in range(k + 1):
                # From flat
                if dp[t][0] != INF:
                    # Buy -> long
                    new_dp[t][1] = max(new_dp[t][1], dp[t][0] - price)
                    # Short sell -> short
                    new_dp[t][2] = max(new_dp[t][2], dp[t][0] + price)
                
                # From long
                if t < k and dp[t][1] != INF:
                    # Sell -> flat (complete transaction)
                    new_dp[t + 1][0] = max(new_dp[t + 1][0], dp[t][1] + price)
                
                # From short
                if t < k and dp[t][2] != INF:
                    # Buy back -> flat (complete transaction)
                    new_dp[t + 1][0] = max(new_dp[t + 1][0], dp[t][2] - price)

            dp = new_dp
        
        # Best profit with at most k transactions, must end flat
        return max(dp[t][0] for t in range(k + 1))
