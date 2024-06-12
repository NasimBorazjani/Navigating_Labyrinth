
import heapq


def initialize():
   # Define the initial state of the city map as a 2d tuple
   initial_state = (('16', '2', '16', 'x', 'x', 'x', '1', '16', 'x'),
                   ('x', 'x', '19', 'x', '3', 'x', 'x', 'x', 'x'),
                   ('x', 'x', 'x', '3', 'x', '2', 'x', '10', 'x'),
                   ('11', '5', '20', 'x', '1', '3', '1', 'x', '9', 'x'),
                   ('x', 'x', '8', '19', 'x', 'x', 'x', '16', '15'),
                   ('x', '3', '5', '10', 'x', 'x', '4', '1', 'x'),
                   ('9', '18', '10', '17', '5', '6', 'x', 'x', 'x', '5'),
                   ('x', 'x', '14', '5', '18', 'x', 'x', '1', '15', '1'),
                   ('13', 'x', '13', '13', '14', '2', '19', '12', 'x', '1'),
                   ('9', '6', 'x', '4', '12', '1', '13', '8', '2', '13'))
   num_rows = 10
   num_cols = 10
   start_coord = (7, 9)
   end_coord = (3, 2)
   districts = [(0, 3), (4, 6), (7, 9)]


   visited_costs = {}
   visited_costs[initial_state] = 0


   queue = [(0, 0, [], initial_state)]
  
   return initial_state, num_rows, num_cols, start_coord, end_coord, districts, visited_costs, queue
  
def a_star():
  
   initial_state, num_rows, num_cols, start_coord, end_coord, districts, visited_costs, queue = initialize()


   while queue:
       _, g, actions, state = heapq.heappop(queue)


       # Check if the current state is the goal state
       if start_coord == end_coord and all(any(start_coord[0] >= district[0] and start_coord[0] <= district[1] for district in districts) for start_coord in actions):
           return actions


       # Generate all possible actions from the current state, which involves moving Ben to a neighboring workshop in a valid direction
       for d_row, d_col in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
           new_coord = (start_coord[0] + d_row, start_coord[1] + d_col)
           # Check if the new state would be valid, ie the new position is within the bounds of the map, and the new position is not in a district that has already been visited
           if 0 <= new_coord[0] < num_rows and 0 <= new_coord[1] < num_cols and state[new_coord[0]][new_coord[1]] != 'x' and all(new_coord[0] not in range(district[0], district[1] + 1) for district in districts for start_coord in actions):
               # Generate the new state
               new_state = [list(row[:]) for row in state]
               number_to_be_moved = new_state[start_coord[0]][start_coord[1]]
               new_state[start_coord[0]][start_coord[1]] = 'x'
               new_state[new_coord[0]][new_coord[1]] = number_to_be_moved
               new_state = tuple(tuple(row) for row in new_state)
               # The additional cost of this state is the value of the number moved as we are trying to minimize the sum of the numbers in the grid
               new_cost = g + int(number_to_be_moved)
              
               if new_state not in visited_costs or new_cost < visited_costs[new_state]:
                   visited_costs[new_state] = new_cost
                   # Relaxing the constraints on the columns sums and the diagonal sum to calculate the heuristic
                   h = heuristic(new_state, end_coord, districts)
                   heapq.heappush(queue, (new_cost + h, new_cost, actions + [(start_coord, new_coord)], new_state))


                   # Update the start_coord to the new_coord for the next iteration
                   start_coord = new_coord
   return None




def heuristic(state, end_coord, districts):
   # Relax the constraints on the districts to compute an admissible and consistent heuristic
   # This heuristic considers the sum of the distances from the current position to the end position and the district centers, for districts that have not been visited yet
   # The heuristic is admissible because it never overestimates the cost to reach the goal, as it only considers the remaining districts to visit
   # The heuristic is consistent, ie non-decreasing along the path to the goal state, because the cost of moving to a new position is the distance moved, which is always greater than or equal to the distance moved in the heuristic
   # Also the cost of the goal state is 0, as Ben has reached the destination


   h = 0
   for district in districts:
       if any(start_coord[0] >= district[0] and start_coord[0] <= district[1] for start_coord in actions):
           continue
       else:
           district_center = (district[0] + district[1]) // 2
           h += abs(district_center - end_coord[0]) + abs(district_center - end_coord[1])
   return h


print(a_star())
