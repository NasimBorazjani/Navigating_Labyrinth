
import heapq


def a_star():
   # Define the initial state of the city map as a 2d tuple
   city_map = [['6', '16', 'x', 'x', '15', 'x', '14', '11', 'x'],
               ['5', '2', '1', 'x', '3', 'x', '4', '13', 'x'],
               ['x', '7', 'x', 'x', '13', 'x', '10', '14', '5'],
               ['6', '16', 'x', '13', '6', 'x', '16', 'x', 'x'],
               ['x', '1', '17', 'x', '6', '3', 'x', 'x', '3'],
               ['11', '10', '7', '19', '15', '8', '12', '6', 'x'],
               ['18', 'x', 'x', '9', '8', '9', 'x', 'x', '13'],
               ['4', 'x', 'x', 'x', '18', '20', 'x', 'x', 'x'],
               ['x', 'x', '8', 'x', '18', '2', '6', '13', 'x']]
   # Define the start and end positions
   start_pos = (5, 5)
   end_pos = (1, 0)
   # Define the districts
   districts = [(0, 1), (2, 4), (5, 8)]


   # Initialize a dictionary to store the cost of reaching each visited state
   visited_costs = {}
   visited_costs[start_pos] = 0


   # Initialize a priority queue of states not yet visited, with the start position as the first element. The priority of each element is the cost to reach that state (g) + the estimate remaining cost (h) to reach the goal
   # Record the path taken to reach each state in a list; no path taken to reach the start position
   queue = [(0, 0, [start_pos], start_pos)]


   # While there are un-visited states
   while queue:
       # Pop the state with the lowest sum of the cost so far and estimated cost to the goal from the queue
       _, g, path, current_pos = heapq.heappop(queue)


       # Check if the current position is the end position
       if current_pos == end_pos:
           return path


       # Generate all possible actions from the current position, which includes moving to any of the 4 directions (north, south, east, west)
       for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
           new_pos = (current_pos[0] + dx, current_pos[1] + dy)
           # Check if the new position is valid, ie within the city map, not an x, and not visited before
           if (0 <= new_pos[0] < len(city_map) and 0 <= new_pos[1] < len(city_map[0]) and
               city_map[new_pos[0]][new_pos[1]] != 'x' and new_pos not in path):
               # Generate the new state
               new_cost = g + int(city_map[new_pos[0]][new_pos[1]])
               # Check if the new state satisfies the district visiting constraint
               if any(start_district <= new_pos[0] <= end_district for start_district, end_district in districts):
                   # If the new state is unvisited or we found a new path with a lower cost to reach this state, add it to the queue of un-visited states
                   if new_pos not in visited_costs or new_cost < visited_costs[new_pos]:
                       visited_costs[new_pos] = new_cost
                       heapq.heappush(queue, (new_cost + heuristic(new_pos, end_pos), new_cost, path + [new_pos], new_pos))
   return None


def heuristic(current_pos, end_pos):
   # An admissible and consistent heuristic is the Manhattan distance between the current position and the end position
   # This heuristic is admissible because it never overestimates the cost to reach the goal
   # It is consistent because moving to a neighboring position increases the heuristic cost of the successor node by a max of 1 (if the moved position is in a different district), which is equal to the cost of reaching the successor node
   return abs(current_pos[0] - end_pos[0]) + abs(current_pos[1] - end_pos[1])


print(a_star())
