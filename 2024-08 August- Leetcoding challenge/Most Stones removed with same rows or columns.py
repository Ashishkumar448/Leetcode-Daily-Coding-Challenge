class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        def dfs(graph: List[List[int]], u: int, seen: Set[int]):
            for v in graph[u]:
                if v not in seen:
                    seen.add(v)
                    dfs(graph, v, seen)
        
        num_of_islands = 0
        graph = [[] for _ in range(len(stones))]
        seen = set()
        
        for i in range(len(stones)):
            for j in range(i + 1, len(stones)):
                if stones[i][0] == stones[j][0] or stones[i][1] == stones[j][1]:
                    graph[i].append(j)
                    graph[j].append(i)
        
        for i in range(len(stones)):
            if i not in seen:
                seen.add(i)
                dfs(graph, i, seen)
                num_of_islands += 1
        
        return len(stones) - num_of_islands
