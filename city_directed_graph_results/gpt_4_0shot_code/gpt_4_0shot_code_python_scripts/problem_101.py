
def dfs(city, graph, visited, path, count):
    path.append(city)
    visited[city] = True

    if city in ['I', 'N']:
        count[city] += 1

    if count['I'] == 2 and count['N'] == 2:
        return path

    for neighbor in graph[city]:
        if not visited[neighbor] or (neighbor in ['I', 'N'] and count[neighbor] < 2):
            result = dfs(neighbor, graph, visited, path, count)
            if result:
                return result

    path.pop()
    visited[city] = False
    if city in ['I', 'N']:
        count[city] -= 1

    return None

def solve():
    graph = {
        'S': ['Z', 'P', 'B', 'A', 'L', 'E'],
        'Z': ['G'],
        'I': ['Z', 'F', 'A', 'M'],
        'R': ['S', 'Z', 'I', 'P', 'B', 'M', 'G'],
        'P': ['T', 'E'],
        'T': ['A'],
        'X': ['I', 'R', 'P', 'B', 'L', 'M', 'G'],
        'B': ['F', 'N'],
        'F': ['Z', 'X', 'A'],
        'A': ['N'],
        'L': ['Z', 'I', 'R', 'P', 'A', 'N'],
        'M': ['F', 'N', 'E'],
        'G': ['P', 'A', 'M'],
        'N': ['R', 'P', 'B', 'M', 'G', 'E'],
        'E': ['R', 'T', 'A', 'G', 'N']
    }

    visited = {city: False for city in graph}
    count = {'I': 0, 'N': 0}
    path = []

    return dfs('P', graph, visited, path, count)

print(solve())
