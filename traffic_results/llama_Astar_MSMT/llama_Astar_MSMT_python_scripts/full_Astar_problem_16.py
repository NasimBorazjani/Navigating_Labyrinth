
import heapq


def initialize():
   # Define the initial state of the city as a 2d tuple
   initial_state = (('x', 'x', 'x', 16, 1, 13, 17, 7, 14, 'x'),
                   ('x', 10, 'x', 12, 'x', 13, 'x', 8, 19, 4),
                   (9, 13, 'x', 13, 'x', 'x', 15, 'x', 'x', 16),
                   (3, 8, 'x', 16, 12, 'x', 'x', 'x', 'x', 13),
                   (13, 'x', 1, 15, 18, 8, 'x', 10, 'x', 'x'),
                   (8, 1, 2, 14, 'x', 8, 'x', 'x', 11),
                   (14, 13, 15, 'x', 16, 'x', 13, 'x', 19),
                   ('x', 4, 10, 'x', 'x', 16, 'x', 11, 'x', 'x'),
                   ('x', 14, 'x', 'x', 'x', 'x', 18, 6, 18),
                   ('x', 3, 2, 6, 7, 'x', 'x', 9, 8, 5))
   num_rows = 9
   num_cols = 10
   start_pos = (5, 1)
   end_pos = (3, 9)
   districts = [(0, 3), (4, 5), (6, 9)]


   visited_costs = {}
   visited_costs[initial_state] = 0


   queue = [(0, 0, [], initial_state)]
  
   return initial_state, num_rows, num_cols, start_pos, end_pos, districts, visited_costs, queue
  
def a_star():
  
   initial_state, num_rows, num_cols, start_pos, end_pos, districts, visited_costs, queue = initialize()


   while queue:
       _, g, actions, state = heapq.heappop(queue)


       # Check if the current state is the goal state
       if start_pos == end_pos:
           return actions


       # Generate all possible actions from the current state, which includes moving to a neighboring workshop in a valid direction (north, south, east, west)
       for d_row, d_col in [(0, -1), (0, 1), (1, 0), (-1, 0)]:
           new_pos = (start_pos[0] + d_row, start_pos[1] + d_col)
           # Check if the new position is valid, ie within the bounds of the city, not a closed workshop, and not visited before
           if (0 <= new_pos[0] < num_rows and 0 <= new_pos[1] < num_cols and state[new_pos[0]][new_pos[1]] != 'x' and new_pos not in actions):
               # Generate the new state
               new_state = [list(row[:]) for row in state]
               new_state[start_pos[0]][start_pos[1]] = 'x'
               new_state[new_pos[0]][new_pos[1]] = 1
               new_state = tuple(tuple(row) for row in new_state)
               # The cost so far is the time taken to reach the new workshop, as we are trying to minimize the total time taken
               new_cost = g + 1
              
               # If the new state is unvisited or we found a new path with a lower cost to reach this state, add it to the queue of un-visited states
               if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                   visited_costs[new_state] = new_cost
                   heapq.heappush(queue, (new_cost + heuristic(new_state, end_pos), new_cost, actions + [new_pos], new_state))


                   # Update the starting position for the next iteration
                   start_pos = new_pos
   return None


def heuristic(state, end_pos):
   # An admissible and consistent heuristic is the distance between the current position and the destination position, using the Manhattan distance
   # This heuristic relaxes the constraint that the car can only move north, south, east, or west
   # It is admissible because it never overestimates the cost to reach the goal, as the car can always move in a straight line to the destination
   # It's consistent because moving the car to a neighboring workshop reduces the heuristic cost of the successor node by a max of 1 (if the moved workshop is closer to the destination), which is equal to the cost of reaching the successor node
   return abs(end_pos[0] - start_pos[0]) + abs(end_pos[1] - start_pos[1])


print(a_star())
