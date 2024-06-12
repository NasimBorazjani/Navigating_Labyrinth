
import heapq


def a_star():
   # Define the initial state of the city map as a 2d tuple
   city_map = (['14', 'x', '11', 'x', 'x', '8', '15', '17', '18', 'x', '11'],
               ['13', '9', '2', '7', '9', '12', '7', 'x', 'x', 'x', '12'],
               ['x', '2', '8', '13', '5', 'x', 'x', '7', '18', 'x', 'x'],
               ['19', '6', '1', '6', '19', '13', '14', 'x', 'x', '17', 'x'],
               ['x', '9', '6', 'x', 'x', '14', '10', 'x', 'x', '5', 'x'],
               ['12', 'x', 'x', 'x', '7', '17', '11', 'x', 'x', '1', 'x'],
               ['x', '16', 'x', '2', '11', '15', '6', 'x', '14', '14', '4'],
               ['x', '15', '14', '11', 'x', '17', '20', '18', '4', '16', '8'],
               ['x', '3', '6', '4', '1', '5', 'x', 'x', '3', '7', '9'],
               ['18', '14', '3', '4', 'x', 'x', 'x', '12', '15', '10', 'x'],
               ['x', '8', 'x', '1', '18', 'x', 'x', 'x', 'x', 'x', 'x'])
   num_rows = 10
   num_cols = 11
   start = (6, 10)
   end = (3, 2)
   districts = [(0, 3), (4, 5), (6, 10)]


   # Initialize a dictionary to store the cost of reaching each visited state
   visited_costs = {}
   visited_costs[start] = 0


   # Initialize a priority queue of states not yet visited, with the start state as the first element. The priority of each element is the cost to reach that state (g) + the estimate remaining cost (h) to reach the end
   # Record the path taken to reach each state in a list; no path taken to reach the start state
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
           # Check if the new state is valid, ie if the new state is within the city map, not an 'x' workshop, and in the same district as the current state
           if (0 <= new_state[0] < num_rows and 0 <= new_state[1] < num_cols and
               city_map[new_state[0]][new_state[1]] != 'x' and
               any(districts[i][0] <= new_state[0] <= districts[i][1] for i in range(len(districts)) if districts[i][0] <= state[0] <= districts[i][1])):
               # The cost so far is the number of moves made, as the task is to minimize the number of moves required to reach the end state
               new_cost = g + 1
              
               # If the new state is unvisited or we found a new path with a lower cost to reach this state, add it to the queue of un-visited states
               if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                   visited_costs[new_state] = new_cost
                   heapq.heappush(queue, (new_cost + heuristic(new_state, end), new_cost, actions + [new_state], new_state))
                  
   return None


def heuristic(state, end):
   # An admissible and consistent heuristic is the Manhattan distance between the current state and the end state
   # This heuristic relaxes the constraint that Ben can only move to workshops in the same district
   # It is admissible because it never overestimates the cost to reach the goal, as the heuristic cost of the successor node is always less than or equal to the cost of reaching the goal from the successor node
   # It's consistent because moving to a workshop in the same district reduces the heuristic cost of the successor node by a max of 1 (if the moved workshop is in the same district but not in the same row or column), which is equal to the cost of reaching the successor node
   return abs(state[0] - end[0]) + abs(state[1] - end[1])


print(a_star())
