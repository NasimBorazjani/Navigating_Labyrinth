
import heapq


def a_star():
   # Define the initial state of the city map as a 2d tuple
   city_map = (['19', 'x', '17', '14', '3', 'x', '10', '5', '2'],
               ['x', 'x', '1', 'x', 'x', '19', '7', '1'],
               ['16', '12', 'x', '3', '19', '2', '14', '1', '14'],
               ['x', '1', '16', 'x', '12', '3', '13', 'x', '3'],
               ['x', 'x', '7', '19', '10', 'x', '5', 'x', '19'],
               ['5', 'x', 'x', '6', '14', 'x', 'x', '10', '12'],
               ['x', 'x', 'x', 'x', '18', 'x', 'x', '15', '12'],
               ['x', 'x', '16', '8', 'x', '3', '4', 'x', 'x'],
               ['x', 'x', 'x', '16', 'x', 'x', '8', '14', '7'])
   num_rows = 9
   num_cols = 9
   start = (3, 1)
   end = (5, 8)
   districts = [(0, 3), (4, 4), (5, 8)]


   # Initialize a dictionary to store the cost of reaching each visited state
   visited_costs = {}
   visited_costs[start] = 0


   # Initialize a priority queue of states not yet visited, with the start state as the first element. The priority of each element is the cost to reach that state (g) + the estimate remaining cost (h) to reach the goal
   # Record the workshops visited in a list; no workshops visited to reach the start state
   queue = [(0, 0, [], start)]


   # While there are un-visited states
   while queue:
       # Pop the state with the lowest sum of the cost so far and estimated cost to the goal from the queue
       _, g, actions, state = heapq.heappop(queue)


       # Check if the current state is the goal state
       if state == end:
           return actions


       # Generate all possible actions from the current state, which includes moving to any of the 4 neighboring workshops if it's in the same district and not visited yet
       for d_row, d_col in [(0, -1), (0, 1), (1, 0), (-1, 0)]:
           new_state = (state[0] + d_row, state[1] + d_col)
           # Check if the new state is valid, ie if the new state is within the city map, not visited yet, and in the same district as the current state
           if (0 <= new_state[0] < num_rows and 0 <= new_state[1] < num_cols and
               city_map[new_state[0]][new_state[1]] != 'x' and
               any(districts[i][0] <= new_state[0] < districts[i][1] for i in range(len(districts)) if districts[i][0] <= state[0] < districts[i][1])):
               # The cost so far is the number of workshops visited, as the task is to minimize the number of workshops visited to reach the goal state
               new_cost = g + 1
              
               # If the new state is unvisited or we found a new path with a lower cost to reach this state, add it to the queue of not-yet-visited states
               if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                   visited_costs[new_state] = new_cost
                   heapq.heappush(queue, (new_cost + heuristic(new_state, end), new_cost, actions + [new_state], new_state))
                  
   return None


def heuristic(state, goal):
   # An admissible and consistent heuristic is the Manhattan distance between the current state and the goal state
   # This heuristic relaxes the constraint that Ben can only move to neighboring workshops in the same district
   # It is admissible because it never overestimates the cost to reach the goal, as the heuristic cost of the successor node is always less than or equal to the cost of reaching the goal from the current state
   # It's consistent because moving to a neighboring workshop in the same district reduces the heuristic cost of the successor node by a max of 1 (if the new workshop is in a different district), which is equal to the cost of reaching the successor node
   return abs(state[0] - goal[0]) + abs(state[1] - goal[1])


print(a_star())
