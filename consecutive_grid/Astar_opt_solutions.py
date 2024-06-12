import heapq
import math
import numpy as np
import sys

def a_star(initial_state, min_number, max_number):
    num_rows = len(initial_state)
    num_cols = len(initial_state[0])
    initial_state =  [[int(i) if i != "" else 'x' for i in row] for row in initial_state]
    initial_state = tuple(tuple(row) for row in initial_state)

    numbers = set(range(min_number, max_number))


    visited_costs = {}
    visited_costs[initial_state] = 0

    queue = [(0, 0, [], initial_state)]

    while queue:
        _, g, actions, state = heapq.heappop(queue)

        # The goal state must not have any unknown numbers, thus we need to get (the coordinates of) the unknown numbers to check wether the current state is the goal state 
        x_coords = [(i, j) for i, row in enumerate(state) for j, element in enumerate(row) if element == 'x']
        if not x_coords:
            # Convert the cells of the state to ints to calulate and compare the sum of the specifiec positions in the current state with the given goal sums
            if ((all(row[i] < row[i+1] for i in range(len(row)-1)) or all(row[i] > row[i+1] for i in range(len(row)-1)) for row in state)
                and (all(col[i] < col[i+1] for i in range(len(col)-1)) or all(col[i] > col[i+1] for i in range(len(col)-1)) for col in zip(*state))):
                return actions

        # If the state has at least 1 remaining unknown number, generate all possible actions from the current state, which includes replacing the next x in the grid with any of unique integers in the range 
        else:
            first_x_coord = x_coords[0]
            # The number must be unique and not be present in any other cells of the grid
            used_numbers  = set(int(cell) for row in state for cell in row if cell != 'x')
            available_numbers = sorted(list(numbers - used_numbers))
            for number in available_numbers:
               
                new_state = [list(row[:]) for row in state]
                new_state[first_x_coord[0]][first_x_coord[1]] = number
                
                is_valid = True
                for row in new_state:
                    row = list(filter(lambda x: x != 'x', row))
                    if not (all(row[i] < row[i+1] for i in range(len(row)-1)) or all(row[i] > row[i+1] for i in range(len(row)-1))):
                        is_valid = False
                        break
                
                if is_valid:
                    for col in zip(*new_state):
                        col = list(filter(lambda x: x != 'x', col))
                        if not (all(col[i] < col[i+1] for i in range(len(col)-1)) or all(col[i] > col[i+1] for i in range(len(col)-1))):
                            is_valid = False
                            break
                
                if is_valid:
                
                    # Generate the new state 
                    new_state = tuple(tuple(row) for row in new_state)
                    # The additional cost of this state is the value of the number replaced with x as we are trying to minimize the sum of the numbers in the grid
                    new_cost = g
                    if first_x_coord[0] == 0:
                        new_cost += number
                    if first_x_coord[1] == num_cols - 1:
                        new_cost += number
                    if first_x_coord[0] == first_x_coord[1]:
                        new_cost += number
                     
                    if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                        visited_costs[new_state] = new_cost
                        # Relaxing the constraints on the columns sums and the diagonal sum to calculate the heuristic
                        h = heuristic(new_state, numbers)
                        heapq.heappush(queue, (new_cost + h, new_cost, actions + [(first_x_coord[0], first_x_coord[1], number)], new_state))
    return None


def heuristic(state, numbers):
    state = [list(row[:]) for row in state]
    used_numbers = set(int(cell) for row in state for cell in row if cell != 'x')
    available_numbers = sorted(list(numbers - used_numbers))
    h = 0
    
    #first iterate though cells that appear twice in the cost
    if state[0][0] == 'x':
        next_smallest_num = available_numbers.pop(0)
        h += 2*next_smallest_num
        state[0][0] = next_smallest_num
        
    if state[0][-1] == 'x':
        next_smallest_num = available_numbers.pop(0)
        h += 2*next_smallest_num
        state[0][-1] = next_smallest_num
    
    if state[-1][-1] == 'x':
        next_smallest_num = available_numbers.pop(0)
        h += 2*next_smallest_num
        state[-1][-1] = next_smallest_num
        
            
            
    for i in range(len(state)):
        for j in range(len(state[0])):
            if i == 0 or j == len(state[0]) - 1 or i == j:
                if state[i][j] == 'x':
                    next_smallest_num = available_numbers.pop(0)
                    if i == 0:
                        h += next_smallest_num
                    if j == len(state[0]) - 1:
                        h += next_smallest_num
                    if i == j:
                        h += next_smallest_num
                    
    return h

import time
def main():
    # Read the initial state from the command line
    
    initial_state = eval(sys.argv[1])
    min_number = eval(sys.argv[2])
    max_number = eval(sys.argv[3])
    
    s = time.time()
    print(a_star(initial_state, min_number, max_number))
    e = time.time()
    #print(e-s)

if __name__ == "__main__":
    main()
    
