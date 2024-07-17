from typing import List

class Solution:
    def numSubarrayBoundedMax(self, nums: List[int], left: int, right: int) -> int:
        def count(bound: int) -> int:
            ans = curr = 0
            for num in nums:
                curr = curr + 1 if num <= bound else 0
                ans += curr
            return ans
        
        return count(right) - count(left - 1)

# Example usage
solution = Solution()
print(solution.numSubarrayBoundedMax([2, 1, 4, 3], 2, 3))  # Output: 3
print(solution.numSubarrayBoundedMax([2, 9, 2, 5, 6], 2, 8))  # Output: 7
