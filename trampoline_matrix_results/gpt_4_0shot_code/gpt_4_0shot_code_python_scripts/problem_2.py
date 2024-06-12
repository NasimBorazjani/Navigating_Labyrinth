
def dfs(pos, jumps, path):
    if jumps == 3 and pos == (8, 0):
        return path
    if jumps > 3 or pos[0] < 0 or pos[0] > 8 or pos[1] < 0 or pos[1] > 8 or park[pos[0]][pos[1]] == 1:
        return None
    for dx, dy in [(-1, -1), (-1, 1), (1, -1), (1, 1)]:
        new_pos = (pos[0] + dx, pos[1] + dy)
        result = dfs(new_pos, jumps + 1, path + [new_pos])
        if result is not None:
            return result
    return None

park = [
    [1, 1, 0, 1, 0, 0, 1, 1, 1],
    [1, 1, 1, 0, 1, 0, 1, 1, 1],
    [0, 1, 0, 1, 1, 0, 0, 0, 0],
    [1, 1, 1, 0, 1, 1, 0, 1, 0],
    [0, 1, 0, 1, 1, 0, 0, 1, 1],
    [0, 0, 0, 0, 0, 0, 1, 0, 1],
    [0, 1, 0, 1, 1, 0, 1, 0, 0],
    [1, 0, 0, 1, 1, 0, 0, 1, 0],
    [0, 0, 0, 0, 0, 0, 0, 1, 0]
]

print(dfs((0, 4), 0, [(0, 4)]))
