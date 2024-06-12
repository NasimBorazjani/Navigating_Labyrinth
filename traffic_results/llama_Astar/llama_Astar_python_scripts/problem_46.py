
import heapq


def a_star():
   # Define the initial state of the city map as a 2d tuple
   city_map = [['3', '14', '2', 'x', 'x', 'x', '19', '13', '17', '12', '8', 'x'],
               ['1', '2', '13', '1', '4', '19', 'x', 'x', '16', 'x', 'x', '12'],
               ['9', '8', '9', '15', 'x', '12', 'x', 'x', 'x', 'x', 'x', '14'],
               ['11', '1', '10', '18', 'x', '16', '1', '12', 'x', 'x', 'x', 'x'],
               ['7', '16', '13', '10', '13', 'x', '14', 'x', 'x', '9', 'x', '7'],
               ['19', '7', '7', '20', '13', '14', '18', 'x', 'x', '7', '5', 'x'],
               ['4', 'x', '11', 'x', 'x', '2', '7', '1', '5', 'x', 'x', 'x'],
               ['x', 'x', 'x', 'x', 'x', 'x', 'x', '18', 'x', '1', 'x'],
               ['4', 'x', 'x', '9', '19', '2', '18', '8', '16', '14', '19', '7'],
               ['x', 'x', 'x', 'x', '9', 'x', '17', '17', '1', '2', '2', '15'],
               ['18', 'x', 'x', 'x', 'x', 'x', '11', '10', 'x', '17', 'x', 'x'],
               ['9', 'x', 'x', 'x', '10', '3', 'x', 'x', '13', 'x', '2', 'x']]
   num_rows = 11
   num_cols = 12
   start = (1, 0)
   end = (8, 10)
   districts = [(0, 1), (2, 7), (8, 11)]


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


       # Generate all possible actions from the current state, which includes moving to any of the 4 neighboring workshops if it's not an 'x' and the district of the new workshop is not visited yet
       for d_row, d_col in [(0, -1), (0, 1), (1, 0), (-1, 0)]:
           new_row, new_col = state[0] + d_row, state[1] + d_col
           if (0 <= new_row < num_rows and 0 <= new_col < num_cols and
               city_map[new_row][new_col] != 'x' and
               any(districts[i][0] <= new_row < districts[i][1] for i in range(len(districts)) if (new_row, new_col) not in actions)):
               # The actions is valid, generate the new state
               new_state = (new_row, new_col)
               # The cost so far is the number of moves made, as our objective is to minimize the number of moves required to reach the end state
               new_cost = g + 1
              
               # If the new state is unvisited or we found a new path with a lower cost to reach this state, add it to the queue of not-yet-visited states
               if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                   visited_costs[new_state] = new_cost
                   heapq.heappush(queue, (new_cost + heuristic(new_state, end, city_map), new_cost, actions + [new_state], new_state))
                  
   return None


def heuristic(state, end, city_map):
   # An admissible and consistent heuristic is the Manhattan distance between the current state and the end state
   # This heuristic relaxes the constraint that Ben can only move to a workshop in the same district
   # It is admissible because it never overestimates the cost to reach the goal, as each move is either horizontal or vertical
   # It's consistent because moving to a workshop in a different district is costlier, as it involves moving to a workshop in a different district first
   # Thus h(s) is always less than or equal to c(s, n)(equal to 1) + h(n)
   return abs(state[0] - end[0]) + abs(state[1] - end[1])


print(a_star())
