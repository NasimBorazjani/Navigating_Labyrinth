
import heapq


def a_star():
   # Define the initial state of the city map as a 2d tuple
   city_map = [['x', 18, 'x', 5, 'x', 6, 5, 'x', 6, 17, 'x'],
               ['x', 'x', 1, 5, 9, 13, 'x', 2, 'x', 'x', 2],
               ['x', 17, 12, 'x', 'x', 'x', 5, 'x', 'x', 17, 'x'],
               [9, 3, 13, 8, 'x', 7, 'x', 'x', 4, 2, 'x'],
               [11, 17, 'x', 10, 'x', 'x', 'x', 17, 15, 11],
               ['x', 10, 10, 14, 9, 7, 1, 5, 'x', 'x', 7],
               ['x', 5, 6, 12, 8, 9, 4, 'x', 'x', 4, 9],
               ['x', 4, 13, 14, 'x', 12, 17, 13, 'x', 'x', 'x'],
               ['x', 8, 'x', 19, 11, 7, 7, 19, 15, 14, 7],
               [11, 8, 'x', 11, 10, 16, 'x', 'x', 9, 'x', 5],
               [9, 4, 'x', 'x', 1, 11, 14, 'x', 'x', 'x', 10]]
   num_rows = 10
   num_cols = 11
   start = (7, 8)
   end = (2, 1)
   districts = [(0, 2), (3, 7), (8, 10)]


   # Initialize a dictionary to store the cost of reaching each visited state
   visited_costs = {}
   visited_costs[start] = 0


   # Initialize a priority queue of states not yet visited, with the start state as the first element. The priority of each element is the cost to reach that state (g) + the estimate remaining cost (h) to reach the end
   # Record the path taken to reach each state in a list; no path taken to reach the start state
   queue = [(0, 0, [], start)]


   # While there are un-visited states
   while queue:
       # Pop the state with the lowest sum of the cost so far and estimated cost to the end from the queue
       _, g, actions, state = heapq.heappop(queue)


       # Check if the current state is the end state
       if state == end:
           return actions


       # Generate all possible actions from the current state, which includes moving to any of the 4 neighboring workshops if it's not an 'x' and the district of the current workshop is visited at least once
       for d_row, d_col in [(0, -1), (0, 1), (1, 0), (-1, 0)]:
           new_row, new_col = state[0] + d_row, state[1] + d_col
           # Check if the new state would be valid, ie if the new workshop is within the bounds of the city and is not an 'x'
           if 0 <= new_row < num_rows and 0 <= new_col < num_cols and city_map[new_row][new_col] != 'x':
               # Check if the district of the new workshop has been visited at least once
               if any(districts[i][0] <= new_row <= districts[i][1] for i in range(len(districts)) if i not in actions):
                   # The actions is valid, generate the new state
                   new_state = (new_row, new_col)
                   # The cost so far is the number of workshops visited, as our objective is to minimize the number of workshops visited to reach the end state
                   new_cost = g + 1
                  
                   # If the new state is unvisited or we found a new path with a lower cost to reach this state, add it to the queue of not-yet-visited states
                   if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                       visited_costs[new_state] = new_cost
                       heapq.heappush(queue, (new_cost + heuristic(new_state, end, city_map, districts), new_cost, actions + [new_state], new_state))
                      
   return None


def heuristic(state, end, city_map, districts):
   # An admissible and consistent heuristic is the sum of the Manhattan distances (the shortest path) of each district from the current state to the end state
   # The heuristic relaxes the constraint that a district must be visited at least once
   # Thus the heuristic reports a lower estimate on the cost to reach the end state and is admissible
   # The heuristic is consistent because the cost of moving a district to a neighboring district is always 1, which is exactly the decrease in the Manhattan distance, if the district is moved towards the end state, otherwise the estimated cost of the successor node is the same or higher, and he heuristic estimate for the end state is 0, as the distance of each district from the end state would be 0 in the end state.
   h = 0
   for district in districts:
       # Get the district of the current state
       current_district = next(i for i in range(len(districts)) if districts[i][0] <= state[0] <= districts[i][1])
       # Add the the Manhattan distance of the current and end districts to the estimate
       h += abs(district[0] - end[0]) + abs(district[1] - end[1])
   return h


print(a_star())
