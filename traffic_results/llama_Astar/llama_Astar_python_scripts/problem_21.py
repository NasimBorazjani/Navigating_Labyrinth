
import heapq


def a_star():
   # Define the initial state of the city map as a 2d tuple
   city_map = (['15', '4', '9', '10', '19', 'x', '12', '4', 'x', '15'],
               ['12', '19', '11', 'x', 'x', 'x', 'x', '7', '6', '3'],
               ['4', 'x', '8', 'x', 'x', 'x', '11', '1', '6'],
               ['x', 'x', '5', 'x', 'x', 'x', '12', '6', '6', 'x'],
               ['x', '14', 'x', 'x', '14', '11', '2', '9', '6', '14'],
               ['8', '8', '5', '17', '7', 'x', '1', '2', 'x', '6'],
               ['18', 'x', 'x', '15', 'x', '15', '4', 'x', 'x', '7'],
               ['19', 'x', '10', '18', '14', 'x', '14', '9', '8', '6'],
               ['19', 'x', '14', 'x', '10', '8', '15', 'x', '15', 'x'],
               ['12', '1', 'x', '5', '3', '3', 'x', 'x', 'x', 'x'])
   num_rows = 10
   num_cols = 10
   start = (1, 9)
   end = (6, 3)
   districts = [(0, 1), (2, 6), (7, 9)]


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


       # Generate all possible actions from the current state, which includes moving to any of the 4 neighboring workshops if it's not an 'x' and the destination district has not been visited yet
       for d_row, d_col in [(0, -1), (0, 1), (1, 0), (-1, 0)]:
           new_state = (state[0] + d_row, state[1] + d_col)
           # Check if the new state is valid, ie if the new state is within the city map and the destination district has not been visited yet
           if (0 <= new_state[0] < num_rows and 0 <= new_state[1] < num_cols and
               city_map[new_state[0]][new_state[1]] != 'x' and
               any(districts[i][0] <= new_state[0] <= districts[i][1] for i in range(len(districts)) if i not in actions)):
               # The cost so far is the number of moves made, as the task is to minimize the number of moves required to reach the end state
               new_cost = g + 1
              
               # If the new state is unvisited or we found a new path with a lower cost to reach this state, add it to the queue of un-visited states
               if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                   visited_costs[new_state] = new_cost
                   # The heuristic is the Manhattan distance to the end state
                   h = abs(new_state[0] - end[0]) + abs(new_state[1] - end[1])
                   heapq.heappush(queue, (new_cost + h, new_cost, actions + [new_state], new_state))
   return None


print(a_star())
