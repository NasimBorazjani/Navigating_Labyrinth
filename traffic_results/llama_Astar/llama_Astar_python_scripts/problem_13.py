
import heapq


def a_star():
   # Define the initial state of the city map as a 2d tuple
   city_map = [['x', 'x', 'x', 'x', 9, 'x', 20, 3, 9],
               [17, 11, 17, 'x', 9, 2, 7, 'x', 15],
               ['x', 4, 2, 19, 12, 6, 'x', 4, 17],
               [15, 'x', 'x', 15, 11, 19, 'x', 9, 5],
               [3, 9, 19, 15, 2, 'x', 'x', 18, 'x'],
               [19, 5, 9, 11, 9, 'x', 'x', 3, 'x'],
               ['x', 'x', 2, 8, 8, 'x', 'x', 'x', 19],
               ['x', 'x', 14, 'x', 'x', 'x', 18, 'x', 18],
               ['x', 14, 18, 7, 8, 'x', 10, 15, 'x']]
   # Define the start and end positions
   start = (3, 7)
   end = (5, 0)
   # Define the districts
   districts = [(0, 3), (4, 4), (5, 8)]


   # Initialize a dictionary to store the cost of reaching each visited state
   visited_costs = {}
   visited_costs[start] = 0


   # Initialize a priority queue of states not yet visited, with the start state as the first element. The priority of each element is the cost to reach that state (g) + the estimate remaining cost (h) to reach the goal
   # Record the path taken to reach each state in a list; no path taken to reach the start state
   queue = [(0, 0, [start], start)]


   # While there are un-visited states
   while queue:
       # Pop the state with the lowest sum of the cost so far and estimated cost to the goal from the queue
       _, g, path, current = heapq.heappop(queue)


       # Check if the current state is the end state
       if current == end:
           return path


       # Generate all possible actions from the current state, which includes moving to any of the 4 neighboring positions in the city map
       for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
           new_pos = (current[0] + dx, current[1] + dy)
           # Check if the new position is valid, ie within the bounds of the city map and not a closed workshop
           if (0 <= new_pos[0] < len(city_map) and 0 <= new_pos[1] < len(city_map[0]) and
               city_map[new_pos[0]][new_pos[1]] != 'x'):
               # Generate the new state
               new_state = new_pos
               # The cost so far is the number of moves made, as the task is to minimize the number of moves required to reach the goal state
               new_cost = g + 1


               # If the new state is unvisited or we found a new path with a lower cost to reach this state, add it to the queue of un-visited states
               if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                   visited_costs[new_state] = new_cost
                   heapq.heappush(queue, (new_cost + heuristic(new_state, end, districts), new_cost, path + [new_state], new_state))
   return None


def heuristic(current, end, districts):
   # An admissible and consistent heuristic for this problem is the Manhattan distance to the end position, plus a penalty for each district not visited
   # This heuristic relaxes the constraint that Ben must visit at least one workshop in each district
   # It is admissible because it never overestimates the cost to reach the goal, as each unvisited district must be visited at least once
   # It's consistent because moving to a new position can only decrease the heuristic cost of the successor node, as the heuristic cost of the successor node is the sum of the Manhattan distance to the end position and the number of unvisited districts, and the Manhattan distance can only decrease, and the number of unvisited districts can only decrease or stay the same
   h = abs(current[0] - end[0]) + abs(current[1] - end[1])
   for district in districts:
       if district[0] <= current[0] < district[1] and district not in [d for d, _ in districts if d[0] <= current[0] < d[1]]:
           h += 1
   return h


print(a_star())
