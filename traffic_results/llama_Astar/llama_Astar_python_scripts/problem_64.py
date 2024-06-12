
import heapq


def a_star():
   # Define the initial state of the city map as a 2d tuple
   city_map = [['8', 'x', '12', '16', 'x', 'x', 'x', '7', 'x', 'x', 'x', 'x'],
               ['x', 'x', 'x', 'x', '16', '7', '8', 'x', '17', '19', 'x'],
               ['7', 'x', '13', '19', 'x', '6', 'x', '14', '18', 'x', '19'],
               ['9', '20', '2', 'x', '10', '6', 'x', '18', 'x', 'x', 'x', '18'],
               ['x', 'x', '8', '12', '7', '14', '13', '9', '8', '6', '14', '11', '7'],
               ['x', '14', 'x', 'x', 'x', '19', '13', '15', '3', '12', '16', '16', '3'],
               ['x', 'x', 'x', '13', 'x', '9', '13', '10', 'x', '14', 'x', '4', '18'],
               ['6', '12', '10', 'x', 'x', '18', '7', '20', '18', 'x', '13', '1', 'x'],
               ['x', '5', 'x', '18', '12', 'x', 'x', '3', '12', '14', '19', '16', 'x'],
               ['10', 'x', '19', 'x', 'x', 'x', 'x', '11', '14', '16', '12', 'x', '8'],
               ['8', 'x', 'x', 'x', 'x', 'x', '9', '16', '15', 'x', 'x', '8'],
               ['x', 'x', '2', 'x', '1', 'x', '16', 'x', 'x', '3', 'x']]
   num_rows = 12
   num_cols = 12
   start = (3, 0)
   end = (6, 12)
   districts = [(0, 3), (4, 5), (6, 12)]


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


       # Generate all possible actions from the current state, which includes moving to any of the 4 directions (north, south, east, west) if the destination is not an 'x' and the district constraint is satisfied
       for d_row, d_col in [(0, -1), (0, 1), (1, 0), (-1, 0)]:
           new_row, new_col = current[0] + d_row, current[1] + d_col
           # Check if the new state would be valid, ie the destination is not an 'x' and the district constraint is satisfied
           if (0 <= new_row < num_rows and 0 <= new_col < num_cols and
               city_map[new_row][new_col] != 'x' and
               any(districts[i][0] <= new_row <= districts[i][1] for i in range(len(districts)) if not any(districts[i][0] <= path[j][0] <= districts[i][1] for j in range(len(path))))):
               # Generate the new state
               new_state = (new_row, new_col)
               # The cost so far is the number of moves made, as the task is to minimize the number of moves required to reach the end state
               new_cost = g + 1
              
               # If the new state is unvisited or we found a new path with a lower cost to reach this state, add it to the queue of un-visited states
               if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                   visited_costs[new_state] = new_cost
                   heapq.heappush(queue, (new_cost + heuristic(new_state, end), new_cost, path + [new_state], new_state))
   return None


def heuristic(state, end):
   # An admissible and consistent heuristic for this problem is the Euclidean distance from the current state to the end state
   # This heuristic is admissible because it never overestimates the cost to reach the goal, as the Euclidean distance is a lower bound on the actual cost
   # It is consistent because moving to a neighboring state always increases the heuristic cost of the successor node by a value greater than or equal to the cost of reaching the successor node
   # Thus h(n) can never be greater than c(n, n’)(equal to 1) + h(n’)
   return math.sqrt((state[0] - end[0]) ** 2 + (state[1] - end[1]) ** 2)


print(a_star())
