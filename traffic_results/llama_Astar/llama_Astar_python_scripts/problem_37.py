
import heapq


def a_star():
   # Define the initial state of the city map as a 2d tuple
   city_map = (['15', 'x', '12', '9', '19', 'x', 'x', '13', 'x', '16'],
               ['14', '6', '3', '18', 'x', '8', '18', 'x', 'x', 'x', 'x'],
               ['16', '10', '9', '4', '9', '5', '15', '4', 'x', 'x', '2'],
               ['5', '9', 'x', '8', '1', '15', '7', '15', 'x', 'x', 'x'],
               ['6', 'x', '3', 'x', '4', '6', '6', '19', 'x', '16', '13'],
               ['17', 'x', '11', '5', '18', '11', '18', 'x', 'x', '10', '19'],
               ['6', '3', 'x', 'x', '10', '18', '2', 'x', 'x', 'x', 'x'],
               ['x', 'x', '4', '2', 'x', '13', '7', 'x', '3', '19', '16'],
               ['x', '1', '10', 'x', '15', 'x', '7', 'x', '1', '7', '10'],
               ['x', 'x', 'x', '4', '7', 'x', '7', 'x', 'x', '6', 'x'],
               ['16', 'x', '15', '3', 'x', '8', 'x', 'x', '13', 'x', '14'])
   num_rows = 10
   num_cols = 11
   start = (7, 5)
   end = (1, 0)
   districts = [(0, 1), (2, 6), (7, 10)]


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
           # Check if the new state is valid, ie if the new state is within the grid and the district of the new state is different from the current state
           if (0 <= new_state[0] < num_rows and 0 <= new_state[1] < num_cols and
               city_map[new_state[0]][new_state[1]] != 'x' and
               any(districts[i][0] <= new_state[0] <= districts[i][1] for i in range(len(districts)) if i != state[2]) and
               any(districts[i][0] <= state[0] <= districts[i][1] for i in range(len(districts)) if i != new_state[2])):
               # Calculate the district of the new state
               new_state = (new_state[0], new_state[1], next(i for i in range(len(districts)) if districts[i][0] <= new_state[0] <= districts[i][1]))
               # The cost so far is the number of moves made, as the task is to minimize the number of moves required to reach the end state
               new_cost = g + 1
              
               # If the new state is unvisited or we found a new path with a lower cost to reach this state, add it to the queue of un-visited states
               if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                   visited_costs[new_state] = new_cost
                   heapq.heappush(queue, (new_cost + heuristic(new_state, end), new_cost, actions + [new_state], new_state))
   return None


def heuristic(state, end):
   # An admissible and consistent heuristic is the Manhattan distance between the current state and the end state
   # This heuristic relaxes the constraint that Ben can only visit workshops in different districts, as the heuristic estimate for the goal state is 0, as the distance of the goal state would be 0 in the goal state.
   return abs(state[0] - end[0]) + abs(state[1] - end[1])


print(a_star())
