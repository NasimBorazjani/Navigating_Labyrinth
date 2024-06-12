
import heapq


def a_star():
   # Define the initial state of the city map as a 2d tuple
   city_map = [['8', '15', '3', '10', '6', '15', 'x', '4', 'x', 'x', 'x', 'x', 'x'],
               ['3', 'x', '14', '8', '16', '19', 'x', '18', '4', 'x', '2', 'x', '6', 'x'],
               ['18', '18', 'x', '4', 'x', '17', '11', '10', '17', '9', 'x', '4', '1', '5'],
               ['x', '2', 'x', '12', '1', 'x', '13', '17', '14', '15', 'x', '15', 'x'],
               ['x', 'x', 'x', '15', 'x', '2', '2', '11', '7', 'x', '5', '7', '4', '18'],
               ['16', 'x', '5', 'x', '19', '12', '5', '9', '13', '16', '9', 'x', '3', 'x'],
               ['x', 'x', 'x', 'x', '14', '18', 'x', '16', '13', 'x', '1', '5', '10', 'x'],
               ['3', '11', 'x', '1', '8', 'x', 'x', 'x', '18', '8', '11', 'x', 'x', '6'],
               ['19', '2', 'x', '19', '5', 'x', 'x', 'x', '9', 'x', '6', 'x', 'x', '4'],
               ['x', '2', 'x', '10', '9', '15', 'x', 'x', 'x', '16', 'x', '8', 'x', 'x'],
               ['18', '8', '10', 'x', '3', 'x', '11', 'x', 'x', '17', 'x', 'x', 'x', '3', 'x']]
   num_rows = 12
   num_cols = 14
   start = (2, 0)
   end = (6, 11)
   districts = [(0, 2), (3, 5), (6, 13)]


   # Initialize a dictionary to store the cost of reaching each visited state
   visited_costs = {}
   visited_costs[start] = 0


   # Initialize a priority queue of states not yet visited, with the initial state as the first element. The priority of each element is the cost to reach that state (g) + the estimate remaining cost (h) to reach the goal
   # Record the path taken to reach each state in a list; no path performed to reach the initial state
   queue = [(0, 0, [], start)]


   # While there are un-visited states
   while queue:
       # Pop the state with the lowest sum of the cost so far and estimated cost to the goal from the queue
       _, g, actions, state = heapq.heappop(queue)


       # Check if the current state is the goal state
       if state == end:
           return actions


       # Generate all possible actions from the current state, which includes moving to any of the 4 neighboring workshops if it's not an 'x' and the district of the new workshop is not visited yet
       for d_row, d_col in [(0, -1), (0, 1), (1, 0), (-1, 0)]:
           new_row, new_col = state[0] + d_row, state[1] + d_col
           if 0 <= new_row < num_rows and 0 <= new_col < num_cols and city_map[new_row][new_col] != 'x' and any(districts[i][0] <= new_row <= districts[i][1] for i in range(3) if (districts[i][0] <= state[0] <= districts[i][1]) and (districts[i][0] <= new_row <= districts[i][1])):
               # The actions is valid, generate the new state
               new_state = (new_row, new_col)
               # The cost so far is the number of moves made, as our objective is to minimize the number of moves required to reach the goal state
               new_cost = g + 1
              
               # If the new state is unvisited or we found a new path with a lower cost to reach this state, add it to the queue of not-yet-visited states
               if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                   visited_costs[new_state] = new_cost
                   heapq.heappush(queue, (new_cost + heuristic(new_state, end, city_map), new_cost, actions + [new_state], new_state))
                  
   return None


def heuristic(state, goal, city_map):
   # An admissible and consistent heuristic is the Manhattan distance from the current state to the goal state
   # This heuristic relaxes the constraint that Ben can only move to workshops in the same district
   # It is admissible because it never overestimates the cost to reach the goal, as the Manhattan distance is a lower bound on the actual cost
   # The heuristic is consistent because moving to a workshop in a different district increases the heuristic cost of the successor node by a max of 1 (if the moved workshop's district matches the most common district in the new workshop but not in the old one), which is equal to the cost of reaching the successor node
   return abs(state[0] - goal[0]) + abs(state[1] - goal[1])


print(a_star())
