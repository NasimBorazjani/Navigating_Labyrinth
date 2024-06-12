
def solve_puzzle(puzzle):
    # Flatten the puzzle
    flat_puzzle = [item for sublist in puzzle for item in sublist if item != '_']
    # Sort the puzzle in descending order
    sorted_puzzle = sorted(flat_puzzle, reverse=True)
    # Initialize the solution
    solution = []
    # Iterate over the puzzle
    for i in range(len(sorted_puzzle)):
        # If the current tile is not in its correct position
        if flat_puzzle[i] != sorted_puzzle[i]:
            # Find the correct tile
            correct_tile = flat_puzzle.index(sorted_puzzle[i])
            # Swap the tiles
            flat_puzzle[i], flat_puzzle[correct_tile] = flat_puzzle[correct_tile], flat_puzzle[i]
            # Add the tile to the solution
            solution.append(sorted_puzzle[i])
    # Return the solution
    return solution

# Test the function
puzzle = [[26, 39, 50, 35], ['_', 67, 2, 71], [48, 41, 37, 56]]
print(solve_puzzle(puzzle))
