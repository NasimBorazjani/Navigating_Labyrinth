
import heapq


def a_star():
   # Define the initial state of the city map as a 2d tuple
   city_map = [['x', 11, 5, 18, 'x', 14, 7, 'x', 15, 11, 14],
               ['x', 'x', 'x', 'x', 13, 13, 11, 17, 8, 13, 'x'],
               ['x', 8, 1, 5, 17, 'x', 4, 8, 20, 7, 4],
               ['x', 10, 'x', 'x', 18, 1, 'x', 'x', 20, 'x', 'x'],
               [18, 15, 'x', 6, 'x', 4, 3, 4, 3, 13, 'x'],
               [5, 1, 'x', 4, 'x', 'x', 'x', 11, 'x', 14, 18],
               [19, 19, 'x', 'x', 'x', 'x', 15, 'x', 10, 'x', 'x'],
               [15, 5, 7, 'x', 14, 6, 'x', 'x', 'x', 13, 'x'],
               [18, 7, 'x', 19, 'x', 12, 'x', 'x', 15, 'x', 'x'],
               [10, 9, 'x', 1, 'x', 'x', 15, 'x', 11, 'x', 2],
               ['x', 'x', 8, 'x', 19, 1, 3, 'x', 'x', 8, 'x']]
   num_rows = 10
   num_cols = 11
   start = (7, 0)
   end = (3, 8)
   districts = [(0, 1), (2, 6), (7, 10)]


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
           # Check if the new state would be valid, ie if the new workshop is within the bounds of the city and is not an 'x'
           if 0 <= new_row < num_rows and 0 <= new_col < num_cols and city_map[new_row][new_col] != 'x':
               # Check if the district of the new workshop has been visited
               if any(districts[i][0] <= new_row <= districts[i][1] for i in range(len(districts)) if (districts[i][0], districts[i][1]) not in actions):
                   # The actions is valid, generate the new state
                   new_state = (new_row, new_col)
                   # The cost so far is the number of workshops visited, as our objective is to minimize the number of workshops visited to reach the end state
                   new_cost = g + 1
                  
                   # If the new state is unvisited or we found a new path with a lower cost to reach this state, add it to the queue of not-yet-visited states
                   if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                       visited_costs[new_state] = new_cost
                       heapq.heappush(queue, (new_cost + heuristic(new_state, end, city_map), new_cost, actions + [(new_row, new_col)], new_state))
                      
   return None


def heuristic(state, end, city_map):
   # An admissible and consistent heuristic is the Manhattan distance from the current state to the end state
   # This heuristic relaxes the constraint that Ben can only move to neighboring workshops
   # It is admissible because it never overestimates the cost to reach the goal, as each move is either horizontal or vertical
   # It's consistent because moving to a neighboring workshop increases the heuristic cost of the successor node by a max of 1 (if the moved workshop is in a different district), which is equal to the cost of reaching the successor node
   return abs(state[0] - end[0]) + abs(state[1] - end[1])


print(a_star())
