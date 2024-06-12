
import heapq


def a_star():
   # Define the initial state of the city map as a 2d tuple
   city_map = [['8', 'x', '7', '10', 'x', '12', '5', 'x'],
               ['x', 'x', '4', '11', '16', '4', '12', '15', 'x'],
               ['3', 'x', '16', '16', '4', 'x', 'x', 'x', 'x'],
               ['11', '6', '3', '12', '8', '2', '19', '14', 'x'],
               ['20', '18', '19', 'x', '4', '18', 'x', '15', '13'],
               ['8', '15', 'x', '16', '11', 'x', '10', '14', '1'],
               ['x', 'x', 'x', '19', 'x', 'x', 'x', 'x', 'x'],
               ['7', 'x', 'x', 'x', 'x', 'x', '1', '7', '8'],
               ['15', '3', 'x', 'x', 'x', 'x', 'x', 'x', 'x']]
   # Define the start and end positions
   start_pos = (5, 0)
   end_pos = (3, 7)
   # Define the districts
   districts = [(0, 3), (4, 4), (5, 8)]


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


       # Generate all possible actions from the current position, which includes moving to any of the 4 neighboring positions in the city map
       for d_row, d_col in [(0, -1), (0, 1), (1, 0), (-1, 0)]:
           new_pos = (current_pos[0] + d_row, current_pos[1] + d_col)
           # Check if the new position is valid, ie within the bounds of the city map and not a closed workshop
           if (0 <= new_pos[0] < len(city_map) and 0 <= new_pos[1] < len(city_map[0]) and
               city_map[new_pos[0]][new_pos[1]] != 'x'):
               # Generate the new state
               new_cost = g + int(city_map[new_pos[0]][new_pos[1]])
               # Check if the new state would be valid, ie the new position is in a different district than the current position
               if any(start <= new_pos[0] <= end for start, end in districts if start != current_pos[0]):
                   # The cost so far is the number of moves made, as the task is to minimize the number of moves required to reach the goal position
                   new_path = path + [new_pos]
                   # If the new state is unvisited or we found a new path with a lower cost to reach this state, add it to the queue of un-visited states
                   if new_pos not in visited_costs or new_cost < visited_costs[new_pos]:
                       visited_costs[new_pos] = new_cost
                       h = heuristic(new_pos, end_pos)
                       heapq.heappush(queue, (new_cost + h, new_cost, new_path, new_pos))
   return None


def heuristic(current_pos, end_pos):
   # An admissible and consistent heuristic is the Manhattan distance between the current position and the end position
   # This heuristic relaxes the constraint that Ben can only move to a workshop in a different district
   # It is admissible because it never overestimates the cost to reach the goal, as the heuristic cost of the successor node is always less than or equal to the cost of reaching the goal from the current node
   # It's consistent because moving to a workshop in a different district reduces the heuristic cost of the successor node by a max of 1 (if the new district is closer to the end position), which is equal to the cost of reaching the successor node
   return abs(current_pos[0] - end_pos[0]) + abs(current_pos[1] - end_pos[1])


print(a_star())
