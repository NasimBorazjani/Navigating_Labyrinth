import heapq


def a_star():
    # Define the city, encoding travel times as integers and closed workshops as 'x'
    city = [[19, 'x', 1, 'x', 2, 17, 'x', 'x', 'x'],
            ['x', 'x', 14, 'x', 11, 'x', 'x', 18, 'x'],
            [19, 'x', 19, 7, 'x', 6, 'x', 'x', 'x'],
            [6, 'x', 'x', 3, 'x', 8, 10, 'x', 16],
            [3, 7, 'x', 14, 'x', 10, 9, 6, 15],
            [13, 'x', 6, 1, 'x', 'x', 'x', 12, 14],
            ['x', 8, 5, 16, 14, 'x', 10, 5, 16],
            [18, 4, 9, 1, 11, 9, 9, 18, 13],
            ['x', 'x', 16, 13, 16, 'x', 17, 'x', 11]]

    # Encoding other variables of the problem
    num_rows = 9
    num_cols = 9
    initial_coordinate = (3, 8)
    goal_coordinate = (6, 1)
    district_1_last_row = 3
    district_2_last_row = 5

    # The information we must encode for each state includes Ben's current coordinate and wether or not he has visited any of the 3 districts on his path to the current workshop in the following format: (state_coordinate, visited_d1, visited_d1, visited_d2, visited_d3)
    # Since the initial coordinate is in district 1 (in row 3 which is the last row of district 1), we must set visited_d1 to True 
    initial_state = (initial_coordinate, True, False, False)
    
    visited_costs = {}
    visited_costs[initial_state] = 0
    
    # Ben has already visited the initial_coordinate, so it must be added to his path
    queue = [(0, 0, [initial_coordinate], initial_state)]
    
    while queue:
        _, g, path, state = heapq.heappop(queue)

        # Unpack the information encoded in each state
        state_coord, visited_d1, visited_d2, visited_d3 = state

        # If Ben's current coordinate is the goal coordinate, and he has visited all 3 districts on his path to the goal coordinate, return his path
        if state_coord == goal_coordinate and visited_d1 and visited_d2 and visited_d3:
            return path

        # Generate all possible actions from the current state, which includes moving to any of the 4 neighboring workshops
        for d_row, d_col in [(0, -1), (0, 1), (1, 0), (-1, 0)]:
            new_row, new_col = state_coord[0] + d_row, state_coord[1] + d_col
            # Check if the new coordinate is valid, ie if the new workshop is within the bounds of the city and it is not closed
            if 0 <= new_row < num_rows and 0 <= new_col < num_cols and city[new_row][new_col] != 'x':
                # To generate the new state, we must update the districts that Ben has visited 
                # In the new state, the districts Ben visited will include all the districts from the current state, as well as the district where the new coordinate is located
                visited_d1_new = state[1]
                visited_d2_new = state[2]
                visited_d3_new = state[3]
                if 0 <= new_row <= district_1_last_row:
                    visited_d1_new = True
                elif district_1_last_row < new_row <= district_2_last_row:
                    visited_d2_new = True
                elif district_2_last_row < new_row <= num_rows - 1:
                    visited_d3_new = True
                # Generate the new state
                new_state = ((new_row, new_col), visited_d1_new, visited_d2_new, visited_d3_new)
                # Cost of the new state is the travel time to get to the new workshop in the city matrix
                new_cost = g + int(city[new_row][new_col])

                if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                    visited_costs[new_state] = new_cost
                    # The coordinate of the new state must be added to the path
                    heapq.heappush(queue, (g + heuristic(state_coord, goal_coordinate), new_cost, path + [new_state[0]], new_state))
    return None


def heuristic(state, goal):
    # An admissible and consistent heuristic for this problem is the Manhattan distance (shortest path) from the current workshop to the goal workshop
    # The heuristic relaxes the constraints that the travel time between different workshops is not the same, that we cannot travel through the workshops that are closed, and that Ben has to visit all 3 districts; ie It presumes we can move directly to any given coordinate toward the goal
    # Thus the heuristic reports a lower estimate on the cost of reaching the goal state and is admissible
    # The heuristic is consistent because the estimated cost from the current state to the goal can never be greater than the sum of cost from the current node to a successor node plus the estimated cost from the successor node to the goal because the cost of moving from one workshop to an adjacent workshop is the travel time between the workshops, which is always greater than or equal to 1, the decrease in the Manhattan distance
    return abs(state[0] - goal[0]) + abs(state[1] - goal[1])


print(a_star())