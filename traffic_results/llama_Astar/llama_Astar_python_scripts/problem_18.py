
import heapq


def a_star():
   # Define the initial state of the city map as a 2d tuple
   city_map = (['13', 'x', 'x', 'x', 'x', 'x', '8', 'x', '6'],
               ['x', 'x', 'x', '8', '10', 'x', '17', 'x', '15', '14'],
               ['x', '6', 'x', 'x', 'x', '16', '12', '7', '8', '11'],
               ['x', '15', 'x', '1', '11', '19', '9', '17', 'x', 'x'],
               ['18', '20', '16', '19', '12', '1', 'x', 'x', 'x', '5'],
               ['11', 'x', '18', '14', 'x', '2', 'x', '9', '8', '1'],
               ['x', '2', '5', '16', '3', '9', '2', '18', 'x', 'x'],
               ['x', '8', '15', '17', '16', '6', 'x', '3', 'x', '10'],
               ['3', 'x', 'x', 'x', '8', '9', '10', 'x', '6', 'x'],
               ['6', 'x', '9', '16', '1', '3', '16', '18', 'x', 'x'])
   num_rows = 10
   num_cols = 10
   start = (1, 8)
   end = (4, 1)
   districts = [(0, 1), (2, 4), (5, 9)]


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
           if (0 <= new_state[0] < num_rows and 0 <= new_state[1] < num_cols and
               city_map[new_state[0]][new_state[1]] != 'x' and
               any(districts[i][0] <= new_state[0] <= districts[i][1] for i in range(len(districts)) if i != actions[-1][0])):
               # The cost so far is the number of moves made, as the task is to minimize the number of moves required
               new_cost = g + 1
              
               # If the new state is unvisited or we found a new path with a lower cost to reach this state, add it to the queue of un-visited states
               if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                   visited_costs[new_state] = new_cost
                   # The heuristic is the Manhattan distance to the end state
                   h = abs(new_state[0] - end[0]) + abs(new_state[1] - end[1])
                   heapq.heappush(queue, (new_cost + h, new_cost, actions + [new_state], new_state))
   return None


print(a_star())
