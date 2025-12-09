from collections import defaultdict

MOD = 10**9 + 7

class Solution:
    def specialTriplets(self, nums: List[int]) -> int:
        right = defaultdict(int)
        for x in nums:
            right[x] += 1
        
        left = defaultdict(int)
        ans = 0
        
        for j in range(len(nums)):
            val = nums[j]
            right[val] -= 1  # remove current from right side

            target = val * 2

            # count valid i choices on left and k choices on right
            if target in left and target in right:
                ans = (ans + left[target] * right[target]) % MOD

            left[val] += 1  # add current to the left

        return ans
