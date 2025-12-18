from typing import List

class Solution:
    def maxProfit(self, prices: List[int], strategy: List[int], k: int) -> int:
        n = len(prices)

        # Base profit
        base_profit = sum(strategy[i] * prices[i] for i in range(n))

        # Prefix sums
        pref_sp = [0] * (n + 1)   # prefix of strategy[i] * prices[i]
        pref_p = [0] * (n + 1)    # prefix of prices[i]

        for i in range(n):
            pref_sp[i + 1] = pref_sp[i] + strategy[i] * prices[i]
            pref_p[i + 1] = pref_p[i] + prices[i]

        half = k // 2
        best_delta = 0

        for i in range(n - k + 1):
            # First half: remove original contribution
            first_half = pref_sp[i + half] - pref_sp[i]

            # Second half: add prices, remove original contribution
            second_half_prices = pref_p[i + k] - pref_p[i + half]
            second_half_original = pref_sp[i + k] - pref_sp[i + half]

            delta = -first_half + (second_half_prices - second_half_original)
            best_delta = max(best_delta, delta)

        return base_profit + best_delta
