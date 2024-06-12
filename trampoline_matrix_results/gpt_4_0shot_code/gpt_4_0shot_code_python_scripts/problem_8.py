
def dfs(pos, jumps, path):
    if jumps < 0 or pos[0] < 0 or pos[0] >= 9 or pos[1] < 0 or pos[1] >= 9 or park[pos[0]][pos[1]] == 1:
        return None
    if jumps == 0 and pos == (8, 3):
        return path
    if jumps == 0:
        return None
    directions = [(-1, -1), (-1, 1), (1, -1), (1, 1)]
    for direction in directions:
        new_pos = (pos[0] + direction[0], pos[1] + direction[1])
        result = dfs(new_pos, jumps - 1, path + [new_pos])
        if result is not None:
            return result
    return None

park = [
    [0, 1, 1, 1, 0, 0, 0, 1, 0],
    [0, 1, 1, 0, 1, 0, 1, 0, 0],
    [1, 0, 1, 1, 1, 1, 0, 0, 1],
    [0, 0, 1, 0, 1, 1, 1, 0, 1],
    [1, 0, 1, 1, 0, 1, 1, 0, 1],
    [1, 1, 1, 1, 1, 0, 0, 0, 0],
    [0, 0, 1, 1, 1, 0, 0, 0, 1],
    [1, 1, 1, 0, 0, 0, 0, 1, 1],
    [1, 1, 1, 0, 0, 0, 0, 1, 1]
]

print(dfs((0, 8), 3, [(0, 8)]))
