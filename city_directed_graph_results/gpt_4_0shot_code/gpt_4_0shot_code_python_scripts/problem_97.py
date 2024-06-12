
def dfs(graph, node, visited, path, dest_visited):
    path.append(node)
    if node in ['N', 'Y']:
        dest_visited[node] += 1
    if dest_visited['N'] == 2 and dest_visited['Y'] == 2:
        return path
    for neighbor in graph[node]:
        if visited[neighbor] < 2 and (neighbor not in ['N', 'Y'] or dest_visited[neighbor] < 2):
            visited[neighbor] += 1
            result = dfs(graph, neighbor, visited, path, dest_visited)
            if result:
                return result
            visited[neighbor] -= 1
    path.pop()
    if node in ['N', 'Y']:
        dest_visited[node] -= 1
    return None

def solve():
    graph = {
        'Q': ['R', 'A', 'O', 'E'],
        'R': ['J', 'A'],
        'Y': ['R', 'W', 'A', 'O', 'U', 'V', 'X'],
        'W': ['E'],
        'H': ['Y', 'O', 'E', 'V'],
        'J': ['Y', 'W', 'H', 'O', 'U', 'L'],
        'A': ['W', 'N', 'E'],
        'O': ['R', 'W', 'V'],
        'N': ['R', 'Y', 'A', 'E', 'P'],
        'U': ['W', 'H'],
        'E': ['Y', 'W', 'O', 'X'],
        'L': ['R', 'W', 'A'],
        'P': ['Y', 'N', 'U', 'E'],
        'V': ['H', 'J', 'L', 'P'],
        'X': ['H', 'A', 'N', 'Q', 'V']
    }
    visited = {node: 0 for node in graph}
    visited['Q'] = 1
    dest_visited = {'N': 0, 'Y': 0}
    path = dfs(graph, 'Q', visited, [], dest_visited)
    return path

print(solve())
