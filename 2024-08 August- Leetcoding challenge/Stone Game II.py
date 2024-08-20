class Solution:
    def stoneGameII(self, piles):
        n = len(piles)
        mem = [[-1] * n for _ in range(n)]
        suffix = [0] * n  # suffix[i] := sum(piles[i..n))

        suffix[-1] = piles[-1]
        for i in range(n - 2, -1, -1):
            suffix[i] = suffix[i + 1] + piles[i]

        return self._stoneGameII(suffix, 0, 1, mem)

    # Returns the maximum number of stones Alice can get from piles[i..n) with M.
    def _stoneGameII(self, suffix, i, M, mem):
        if i + 2 * M >= len(suffix):
            return suffix[i]
        if mem[i][M] != -1:
            return mem[i][M]

        opponent = suffix[i]

        for X in range(1, 2 * M + 1):
            opponent = min(opponent, self._stoneGameII(suffix, i + X, max(M, X), mem))

        mem[i][M] = suffix[i] - opponent
        return mem[i][M]
