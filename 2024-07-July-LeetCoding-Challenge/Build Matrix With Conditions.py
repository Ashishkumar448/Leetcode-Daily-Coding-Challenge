from typing import List
from collections import deque, defaultdict

class Solution:
    def buildMatrix(self, k: int, rowConditions: List[List[int]], colConditions: List[List[int]]) -> List[List[int]]:
        def topologicalSort(graph, indegree, k):
            order = []
            queue = deque([i for i in range(1, k + 1) if indegree[i] == 0])
            
            while queue:
                node = queue.popleft()
                order.append(node)
                
                for neighbor in graph[node]:
                    indegree[neighbor] -= 1
                    if indegree[neighbor] == 0:
                        queue.append(neighbor)
            
            return order if len(order) == k else []
        
        # Create graph and indegree for row conditions
        rowGraph = defaultdict(list)
        rowIndegree = [0] * (k + 1)
        
        for u, v in rowConditions:
            rowGraph[u].append(v)
            rowIndegree[v] += 1
        
        # Create graph and indegree for column conditions
        colGraph = defaultdict(list)
        colIndegree = [0] * (k + 1)
        
        for u, v in colConditions:
            colGraph[u].append(v)
            colIndegree[v] += 1
        
        # Get the topological orders
        rowOrder = topologicalSort(rowGraph, rowIndegree, k)
        colOrder = topologicalSort(colGraph, colIndegree, k)
        
        if not rowOrder or not colOrder:
            return []
        
        # Map elements to their positions in the orders
        rowPos = {val: idx for idx, val in enumerate(rowOrder)}
        colPos = {val: idx for idx, val in enumerate(colOrder)}
        
        # Build the matrix
        matrix = [[0] * k for _ in range(k)]
        
        for num in range(1, k + 1):
            matrix[rowPos[num]][colPos[num]] = num
        
        return matrix

# Example usage:
solution = Solution()
k = 3
rowConditions = [[1, 2], [2, 3]]
colConditions = [[2, 1], [3, 2]]
matrix = solution.buildMatrix(k, rowConditions, colConditions)

for row in matrix:
    print(row)
