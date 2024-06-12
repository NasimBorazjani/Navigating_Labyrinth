
import heapq


def a_star():
   # Define the initial state of the city map as a 2d tuple
   city_map = [['x', 'x', 17, 12, 12, 10, 9, 9, 18, 'x', 1],
               ['x', 8, 'x', 9, 'x', 'x', 18, 5, 1, 12, 14],
               [2, 19, 4, 'x', 'x', 'x', 'x', 'x', 'x', 15, 'x'],
               [17, 8, 6, 'x', 'x', 10, 15, 'x', 'x', 'x', 13],
               ['x', 'x', 'x', 9, 17, 'x', 'x', 'x', 'x', 12, 17],
               ['x', 20, 3, 1, 14, 8, 9, 20, 10, 8, 8],
               [18, 19, 4, 12, 3, 1, 'x', 'x', 20, 6, 3],
               [4, 6, 9, 'x', 8, 10, 'x', 'x', 6, 9, 6],
               [15, 'x', 'x', 'x', 'x', 'x', 16, 'x', 15, 4, 'x'],
               ['x', 'x', 'x', 4, 'x', 'x', 'x', 13, 'x', 'x'],
               ['x', 3, 'x', 'x', 'x', 'x', 1, 'x', 5, 13]]
   num_rows = 10
   num_cols = 11
   start = (3, 10)
   end = (6, 1)
   # The districts are represented as a list of tuples, where each tuple contains the start and end row of each district
   districts = [(0, 3), (4, 5), (6, 10)]


   # Initialize a dictionary to store the cost of reaching each visited state
   visited_costs = {}
   visited_costs[start] = 0


   # Initialize a priority queue of states not yet visited, with the start state as the first element. The priority of each element is the cost to reach that state (g) + the estimate remaining cost (h) to reach the end
   # Record the path taken to reach each state in a list; no path performed to reach the start state
   queue = [(0, 0, [], start)]


   # While there are un-visited states
   while queue:
       # Pop the state with the lowest sum of the cost so far and estimated cost to the end from the queue
       _, g, actions, state = heapq.heappop(queue)


       # Check if the current state is the end state
       if state == end:
           return actions


       # Generate all possible actions from the current state, which includes moving to any of the 4 neighboring workshops if it's not in a different district
       for d_row, d_col in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
           new_state = (state[0] + d_row, state[1] + d_col)
           # Check if the new state is valid, ie within the bounds of the city map, not moving to a different district, and not moving to a closed workshop
           if (0 <= new_state[0] < num_rows and 0 <= new_state[1] < num_cols and
               any(districts[i][0] <= new_state[0] <= districts[i][1] for i in range(len(districts)) if districts[i][0] <= state[0] <= districts[i][1]) and
               city_map[new_state[0]][new_state[1]] != 'x'):
               # The cost so far is the number of moves made, as the task is to minimize the number of moves required to reach the end state
               new_cost = g + city_map[new_state[0]][new_state[1]]
              
               # If the new state is unvisited or we found a new path with a lower cost to reach this state, add it to the queue of un-visited states
               if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                   visited_costs[new_state] = new_cost
                   heapq.heappush(queue, (new_cost + heuristic(new_state, end), new_cost, actions + [new_state], new_state))
   return None


def heuristic(state, end):
   # An admissible and consistent heuristic is the Manhattan distance between the current state and the end state
   # This heuristic relaxes the constraint that Ben can only move to workshops in the same district
   # It is admissible because it never overestimates the cost to reach the goal, as the heuristic cost of the successor node is always less than or equal to the cost of reaching the goal from the successor node
   # It's consistent because moving to a workshop in a different district increases the heuristic cost of the successor node by a max of 1 (if the new district is closer to the end state), which is equal to the cost of reaching the successor node
   return abs(state[0] - end[0]) + abs(state[1] - end[1])


print(a_star())
