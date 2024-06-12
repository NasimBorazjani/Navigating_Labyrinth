import heapq
import sys

def a_star(city, initial_coordinate, goal_coordinate,
           district_1_last_row, district_2_last_row):
    
    city =  [[int(i) if i != 'x' else 'x' for i in row] for row in city]
    num_rows = len(city) 
    num_cols = len(city[0])
    
    visited_d1 = False
    visited_d2 = False
    visited_d3 = False
    if 0 <= initial_coordinate[0] <= district_1_last_row:
        visited_d1 = True
    elif district_1_last_row < initial_coordinate[0] <= district_2_last_row:
        visited_d2 = True
    elif district_2_last_row < initial_coordinate[0] <= num_rows - 1:
        visited_d3 = True
    
    initial_state = (initial_coordinate, visited_d1, visited_d2, visited_d3)
    visited_costs = {}
    visited_costs[initial_state] = 0
            
    # Ben has already visited the initial_coordinate, so it must be added to his path
    queue = [(0, 0, [initial_coordinate], (initial_coordinate, visited_d1, visited_d2, visited_d3))]

    while queue:
        _, g, path, state = heapq.heappop(queue)
        
        state_coord, visited_d1, visited_d2, visited_d3 = state

        if state_coord == goal_coordinate and visited_d1 and visited_d2 and visited_d3:
            return path

        # Generate all possible actions from the current state, which includes moving to any of the 4 neighboring workshops
        for d_row, d_col in [(0, -1), (0, 1), (1, 0), (-1, 0)]:
            new_row, new_col = state_coord[0] + d_row, state_coord[1] + d_col
            # Check if the new position is valid, ie if the new workshop is in the city and it is not closed 
            if 0 <= new_row < num_rows and 0 <= new_col < num_cols and city[new_row][new_col] != 'x':
                visited_d1_new = state[1]
                visited_d2_new = state[2]
                visited_d3_new = state[3]
                if 0 <= new_row <= district_1_last_row:
                    visited_d1_new = True
                elif district_1_last_row < new_row <= district_2_last_row:
                    visited_d2_new = True
                elif district_2_last_row < new_row <= num_rows - 1:
                    visited_d3_new = True
                new_state = ((new_row, new_col), visited_d1_new, visited_d2_new, visited_d3_new)
                new_cost = g + int(city[new_row][new_col])

                if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                    visited_costs[new_state] = new_cost
                    heapq.heappush(queue, (g + heuristic(new_state[0], goal_coordinate), new_cost, path + [new_state[0]], new_state))
    return None

def heuristic(state, goal):
    # The heuristic function is the Manhattan distance from the current workshop to the goal workshop
    return abs(state[0] - goal[0]) + abs(state[1] - goal[1])

def main():
    # Read the initial state from the command line
    city = eval(sys.argv[1])
    initial_coordinate = eval(sys.argv[2])
    goal_coordinate =  eval(sys.argv[3])
    district_1_last_row = eval(sys.argv[4])
    district_2_last_row =  eval(sys.argv[5])
    print(a_star(city, initial_coordinate, goal_coordinate,
           district_1_last_row, district_2_last_row))

if __name__ == "__main__":
    main()
    
