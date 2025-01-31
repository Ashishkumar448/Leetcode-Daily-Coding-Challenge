from collections import deque, defaultdict

class Solution:
    def maximumGroups(self, n: int, edges: list[list[int]]) -> int:
        # Create an adjacency list for the graph
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        # To store group assignments
        group = [-1] * (n + 1)  # -1 means unvisited
        max_groups = 0
        
        def bfs(start):
            queue = deque([start])
            group[start] = 0  # Start with group 0
            count = [0, 0]  # Count of nodes in group 0 and group 1
            
            while queue:
                node = queue.popleft()
                count[group[node]] += 1
                
                for neighbor in graph[node]:
                    if group[neighbor] == -1:  # If not visited
                        group[neighbor] = 1 - group[node]  # Alternate groups
                        queue.append(neighbor)
                    elif group[neighbor] == group[node]:  # Conflict found
                        return -1
            
            return min(count)  # Return the smaller count of the two groups
        
        for i in range(1, n + 1):
            if group[i] == -1:  # If this node hasn't been visited yet
                result = bfs(i)
                if result == -1:  # If we found a conflict
                    return -1
                max_groups += result
        
        return max_groups

# Example usage:
sol = Solution()
n = 5
edges = [[1,2], [2,3], [3,4], [4,5]]
print(sol.maximumGroups(n, edges))  # Output will depend on the edges provided
