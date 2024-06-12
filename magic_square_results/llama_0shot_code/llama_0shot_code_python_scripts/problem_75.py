
def magic_square():
    grid = [['x' 'x' 'x' 'x'],
            ['28' '33' 'x' 'x'],
            ['16' 'x' 'x' '37'],
            ['36' '18' '7' '23']]
    rows = [None, 101, 108, None]
    cols = [None, 125, 51, None]
    diag = 90
    solution = []
    min_sum = float('inf')

    def valid(num, pos):
        # Check the same row
        for i in range(4):
            if grid[pos[0]][i] == num:
                return False
        # Check the same column
        for i in range(4):
            if grid[i][pos[1]] == num:
                return False
        # Check the diagonal
        if pos[0] == pos[1] or pos[0] + pos[1] == 3:
            if grid[0][3] + num == diag:
                return False
        return True

    def backtrack(pos, sum):
        nonlocal solution, min_sum
        if pos == (4, 4):
            if sum < min_sum:
                min_sum = sum
                solution = [(i, j, grid[i][j]) for i in range(4) for j in range(4) if grid[i][j] != 'x']
        else:
            for num in range(6, 48):
                if valid(num, pos):
                    grid[pos[0]][pos[1]] = num
                    backtrack((pos[0], pos[1] + 1) if pos[1] < 3 else (pos[0] + 1, 0), sum + num)
                    grid[pos[0]][pos[1]] = 'x'

    backtrack((0, 0), 0)
    return solution
