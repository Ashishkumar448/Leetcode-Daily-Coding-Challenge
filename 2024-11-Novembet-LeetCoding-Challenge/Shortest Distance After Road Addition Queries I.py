from collections import deque

class Solution:
    def shortestDistanceAfterQueries(self, n, queries):
        ans = [0] * len(queries)
        dist = [i for i in range(n)]
        graph = [[] for _ in range(n)]

        for i in range(n - 1):
            graph[i].append(i + 1)

        for i in range(len(queries)):
            u, v = queries[i]
            graph[u].append(v)
            if dist[u] + 1 < dist[v]:
                dist[v] = dist[u] + 1
                self.bfs(graph, v, dist)
            ans[i] = dist[n - 1]

        return ans

    # Performs a BFS to update the shortest distances from the given `start` node
    # to all other reachable nodes in the graph. It updates the `dist` array
    # with the new shortest distances.
    def bfs(self, graph, start, dist):
        q = deque([start])
        while q:
            u = q.popleft()
            for v in graph[u]:
                if dist[u] + 1 < dist[v]:
                    dist[v] = dist[u] + 1
                    q.append(v)
