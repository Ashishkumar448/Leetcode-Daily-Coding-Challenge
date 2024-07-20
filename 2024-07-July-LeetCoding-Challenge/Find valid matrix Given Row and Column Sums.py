from typing import List

class Solution:
    def restoreMatrix(self, rowSum: List[int], colSum: List[int]) -> List[List[int]]:
        rows = len(rowSum)
        cols = len(colSum)
        matrix = [[0] * cols for _ in range(rows)]

        for i in range(rows):
            for j in range(cols):
                min_value = min(rowSum[i], colSum[j])
                matrix[i][j] = min_value
                rowSum[i] -= min_value
                colSum[j] -= min_value

        return matrix

# Example usage:
rowSum = [5, 7, 10]
colSum = [8, 6, 8]
solution = Solution()
matrix = solution.restoreMatrix(rowSum, colSum)

for row in matrix:
    print(row)
