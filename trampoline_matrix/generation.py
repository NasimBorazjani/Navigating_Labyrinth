

import numpy as np
import random

def generate(edge_length, seed):
    path_created = False
    while not path_created:
        seed += 1
        random.seed(seed)
        np.random.seed(seed)
        # Create a matrix filled with 1s
        matrix = [[np.random.choice([0, 1], p=[0.4, 0.6]) for _ in range(edge_length)] for _ in range(edge_length)]

        # Randomly choose start and end indices
        start = (random.randint(0, edge_length-1), random.randint(0, edge_length-1))
        end = (random.randint(0, edge_length-1), random.randint(0, edge_length-1))
        while abs(start[0] - end[0]) + abs(start[1] - end[1]) < 1.3 *edge_length:
            start = (random.randint(0, edge_length-1), random.randint(0, edge_length-1))
            end = (random.randint(0, edge_length-1), random.randint(0, edge_length-1))


        num_req_diagonal_moves = edge_length//3
        
        # Create a stack for DFS algorithm
        stack = []
        stack.append(start)

        # Create a set to store visited cells
        visited = set()
        visited.add(start)
        
        num_diagonal_moves = 0
        len_path = 0

        while stack:
            # Directions for moving 
            if num_diagonal_moves < num_req_diagonal_moves:
                directions = [(0, 1), (0, -1), (1, 0), (1, -1), (1, 1), (-1, 0), (-1, 1), (-1, -1)]
                diagonal_directions = [(1, -1), (1, 1), (-1, 1), (-1, -1)]
            else:
                diagonal_directions = []
                directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
            
            seed += 1
            random.seed(seed)
            current = stack[-1]
            len_path += 1
            matrix[current[0]][current[1]] = 0

            # Check if we reached the destination
            if current == end:
                if len_path <= 2* edge_length + 2 and num_diagonal_moves == num_req_diagonal_moves:
                    path_created = True
                break

            # Get the list of unvisited neighbors
            neighbors = [(current[0] + d[0], current[1] + d[1]) for d in directions
                        if 0 <= current[0] + d[0] < edge_length and 0 <= current[1] + d[1] < edge_length and
                        (current[0] + d[0], current[1] + d[1]) not in visited]
            
            diagonal_neighbors =  [(current[0] + d[0], current[1] + d[1]) for d in diagonal_directions
                        if 0 <= current[0] + d[0] < edge_length and 0 <= current[1] + d[1] < edge_length and
                        (current[0] + d[0], current[1] + d[1]) not in visited]

            if neighbors:
                # Choose a random neighbor and add it to the stack
                next_cell = random.choice(neighbors)
                if next_cell in diagonal_neighbors:
                    num_diagonal_moves += 1
                stack.append(next_cell)
                visited.add(next_cell)
            else:
                # If there are no unvisited neighbors, pop the current cell from the stack
                stack.pop() 

    return matrix, start, end, num_req_diagonal_moves

def matrix_to_string(matrix):
    return '\n'.join(' '.join(str(cell) for cell in row) for row in matrix)


# Test the function

"""matrix, start, end, num_allowed_d_moves = generate(5, 1)
print(matrix, start, end, num_allowed_d_moves)
print(matrix_to_string(matrix))"""

