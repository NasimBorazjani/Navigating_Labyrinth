
import heapq

# Convert adjacency matrix to dictionary
graph = {
    'Q': [0, 0, 0, 0, 0, 1, 0, 0, 0],
    'T': [1, 0, 1, 1, 0, 0, 0, 0, 0],
    'A': [0, 0, 0, 0, 1, 0, 0, 0, 0],
    'X': [0, 0, 0, 0, 1, 0, 1, 1, 1],
    'M': [1, 0, 0, 0, 0, 0, 0, 1, 0],
    'Y': [0, 1, 1, 1, 0, 0, 0, 0, 0],
    'Z': [0, 0, 0, 0, 1, 1, 0, 1, 0],
    'B': [1, 1, 1, 0, 0, 0, 0, 0, 0],
    'S': [0, 1, 0, 0, 0, 1, 0, 0, 1],
    'E': [0, 0, 1, 1, 1, 0, 0, 1, 1],
}

# Dijkstra's algorithm
def shortest_path(graph, start, end):
    queue = []
    heapq.heappush(queue, (0, start, []))
    seen = set()
    while queue:
        (cost, node, path) = heapq.heappop(queue)
        if node not in seen:
            seen.add(node)
            path = path + [node]
            if node == end:
                return cost, path
            for c, neighbour in enumerate(graph[node]):
                if neighbour:
                    heapq.heappush(queue, (cost + 1, chr(ord('A') + c), path))
    return float('inf')

# Find shortest paths to 'T' and 'E'
cost1, path1 = shortest_path(graph, 'Q', 'T')
cost2, path2 = shortest_path(graph, 'Q', 'E')

# Calculate total time
total_time = cost1 + cost2 - 1  # subtract 1 because we count 'Q' twice

# Generate path
path = path1[:path1.index('T')+1] + path2[::-1][:path2[::-1].index('E')+1]

print(path)
