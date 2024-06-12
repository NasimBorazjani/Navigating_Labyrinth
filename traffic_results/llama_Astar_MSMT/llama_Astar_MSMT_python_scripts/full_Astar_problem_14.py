
import heapq


def initialize():
   # Define the initial state of the city map as a 2d tuple
   city_map = [['x', 3, 13, 18, 'x', 'x', 3, 'x', 'x'],
               ['x', 3, 'x', 'x', 18, 1, 13, 'x', 'x'],
               ['x', 'x', 'x', 6, 'x', 13, 'x', 11, 1],
               [4, 3, 'x', 'x', 'x', 'x', 6, 6, 11],
               [14, 16, 'x', 'x', 'x', 'x', 'x', 18, 11],
               [14, 'x', 11, 'x', 'x', 4, 'x', 1, 'x'],
               [18, 7, 1, 'x', 8, 'x', 'x', 'x', 'x'],
               [4, 9, 6, 12, 13, 19, 'x', 14, 4],
               ['x', 'x', 17, 12, 7, 7, 9, 3, 1]]
   num_rows = 9
   num_cols = 9
   # The start and end workshops
   start = (3, 1)
   end = (7, 8)
   # The districts
   districts = [(0, 3), (4, 6), (7, 8)]


   visited_costs = {}
   visited_costs[start] = 0


   queue = [(0, 0, [], start)]
  
   return city_map, num_rows, num_cols, start, end, districts, visited_costs, queue
  
def a_star():
  
   city_map, num_rows, num_cols, start, end, districts, visited_costs, queue = initialize()


   while queue:
       _, g, actions, state = heapq.heappop(queue)


       # Check if the current state is the goal state
       if state == end:
           return actions


       # Generate all possible actions from the current state, which includes moving to any of the 4 neighboring workshops if it's not an 'x' and it's in a different district
       for d_row, d_col in [(0, -1), (0, 1), (1, 0), (-1, 0)]:
           new_row, new_col = state[0] + d_row, state[1] + d_col
           # Check if the new state would be valid, ie if the new workshop is within the bounds of the city map, it's not an 'x', and it's in a different district
           if (0 <= new_row < num_rows and 0 <= new_col < num_cols and
               city_map[new_row][new_col] != 'x' and
               any(start_row <= new_row <= end_row for start_row, end_row in districts) and
               any(start_col <= new_col <= end_col for start_col, end_col in districts)):
               # The actions is valid, generate the new state
               new_state = (new_row, new_col)
               # The cost so far is the number of moves made, as we are trying to minimize the number of moves required to reach the goal state
               new_cost = g + 1
              
               # If the new state is unvisited or we found a new path with a lower cost to reach this state, add it to the queue of un-visited states
               if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                   visited_costs[new_state] = new_cost
                   heapq.heappush(queue, (new_cost + heuristic(new_state, end, city_map, districts), new_cost, actions + [new_state], new_state))
                  
   return None


def heuristic(state, goal, city_map, districts):
   # An admissible and consistent heuristic is the sum of the Manhattan distances (the shortest path) of each workshop from its goal position
   # The heuristic relaxes the constraint that a workshop can only be visited if it's in a different district, presuming we can move the workshops to their goal position by moving them to any of the other workshops
   # Thus the heuristic reports a lower estimate on the cost to reach goal state and is admissible
   # The heuristic is consistent because the cost of moving a workshop to a neighboring coordinate is always 1, which is exactly the decrease in the Manhattan distance, if the workshop is moved toward its goal position, otherwise the estimated cost of the successor node is the same or higher, and he heuristic estimate for the goal state is 0, as the distance of each workshop from its goal position would be 0 in the goal state.
   h = 0
   for d_row, d_col in districts:
       for row in range(d_row, d_col + 1):
           for col in range(num_cols):
               if city_map[row][col] != 'x':
                   h += abs(row - state[0]) + abs(col - state[1])
   return h


print(a_star())
