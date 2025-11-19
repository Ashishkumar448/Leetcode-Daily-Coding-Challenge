class Solution:
    def findFinalValue(self, nums: List[int], original: int) -> int:
        # Convert the list to a set for O(1) lookup time
        nums_set = set(nums)
      
        # Keep doubling the original value while it exists in the set
        while original in nums_set:
            # Left shift by 1 is equivalent to multiplying by 2
            original = original << 1
      
        # Return the final value after all doublings
        return original
