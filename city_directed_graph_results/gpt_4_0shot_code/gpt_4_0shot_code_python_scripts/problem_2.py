
from collections import defaultdict

def dfs(graph, start, path=[]):
    path = path + [start]
    paths = [path]
    for node in graph[start]:
        if node not in path or (node in ['K', 'Q'] and path.count(node) < 2):
            newpaths = dfs(graph, node, path)
            for newpath in newpaths:
                paths.append(newpath)
    return paths

def solve():
    graph = {
        'S': ['I', 'Q'],
        'U': ['X'],
        'X': ['R', 'K'],
        'D': ['U', 'Z'],
        'I': ['U', 'Q'],
        'Z': ['I', 'K'],
        'R': ['S', 'U'],
        'M': ['X', 'I'],
        'K': ['R', 'M'],
        'Q': ['U', 'D', 'I', 'Z', 'K']
    }
    paths = dfs(graph, 'D')
    paths = [path for path in paths if path.count('K') == 2 and path.count('Q') == 2]
    paths.sort(key=len)
    return paths[0] if paths else None

print(solve())
