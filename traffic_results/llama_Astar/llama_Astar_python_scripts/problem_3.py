
import heapq


def a_star():
   # Define the initial state of the city map as a 2d tuple
   city_map = (['10', '14', '4', '16', 'x', '17', '5', 'x', 'x'],
               ['5', '20', '16', '3', '1', '8', 'x', '16', '19'],
               ['1', 'x', '5', '13', '3', '15', '19', '15', 'x'],
               ['x', '16', '13', '20', 'x', '8', 'x', 'x', 'x'],
               ['x', '16', 'x', '17', '11', '1', 'x', '15', 'x'],
               ['10', 'x', '14', '11', '5', '7', '12', 'x', '5'],
               ['7', 'x', '15', 'x', '15', '8', '3', '6', '7'],
               ['x', '12', '14', 'x', 'x', 'x', '16', '3', '13'],
               ['19', '5', '10', 'x', 'x', 'x', '9', '7', '14'])
   num_rows = 9
   num_cols = 9
   start = (7, 7)
   end = (1, 2)
   districts = [(0, 1), (2, 6), (7, 8)]


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


       # Generate all possible actions from the current state, which includes moving to any of the 4 neighboring workshops if it's not an 'x' and the destination district has not been visited yet
       for d_row, d_col in [(0, -1), (0, 1), (1, 0), (-1, 0)]:
           new_row, new_col = state[0] + d_row, state[1] + d_col
           # Check if the new state would be valid, ie if the new position is within the bounds of the city map and the destination district has not been visited yet
           if 0 <= new_row < num_rows and 0 <= new_col < num_cols and city_map[new_row][new_col] != 'x' and any(start[0] <= new_row <= end[0] for start, end in districts):
               # The actions is valid, generate the new state
               new_state = (new_row, new_col)
               # The cost so far is the number of moves made, as our objective is to minimize the number of moves required to reach the goal state
               new_cost = g + int(city_map[new_row][new_col])
              
               # If the new state is unvisited or we found a new path with a lower cost to reach this state, add it to the queue of not-yet-visited states
               if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                   visited_costs[new_state] = new_cost
                   heapq.heappush(queue, (new_cost + heuristic(new_state, end), new_cost, actions + [new_state], new_state))
                  
   return None


def heuristic(state, goal):
   # An admissible and consistent heuristic is the Euclidean distance between the current state and the goal state
   # This heuristic relaxes the constraint that Ben can only move to neighboring workshops
   # It is admissible because it never overestimates the cost to reach the goal, as the Euclidean distance is a lower bound on the actual travel time
   # The heuristic is consistent because moving to a neighboring workshop reduces the heuristic cost of the successor node by a max of sqrt(2), which is equal to the cost of reaching the successor node
   return math.sqrt((state[0] - goal[0]) ** 2 + (state[1] - goal[1]) ** 2)


print(a_star())
