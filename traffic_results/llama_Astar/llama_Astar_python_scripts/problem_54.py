
import heapq


def a_star():
   # Define the initial state of the city map as a 2d tuple
   city_map = [['19', '14', '16', '4', '15', '16', '15', 'x', '9', 'x', 'x', 'x'],
               ['x', '7', '12', '6', 'x', '12', 'x', '3', 'x', '14', '5', '9'],
               ['1', '12', 'x', 'x', '12', 'x', 'x', 'x', 'x', '10', '1'],
               ['x', '1', '15', '14', 'x', '2', '13', 'x', 'x', 'x', '10', '9'],
               ['7', 'x', '13', 'x', '14', '1', '14', '8', 'x', 'x', '8', '5'],
               ['18', 'x', '8', '13', '12', '13', 'x', 'x', 'x', '14', 'x'],
               ['x', '15', 'x', 'x', 'x', 'x', 'x', 'x', 'x', '17', '10'],
               ['x', '5', 'x', '4', 'x', 'x', '3', '5', '6', '6', '11'],
               ['x', '15', '6', 'x', '4', '18', 'x', 'x', '14', '10', '2', '8'],
               ['13', '10', '13', '7', '3', '6', 'x', 'x', '10', '17', '10', '15'],
               ['4', 'x', 'x', '7', '19', '4', '13', '13', '12', 'x', 'x', '13'],
               ['5', 'x', 'x', '9', '19', '18', 'x', 'x', '16', 'x', '2', 'x']]
   num_rows = 12
   num_cols = 12
   start = (4, 11)
   end = (9, 2)
   districts = [(0, 3), (4, 8), (9, 11)]


   # Initialize a dictionary to store the cost of reaching each visited state
   visited_costs = {}
   visited_costs[start] = 0


   # Initialize a priority queue of states not yet visited, with the start state as the first element. The priority of each element is the cost to reach that state (g) + the estimate remaining cost (h) to reach the goal
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
           new_state = (state[0] + d_row, state[1] + d_col)
           # Check if the new state is valid, ie if the new state is within the grid and the destination district has not been visited yet
           if (0 <= new_state[0] < num_rows and 0 <= new_state[1] < num_cols and
               city_map[new_state[0]][new_state[1]] != 'x' and
               any(start[0] <= new_state[0] <= end[0] and start[1] <= new_state[1] <= end[1] for start, end in districts)):
               # The actions is valid, generate the new state
               new_cost = g + int(city_map[new_state[0]][new_state[1]])
              
               # If the new state is unvisited or we found a new path with a lower cost to reach this state, add it to the queue of not-yet-visited states
               if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                   visited_costs[new_state] = new_cost
                   heapq.heappush(queue, (new_cost + heuristic(new_state, end), new_cost, actions + [new_state], new_state))
                  
   return None


def heuristic(state, goal):
   # An admissible and consistent heuristic is the Euclidean distance between the current state and the goal state
   # This heuristic relaxes the constraint that Ben can only move to neighboring workshops
   # It is admissible because it never overestimates the cost to reach the goal, as the Euclidean distance is a lower bound on the actual path length
   # It's consistent because moving to a neighboring workshop reduces the heuristic cost of the successor node by a max of sqrt(2), which is equal to the cost of reaching the successor node
   # Thus h(s) is always less than or equal to c(s, n)(equal to sqrt(2)) + h(n)
   return math.sqrt((state[0] - goal[0]) ** 2 + (state[1] - goal[1]) ** 2)


print(a_star())
