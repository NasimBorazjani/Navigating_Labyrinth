
import heapq


def a_star():
   # Define the initial state of the city map as a 2d tuple
   city_map = [['5', '10', 'x', 'x', 'x', '16', 'x', 'x', '16', 'x', '10', '8', 'x'],
               ['1', 'x', '13', 'x', '7', 'x', 'x', 'x', '10', '3', '3', '13', '18', '11'],
               ['14', 'x', 'x', 'x', '9', '16', '16', '15', 'x', 'x', '15', 'x', '4', '4'],
               ['15', 'x', '3', 'x', 'x', '17', 'x', 'x', '15', '6', '3', 'x', '1'],
               ['12', '8', 'x', '10', 'x', 'x', '13', '10', 'x', 'x', '6', '3', 'x', '1'],
               ['x', 'x', 'x', '5', '8', '9', '6', '14', '1', 'x', 'x', '2', '12', 'x'],
               ['13', 'x', 'x', 'x', '16', '6', 'x', '17', '12', 'x', '17', '8', 'x', '17', '18', '8', 'x'],
               ['10', 'x', '14', '15', 'x', 'x', 'x', '20', 'x', '17', '18', '8', 'x', '4'],
               ['x', '11', '3', 'x', 'x', 'x', '7', 'x', '4', 'x', 'x', '11', '2'],
               ['7', 'x', 'x', '10', 'x', '19', 'x', '7', '17', 'x', 'x', '14', 'x', '15'],
               ['12', '11', 'x', 'x', '9', '7', 'x', '15', '1', '5', '5', '11', '15', 'x'],
               ['x', '9', '9', 'x', 'x', 'x', '8', 'x', '8', '8', '19', '11', '12', '12'],
               ['x', '17', '5', 'x', 'x', '17', 'x', 'x', '12', 'x', '15', '12', '10', 'x']]
   num_rows = 13
   num_cols = 14
   start = (10, 12)
   end = (4, 3)
   districts = [(0, 4), (5, 9), (10, 13)]


   # Initialize a dictionary to store the cost of reaching each visited state
   visited_costs = {}
   visited_costs[start] = 0


   # Initialize a priority queue of states not yet visited, with the start state as the first element. The priority of each element is the cost to reach that state (g) + the estimate remaining cost (h) to reach the end
   # Record the path to reach each state in a list; no path performed to reach the start state
   queue = [(0, 0, [], start)]


   # While there are un-visited states
   while queue:
       # Pop the state with the lowest sum of the cost so far and estimated cost to the end from the queue
       _, g, actions, state = heapq.heappop(queue)


       # Check if the current state is the end state
       if state == end:
           return actions


       # Generate all possible actions from the current state, which includes moving to any of the 4 neighboring workshops if it's not an 'x' and the district of the new state is different from the current state
       for d_row, d_col in [(0, -1), (0, 1), (1, 0), (-1, 0)]:
           new_row, new_col = state[0] + d_row, state[1] + d_col
           if (0 <= new_row < num_rows and 0 <= new_col < num_cols and
               city_map[new_row][new_col] != 'x' and
               any(districts[i][0] <= new_row < districts[i][1] for i in range(3) if not (districts[i][0] <= state[0] < districts[i][1]))):
               # The actions is valid, generate the new state
               new_state = (new_row, new_col)
               # The cost so far is the number of moves made, as our objective is to minimize the number of moves required to reach the end state
               new_cost = g + 1
              
               # If the new state is unvisited or we found a new path with a lower cost to reach this state, add it to the queue of not-yet-visited states
               if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                   visited_costs[new_state] = new_cost
                   heapq.heappush(queue, (new_cost + heuristic(new_state, end, city_map), new_cost, actions + [new_state], new_state))
                  
   return None


def heuristic(state, end, city_map):
   # An admissible and consistent heuristic is the Manhattan distance between the current state and the end state
   # This heuristic relaxes the constraint that Ben can only move to workshops in the same district
   # It is admissible because it never overestimates the cost to reach the goal, as the Manhattan distance is a lower bound on the actual cost
   # The heuristic is consistent because moving to a workshop in a different district increases the heuristic cost of the successor node by a max of 1 (if the moved workshop is in a different district), which is equal to the cost of reaching the successor node
   return abs(state[0] - end[0]) + abs(state[1] - end[1])


print(a_star())
