
import heapq


def a_star():
   # Define the initial state of the city map as a 2d tuple
   city_map = [['x', 17, 14, 18, 'x', 'x', 8, 18, 10, 5, 5, 'x', 'x'],
               ['x', 'x', 'x', 'x', 17, 18, 17, 17, 6, 12, 'x', 7, 16],
               [17, 'x', 17, 6, 18, 'x', 10, 13, 10, 19, 15, 4, 13],
               [15, 5, 15, 3, 17, 3, 'x', 'x', 18, 15, 19, 3, 2],
               ['x', 'x', 'x', 'x', 2, 10, 'x', 'x', 'x', 18, 14, 5, 12],
               ['x', 16, 'x', 12, 4, 7, 'x', 'x', 9, 'x', 'x', 'x'],
               ['x', 7, 'x', 'x', 16, 2, 9, 1, 3, 'x', 'x', 4, 'x'],
               [15, 16, 'x', 10, 1, 16, 'x', 'x', 2, 18, 1, 'x', 'x'],
               ['x', 'x', 8, 3, 'x', 19, 'x', 'x', 'x', 5, 9, 'x', 'x'],
               ['x', 8, 12, 14, 'x', 'x', 'x', 16, 'x', 8, 'x', 3, 2],
               [8, 1, 'x', 'x', 'x', 'x', 13, 'x', 'x', 'x', 9, 'x', 12],
               ['x', 'x', 3, 3, 11, 'x', 'x', 16, 'x', 'x', 5, 'x', 'x'],
               ['x', 11, 17, 'x', 'x', 'x', 'x', 9, 'x', 'x', 2, 15, 'x']]
   num_rows = 12
   num_cols = 13
   start = (3, 10)
   end = (9, 2)
   districts = [(0, 3), (4, 8), (9, 12)]


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


       # Generate all possible actions from the current state, which includes moving to any of the 4 neighboring workshops if it's not an 'x' and the district of the new state is different from the current state
       for d_row, d_col in [(0, -1), (0, 1), (1, 0), (-1, 0)]:
           new_state = (state[0] + d_row, state[1] + d_col)
           # Check if the new state is valid, ie if the new state is within the city map and the district of the new state is different from the current state
           if (0 <= new_state[0] < num_rows and 0 <= new_state[1] < num_cols and city_map[new_state[0]][new_state[1]] != 'x' and any(start[0] < new_state[0] <= end[0] for start, end in districts) and any(start[1] < new_state[1] <= end[1] for start, end in districts) and new_state != state:
               # The cost so far is the number of moves made, as the task is to minimize the number of moves required to reach the end state
               new_cost = g + 1
              
               # If the new state is unvisited or we found a new path with a lower cost to reach this state, add it to the queue of un-visited states
               if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                   visited_costs[new_state] = new_cost
                   heapq.heappush(queue, (new_cost + heuristic(new_state, end), new_cost, actions + [new_state], new_state))
                  
   return None


def heuristic(state, end):
   # An admissible and consistent heuristic is the Manhattan distance between the current state and the end state
   # This heuristic relaxes the constraint that Ben can only visit workshops in different districts
   # It is admissible because it never overestimates the cost to reach the goal, as the heuristic cost of the successor node is always less than or equal to the cost of reaching the goal from the successor node
   # It's consistent because moving to a workshop in a different district reduces the heuristic cost of the successor node by a max of 1 (if the new district is closer to the end state), which is equal to the cost of reaching the successor node
   return abs(state[0] - end[0]) + abs(state[1] - end[1])


print(a_star())
