class Solution:
    def strangePrinter(self, s: str) -> int:
        n = len(s)
        mem = [[0] * n for _ in range(n)]
        return self._strange_printer_helper(s, 0, n - 1, mem)

    def _strange_printer_helper(self, s: str, i: int, j: int, mem: list) -> int:
        if i > j:
            return 0
        if mem[i][j] > 0:
            return mem[i][j]

        # Print s[i].
        mem[i][j] = self._strange_printer_helper(s, i + 1, j, mem) + 1

        for k in range(i + 1, j + 1):
            if s[k] == s[i]:
                mem[i][j] = min(mem[i][j], 
                                self._strange_printer_helper(s, i, k - 1, mem) + 
                                self._strange_printer_helper(s, k + 1, j, mem))

        return mem[i][j]
