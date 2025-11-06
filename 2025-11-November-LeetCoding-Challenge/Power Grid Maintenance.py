class Solution:
    def processQueries(self, c: int, connections: List[List[int]], queries: List[List[int]]) -> List[int]:
        from collections import defaultdict
        import bisect
        
        parent = list(range(c + 1))
        size = [1] * (c + 1)
        
        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]
        
        def union(a, b):
            ra, rb = find(a), find(b)
            if ra == rb:
                return
            if size[ra] < size[rb]:
                ra, rb = rb, ra
            parent[rb] = ra
            size[ra] += size[rb]
        
        # Step 1: Union all connections
        for u, v in connections:
            union(u, v)
        
        # Step 2: Group nodes by component
        comp_members = defaultdict(list)
        for i in range(1, c + 1):
            comp_members[find(i)].append(i)
        
        # Step 3: Maintain sorted list of online nodes per component
        comp_online = {}
        for root, nodes in comp_members.items():
            comp_online[root] = sorted(nodes)
        
        online = [True] * (c + 1)
        res = []
        
        # Step 4: Process queries
        for qtype, x in queries:
            root = find(x)
            
            if qtype == 1:
                if online[x]:
                    res.append(x)
                else:
                    lst = comp_online[root]
                    if lst:
                        res.append(lst[0])  # smallest online node
                    else:
                        res.append(-1)
            
            else:  # qtype == 2
                if online[x]:
                    online[x] = False
                    lst = comp_online[root]
                    idx = bisect.bisect_left(lst, x)
                    if idx < len(lst) and lst[idx] == x:
                        lst.pop(idx)
        
        return res
