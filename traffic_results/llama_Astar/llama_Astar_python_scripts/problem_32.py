
import heapq


def a_star():
   # Define the initial state of the city map as a 2d tuple
   city_map = [['x', 'x', 13, 'x', 'x', 7, 13, 3, 'x', 13],
               [10, 4, 'x', 4, 12, 2, 'x', 3, 4, 'x', 15],
               ['x', 3, 'x', 'x', 15, 9, 'x', 'x', 18, 17, 14],
               [5, 'x', 'x', 'x', 3, 'x', 17, 9, 17],
               [8, 3, 13, 'x', 5, 7, 8, 17, 7, 'x', 'x'],
               ['x', 'x', 13, 2, 2, 11, 6, 8, 'x', 'x', 'x'],
               ['x', 1, 9, 6, 5, 13, 16, 1, 7, 5, 'x'],
               [4, 'x', 13, 'x', 10, 18, 3, 'x', 'x', 19, 19],
               ['x', 'x', 'x', 2, 5, 9, 13, 'x', 7, 1, 'x'],
               ['x', 'x', 7, 'x', 'x', 5, 19, 'x', 'x', 'x', 'x'],
               ['x', 'x', 'x', 6, 'x', 19, 'x', 'x', 'x', 'x', 1]]
   num_rows = 10
   num_cols = 10
   start = (5, 2)
   end = (2, 10)
   districts = [(0, 2), (3, 4), (5, 10)]


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


       # Generate all possible actions from the current state, which includes moving to a neighboring workshop in a valid direction
       for d_row, d_col in [(0, -1), (0, 1), (1, 0), (-1, 0)]:
           new_row, new_col = state[0] + d_row, state[1] + d_col
           # Check if the new state would be valid, ie the new position is within the bounds of the city map, there's no x in that position, and the new position is in a different district from the current state
           if (0 <= new_row < num_rows and 0 <= new_col < num_cols and city_map[new_row][new_col] != 'x' and any(start[0] // 3 < new_row < end[0] // 3 or start[1] // 3 < new_col < end[1] // 3 for start, end in districts)):
               # The actions is valid, generate the new state
               new_state = (new_row, new_col)
               # The cost so far is the number of moves made, as our objective is to minimize the number of moves required to reach the goal state
               new_cost = g + city_map[new_row][new_col]
              
               # If the new state is unvisited or we found a new path with a lower cost to reach this state, add it to the queue of not-yet-visited states
               if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                   visited_costs[new_state] = new_cost
                   heapq.heappush(queue, (new_cost + heuristic(new_state, end), new_cost, actions + [new_state], new_state))
                  
   return None


def heuristic(state, goal):
   # An admissible and consistent heuristic is the Manhattan distance between the current state and the goal state
   # This heuristic relaxes the constraint that Ben can only move to a neighboring workshop in a valid direction
   # It is admissible because it never overestimates the cost to reach the goal, as each move in the heuristic cost of the successor node is a valid move in the actual problem
   # It's consistent because moving to a neighboring workshop in a valid direction reduces the heuristic cost of the successor node by a max of 1 (if the moved workshop is in the same district as the current state), which is equal to the cost of reaching the successor node
   return abs(state[0] - goal[0]) + abs(state[1] - goal[1])


print(a_star())
