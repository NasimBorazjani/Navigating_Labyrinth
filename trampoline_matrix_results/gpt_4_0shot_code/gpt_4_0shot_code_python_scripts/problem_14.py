
def dfs(pos, park, path, jumps):
    x, y = pos
    if not (0 <= x < 9 and 0 <= y < 9) or park[x][y] == 1:
        return None
    if jumps < 0:
        return None
    if pos == (7, 0) and jumps == 0:
        return path + [pos]
    park[x][y] = 1
    shortest = None
    for dx, dy in [(-1, -1), (-1, 1), (1, -1), (1, 1)]:
        result = dfs((x + dx, y + dy), park, path + [pos], jumps - 1)
        if result is not None and (shortest is None or len(result) < len(shortest)):
            shortest = result
    park[x][y] = 0
    return shortest

park = [
    [1, 0, 0, 0, 0, 1, 1, 0, 0],
    [1, 0, 0, 1, 0, 1, 1, 0, 0],
    [0, 0, 1, 0, 1, 0, 0, 0, 1],
    [1, 0, 0, 1, 1, 0, 0, 0, 0],
    [0, 0, 0, 0, 1, 1, 1, 0, 1],
    [0, 0, 0, 1, 1, 0, 1, 1, 0],
    [0, 1, 1, 0, 1, 1, 0, 1, 0],
    [0, 1, 0, 0, 1, 0, 0, 0, 0],
    [0, 0, 0, 0, 1, 0, 1, 1, 0]
]

print(dfs((0, 7), park, [], 3))
