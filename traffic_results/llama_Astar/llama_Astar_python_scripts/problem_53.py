
import heapq


def a_star():
   # Define the initial state of the city map as a 2d tuple
   city_map = (['18', 'x', 'x', '14', '5', 'x', 'x', '5', '18', 'x', '3', 'x'],
               ['x', 'x', 'x', '9', '2', '2', 'x', '15', '14', '12', 'x', '18'],
               ['x', 'x', '3', '16', '3', '9', 'x', '16', 'x', '14', 'x', '17'],
               ['x', 'x', 'x', '19', '7', '20', 'x', 'x', '11', '4', 'x', '4'],
               ['7', 'x', '8', '11', 'x', '1', '15', '5', 'x', 'x', '11', 'x'],
               ['x', 'x', 'x', 'x', 'x', 'x', '6', '11', 'x', 'x', 'x', '8'],
               ['x', '15', '2', 'x', 'x', '18', 'x', '1', '16', '15', '6', '5'],
               ['x', '4', '18', '8', '9', 'x', 'x', '17', '20', '13', 'x', '10'],
               ['x', '16', 'x', '19', 'x', '17', 'x', '13', '11', '14', '2', 'x'],
               ['12', 'x', '11', 'x', '5', '3', 'x', '13', '17', '6', 'x', 'x'],
               ['14', 'x', 'x', 'x', 'x', 'x', 'x', 'x', '11', 'x', '16', 'x'],
               ['12', 'x', 'x', '12', 'x', '10', 'x', '18', '14', '8', 'x', 'x'])
   num_rows = 12
   num_cols = 12
   start = (3, 3)
   end = (7, 11)
   districts = [(0, 3), (4, 6), (7, 11)]


   # Initialize a dictionary to store the cost of reaching each visited state
   visited_costs = {}
   visited_costs[start] = 0


   # Initialize a priority queue of states not yet visited, with the start state as the first element. The priority of each element is the cost to reach that state (g) + the estimate remaining cost (h) to reach the end
   # Record the workshops visited in a list; no workshops visited to reach the start state
   queue = [(0, 0, [], start)]


   # While there are un-visited states
   while queue:
       # Pop the state with the lowest sum of the cost so far and estimated cost to the end from the queue
       _, g, actions, state = heapq.heappop(queue)


       # Check if the current state is the end state
       if state == end:
           return actions


       # Generate all possible actions from the current state, which includes moving to any of the 4 neighboring workshops if it's in the same district
       for d_row, d_col in [(0, -1), (0, 1), (1, 0), (-1, 0)]:
           new_state = (state[0] + d_row, state[1] + d_col)
           # Check if the new state is valid, ie if the new state is within the city map, and if the new state is in the same district as the current state
           if (0 <= new_state[0] < num_rows and 0 <= new_state[1] < num_cols and
               any(districts[i][0] <= new_state[0] <= districts[i][1] for i in range(len(districts)) if districts[i][0] <= state[0] <= districts[i][1]) and
               city_map[new_state[0]][new_state[1]] != 'x'):
               # The cost so far is the number of workshops visited, as the task is to minimize the number of workshops visited to reach the end state
               new_cost = g + 1
              
               # If the new state is unvisited or we found a new path with a lower cost to reach this state, add it to the queue of un-visited states
               if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                   visited_costs[new_state] = new_cost
                   heapq.heappush(queue, (new_cost + heuristic(new_state, end), new_cost, actions + [new_state], new_state))
   return None


def heuristic(state, end):
   # An admissible and consistent heuristic is the Manhattan distance between the current state and the end state
   # This heuristic relaxes the constraint that Ben can only move to workshops in the same district
   # It is admissible because it never overestimates the cost to reach the goal, as each move is either horizontal or vertical
   # It's consistent because moving to a workshop in a different district increases the heuristic cost of the successor node by a max of 1 (if the moved workshop is in a different district), which is equal to the cost of reaching the successor node
   return abs(state[0] - end[0]) + abs(state[1] - end[1])


print(a_star())
