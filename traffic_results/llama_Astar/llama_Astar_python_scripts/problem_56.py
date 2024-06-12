
import heapq


def a_star():
   # Define the initial state of the city map as a 2d tuple
   city_map = [['2', 'x', 'x', '14', 'x', '19', '6', 'x', 'x', '14', '18', 'x'],
               ['x', '10', '1', '15', 'x', 'x', 'x', 'x', '17', '2', '9', '12'],
               ['13', '14', 'x', '2', 'x', 'x', '10', '10', 'x', 'x', 'x', 'x'],
               ['9', '17', '3', '15', '4', '4', 'x', '9', '15', '16', 'x', '9'],
               ['10', '7', '3', '8', 'x', '7', 'x', '16', '3', '7', 'x', 'x'],
               ['16', '20', '16', '19', '18', '3', 'x', 'x', '11', '14', '5', 'x'],
               ['14', '13', '8', '14', '12', '19', '6', '3', '19', '10', '11', 'x'],
               ['x', '18', 'x', 'x', '4', '19', '6', '14', '15', '17', '7', 'x'],
               ['x', '2', 'x', 'x', 'x', 'x', '7', 'x', '19', 'x', 'x'],
               ['x', '3', '14', '1', 'x', '18', '4', '12', 'x', '3', '10', 'x'],
               ['2', 'x', '16', '13', 'x', '17', 'x', 'x', '17', '16', '4', '10'],
               ['x', '4', '10', 'x', 'x', '7', 'x', '19', '7', 'x', 'x']]
   num_rows = 12
   num_cols = 12
   start = (6, 9)
   end = (3, 0)
   districts = [(0, 3), (4, 6), (7, 11)]


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
   # An admissible and consistent heuristic for this problem is the sum of the distances from the current state to the end state and the districts not yet visited
   # This heuristic relaxes the constraint that Ben must visit at least 1 workshop in each district on his path to the destination
   # It is admissible because it never overestimates the cost to reach the goal, as each district not visited must be visited at least once
   # It's consistent because moving to a district results in a decrease in the heuristic cost of the successor node by a max of 1 (if the moved district is the one not visited), which is equal to the cost of reaching the successor node
   # Thus h(s) is always less than or equal to c(s, n)(equal to 1) + h(n)
   h = 0
   # Calculate the distance from the current state to the end state
   h += abs(state[0] - end[0]) + abs(state[1] - end[1])
   # Calculate the distance from the current state to the districts not yet visited
   for district in districts:
       if district not in path:
           h += min(abs(state[0] - (district[0] + district[1]) // 2), abs(state[1] - (district[0] + district[1]) // 2))
   return h


print(a_star())
