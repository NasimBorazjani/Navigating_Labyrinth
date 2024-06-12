
import heapq


def a_star():
   # Define the initial state of the city map as a 2d tuple
   city_map = (['15', 'x', '8', '6', '9', 'x', 'x', 'x', 'x'],
               ['14', 'x', '8', 'x', '5', '11', 'x', '9'],
               ['x', '17', '8', 'x', '17', '15', '12', 'x', 'x', '13'],
               ['x', '13', 'x', 'x', '2', '17', '17', '1', 'x'],
               ['6', 'x', '1', '5', '17', 'x', '2', '18', '11', '7'],
               ['12', '8', '17', '10', 'x', 'x', 'x', '15', 'x', '16'],
               ['12', '12', 'x', '4', 'x', '13', 'x', '10', 'x', '16'],
               ['x', 'x', '10', 'x', '6', 'x', 'x', 'x', '8', '5'],
               ['x', '2', '11', '18', '15', 'x', '11', 'x', 'x', '12'],
               ['x', 'x', '14', 'x', 'x', '7', '14', '15', '18', '9'])
   num_rows = 10
   num_cols = 10
   start = (5, 0)
   end = (3, 8)
   districts = [(0, 3), (4, 4), (5, 9)]


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
           new_state = (state[0] + d_row, state[1] + d_col)
           # Check if the new state is valid, ie if the new state is within the city map boundaries and the destination district has not been visited yet
           if (0 <= new_state[0] < num_rows and 0 <= new_state[1] < num_cols and
               city_map[new_state[0]][new_state[1]] != 'x' and
               any(start[0] <= new_state[0] <= end[0] <= end[0] or
                   start[1] <= new_state[1] <= end[1] <= end[1] for start, end in districts)):
               # The cost so far is the number of moves made, as the task is to minimize the number of moves required to reach the goal state
               new_cost = g + int(city_map[state[0] + d_row][state[1] + d_col])
              
               # If the new state is unvisited or we found a new path with a lower cost to reach this state, add it to the queue of un-visited states
               if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                   visited_costs[new_state] = new_cost
                   heapq.heappush(queue, (new_cost + heuristic(new_state, end), new_cost, actions + [new_state], new_state))
                  
   return None


def heuristic(state, goal):
   # An admissible and consistent heuristic is the Euclidean distance between the current state and the goal state
   # This heuristic is admissible because it never overestimates the cost to reach the goal, as the Euclidean distance is a lower bound on the actual path length
   # It is consistent because moving from one state to another always increases the heuristic cost of the successor node by a value greater than or equal to the cost of reaching the successor node
   # Thus h(s) is always less than or equal to c(s, n)(equal to the actual cost of moving from s to n) + h(n)
   return math.sqrt((state[0] - goal[0]) ** 2 + (state[1] - goal[1]) ** 2)


print(a_star())
