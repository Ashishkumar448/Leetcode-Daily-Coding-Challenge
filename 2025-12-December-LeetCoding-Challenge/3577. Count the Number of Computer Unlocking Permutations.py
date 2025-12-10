class Solution:
    def countPermutations(self, complexity):
        MOD = 10**9 + 7
        n = len(complexity)

        # Fenwick Tree for counting smaller complexities seen so far
        def fenwick_update(bit, i, v):
            while i < len(bit):
                bit[i] += v
                i += i & -i
        
        def fenwick_sum(bit, i):
            s = 0
            while i > 0:
                s += bit[i]
                i -= i & -i
            return s
        
        # coordinate compression
        vals = sorted(set(complexity))
        comp = {v: i+1 for i, v in enumerate(vals)}  # 1-based
        
        bit = [0] * (len(vals) + 2)
        
        parents = [0] * n
        
        for i in range(n):
            c = comp[complexity[i]]
            parents[i] = fenwick_sum(bit, c - 1)   # count smaller elements before i
            fenwick_update(bit, c, 1)
        
        # If any computer (except 0) has no parent -> impossible
        for i in range(1, n):
            if parents[i] == 0:
                return 0
        
        # Count valid permutations
        answer = 1
        available = 1  # at start only 0 is available
        
        for i in range(1, n):
            answer = (answer * available) % MOD
            available += 1
        
        return answer % MOD
