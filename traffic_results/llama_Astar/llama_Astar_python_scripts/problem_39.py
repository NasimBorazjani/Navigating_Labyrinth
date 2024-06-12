
import heapq


def a_star():
   # Define the initial state of the city map as a 2d tuple
   city_map = (['15', '8', '18', '3', '19', 'x', '17', 'x', 'x', 'x', 'x'],
               ['19', '16', 'x', '18', '20', '2', '5', '7', '11', '12', '3'],
               ['18', 'x', '18', '1', '2', 'x', 'x', 'x', '12', '16', '4'],
               ['9', '20', '4', '19', '5', '15', 'x', 'x', 'x', '6', '4'],
               ['x', '18', '8', '1', 'x', '7', '1', '7', '10', '1', '4'],
               ['x', '18', 'x', '18', '19', '9', '18', '5', '15', '1', '7'],
               ['3', 'x', '12', '14', 'x', 'x', 'x', 'x', '1', 'x', 'x'],
               ['x', '12', '6', 'x', '6', 'x', '1', '1', '7', 'x', 'x'],
               ['x', '5', '10', '14', '2', 'x', 'x', '7', '11', '3', 'x'],
               ['6', '9', '13', 'x', 'x', 'x', 'x', 'x', 'x', 'x', '3'],
               ['19', '12', 'x', '15', 'x', '14', 'x', '9', 'x', 'x', '19'])
   num_rows = 10
   num_cols = 11
   start = (3, 1)
   end = (5, 10)
   districts = [(0, 2), (3, 4), (5, 10)]


   # Initialize a dictionary to store the cost of reaching each visited state
   visited_costs = {}
   visited_costs[start] = 0


   # Initialize a priority queue of states not yet visited, with the initial state as the first element. The priority of each element is the cost to reach that state (g) + the estimate remaining cost (h) to reach the goal
   # Record the actions required to get to each state in a list; no actions performed to reach the initial state
   queue = [(0, 0, [], start)]


   # While there are un-visited states
   while queue:
       # Pop the state with the lowest sum of the cost so far and estimated cost to the goal from the queue
       _, g, actions, state = heapq.heappop(queue)


       # Check if the current state is the goal state
       if state == end:
           return actions


       # Generate all possible actions from the current state, which includes moving to any of the 4 directions (north, south, east, west) from the current workshop
       for d_row, d_col in [(0, -1), (0, 1), (1, 0), (-1, 0)]:
           new_row, new_col = state[0] + d_row, state[1] + d_col
           # Check if the new state would be valid, ie the new position is within the bounds of the city map and there's no closed workshop at the new position
           if 0 <= new_row < num_rows and 0 <= new_col < num_cols and city_map[new_row][new_col] != 'x':
               # The new state is valid, generate the new state
               new_state = (new_row, new_col)
               # The cost so far is the number of moves made, as the task is to minimize the number of moves required to reach the goal state
               new_cost = g + 1


               # Check if the new state visits at least one workshop in each district
               if all(start_row <= new_row <= end_row for start_row, end_row in districts):
                   # If the new state is unvisited or we found a new path with a lower cost to reach this state, add it to the queue of un-visited states
                   if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                       visited_costs[new_state] = new_cost
                       h = heuristic(new_state, end)
                       heapq.heappush(queue, (new_cost + h, new_cost, actions + [new_state], new_state))
   return None


def heuristic(state, goal):
   # An admissible and consistent heuristic is the Euclidean distance from the current state to the goal state
   # This heuristic is admissible because it never overestimates the cost to reach the goal, as the Euclidean distance is a lower bound on the actual path length
   # It is consistent because moving from one state to another always increases the heuristic cost of the successor node by a value greater than or equal to the cost of reaching the successor node
   # Thus h(n) can never be greater than c(n, n’)(equal to 1) + h(n’)
   return math.sqrt((state[0] - goal[0]) ** 2 + (state[1] - goal[1]) ** 2)


print(a_star())
