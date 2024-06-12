
import heapq


def a_star():
   # Define the initial state of the city map as a 2d tuple
   city_map = [['x', 'x', 6, 'x', 'x', 'x', 15, 'x', 'x'],
               ['x', 17, 13, 13, 'x', 12, 'x', 3, 10, 2],
               ['x', 5, 13, 15, 4, 'x', 'x', 20, 6, 2],
               ['x', 9, 'x', 6, 2, 16, 18, 9, 13, 'x'],
               ['x', 'x', 15, 17, 'x', 10, 11, 'x', 'x', 'x'],
               [3, 'x', 3, 17, 8, 'x', 1, 16, 'x'],
               ['x', 'x', 13, 15, 'x', 'x', 11, 'x', 'x', 4],
               ['x', 'x', 12, 1, 'x', 'x', 'x', 14, 11, 'x'],
               ['x', 14, 'x', 'x', 19, 13, 4, 'x', 'x', 'x'],
               [1, 'x', 'x', 14, 11, 19, 2, 17, 2, 5]]
   num_rows = 10
   num_cols = 10
   start = (2, 9)
   end = (5, 2)
   districts = [(0, 2), (3, 4), (5, 9)]


   # Initialize a dictionary to store the cost of reaching each visited state
   visited_costs = {}
   visited_costs[start] = 0


   # Initialize a priority queue of states not yet visited, with the start state as the first element. The priority of each element is the cost to reach that state (g) + the estimate remaining cost (h) to reach the end
   # Record the workshops visited in a list; no workshops visited to reach the start state
   queue = [(0, 0, [], start)]


   # While there are un-visited states
   while queue:
       # Pop the state with the lowest sum of the cost so far and estimated cost to the end from the queue
       _, g, actions, state = heapq.heappop(queue)


       # Check if the current state is the end state
       if state == end:
           return actions


       # Generate all possible actions from the current state, which includes moving to any of the 4 directions (north, south, east, west) from the current state, provided there's no 'x' in that direction
       for d_row, d_col in [(0, -1), (0, 1), (1, 0), (-1, 0)]:
           new_state = (state[0] + d_row, state[1] + d_col)
           # Check if the new state is valid, ie within the bounds of the city map and not a closed workshop
           if (0 <= new_state[0] < num_rows and 0 <= new_state[1] < num_cols and city_map[new_state[0]][new_state[1]] != 'x'):
               # The cost so far is the number of workshops visited, as the task is to minimize the number of workshops visited to reach the end state
               new_cost = g + 1
              
               # Check if the new state has visited at least 1 workshop in each district
               if all(start_row <= new_state[0] <= end_row for start_row, end_row in districts):
                   # If the new state is unvisited or we found a new path with a lower cost to reach this state, add it to the queue of un-visited states
                   if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                       visited_costs[new_state] = new_cost
                       heapq.heappush(queue, (new_cost + heuristic(new_state, end), new_cost, actions + [new_state], new_state))
                      
   return None


def heuristic(state, end):
   # An admissible and consistent heuristic is the Euclidean distance from the current state to the end state
   # This heuristic is admissible because it never overestimates the cost to reach the goal, as the Euclidean distance is a lower bound on the actual path length
   # It is consistent because moving to a neighboring state always increases the heuristic cost of the successor node by a value greater than or equal to the cost of reaching the successor node
   # Thus h(s) is always less than or equal to c(s, n)(equal to 1) + h(n)
   return math.sqrt((state[0] - end[0]) ** 2 + (state[1] - end[1]) ** 2)


print(a_star())
