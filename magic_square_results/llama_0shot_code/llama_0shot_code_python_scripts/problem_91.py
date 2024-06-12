
def can_place(grid, row, col, num):
    # Check the number in the row
    if num in grid[row]:
        return False
    # Check the number in the column
    if num in [grid[i][col] for i in range(4)]:
        return False
    # Check the number in the main diagonal
    if col == row and num in [grid[i][i] for i in range(4)]:
        return False
    # Check the number in the secondary diagonal
    if col == 3 - row and num in [grid[i][3 - i] for i in range(4)]:
        return False
    return True

def solve(grid, row, col, num_list):
    if num_list == []:
        return True
    num = num_list[0]
    for r in range(4):
        for c in range(4):
            if grid[r][c] == 'x' and can_place(grid, r, c, num):
                grid[r][c] = num
                if solve(grid, row, col, num_list[1:]):
                    return True
                grid[r][c] = 'x'
        return False

def magic_square():
    grid = [['62', 'x', 'x', 'x'],
            ['x', '35', '60', 'x'],
            ['x', '39', 'x', '54'],
            ['x', '55', '34', 'x']]
    num_list = [i for i in range(22, 69)]
    solve(grid, 0, 0, num_list)
    return grid

def main():
    grid = magic_square()
    print(grid)

if __name__ == "__main__":
    main()
