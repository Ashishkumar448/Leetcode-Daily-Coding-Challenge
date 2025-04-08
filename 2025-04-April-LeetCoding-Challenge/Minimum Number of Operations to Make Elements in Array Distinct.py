class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        ops = 0
        while len(nums) > 0:
            seen = set()
            duplicate = False
            for num in nums:
                if num in seen:
                    duplicate = True
                    break
                seen.add(num)
            if not duplicate:
                break
            # remove first 3 elements or all if less than 3
            nums = nums[3:] if len(nums) >= 3 else []
            ops += 1
        return ops
