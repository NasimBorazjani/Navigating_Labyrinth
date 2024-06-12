
import heapq


def a_star():
   # Define the initial state of the city map as a 2d tuple
   city_map = [['x', 12, 'x', 'x', 'x', 5, 9, 14, 6, 'x', 3, 14, 'x'],
               ['x', 'x', 3, 'x', 11, 'x', 13, 'x', 'x', 'x', 9, 8],
               ['x', 18, 'x', 'x', 'x', 13, 4, 5, 'x', 'x', 'x', 'x', 13, 'x'],
               [10, 4, 'x', 'x', 'x', 'x', 'x', 18, 'x', 15, 'x', 'x', 'x'],
               ['x', 1, 7, 'x', 7, 6, 'x', 3, 'x', 2, 'x', 'x', 5],
               ['x', 15, 5, 'x', 'x', 10, 'x', 19, 'x', 'x', 'x', 10, 6],
               ['x', 18, 1, 2, 'x', 7, 16, 19, 'x', 'x', 10, 8, 8],
               [8, 'x', 'x', 6, 2, 'x', 'x', 7, 11, 5, 11, 2],
               ['x', 4, 1, 1, 5, 12, 3, 6, 2, 1, 'x', 3, 8],
               ['x', 'x', 5, 5, 14, 15, 7, 'x', 'x', 11, 'x', 7, 9],
               ['x', 6, 12, 16, 17, 'x', 'x', 4, 'x', 19, 9, 5, 'x'],
               [12, 'x', 4, 'x', 8, 4, 'x', 5, 'x', 'x', 5, 'x']]
   num_rows = len(city_map)
   num_cols = len(city_map[0])
   start = (6, 12)
   end = (4, 1)
   districts = [(0, 4), (5, 5), (6, 12)]


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


       # Generate all possible actions from the current state, which includes moving to any of the 4 neighboring workshops if it's not an 'x' and has not been visited yet
       for d_row, d_col in [(0, -1), (0, 1), (1, 0), (-1, 0)]:
           new_row, new_col = state[0] + d_row, state[1] + d_col
           if (0 <= new_row < num_rows and 0 <= new_col < num_cols and
               city_map[new_row][new_col] != 'x' and
               (new_row, new_col) not in actions):
               # Check if the new state would be valid, ie the new workshop is in the same district as the current workshop
               if any(district[0] <= new_row < district[1] for district in districts):
                   # Generate the new state
                   new_state = (new_row, new_col)
                   # The cost so far is the number of workshops visited, as the task is to minimize the number of workshops visited to reach the goal state
                   new_cost = g + 1
                  
                   # If the new state is unvisited or we found a new path with a lower cost to reach this state, add it to the queue of un-visited states
                   if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                       visited_costs[new_state] = new_cost
                       heapq.heappush(queue, (new_cost + heuristic(new_state, end, city_map), new_cost, actions + [new_state], new_state))
   return None


def heuristic(state, goal, city_map):
   # An admissible and consistent heuristic for this problem is the Manhattan distance between the current state and the goal state
   # This heuristic relaxes the constraint that Ben can only move to workshops in the same district
   # It is admissible because it never overestimates the cost to reach the goal, as the Manhattan distance is a lower bound on the actual cost
   # It's consistent because moving to a workshop in a different district increases the heuristic cost of the successor node by a max of 1 (if the new workshop is in a different district but the same row or column), which is equal to the cost of reaching the successor node
   # Thus h(s) is always less than or equal to c(s, n)(equal to 1) + h(n)
   return abs(state[0] - goal[0]) + abs(state[1] - goal[1])


print(a_star())
