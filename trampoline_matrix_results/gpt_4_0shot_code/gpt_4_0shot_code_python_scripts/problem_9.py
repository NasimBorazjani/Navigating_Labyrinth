
def dfs(pos, jumps, path):
    if jumps == 3:
        if pos == (8, 8):
            return path
        else:
            return None

    x, y = pos
    for dx, dy in [(-1, -1), (-1, 1), (1, -1), (1, 1)]:
        nx, ny = x + dx, y + dy
        if 0 <= nx < 9 and 0 <= ny < 9 and park[nx][ny] == 0:
            result = dfs((nx, ny), jumps + 1, path + [(nx, ny)])
            if result is not None:
                return result

    return None

park = [
    [1, 0, 1, 1, 1, 0, 1, 1, 1],
    [0, 1, 0, 0, 1, 1, 1, 0, 0],
    [1, 0, 1, 0, 1, 1, 1, 0, 0],
    [1, 1, 1, 0, 0, 0, 1, 1, 0],
    [1, 1, 0, 1, 0, 1, 0, 1, 1],
    [1, 0, 1, 1, 0, 1, 1, 1, 0],
    [0, 1, 0, 0, 0, 1, 1, 0, 0],
    [0, 1, 0, 0, 0, 1, 0, 1, 1],
    [1, 1, 0, 0, 0, 0, 0, 0, 0]
]

print(dfs((1, 2), 0, [(1, 2)]))
