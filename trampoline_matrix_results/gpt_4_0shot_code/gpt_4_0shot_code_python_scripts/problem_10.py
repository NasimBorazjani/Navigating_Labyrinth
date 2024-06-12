
def dfs(pos, trampolines, visited, path, jumps):
    if jumps < 0 or pos[0] < 0 or pos[0] >= 9 or pos[1] < 0 or pos[1] >= 9 or trampolines[pos[0]][pos[1]] == 1 or pos in visited:
        return None
    if jumps == 0 and pos == (2, 1):
        return path + [pos]
    visited.add(pos)
    shortest_path = None
    for dx, dy in [(-1, -1), (-1, 1), (1, -1), (1, 1)]:
        new_path = dfs((pos[0] + dx, pos[1] + dy), trampolines, visited, path + [pos], jumps - 1)
        if new_path is not None and (shortest_path is None or len(new_path) < len(shortest_path)):
            shortest_path = new_path
    visited.remove(pos)
    return shortest_path

trampolines = [
    [0, 1, 0, 1, 0, 1, 1, 1, 0],
    [1, 0, 1, 0, 0, 0, 1, 0, 0],
    [0, 0, 0, 1, 1, 1, 0, 1, 1],
    [1, 0, 0, 0, 0, 1, 1, 0, 1],
    [0, 0, 0, 0, 1, 0, 0, 1, 0],
    [1, 0, 0, 0, 1, 1, 1, 0, 1],
    [0, 1, 0, 0, 1, 0, 1, 1, 0],
    [0, 1, 0, 0, 1, 0, 0, 0, 1],
    [1, 1, 0, 0, 0, 0, 0, 1, 0]
]
print(dfs((8, 8), trampolines, set(), [], 3))
