
import heapq


def a_star():
   # Define the initial state of the city map as a 2d tuple
   city_map = [['x', 10, 2, 'x', 'x', 'x', 3, 'x', 4, 'x', 14],
               ['x', 'x', 17, 16, 8, 'x', 'x', 'x', 'x', 1, 'x'],
               [18, 18, 16, 16, 15, 'x', 'x', 17, 12, 16, 15],
               ['x', 4, 'x', 'x', 18, 9, 'x', 15, 'x', 1, 9],
               [3, 2, 7, 'x', 'x', 17, 2, 14, 'x', 4, 2],
               [16, 17, 6, 4, 9, 2, 5, 7, 'x', 'x', 7],
               ['x', 'x', 12, 'x', 'x', 16, 1, 11, 'x', 'x', 4],
               ['x', 'x', 13, 'x', 'x', 19, 16, 9, 'x', 'x', 'x'],
               ['x', 'x', 'x', 9, 7, 'x', 11, 5, 'x', 'x', 'x'],
               ['x', 2, 'x', 'x', 'x', 4, 5, 'x', 10, 'x', 'x'],
               ['x', 'x', 'x', 12, 16, 'x', 6, 16, 'x', 18, 7]]
   num_rows = 10
   num_cols = 11
   start = (3, 10)
   end = (6, 2)
   districts = [(0, 3), (4, 5), (6, 10)]


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


       # Generate all possible actions from the current state, which includes moving to any of the 4 neighboring workshops if it's not an 'x' and the district of the current workshop is visited
       for d_row, d_col in [(0, -1), (0, 1), (1, 0), (-1, 0)]:
           new_row, new_col = state[0] + d_row, state[1] + d_col
           # Check if the new state would be valid, ie if the new workshop is within the bounds of the city map and is not an 'x'
           if 0 <= new_row < num_rows and 0 <= new_col < num_cols and city_map[new_row][new_col] != 'x':
               # Check if the district of the new workshop has been visited
               if any(start[0] <= new_row <= end[0] for start, end in districts):
                   # Generate the new state
                   new_state = (new_row, new_col)
                   # The cost so far is the number of workshops visited, as the task is to minimize the number of workshops visited to reach the end state
                   new_cost = g + 1


                   # If the new state is unvisited or we found a new path with a lower cost to reach this state, add it to the queue of not-yet-visited states
                   if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                       visited_costs[new_state] = new_cost
                       heapq.heappush(queue, (new_cost + heuristic(new_state, end), new_cost, actions + [new_state], new_state))
                      
   return None


def heuristic(state, end):
   # An admissible and consistent heuristic is the Euclidean distance between the current state and the end state
   # This heuristic relaxes the constraint that Ben can only move to neighboring workshops
   # It is admissible because it never overestimates the cost to reach the goal, as the Euclidean distance is a lower bound on the actual travel time
   # It's consistent because moving to a neighboring workshop reduces the heuristic cost of the successor node by a max of 1 (if the moved workshop is closer to the end workshop), which is equal to the cost of reaching the successor node
   return math.sqrt((state[0] - end[0]) ** 2 + (state[1] - end[1]) ** 2)


print(a_star())
