import heapq
import sys

def a_star(grid, initial_coordinate, goal_coordinate,
           num_diag_moves_req):
    
    num_rows = len(grid) 
    num_cols = len(grid[0])

    visited_costs = {}
    visited_costs[initial_coordinate] = 0
    
    queue = [(0, 0, [initial_coordinate], (initial_coordinate, 0))]

    while queue:
        _, g, path, state = heapq.heappop(queue)
        
        state_coord, num_diag_moves_made = state

        if state_coord == goal_coordinate:
            return path

        # Generate all possible actions from the current state, which includes moving to any of the 4 neighboring workshops
        if num_diag_moves_made < num_diag_moves_req:
            directions = [(0, 1), (0, -1), (1, 0), (1, -1), (1, 1), (-1, 0), (-1, 1), (-1, -1)]
            diagonal_directions = [(1, -1), (1, 1), (-1, 1), (-1, -1)]
        else:
            diagonal_directions = []
            directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        for d_row, d_col in directions:
            new_row, new_col = state_coord[0] + d_row, state_coord[1] + d_col
            # Check if the new position is valid, ie if the new workshop is in the city and it is not closed 
            if 0 <= new_row < num_rows and 0 <= new_col < num_cols and grid[new_row][new_col] != 1:
                if (d_row, d_col) in diagonal_directions:
                    num_diag_moves_made_new = num_diag_moves_made +1
                else:
                    num_diag_moves_made_new = num_diag_moves_made 
                new_state = ((new_row, new_col), num_diag_moves_made_new)
                new_cost = g + 1

                if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                    visited_costs[new_state] = new_cost
                    heapq.heappush(queue, (new_cost + heuristic(new_state[0], goal_coordinate), new_cost, path + [new_state[0]], new_state))
    return None

def heuristic(state, goal):
    # as a lower bound consider all diagonal moves are possible
    return max(abs(state[0] - goal[0]), abs(state[1] - goal[1]))

def main():
    # Read the initial state from the command line
    city = eval(sys.argv[1])
    initial_coordinate = eval(sys.argv[2])
    goal_coordinate =  eval(sys.argv[3])
    num_diag_moves_req = eval(sys.argv[4])
    print(a_star(city, initial_coordinate, goal_coordinate,
          num_diag_moves_req))

if __name__ == "__main__":
    main()
    
