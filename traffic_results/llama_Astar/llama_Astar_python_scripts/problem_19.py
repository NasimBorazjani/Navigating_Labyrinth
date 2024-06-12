
import heapq


def a_star():
   # Define the initial state of the city map as a 2d tuple
   city_map = [['x', 16, 15, 14, 2, 12, 3, 'x', 7, 7],
               [11, 'x', 'x', 'x', 4, 10, 5, 'x', 'x', 'x'],
               [12, 'x', 3, 'x', 'x', 19, 'x', 'x', 'x', 'x'],
               [16, 15, 13, 'x', 12, 'x', 'x', 1, 7],
               [2, 6, 'x', 5, 'x', 14, 7, 8, 18],
               [19, 17, 2, 11, 8, 17, 12, 8, 9, 14],
               [11, 1, 10, 11, 'x', 'x', 19, 6, 2, 18],
               [7, 'x', 10, 15, 'x', 'x', 'x', 'x', 18, 17],
               [11, 6, 'x', 'x', 'x', 5, 'x', 7, 12, 20],
               ['x', 'x', 2, 15, 'x', 17, 'x', 'x', 10, 11]]
   num_rows = 9
   num_cols = 10
   start = (5, 0)
   end = (3, 9)
   districts = [(0, 3), (4, 5), (6, 9)]


   # Initialize a dictionary to store the cost of reaching each visited state
   visited_costs = {}
   visited_costs[start] = 0


   # Initialize a priority queue of states not yet visited, with the initial state as the first element. The priority of each element is the cost to reach that state (g) + the estimate remaining cost (h) to reach the goal
   # Record the path taken to reach each state in a list; no path performed to reach the initial state
   queue = [(0, 0, [start], start)]


   # While there are un-visited states
   while queue:
       # Pop the state with the lowest sum of the cost so far and estimated cost to the goal from the queue
       _, g, path, current = heapq.heappop(queue)


       # Check if the current state is the goal state
       if current == end:
           return path


       # Generate all possible actions from the current state, which includes moving to any of the 4 directions (north, south, east, west)
       for d_row, d_col in [(0, -1), (0, 1), (1, 0), (-1, 0)]:
           new_row, new_col = current[0] + d_row, current[1] + d_col
           # Check if the new state would be valid, ie the new position is within the bounds of the city map and there's no x in that position
           if 0 <= new_row < num_rows and 0 <= new_col < num_cols and city_map[new_row][new_col] != 'x':
               # The new state is valid, generate the new state
               new_state = (new_row, new_col)
               # The cost so far is the number of moves made, as the task is to minimize the number of moves required to reach the goal state
               new_cost = g + city_map[new_row][new_col]


               # If the new state is unvisited or we found a new path with a lower cost to reach this state, add it to the queue of un-visited states
               if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                   visited_costs[new_state] = new_cost
                   # Check if the new state satisfies the constraint of visiting at least 1 workshop in each district
                   if any(district[0] <= new_row <= district[1] for district in districts):
                       heapq.heappush(queue, (new_cost + heuristic(new_state, end), new_cost, path + [new_state], new_state))
   return None


def heuristic(state, goal):
   # An admissible and consistent heuristic is the Manhattan distance between the current state and the goal state
   # This heuristic relaxes the constraint that Ben can only move to a workshop in the same district
   # It is admissible because it never overestimates the cost to reach the goal, as the Manhattan distance is a lower bound on the actual cost
   # It's consistent because moving to a workshop in a different district increases the heuristic cost of the successor node by a max of 1 (if the moved workshop is in a different district), which is equal to the cost of reaching the successor node
   return abs(state[0] - goal[0]) + abs(state[1] - goal[1])


print(a_star())
