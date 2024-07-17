from typing import List

class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        if not nums:
            return []

        # Coordinate compression
        sorted_nums = sorted(set(nums))
        ranks = {num: i + 1 for i, num in enumerate(sorted_nums)}

        # Initialize BIT
        BIT = [0] * (len(sorted_nums) + 1)
        
        def update(index, value):
            while index < len(BIT):
                BIT[index] += value
                index += index & -index
        
        def query(index):
            total = 0
            while index > 0:
                total += BIT[index]
                index -= index & -index
            return total
        
        # Result array
        result = []
        
        # Traverse the nums array from right to left
        for num in reversed(nums):
            rank = ranks[num]
            result.append(query(rank - 1))
            update(rank, 1)
        
        return result[::-1]

# Example usage
solution = Solution()
print(solution.countSmaller([5, 2, 6, 1]))  # Output: [2, 1, 1, 0]
