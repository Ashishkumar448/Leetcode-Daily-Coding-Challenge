from typing import List

class Solution:
    def threeEqualParts(self, arr: List[int]) -> List[int]:
        # Count the number of 1s in the array
        num_ones = sum(arr)
        
        # If the number of 1s is not divisible by 3, return [-1, -1]
        if num_ones % 3 != 0:
            return [-1, -1]
        
        # If there are no 1s, the array is already splitable into any three parts
        if num_ones == 0:
            return [0, len(arr) - 1]
        
        # Each part must have exactly num_ones // 3 ones
        k = num_ones // 3
        
        # Find the starting index of each part
        first = second = third = ones_seen = 0
        for i, num in enumerate(arr):
            if num == 1:
                ones_seen += 1
                if ones_seen == 1:
                    first = i
                elif ones_seen == k + 1:
                    second = i
                elif ones_seen == 2 * k + 1:
                    third = i
                    break
        
        # Compare the three parts
        while third < len(arr) and arr[first] == arr[second] == arr[third]:
            first += 1
            second += 1
            third += 1
        
        if third == len(arr):
            return [first - 1, second]
        return [-1, -1]

# Example usage
solution = Solution()
print(solution.threeEqualParts([1, 0, 1, 0, 1]))  # Output: [0, 3]
print(solution.threeEqualParts([1, 1, 0, 1, 1]))  # Output: [-1, -1]
