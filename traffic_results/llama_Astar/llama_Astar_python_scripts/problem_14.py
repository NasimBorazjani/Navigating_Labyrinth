
import heapq


def a_star():
   # Define the initial state of the city map as a 2d tuple
   city_map = [['x', 3, 13, 18, 'x', 'x', 3, 'x', 'x'],
               ['x', 3, 'x', 'x', 18, 1, 13, 'x', 'x'],
               ['x', 'x', 'x', 6, 'x', 13, 11, 1],
               [4, 3, 'x', 'x', 'x', 'x', 6, 6, 11],
               [14, 16, 'x', 'x', 'x', 'x', 18, 11],
               [14, 'x', 11, 'x', 'x', 4, 'x', 1, 'x'],
               [18, 7, 1, 'x', 8, 'x', 'x', 'x', 'x'],
               [4, 9, 6, 12, 13, 19, 'x', 14, 4],
               ['x', 'x', 17, 12, 7, 7, 9, 3, 1]]
   # Define the start and end positions
   start = (3, 1)
   end = (7, 8)
   # Define the districts
   districts = [(0, 3), (4, 6), (7, 8)]


   # Initialize a dictionary to store the cost of reaching each visited state
   visited_costs = {}
   visited_costs[start] = 0


   # Initialize a priority queue of states not yet visited, with the start state as the first element. The priority of each element is the cost to reach that state (g) + the estimate remaining cost (h) to reach the goal
   # Record the path to reach each state in a list; no path performed to reach the initial state
   queue = [(0, 0, [start], start)]


   # While there are un-visited states
   while queue:
       # Pop the state with the lowest sum of the cost so far and estimated cost to the goal from the queue
       _, g, path, current = heapq.heappop(queue)


       # Check if the current state is the end state
       if current == end:
           return path


       # Generate all possible actions from the current state, which includes moving to any of the 4 directions (north, south, east, west)
       for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
           # Check if the new state would be valid, ie the new state must be within the city map and not a closed workshop
           new_state = (current[0] + dx, current[1] + dy)
           if (0 <= new_state[0] < len(city_map) and 0 <= new_state[1] < len(city_map[0]) and city_map[new_state[0]][new_state[1]] != 'x'):
               # Check if the new state would visit at least 1 workshop in each district
               if all(start_row <= new_state[0] <= end_row for start_row, end_row in districts):
                   # The cost so far is the number of moves made, as the task is to minimize the number of moves required
                   new_cost = g + city_map[new_state[0]][new_state[1]]


                   # If the new state is unvisited or we found a new path with a lower cost to reach this state, add it to the queue of un-visited states
                   if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                       visited_costs[new_state] = new_cost
                       heapq.heappush(queue, (new_cost + heuristic(new_state, end), new_cost, path + [new_state], new_state))
   return None


def heuristic(current, end):
   # An admissible and consistent heuristic for this problem is the Manhattan distance between the current state and the end state
   # This heuristic is admissible because it never overestimates the cost to reach the goal, as the Manhattan distance is a lower bound on the actual path length
   # It is consistent because moving to a neighboring state always increases the heuristic cost of the successor node by a max of 1 (if the moved state is in a different district), which is equal to the cost of reaching the successor node
   return abs(current[0] - end[0]) + abs(current[1] - end[1])


print(a_star())
