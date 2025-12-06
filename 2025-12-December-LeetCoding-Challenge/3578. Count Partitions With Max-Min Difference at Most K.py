class Solution:
    def countPartitions(self, nums: List[int], k: int) -> int:
        MOD = 10**9 + 7
        n = len(nums)
        
        dp = [0] * (n + 1)
        pref = [0] * (n + 1)
        dp[0] = 1
        pref[0] = 1
        
        from collections import deque
        minD = deque()
        maxD = deque()
        
        j = 0
        for i in range(n):
            while minD and minD[-1] > nums[i]:
                minD.pop()
            minD.append(nums[i])
            
            while maxD and maxD[-1] < nums[i]:
                maxD.pop()
            maxD.append(nums[i])
            
            while maxD[0] - minD[0] > k:
                if minD[0] == nums[j]:
                    minD.popleft()
                if maxD[0] == nums[j]:
                    maxD.popleft()
                j += 1
            
            dp[i+1] = (pref[i] - (pref[j-1] if j > 0 else 0)) % MOD
            pref[i+1] = (pref[i] + dp[i+1]) % MOD
        
        return dp[n]
