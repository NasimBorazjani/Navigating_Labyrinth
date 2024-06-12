
import heapq


def a_star():
   # Define the initial state of the city map as a 2d tuple
   city_map = [['x', 9, 4, 8, 'x', 'x', 4, 'x', 8, 12, 'x', 'x', 14],
               [17, 'x', 3, 'x', 6, 'x', 12, 2, 'x', 'x', 'x', 5, 19],
               ['x', 8, 8, 'x', 5, 'x', 15, 14, 14, 3, 10, 12, 3],
               [4, 'x', 16, 'x', 'x', 11, 12, 'x', 'x', 6, 5, 18, 19],
               ['x', 4, 9, 17, 'x', 'x', 'x', 13, 4, 7, 'x', 2, 16],
               [3, 6, 'x', 'x', 'x', 10, 5, 'x', 18, 10, 9, 20, 4],
               ['x', 'x', 'x', 14, 18, 'x', 'x', 'x', 'x', 16, 'x', 'x', 4],
               [14, 12, 'x', 4, 12, 11, 19, 'x', 3, 2, 'x', 13, 'x'],
               [19, 6, 2, 18, 'x', 'x', 8, 7, 1, 12, 19, 'x', 'x'],
               ['x', 9, 16, 17, 5, 12, 19, 8, 'x', 3, 10, 'x', 'x'],
               ['x', 10, 3, 'x', 14, 16, 2, 16, 4, 10, 18, 15, 'x'],
               ['x', 5, 5, 'x', 13, 'x', 3, 7, 'x', 4, 1, 17, 15],
               [5, 2, 6, 'x', 'x', 'x', 'x', 8, 16, 'x', 'x', 'x', 'x']]
   num_rows = 12
   num_cols = 12
   start = (7, 1)
   end = (2, 10)
   districts = [(0, 2), (3, 7), (8, 12)]


   # Initialize a dictionary to store the cost of reaching each visited state
   visited_costs = {}
   visited_costs[start] = 0


   # Initialize a priority queue of states not yet visited, with the initial state as the first element. The priority of each element is the cost to reach that state (g) + the estimate remaining cost (h) to reach the goal
   # Record the path taken to reach each state in a list; no path performed to reach the initial state
   queue = [(0, 0, [], start)]


   # While there are un-visited states
   while queue:
       # Pop the state with the lowest sum of the cost so far and estimated cost to the goal from the queue
       _, g, actions, state = heapq.heappop(queue)


       # Check if the current state is the goal state
       if state == end:
           return actions


       # Generate all possible actions from the current state, which includes moving to any of the 4 neighboring workshops if it's not an 'x' and not in a different district
       for d_row, d_col in [(0, -1), (0, 1), (1, 0), (-1, 0)]:
           new_row, new_col = state[0] + d_row, state[1] + d_col
           # Check if the new state would be valid, ie if the new workshop is within the city map, not an 'x', and in the same district as the current workshop
           if (0 <= new_row < num_rows and 0 <= new_col < num_cols and
               city_map[new_row][new_col] != 'x' and
               any(districts[i][0] <= new_row <= districts[i][1] for i in range(len(districts)) if districts[i][0] <= state[0] <= districts[i][1])):
               # Generate the new state
               new_state = (new_row, new_col)
               # The cost so far is the number of workshops visited, as the task is to minimize the number of workshops visited to reach the goal state
               new_cost = g + 1
              
               # If the new state is unvisited or we found a new path with a lower cost to reach this state, add it to the queue of not-yet-visited states
               if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                   visited_costs[new_state] = new_cost
                   heapq.heappush(queue, (new_cost + heuristic(new_state, end, city_map), new_cost, actions + [new_state], new_state))
                  
   return None


def heuristic(state, goal, city_map):
   # An admissible and consistent heuristic is the sum of the Manhattan distances (the shortest path) of each workshop from its goal position
   # The heuristic relaxes the constraint that a workshop can only be visited if it's in the same district as the current workshop
   # Thus the heuristic reports a lower estimate on the cost to reach goal state and is admissible
   # The heuristic is consistent because the cost of moving a workshop to a neighboring coordinate is always 1, which is exactly the decrease in the Manhattan distance, if the workshop is moved toward its goal position, otherwise the estimated cost of the successor node is the same or higher, and he heuristic estimate for the goal state is 0, as the distance of each workshop from its goal position would be 0 in the goal state.
   h = abs(state[0] - goal[0]) + abs(state[1] - goal[1])
   return h


print(a_star())
