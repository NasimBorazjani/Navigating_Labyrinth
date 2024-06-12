
def solve_puzzle(puzzle):
    # Flatten the 2D list into a 1D list
    flat_puzzle = [item for sublist in puzzle for item in sublist]
    
    # Sort the list in descending order
    sorted_puzzle = sorted([i for i in flat_puzzle if i != '_'], reverse=True)
    
    # Initialize the solution list
    solution = []
    
    # While the puzzle is not in the correct order
    while flat_puzzle != sorted_puzzle + ['_']:
        # Find the index of the empty spot
        empty_index = flat_puzzle.index('_')
        
        # Find the next highest number that is not in its correct place
        for num in sorted_puzzle:
            num_index = flat_puzzle.index(num)
            if num_index != sorted_puzzle.index(num):
                break
        
        # Swap the empty spot with the next highest number
        flat_puzzle[empty_index], flat_puzzle[num_index] = flat_puzzle[num_index], flat_puzzle[empty_index]
        
        # Add the number to the solution list
        solution.append(num)
    
    return solution

# Test the function
puzzle = [[96, 93, '_', 26, 66], [46, 59, 38, 92, 50], [27, 7, 39, 77, 18]]
print(solve_puzzle(puzzle))
