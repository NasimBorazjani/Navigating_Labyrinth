
import heapq


def a_star():
   # Define the initial state of the city map as a 2d tuple
   city_map = [['19', '12', 'x', 'x', '2', '5', '4', '13', '17', '19', 'x', '2'],
               ['x', '18', 'x', '5', '5', 'x', 'x', '8', '12', '18', 'x', '15'],
               ['x', '9', '4', '10', '7', '20', 'x', '16', '20', '13', '15', 'x'],
               ['8', 'x', 'x', '11', '1', '19', 'x', '14', '6', 'x', '3', 'x'],
               ['10', 'x', '4', '8', '17', 'x', '18', 'x', '7', 'x', '6', '5'],
               ['x', 'x', '3', '1', '8', '18', 'x', '4', '17', 'x', 'x', '13'],
               ['x', 'x', '6', 'x', 'x', 'x', '14', 'x', 'x', '10', '10', 'x'],
               ['x', 'x', '15', 'x', 'x', 'x', 'x', 'x', '2', 'x', 'x', 'x'],
               ['x', 'x', '5', '11', '6', '1', 'x', '6', '14', 'x', 'x', 'x'],
               ['x', '1', '17', '10', '15', 'x', '14', '6', 'x', 'x', 'x', 'x'],
               ['12', '2', 'x', '10', 'x', 'x', '7', 'x', 'x', 'x', 'x', 'x'],
               ['x', '9', '14', 'x', '9', '18', '14', 'x', 'x', 'x', '6', 'x']]
   num_rows = 11
   num_cols = 12
   start = (6, 2)
   end = (2, 10)
   districts = [(0, 1), (2, 5), (6, 11)]


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
               any(districts[i][0] <= new_row < districts[i][1] for i in range(len(districts)) if (districts[i][0] <= state[0] < districts[i][1]) and (districts[i][0] <= new_row < districts[i][1]))):
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
   # This heuristic relaxes the constraint that Ben can only move to workshops in the same district
   # It is admissible because it never overestimates the cost to reach the goal, as each move is either horizontal or vertical
   # It's consistent because moving to a workshop in a different district increases the heuristic cost of the successor node by a max of 1 (if the moved workshop is in the same district as the current one), which is equal to the cost of reaching the successor node
   # Thus h(s) is always less than or equal to c(s, n)(equal to 1) + h(n)
   return abs(state[0] - goal[0]) + abs(state[1] - goal[1])


print(a_star())
