
import heapq

def initialize():
   # Define the initial state of the city map as a 2d tuple
   initial_state = ((10, 14, 4, 16, 'x', 17, 5, 'x', 'x'),
                   (5, 20, 16, 3, 1, 8, 'x', 16, 19),
                   (1, 'x', 5, 13, 3, 15, 19, 15, 'x'),
                   ('x', 16, 13, 20, 'x', 8, 'x', 'x', 'x'),
                   ('x', 16, 'x', 17, 11, 1, 'x', 15, 'x'),
                   (10, 'x', 14, 11, 5, 7, 12, 'x', 5),
                   (7, 'x', 15, 'x', 15, 8, 3, 6, 7),
                   ('x', 12, 14, 'x', 'x', 'x', 16, 3, 13),
                   (19, 5, 10, 'x', 'x', 'x', 9, 7, 14))
   num_rows = 9
   num_cols = 9
   start = (7, 7)
   end = (1, 2)
   districts = {1: [(0, 0), (0, 1)], 2: [(2, 0), (6, 1)], 3: [(7, 0), (8, 1)]}

   visited_costs = {}
   visited_costs[start] = 0

   queue = [(0, 0, [], start)]
  
   return initial_state, num_rows, num_cols, start, end, districts, visited_costs, queue
  
def a_star():
  
   initial_state, num_rows, num_cols, start, end, districts, visited_costs, queue = initialize()

   while queue:
       _, g, actions, state = heapq.heappop(queue)

       # If Ben reaches the destination, return the path taken
       if state == end:
           return actions

       # Generate all possible actions from the current state, which includes moving north, south, east, or west
       for d_row, d_col in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
           new_row, new_col = state[0] + d_row, state[1] + d_col
           # Check if the new state is valid, ie within the bounds of the city map and not a closed workshop
           if 0 <= new_row < num_rows and 0 <= new_col < num_cols and initial_state[new_row][new_col] != 'x':
               new_state = (new_row, new_col)
               new_cost = g + initial_state[new_row][new_col]
              
               # Check if Ben has visited at least 1 workshop in each district on the path
               for district, workshops in districts.items():
                   if state in workshops and new_state not in workshops:
                       new_cost += 100  # Penalize for not visiting a workshop in each district

               if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                   visited_costs[new_state] = new_cost
                   heapq.heappush(queue, (g + abs(new_row - end[0]) + abs(new_col - end[1]), new_cost, actions + [new_state], new_state))
                  
   return None


print(a_star())
