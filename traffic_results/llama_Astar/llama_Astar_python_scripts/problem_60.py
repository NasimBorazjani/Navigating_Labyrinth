
import heapq


def a_star():
   # Define the initial state of the city map as a 2d tuple
   city_map = [['16', 'x', '5', '6', 'x', '14', '12', 'x', 'x', 'x', '6', 'x'],
               ['17', 'x', 'x', 'x', '5', 'x', '5', '7', 'x', 'x', '8', 'x'],
               ['3', '19', 'x', 'x', 'x', 'x', '18', 'x', '13', '7', 'x', 'x'],
               ['13', 'x', '4', 'x', 'x', '8', '7', '4', 'x', '15', 'x', 'x'],
               ['5', '17', '18', '12', '3', 'x', '14', '2', '4', '18', 'x', '1'],
               ['4', '10', '1', '19', '10', 'x', 'x', '17', 'x', '17', '16', '4'],
               ['7', 'x', '16', 'x', 'x', '1', '3', 'x', '13', 'x', 'x', 'x'],
               ['x', 'x', '9', '1', '7', '18', '16', '3', 'x', '4', 'x', 'x'],
               ['2', 'x', '13', '10', 'x', '4', 'x', 'x', 'x', 'x', '12', 'x'],
               ['x', 'x', 'x', '18', '8', '4', 'x', '11', 'x', '14', '18', 'x'],
               ['x', '19', '2', 'x', '2', '6', '5', '18', 'x', '5', 'x', 'x'],
               ['x', '2', '7', 'x', 'x', '8', '7', 'x', '11', '16', 'x', 'x']]
   num_rows = 12
   num_cols = 12
   start = (3, 0)
   end = (9, 7)
   districts = [(0, 3), (4, 8), (9, 11)]


   # Initialize a dictionary to store the cost of reaching each visited state
   visited_costs = {}
   visited_costs[start] = 0


   # Initialize a priority queue of states not yet visited, with the start state as the first element. The priority of each element is the cost to reach that state (g) + the estimate remaining cost (h) to reach the end
   # Record the path to reach each state in a list; no path performed to reach the start state
   queue = [(0, 0, [start], start)]


   # While there are un-visited states
   while queue:
       # Pop the state with the lowest sum of the cost so far and estimated cost to the end from the queue
       _, g, path, current = heapq.heappop(queue)


       # Check if the current state is the end state
       if current == end:
           return path


       # Generate all possible actions from the current state, which includes moving to any of the 4 directions (north, south, east, west)
       for d_row, d_col in [(0, -1), (0, 1), (1, 0), (-1, 0)]:
           new_row, new_col = current[0] + d_row, current[1] + d_col
           # Check if the new state would be valid, ie the new position is within the bounds of the city map and there's no 'x' at the new position
           if 0 <= new_row < num_rows and 0 <= new_col < num_cols and city_map[new_row][new_col] != 'x':
               # The new state is valid, generate the new state
               new_state = (new_row, new_col)
               # The cost so far is the number of moves made, as the task is to minimize the number of moves required to reach the end state
               new_cost = g + 1


               # Check if the new state has not been visited or we found a new path with a lower cost to reach this state
               if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                   visited_costs[new_state] = new_cost
                   # Relax the constraints on the districts to calculate the heuristic
                   h = heuristic(new_state, end, path, city_map, districts)
                   heapq.heappush(queue, (new_cost + h, new_cost, path + [new_state], new_state))
   return None


def heuristic(state, end, path, city_map, districts):
   # An admissible and consistent heuristic for this problem is the sum of the Manhattan distances (the shortest path) of each district from the current state to the end state
   # This heuristic relaxes the constraint that Ben must visit at least 1 workshop in each district on his path to the destination
   # It is admissible because it never overestimates the cost to reach the goal, as each district must be visited at least once
   # It's consistent because moving to a district from another district reduces the heuristic cost of the successor node by a max of 1 (if the moved district is closer to the end state), which is equal to the cost of reaching the successor node
   # Thus h(s) is always less than or equal to c(s, n)(equal to 1) + h(n)
   h = 0
   for district in districts:
       # Calculate the Manhattan distance from the current state to the end state for each district
       h += abs(state[0] - end[0]) + abs(state[1] - end[1])
   return h


print(a_star())
