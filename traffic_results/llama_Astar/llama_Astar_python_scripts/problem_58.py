
import heapq


def a_star():
   # Define the initial state of the city map as a 2d tuple
   city_map = [['x', 'x', 'x', '6', '9', 'x', 'x', '10', '14', '7', '3', '12'],
               ['x', '11', 'x', '3', '14', '16', '17', '1', '4', '14', '8', '16'],
               ['3', 'x', 'x', 'x', '6', '1', '18', '16', 'x', '6', '3', '11'],
               ['x', 'x', '11', '4', '8', 'x', 'x', '1', '3', '9', '8', '7'],
               ['x', 'x', '3', 'x', 'x', 'x', '8', '14', '18', 'x', 'x', '18'],
               ['4', '1', 'x', 'x', 'x', '14', 'x', 'x', 'x', '3', '4', '20'],
               ['1', 'x', 'x', 'x', '14', '19', '15', 'x', 'x', '3', '16', '15'],
               ['x', 'x', '6', '18', 'x', 'x', '16', '1', 'x', '3', 'x', '11'],
               ['x', '3', 'x', '15', 'x', '19', '10', 'x', 'x', 'x', 'x', 'x'],
               ['x', '9', 'x', 'x', 'x', '1', 'x', 'x', 'x', 'x', 'x', '13'],
               ['x', '3', '9', 'x', 'x', 'x', 'x', '1', '10', '11', '8']]
   # Define the start and end positions
   start_pos = (1, 3)
   end_pos = (6, 10)
   # Define the districts
   districts = [(0, 1), (2, 5), (6, 11)]


   # Initialize a dictionary to store the cost of reaching each visited state
   visited_costs = {}
   visited_costs[start_pos] = 0


   # Initialize a priority queue of states not yet visited, with the start position as the first element. The priority of each element is the cost to reach that state (g) + the estimate remaining cost (h) to reach the goal
   # Record the path taken to reach each state in a list; no path taken to reach the start position
   queue = [(0, 0, [], start_pos)]


   # While there are un-visited states
   while queue:
       # Pop the state with the lowest sum of the cost so far and estimated cost to the goal from the queue
       _, g, actions, current_pos = heapq.heappop(queue)


       # Check if the current position is the end position
       if current_pos == end_pos:
           return actions


       # Generate all possible actions from the current position, which includes moving to a neighboring position in the city map if it's not an 'x' and has not been visited yet
       for d_row, d_col in [(0, -1), (0, 1), (1, 0), (-1, 0)]:
           new_pos = (current_pos[0] + d_row, current_pos[1] + d_col)
           # Check if the new position is valid, ie within the bounds of the city map, not an 'x', and not visited yet
           if (0 <= new_pos[0] < len(city_map) and 0 <= new_pos[1] < len(city_map[0]) and
               city_map[new_pos[0]][new_pos[1]] != 'x' and new_pos not in visited_costs):
               # The new position is valid, generate the new state
               new_cost = g + int(city_map[new_pos[0]][new_pos[1]])
               # Check if the new state is in a different district from the current position
               if any(start <= new_pos[0] <= end for start, end in districts if start != current_pos[0]):
                   # If so, add a penalty to the cost to discourage traveling between districts
                   new_cost += 10
              
               # If the new state is unvisited or we found a new path with a lower cost to reach this state, add it to the queue of un-visited states
               if new_pos not in visited_costs or new_cost < visited_costs[new_pos]:
                   visited_costs[new_pos] = new_cost
                   heapq.heappush(queue, (new_cost + heuristic(new_pos, end_pos), new_cost, actions + [new_pos], new_pos))
   return None


def heuristic(pos, goal):
   # An admissible and consistent heuristic is the Manhattan distance between the current position and the goal position
   # This heuristic is admissible because it never overestimates the cost to reach the goal, as the cost of moving from one position to another is always the same as the Manhattan distance between them
   # It's consistent because moving from one position to another always increases the heuristic cost of the successor node by a max of 1 (if moving to a position in a different district), which is equal to the cost of reaching the successor node
   return abs(pos[0] - goal[0]) + abs(pos[1] - goal[1])


print(a_star())
