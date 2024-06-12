
def magic_square():
    grid = [['x' for _ in range(4)] for _ in range(4)]
    grid[1][1] = 41
    grid[1][2] = 17
    grid[2][1] = 13
    grid[2][2] = 43
    grid[0][3] = 9
    grid[1][3] = 24
    grid[2][3] = 27
    grid[3][3] = 11
    rows = {0: None, 1: 116, 2: 124, 3: None}
    cols = {0: None, 1: 144, 2: 76, 3: None}
    diag = 75
    result = []
    for r in range(4):
        for c in range(4):
            if grid[r][c] == 'x':
                for num in range(6, 48):
                    if (rows[r] is None or rows[r] - num in {0, 144, 76}) and \
                            (cols[c] is None or cols[c] - num in {0, 144, 76}) and \
                            (r == c and diag - num in {0, 144, 76, 116, 124}):
                        grid[r][c] = num
                        result.append((r, c, num))
                        break
                else:
                    return None
    if grid[0][0] * grid[1][1] * grid[2][2] * grid[3][3] != 75:
        return None
    return result

print(magic_square())
