def findTheCity(n, edges, distanceThreshold):
    # Initialize distance matrix with infinity
    dist = [[float('inf')] * n for _ in range(n)]
    
    # Distance to itself is zero
    for i in range(n):
        dist[i][i] = 0
        
    # Fill initial distances based on the edges
    for u, v, w in edges:
        dist[u][v] = w
        dist[v][u] = w
        
    # Floyd-Warshall algorithm to find all pairs shortest path
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if dist[i][k] + dist[k][j] < dist[i][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
    
    # Find the city with the smallest number of reachable cities
    min_count = float('inf')
    result_city = -1
    for i in range(n):
        count = sum(1 for j in range(n) if dist[i][j] <= distanceThreshold)
        if count <= min_count:
            min_count = count
            result_city = i
            
    return result_city
