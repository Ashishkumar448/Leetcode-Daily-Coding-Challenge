class Solution:
    def countTrapezoids(self, points: List[List[int]]) -> int:
        MOD = 10**9 + 7
        
        # Count how many points share each y
        cnt = defaultdict(int)
        for x, y in points:
            cnt[y] += 1
        
        # Compute C(cnt[y], 2) for each y where >=2 points exist
        combs = []
        for v in cnt.values():
            if v >= 2:
                combs.append(v * (v - 1) // 2)
        
        if len(combs) < 2:
            return 0
        
        total = sum(combs) % MOD
        total_sq = sum((c * c) % MOD for c in combs) % MOD
        
        # (sum(fi)^2 - sum(fi^2)) / 2
        ans = (total * total - total_sq) % MOD
        ans = ans * pow(2, MOD - 2, MOD) % MOD  # divide by 2 under modulo
        
        return ans
