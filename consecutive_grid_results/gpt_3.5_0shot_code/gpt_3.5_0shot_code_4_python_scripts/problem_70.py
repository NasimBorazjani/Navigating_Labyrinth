
def is_valid(grid, row, col, num):
    for i in range(4):
        if grid[row][i] == num or grid[i][col] == num:
            return False
    
    if row == col:
        for i in range(4):
            if grid[i][i] == num:
                return False
    
    if row + col == 3:
        for i in range(4):
            if grid[i][3-i] == num:
                return False
    
    return True

def solve(grid, replacements, row=0, col=0):
    if row == 4:
        return True
    
    if grid[row][col] != 'x':
        if col == 3:
            return solve(grid, replacements, row+1, 0)
        else:
            return solve(grid, replacements, row, col+1)
    
    for num in range(12, 57):
        if is_valid(grid, row, col, str(num)):
            grid[row][col] = str(num)
            replacements.append((row, col, num))
            
            if col == 3:
                if solve(grid, replacements, row+1, 0):
                    return True
            else:
                if solve(grid, replacements, row, col+1):
                    return True
            
            grid[row][col] = 'x'
            replacements.pop()
    
    return False

grid = [['x', '47', 'x', '55'],
        ['29', '34', 'x', 'x'],
        ['16', 'x', 'x', '35'],
        ['x', '26', 'x', 'x']]

replacements = []
solve(grid, replacements)

print("Solution:")
for row in grid:
    print(row)

print("\nReplacements:")
print(replacements)
