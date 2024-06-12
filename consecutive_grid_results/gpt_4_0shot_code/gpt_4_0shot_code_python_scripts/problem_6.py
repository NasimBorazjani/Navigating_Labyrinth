
def solve(grid, used, i=0, j=0):
    if i == 3:
        return True
    if grid[i][j] == 'x':
        for num in range(41, 75):
            if used[num-41]:
                continue
            if (i > 0 and grid[i-1][j] != 'x' and int(grid[i-1][j]) >= num) or \
               (j > 0 and grid[i][j-1] != 'x' and int(grid[i][j-1]) >= num):
                continue
            grid[i][j] = str(num)
            used[num-41] = True
            if solve(grid, used, i + (j+1)//3, (j+1)%3):
                return True
            grid[i][j] = 'x'
            used[num-41] = False
    elif solve(grid, used, i + (j+1)//3, (j+1)%3):
        return True
    return False

grid = [['41', '48', 'x'], ['x', 'x', '63'], ['x', 'x', '67']]
used = [False]*34
for i in range(3):
    for j in range(3):
        if grid[i][j] != 'x':
            used[int(grid[i][j])-41] = True
solve(grid, used)

result = []
for i in range(3):
    for j in range(3):
        if grid[i][j] != 'x':
            result.append((i, j, int(grid[i][j])))
print(result)
