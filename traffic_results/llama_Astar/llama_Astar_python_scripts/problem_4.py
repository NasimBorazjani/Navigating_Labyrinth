
import heapq


def a_star():
   # Define the initial state of the city map as a 2d tuple
   city_map = (('18', '9', '2', 'x', '9', '14', 'x', '1', 'x'),
               ('3', '14', '18', '7', 'x', '3', 'x', '2', '19'),
               ('6', '18', '20', '3', '13', 'x', '6', '10', 'x'),
               ('20', 'x', '12', '4', '14', '6', 'x', 'x', 'x'),
               ('7', '18', '8', '5', '19', '3', 'x', 'x', '7'),
               ('15', '9', '14', '16', '5', '14', '6', 'x', 'x'),
               ('x', '5', '13', 'x', 'x', '19', 'x', 'x', '2'),
               ('x', 'x', '8', 'x', 'x', 'x', 'x', '17', '12'),
               ('x', '1', 'x', '3', '19', 'x', '2', '18'))
   num_rows = 9
   num_cols = 9
   start = (2, 0)
   end = (5, 6)
   districts = [(0, 2), (3, 4), (5, 8)]


   # Initialize a dictionary to store the cost of reaching each visited state
   visited_costs = {}
   visited_costs[start] = 0


   # Initialize a priority queue of states not yet visited, with the initial state as the first element. The priority of each element is the cost to reach that state (g) + the estimate remaining cost (h) to reach the goal
   # Record the workshops visited in a list; no workshops visited to reach the initial state
   queue = [(0, 0, [], start)]


   # While there are un-visited states
   while queue:
       # Pop the state with the lowest sum of the cost so far and estimated cost to the goal from the queue
       _, g, actions, state = heapq.heappop(queue)


       # Check if the current state is the goal state
       if state == end:
           return actions


       # Generate all possible actions from the current state, which includes moving to any of the 4 directions (north, south, east, west) from the current workshop
       for d_row, d_col in [(0, -1), (0, 1), (1, 0), (-1, 0)]:
           new_state = (state[0] + d_row, state[1] + d_col)
           # Check if the new state would be valid, ie the new state must be within the city map boundaries and the new state must be in the same district as the current state
           if (0 <= new_state[0] < num_rows and 0 <= new_state[1] < num_cols and
               any(start_row <= new_state[0] <= end_row for start_row, end_row in districts) and
               city_map[new_state[0]][new_state[1]] != 'x'):
               # The cost so far is the number of workshops visited, as the task is to minimize the number of workshops visited to reach the goal state
               new_cost = g + 1
              
               # If the new state is unvisited or we found a new path with a lower cost to reach this state, add it to the queue of un-visited states
               if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                   visited_costs[new_state] = new_cost
                   heapq.heappush(queue, (new_cost + heuristic(new_state, end), new_cost, actions + [new_state], new_state))
                  
   return None


def heuristic(state, goal):
   # An admissible and consistent heuristic is the Euclidean distance between the current state and the goal state
   # This heuristic is admissible because it never overestimates the cost to reach the goal, as the Euclidean distance is a lower bound on the actual path length
   # It is consistent because moving from one state to another always either increases or decreases the heuristic cost of the successor node by a factor of sqrt(2), which is equal to the cost of reaching the successor node
   # Thus h(s) is always less than or equal to c(s, n)(equal to sqrt(2)) + h(n)
   return math.sqrt((state[0] - goal[0]) ** 2 + (state[1] - goal[1]) ** 2)


print(a_star())
