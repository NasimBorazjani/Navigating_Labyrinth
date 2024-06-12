
    
import numpy as np
import random

"""def generate(edge_length, seed):
    max_traffic = 20
    path_created = False
    random.seed(seed)
    seed = random.randint(1, 10000)
    while not path_created:
        seed += 1
        random.seed(seed)
        matrix = [[np.random.choice(['x']+[i for i in range(1, max_traffic)], 
                                    p=[0.5] + [0.5/(max_traffic-1) for i in range(1, max_traffic)]) 
                for _ in range(edge_length)] for _ in range(edge_length)]
        
        district_1_last_row = random.randint(1, edge_length//3)
        district_2_last_row = random.randint(edge_length//3+1, 2 * edge_length//3)
        
        # Randomly choose start and end indices 
        #start and end in D2 
        start = (random.randint(district_1_last_row, district_2_last_row + 1), random.randint(0, edge_length-1))
        end = (random.randint(district_1_last_row, district_2_last_row + 1), random.randint(0, edge_length-1))
        while abs(start[0] - end[0]) + abs(start[1] - end[1]) < edge_length:
            seed += 1
            random.seed(seed)
            start = (random.randint(district_1_last_row, district_2_last_row + 1), random.randint(0, edge_length-1))
            end = (random.randint(district_1_last_row, district_2_last_row + 1), random.randint(0, edge_length-1))

        # Create a stack for DFS algorithm
        stack = []
        stack.append(start)

        # Create a set to store visited cells
        visited = set()
        visited.add(start)
        len_path = 0
        
        visited_d1 = False
        visited_d2 = False
        visited_d3 = False

        # Directions for moving up, down, left, right. Make going up int he path more probable
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        while stack:
            seed += 1
            random.seed(seed)
            current = stack[-1]
            len_path += 1
            randint = random.randint(1, max_traffic)
            matrix[current[0]][current[1]] = str(randint)
            
            if 0 <= current[0] <= district_1_last_row:
                visited_d1 = True
            elif district_1_last_row < current[0] <= district_2_last_row:
                visited_d2 = True
            elif district_2_last_row < current[0] <= edge_length - 1:
                visited_d3 = True
                
            
            # Check if we reached the destination
            if current == end and visited_d1 and visited_d2 and visited_d3:
                #path must be relatively efficient
                if len_path <= 2 * edge_length + 2:
                    path_created = True
                break

            # Get the list of unvisited neighbors
            neighbors = [(current[0] + d[0], current[1] + d[1]) for d in directions
                        if 0 <= current[0] + d[0] < edge_length and 0 <= current[1] + d[1] < edge_length and
                        (current[0] + d[0], current[1] + d[1]) not in visited]

            if neighbors:
                # Choose a random neighbor and add it to the stack
                next_cell = random.choice(neighbors)
                stack.append(next_cell)
                visited.add(next_cell)
            else:
                # If there are no unvisited neighbors, pop the current cell from the stack
                stack.pop()

    return matrix, start, end, district_1_last_row, district_2_last_row"""
    

def generate(edge_length, seed):
    max_traffic = 20
    path_created = False
    while not path_created:
        seed += 1
        random.seed(seed)
        np.random.seed(seed)
        matrix = [[np.random.choice(['x']+[i for i in range(1, max_traffic)], 
                                    p=[0.5] + [0.5/(max_traffic-1) for i in range(1, max_traffic)]) 
                for _ in range(edge_length)] for _ in range(edge_length)]
        
        district_1_last_row = random.randint(1, edge_length//3)
        district_2_last_row = random.randint(edge_length//3+1, 2 * edge_length//3)
        
        start = (random.randint(district_1_last_row, district_2_last_row + 1), random.randint(0, edge_length-1))
        end = (random.randint(district_1_last_row, district_2_last_row + 1), random.randint(0, edge_length-1))
        while abs(start[0] - end[0]) + abs(start[1] - end[1]) < edge_length:
            seed += 1
            random.seed(seed)
            start = (random.randint(district_1_last_row, district_2_last_row + 1), random.randint(0, edge_length-1))
            end = (random.randint(district_1_last_row, district_2_last_row + 1), random.randint(0, edge_length-1))

        stack = []
        stack.append(start)

        visited = set()
        visited.add(start)
        len_path = 0

        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        
        # Create a dictionary to store the parent of each cell
        parent = {start: None}

        while stack:
            seed += 1
            random.seed(seed)
            current = stack[-1]
            len_path += 1
            randint = random.randint(1, max_traffic)
            matrix[current[0]][current[1]] = str(randint)
            
                
            if current == end:
                if len_path <= 2 * edge_length + 2:
                    path_created = True
                break

            neighbors = [(current[0] + d[0], current[1] + d[1]) for d in directions
                        if 0 <= current[0] + d[0] < edge_length and 0 <= current[1] + d[1] < edge_length and
                        (current[0] + d[0], current[1] + d[1]) not in visited]

            if neighbors:
                next_cell = random.choice(neighbors)
                stack.append(next_cell)
                visited.add(next_cell)
                # Store the current cell as the parent of the next cell
                parent[next_cell] = current
            else:
                stack.pop()

        # Backtrack from the end cell to the start cell to get the path
        path = []
        current = end
        while current is not None:
            path.append(current)
            current = parent[current]
        path.reverse()
        
        visited_d1 = False
        visited_d2 = False
        visited_d3 = False
        for coord in path:
            if 0 <= coord[0] <= district_1_last_row:
                visited_d1 = True
            elif district_1_last_row < coord[0] <= district_2_last_row:
                visited_d2 = True
            elif district_2_last_row < coord[0] <= edge_length - 1:
                visited_d3 = True
                
        if not (visited_d1 and visited_d2 and visited_d3):
            path_created = False
        
        
    #print(matrix_to_string(matrix), start, end, district_1_last_row, district_2_last_row, path)
    return matrix, start, end, district_1_last_row, district_2_last_row

def matrix_to_string(matrix):
    return '\n'.join(str(row).replace("'", "") for row in matrix)


"""# Test the function
start = (0, 0)
dest = (5, 5)
matrix, _, _, _, _ = generate(10, 1)
print(generate(10, 1))
print(matrix_to_string(matrix))"""

#print(generate(9, 1))


