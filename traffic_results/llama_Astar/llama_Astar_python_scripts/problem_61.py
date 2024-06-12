
import heapq


def a_star():
   # Define the initial state of the city map as a 2d tuple
   city_map = [['13', '13', '16', '8', 'x', '19', '1', '18', '13', '8', 'x', '7', 'x'],
               ['x', '13', 'x', '15', 'x', '12', '20', '1', '13', '19', '4', '17', 'x'],
               ['x', '12', '9', '11', '13', '12', '2', '12', '19', '5', '19', '16', '8'],
               ['x', '12', '18', '19', 'x', '7', 'x', '12', '3', '2', 'x', '16', '11'],
               ['x', '7', 'x', 'x', '8', '13', '15', '3', '1', 'x', '15', '15', 'x'],
               ['11', '9', 'x', '16', '2', '10', '1', '2', '16', '1', 'x', '10', '12'],
               ['x', 'x', '9', '9', '7', 'x', '6', 'x', 'x', '10', '7', '2', 'x'],
               ['x', '13', '10', '8', '1', '11', 'x', 'x', 'x', 'x', 'x', 'x', 'x'],
               ['11', '14', 'x', 'x', 'x', 'x', '4', '8', 'x', 'x', '18', 'x', 'x'],
               ['13', '14', 'x', '10', 'x', 'x', '16', 'x', 'x', 'x', 'x', 'x', 'x'],
               ['x', 'x', '16', 'x', '10', 'x', '17', '12', 'x', '10', 'x', '5'],
               ['9', 'x', '10', 'x', '19', '16', 'x', '6', '9', 'x', 'x', '8', '11']]
   num_rows = 12
   num_cols = 13
   start = (3, 12)
   end = (6, 2)
   districts = [(0, 1), (2, 5), (6, 12)]


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
           if (0 <= new_row < num_rows and 0 <= new_col < num_cols and
               city_map[new_row][new_col] != 'x' and
               any(districts[i][0] <= new_row <= districts[i][1] for i in range(len(districts)) if (districts[i][0] <= state[0] <= districts[i][1]) and not (districts[i][0] <= new_row <= districts[i][1]))):
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
   # An admissible and consistent heuristic is the Manhattan distance between the current state and the goal state
   # This heuristic relaxes the constraint that Ben can only move to a workshop in a district not yet visited
   # It is admissible because it never overestimates the cost to reach the goal, as the Manhattan distance is a lower bound on the actual cost
   # The heuristic is consistent because moving to a workshop in a district not yet visited does not change the actual cost to reach the goal, and the cost of reaching the successor node is the same as the cost of reaching the current state
   return abs(state[0] - goal[0]) + abs(state[1] - goal[1])


print(a_star())
